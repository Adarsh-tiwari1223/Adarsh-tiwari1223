#!/usr/bin/env python3
"""
LinkedIn Official API Publisher & Manager
Tailored for Adarsh Tiwari's Career Command Center.

Enables secure, official, bot-free publishing to LinkedIn via the LinkedIn REST API.
"""

import os
import sys
import json
import argparse
from pathlib import Path
import requests

# Base directories
BASE_DIR = Path(__file__).resolve().parent
ENV_PATH = BASE_DIR / ".env"

def load_env():
    """Load environment variables from linkedin/.env if present."""
    if ENV_PATH.exists():
        with open(ENV_PATH, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    os.environ.setdefault(key.strip(), val.strip().strip('"').strip("'"))

def get_access_token():
    """Retrieve access token from environment or .env file."""
    load_env()
    token = os.getenv("LINKEDIN_ACCESS_TOKEN")
    if not token:
        print("\n[ERROR] Missing LINKEDIN_ACCESS_TOKEN.")
        print("Please create linkedin/.env and set:")
        print("LINKEDIN_ACCESS_TOKEN=your_token_here\n")
        sys.exit(1)
    return token

def get_user_profile(token):
    """
    Fetch authenticated user's profile info (sub, name) from OpenID userinfo.
    Returns (person_urn, full_name, email).
    """
    url = "https://api.linkedin.com/v2/userinfo"
    headers = {"Authorization": f"Bearer {token}"}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        # Fallback to legacy me endpoint
        fallback_url = "https://api.linkedin.com/v2/me"
        fallback_resp = requests.get(fallback_url, headers=headers)
        if fallback_resp.status_code == 200:
            data = fallback_resp.json()
            person_id = data.get("id")
            first_name = data.get("localizedFirstName", "")
            last_name = data.get("localizedLastName", "")
            full_name = f"{first_name} {last_name}".strip()
            return f"urn:li:person:{person_id}", full_name, ""
        
        print(f"[ERROR] Failed to authenticate user profile (HTTP {response.status_code}):")
        print(response.text)
        sys.exit(1)
        
    data = response.json()
    sub = data.get("sub")
    person_urn = sub if sub.startswith("urn:li:person:") else f"urn:li:person:{sub}"
    name = data.get("name", "LinkedIn User")
    email = data.get("email", "")
    return person_urn, name, email

def publish_post(token, text, article_url=None):
    """
    Publish a post to the authenticated user's LinkedIn feed.
    Tries the modern Posts REST API first, then falls back to UGC API.
    """
    person_urn, name, _ = get_user_profile(token)
    print(f"Authenticated as: {name} ({person_urn})")
    
    # Method 1: Modern Posts API
    url_v2024 = "https://api.linkedin.com/rest/posts"
    headers_v2024 = {
        "Authorization": f"Bearer {token}",
        "LinkedIn-Version": "202401",
        "X-Restli-Protocol-Version": "2.0.0",
        "Content-Type": "application/json"
    }
    
    payload_v2024 = {
        "author": person_urn,
        "commentary": text,
        "visibility": "PUBLIC",
        "distribution": {
            "feedDistribution": "MAIN_FEED",
            "targetEntities": [],
            "thirdPartyDistributionChannels": []
        },
        "lifecycleState": "PUBLISHED",
        "isReshareDisabledByAuthor": False
    }
    
    if article_url:
        payload_v2024["content"] = {
            "article": {
                "source": article_url,
                "title": "Technical Insight by Adarsh Tiwari"
            }
        }
        
    response = requests.post(url_v2024, headers=headers_v2024, json=payload_v2024)
    
    if response.status_code in (200, 201):
        post_urn = response.headers.get("x-restli-id", "Created")
        print(f"\n[SUCCESS] Post published via LinkedIn Posts API!")
        print(f"Post URN: {post_urn}")
        return post_urn
    
    # Method 2: Fallback to UGC API
    ugc_url = "https://api.linkedin.com/v2/ugcPosts"
    ugc_headers = {
        "Authorization": f"Bearer {token}",
        "X-Restli-Protocol-Version": "2.0.0",
        "Content-Type": "application/json"
    }
    
    share_content = {
        "shareCommentary": {"text": text},
        "shareMediaCategory": "NONE"
    }
    if article_url:
        share_content["shareMediaCategory"] = "ARTICLE"
        share_content["media"] = [{"status": "READY", "originalUrl": article_url}]
        
    ugc_payload = {
        "author": person_urn,
        "lifecycleState": "PUBLISHED",
        "specificContent": {
            "com.linkedin.ugc.ShareContent": share_content
        },
        "visibility": {
            "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
        }
    }
    
    ugc_response = requests.post(ugc_url, headers=ugc_headers, json=ugc_payload)
    if ugc_response.status_code in (200, 201):
        post_id = ugc_response.json().get("id", "Created")
        print(f"\n[SUCCESS] Post published via LinkedIn UGC API!")
        print(f"Post ID: {post_id}")
        return post_id
    
    print("\n[ERROR] Failed to publish post:")
    print("Modern API Response:", response.status_code, response.text)
    print("UGC API Response:", ugc_response.status_code, ugc_response.text)
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Official LinkedIn API Manager for Adarsh Tiwari")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # verify
    subparsers.add_parser("verify", help="Verify access token and view profile identity")
    
    # post
    post_parser = subparsers.add_parser("post", help="Publish a text post to LinkedIn")
    post_parser.add_argument("--text", type=str, help="Post content text")
    post_parser.add_argument("--file", type=str, help="Path to text file containing post content")
    post_parser.add_argument("--url", type=str, help="Optional article / repository link to attach")
    
    args = parser.parse_args()
    
    if args.command == "verify":
        token = get_access_token()
        urn, name, email = get_user_profile(token)
        print("\n=== LinkedIn API Authentication Status ===")
        print(f"Status:       CONNECTED (Valid Token)")
        print(f"Member Name:  {name}")
        print(f"Member URN:   {urn}")
        if email:
            print(f"Email:        {email}")
        print("Capabilities: Feed Publishing (w_member_social)\n")
        
    elif args.command == "post":
        token = get_access_token()
        text_content = ""
        if args.file:
            with open(args.file, "r", encoding="utf-8") as f:
                text_content = f.read().strip()
        elif args.text:
            text_content = args.text.strip()
        else:
            print("[ERROR] Please provide --text \"content\" or --file path/to/draft.txt")
            sys.exit(1)
            
        publish_post(token, text_content, article_url=args.url)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

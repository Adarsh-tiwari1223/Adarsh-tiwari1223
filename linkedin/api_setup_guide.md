# 🔌 LinkedIn Official Developer API Setup Guide
*2-Minute Setup for Official, Safe Automation*

By connecting the official LinkedIn API, you can publish posts directly from your terminal or command line without any third-party fees and with zero risk of account locking.

---

## Step 1: Create Your Free Developer App (2 Minutes)

1. Open **[https://www.linkedin.com/developers/](https://www.linkedin.com/developers/)** in your browser.
2. Click **Create App** (top right).
3. Fill in the simple details:
   * **App Name:** `Adarsh SDET Automation Manager`
   * **LinkedIn Page:** Link any LinkedIn company page you administer (If you don't have one, create a free 30-second personal page on LinkedIn called "Adarsh Tiwari Labs" or "Adarsh Portfolio").
   * **Privacy Policy URL:** You can paste your GitHub profile URL (`https://github.com/Adarsh-tiwari1223`).
   * **App Logo:** Upload any square profile photo or logo.
4. Agree to the API Terms and click **Create App**.

---

## Step 2: Enable Publishing Products

1. Inside your newly created app, go to the **Products** tab.
2. Find and request these two free products (both approve instantly):
   * **Share on LinkedIn** (Enables `w_member_social` permission to post updates).
   * **Sign In with LinkedIn using OpenID Connect** (Enables profile identity).
3. Click **Request access** for both.

---

## Step 3: Generate Your Access Token

LinkedIn provides an instant OAuth Token Generator directly inside the developer portal:

1. Click on the **Auth** tab in your app.
2. Scroll to the **OAuth 2.0 tools** section and click **Token Generator** (or go to [https://www.linkedin.com/developers/tools/oauth](https://www.linkedin.com/developers/tools/oauth)).
3. Select your App from the dropdown.
4. Check the box for:
   * `w_member_social` (required to post)
   * `openid`
   * `profile`
   * `email`
5. Click **Request Access Token**.
6. A popup will ask you to approve permissions for your own app. Click **Allow**.
7. Copy the generated **Access Token**.

---

## Step 4: Configure Your Local Environment

1. In your workspace, create a file named `.env` inside the `linkedin/` folder (`linkedin/.env`).
2. Add your copied token:
   ```env
   LINKEDIN_ACCESS_TOKEN=AQX...your_full_token_here...
   ```
*(Note: `.env` is already added to `.gitignore`, ensuring your token is never pushed to GitHub).*

---

## Step 5: Test & Publish

### 1. Test Verification
Run in your terminal:
```powershell
python linkedin/linkedin_publisher.py verify
```
*Expected Output:*
```text
=== LinkedIn API Authentication Status ===
Status:       CONNECTED (Valid Token)
Member Name:  Adarsh Tiwari
Member URN:   urn:li:person:XXXXX
Capabilities: Feed Publishing (w_member_social)
```

### 2. Publish a Post
To publish any text post directly:
```powershell
python linkedin/linkedin_publisher.py post --text "A passing UI test does not mean a healthy system. Enforcing the 3-tier validation rule..."
```

Or publish directly from a file:
```powershell
python linkedin/linkedin_publisher.py post --file linkedin/posts/post_1.txt
```

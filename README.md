# Enterprise Multi-Layer Automation Framework (Python + Playwright + Pytest)

![CI Pipeline](https://img.shields.io/badge/build-passing-brightgreen?style=flat-square&logo=githubactions)
![Python Version](https://img.shields.io/badge/python-3.11%2B-blue?style=flat-square&logo=python)
![Playwright](https://img.shields.io/badge/playwright-v1.40%2B-green?style=flat-square&logo=playwright)
![Pytest](https://img.shields.io/badge/pytest-v8.0%2B-orange?style=flat-square&logo=pytest)
![Docker](https://img.shields.io/badge/docker-ready-2496ED?style=flat-square&logo=docker)

A modular, production-ready test automation framework designed for full-stack multi-layer validation: **UI interactions (Playwright)**, **RESTful API endpoints (`requests`)**, and **Database state assertions (SQL)**. Integrated with **GitHub Actions CI/CD** and **Docker** for headless cross-browser test execution.

---

## 🏛️ Architecture & Design Patterns

The framework decouples locators, business actions, test data, and fixtures into an enterprise-grade Page Object Model (POM):

```text
├── .github/
│   └── workflows/
│       └── test_pipeline.yml       # GitHub Actions automated CI run
├── config/
│   ├── config.ini                  # Environment configurations & URLs
│   └── logger.py                   # Centralized structured test logger
├── pages/                          # Page Object Model classes
│   ├── base_page.py                # Wrapper for common Playwright actions
│   ├── login_page.py
│   └── dashboard_page.py
├── tests/
│   ├── ui/                         # UI Playwright tests
│   │   └── test_user_flow.py
│   ├── api/                        # REST API tests
│   │   └── test_auth_and_crud.py
│   └── conftest.py                 # Core fixtures, browser lifecycle, hooks
├── utils/                          # Shared reusable modules
│   ├── api_client.py               # REST API wrapper (Requests / Token injection)
│   ├── db_helper.py                # Database connection & SQL assertion helper
│   └── test_data_loader.py         # Dynamic JSON / YAML test data loader
├── .dockerignore
├── .gitignore
├── Dockerfile                      # Containerized test runner
├── pytest.ini                      # Pytest CLI options, markers, and logging
├── requirements.txt                # Pinned dependencies
└── README.md

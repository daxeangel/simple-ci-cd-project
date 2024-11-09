# CI/CD Sample Project

This project demonstrates setting up a CI/CD pipeline for a Flask application with automated tests.

## Application Overview

- A simple Flask app with two routes:
  - /: Returns "Hello, World!"
  - /greet/<name>: Greets the user with "Hello, <name>!"

## Project Structure

```plaintext
.
├── app.py               # Main application code
├── tests/
│   └── test_app.py      # Test cases
├── requirements.txt     # Dependencies
├── .github/workflows/   # GitHub Actions CI/CD configuration (for GitHub)
│   └── ci.yml
├── .gitlab-ci.yml       # GitLab CI/CD configuration (for GitLab)
├── README.md            # Documentation

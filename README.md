# Simple-Image-Scraper-and-API-Submitter
I made a Python script that:  Downloads an image from a link  Converts it to base64  Sends it to an AI inference API using the model microsoft-florence-2-large  Then sends the response to another URL to submit  It uses requests, base64, and prints the status while running. If anything goes wrong, it stops the script.

# Simple Image Scraper and API Submitter

This is a simple Python script made for a technical evaluation.

## 📌 What it does:
- Downloads an image from a provided URL.
- Converts the image to base64.
- Sends it to an AI inference API using `microsoft-florence-2-large`.
- Sends the AI response to a submission URL.

## 📦 Requirements:
- Python 3
- `requests` library (install with `pip install requests`)

## 🚀 How to run:
1. Replace the `token` value in the script with your token.
2. Run the script:


## 📄 Notes:
- If the image or API request fails, the script will stop.
- The script prints the status of each step in the terminal.

## 📚 Libraries used:
- `requests`
- `base64`
- `sys`

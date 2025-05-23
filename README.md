# AI Image Generator for Google Sheets

This project reads content titles from a Google Sheet, combines them with a specified image style, background color, and theme description, and generates images using an AI API (OpenAI DALL·E 3). The resulting image URLs are then inserted back into the same Google Sheet.

---

## Features

- Reads multiple content titles from a Google Sheet.
- Uses a single shared style, background color, and theme for all prompts.
- Generates descriptive prompts for each title.
- Calls the OpenAI DALL·E API to generate images.
- Inserts the image URLs into a new column in the same sheet.

---

## Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```
## Setup
### 1. Google Sheets API
 
 - Go to Google Cloud Console.

- Create a new project and enable the Google Sheets API and Google Drive API.

- Go to Credentials → Create Service Account Key (JSON).

- Download the your-credentials.json file.

- Share your Google Sheet with the client email from the JSON file.

### 2. OpenAI API Key

- Create an account at platform.openai.com.

- Generate an API key.

- Save it securely (you’ll use it in main.py).

## Running the Script

- Set your OpenAI API key in main.py.

- Replace the path to your Google service account key file.

- Run the script:

```bash
python main.py
```




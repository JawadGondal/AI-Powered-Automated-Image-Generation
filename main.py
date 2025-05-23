# --- Imports ---
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from openai import OpenAI

# --- Setup: API Keys ---
openai_client = OpenAI(api_key="your_api_key")

# --- Setup: Google sheet Authorization ---
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json",scope)
client = gspread.authorize(creds)

# --- Load Google Sheet ---
sheet = client.open_by_url("your_googlesheet_url").sheet1
rows = sheet.get_all_values()

# --- Extract Style, color, and theme ---
headers = rows[0]
values = rows[1]
style = values[headers.index("Image Style")]
bg_color = values[headers.index("Background Color")]
theme = values[headers.index("Theme Description")]
#print(len(headers),headers)

# --- Process each content title ---
for i in range(1, len(rows)):
    content = rows[i][headers.index("Content Title")]
    prompt = f"{style} Use background color:{bg_color}, theme description: {theme},and content title:{content}"
    try:
        response = openai_client.images.generate(
            model= 'dall-e-3',
            prompt=prompt,
            size='1024x1024',
            n=1,
            quality='standard'
        )
    # Insert Image link to sheet
        image_url = response.data[0].url
        sheet.update_cell(i+1, len(headers), image_url)
    except Exception as e:
        print("Error Generating Image", e)


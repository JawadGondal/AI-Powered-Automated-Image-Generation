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

# In current sheet, there is only one background color, theme description, and style.
# The following code block deals with that case.

# --- Extract Style, color, and theme ---
headers = rows[0]
values = rows[1]
style = values[headers.index("Image Style")]
bg_color = values[headers.index("Background Color")]
theme = values[headers.index("Theme Description")]
#print(len(headers),headers)

# If you have unique value of background color, theme description, and style for each content title. Add following cole block in for loop

"""
    style = rows[i][headers.index("Imge Style")]  # Current sheet has column name image style. You can specify it according to your sheet.
    bg_color = rows[i][headers.index("Background Color")] # Specify column name accorind to your sheet.
    theme = rows[i][headers.index("Theme Description")]  # Specify column name according to your sheet.
    # Add here if columns are more than current sheet.
"""

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


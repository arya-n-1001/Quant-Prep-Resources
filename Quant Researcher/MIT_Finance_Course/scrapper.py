import requests
from bs4 import BeautifulSoup
from pathlib import Path
from urllib.parse import urljoin
import re

BASE_URL = "https://ocw.mit.edu"

LECTURE_NOTES_URL = (
    "https://ocw.mit.edu/courses/"
    "18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/"
    "pages/lecture-notes/"
)

# Save next to script
SAVE_DIR = Path(__file__).resolve().parent / "MIT_Finance_Course"
SAVE_DIR.mkdir(parents=True, exist_ok=True)

session = requests.Session()
session.headers.update({
    "User-Agent": "Mozilla/5.0"
})

print("Fetching lecture notes page...")

html = session.get(LECTURE_NOTES_URL).text
soup = BeautifulSoup(html, "html.parser")

lecture_data = []

# Find all resource links and associated lecture titles
for row in soup.find_all("tr"):

    cols = row.find_all("td")

    if len(cols) < 2:
        continue

    lec_num = cols[0].get_text(strip=True)

    link = cols[1].find("a")

    if not link:
        continue

    title = link.get_text(strip=True)

    href = link.get("href", "")

    if "/resources/" not in href:
        continue

    lecture_data.append({
        "number": lec_num,
        "title": title,
        "resource_url": urljoin(BASE_URL, href)
    })

print(f"Found {len(lecture_data)} lecture PDFs\n")

for lecture in lecture_data:

    lec_num = lecture["number"]
    title = lecture["title"]
    resource_url = lecture["resource_url"]

    print(f"Lecture {lec_num}: {title}")

    try:

        resource_html = session.get(resource_url).text
        resource_soup = BeautifulSoup(resource_html, "html.parser")

        pdf_url = None

        for a in resource_soup.find_all("a", href=True):

            href = a["href"]

            if ".pdf" in href.lower():
                pdf_url = urljoin(BASE_URL, href)
                break

        if not pdf_url:
            print("  -> PDF not found")
            continue

        safe_title = re.sub(r'[\\/*?:"<>|]', "", title)

        filename = f"{int(lec_num):02d} - {safe_title}.pdf"

        filepath = SAVE_DIR / filename

        print(f"  -> Downloading {filename}")

        pdf_data = session.get(pdf_url).content

        with open(filepath, "wb") as f:
            f.write(pdf_data)

    except Exception as e:
        print("ERROR:", e)

print("\nDone!")
print(f"Saved to:\n{SAVE_DIR}")
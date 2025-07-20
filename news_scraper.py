
import requests
from bs4 import BeautifulSoup

# URL of the news website
url = "https://www.bbc.com/news"

# Send GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract all headlines with <h3> or <h2> tags (common for news headlines)
    headlines = soup.find_all(['h2', 'h3'])

    with open("headlines.txt", "w", encoding="utf-8") as file:
        for headline in headlines:
            text = headline.get_text(strip=True)
            if text:
                file.write(text + "\n")

    print("Headlines scraped and saved to 'headlines.txt'")
else:
    print(f"Failed to fetch page. Status code: {response.status_code}")

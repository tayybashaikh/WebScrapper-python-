import requests
from bs4 import BeautifulSoup

# Step 1: Website URL
url = "https://www.hindustantimes.com/latest-news"

try:
    # Step 2: Send GET request
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    
    # Step 3: Check status code
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Step 4: Extract all headlines (h3 tags used on this site)
        headlines = soup.find_all("h3")
        
        # Step 5: Save headlines in a text file
        with open("headlines.txt", "w", encoding="utf-8") as file:
            file.write("Top News Headlines:\n\n")
            for h in headlines:
                headline = h.text.strip()
                file.write(headline + "\n")
        
        print("Headlines successfully scraped and saved in 'headlines.txt'!")
    
    else:
        print("Failed to fetch webpage. Status code:", response.status_code)

except Exception as e:
    print("An error occurred:", e)
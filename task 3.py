import requests
from bs4 import BeautifulSoup

# 1. Understand web scraping principles and techniques


# 2. Develop a simple Python script to scrape data from a static web page
url = 'https://example.com'  
response = requests.get(url)

if response.status_code == 200:
    print("Successfully fetched the web page")
else:
    print("Failed to fetch the web page")
    exit()


soup = BeautifulSoup(response.content, 'html.parser')

# 3. Extract relevant information such as text, links, or images from web pages


text_content = soup.get_text()
print("Text Content:")
print(text_content)


links = soup.find_all('a')
print("\nLinks:")
for link in links:
    href = link.get('href')
    link_text = link.get_text()
    print(f"{link_text}: {href}")


images = soup.find_all('img')
print("\nImages:")
for image in images:
    src = image.get('src')
    alt = image.get('alt', 'No alt text')
    print(f"Image Source: {src}, Alt Text: {alt}")


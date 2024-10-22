import requests
from bs4 import BeautifulSoup
import os

# Base URL for CrewAI documentation
base_url = "https://docs.crewai.com"

# The URL of the introduction page
url = "https://docs.crewai.com/introduction"

# Function to scrape a page's text
def scrape_page(page_url):
    response = requests.get(page_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        return soup.get_text()
    else:
        print(f"Failed to fetch the page at {page_url}. Status code: {response.status_code}")
        return None

# Scrape the main page
main_page_text = scrape_page(url)

# Extract hyperlinks from the main page
def extract_hyperlinks(soup):
    links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        # Ignore internal page navigation (like '#') and external links
        if href.startswith("/") and not href.startswith("#"):
            links.append(base_url + href)
    return links

# Get the links from the introduction page
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
hyperlinks = extract_hyperlinks(soup)

# Save the text from the main page
with open("crew_ai_docs.txt", "w") as file:
    if main_page_text:
        file.write(f"Main Page: {url}\n\n{main_page_text}\n\n")

    # Scrape each linked page and append it to the file
    for link in hyperlinks:
        page_text = scrape_page(link)
        if page_text:
            file.write(f"Page: {link}\n\n{page_text}\n\n")
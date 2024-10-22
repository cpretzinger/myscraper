import requests
from bs4 import BeautifulSoup

# Base URL for CrewAI documentation
url = "https://docs.crewai.com/introduction"

# Function to extract hyperlinks
def extract_hyperlinks(soup):
    links = []
    for link in soup.find_all('a', href=True):
        href = link['href']
        # Ignore internal page navigation (like '#')
        if href.startswith("/") and not href.startswith("#"):
            links.append(href)
    return links

# Fetch the page content
response = requests.get(url)
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Extract all the hyperlinks from the page
    hyperlinks = extract_hyperlinks(soup)

    # Save the links to a file or print them
    with open("crew_ai_links.txt", "w") as file:
        for link in hyperlinks:
            full_link = "https://docs.crewai.com" + link  # Make the links absolute
            file.write(full_link + "\n")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")
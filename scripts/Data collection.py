import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

BASE_URL = "https://medlineplus.gov/encyclopedia.html"
HEADERS = {"User-Agent": "Mozilla/5.0"}

def get_letter_links():
    """Scrape the index page to get A-Z links."""
    response = requests.get(BASE_URL, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    alpha_links = []
    for link in soup.select("ul.alpha-links li a"):
        alpha_links.append("https://medlineplus.gov/" + link.get("href"))
    return alpha_links

# Fetch A-Z links
letter_links = get_letter_links()
print(f"Found {len(letter_links)} letter links.")

def get_disease_links(letter_url):
    """Scrape a letter page to get disease names and links."""
    response = requests.get(letter_url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    diseases = []
    for disease in soup.select("li a"):  # Select all links within list items
        if "article" in disease.get("href"):  # Filter only article links
            diseases.append({
                "name": disease.text.strip(),
                "link": "https://medlineplus.gov/ency/" + disease.get("href")
            })
    return diseases


# Example for letter A
diseases = get_disease_links(letter_links[0])
print(f"Found {len(diseases)} diseases for letter A.")

def scrape_disease_page(disease_url):
    """Scrape a disease page to extract required data including symptoms."""
    response = requests.get(disease_url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Initialize the data dictionary
    data = {}
    
    # Extract disease name
    try:
        data["name"] = soup.select_one("div.page-title h1").text.strip()
    except AttributeError:
        data["name"] = None

    # Extract summary
    try:
        data["summary"] = soup.select_one("#ency_summary p").text.strip()
    except AttributeError:
        data["summary"] = None

    # Extract causes
    try:
        causes_section = soup.find("h2", text="Causes").find_next("div", class_="section-body")
        data["causes"] = causes_section.get_text(" ", strip=True)
    except AttributeError:
        data["causes"] = None

    # Extract symptoms
    try:
        symptoms_section = soup.find("h2", text="Symptoms").find_next("div", class_="section-body")
        data["symptoms"] = symptoms_section.get_text(" ", strip=True)
    except AttributeError:
        data["symptoms"] = None

    # Extract home care
    try:
        home_care_section = soup.find("h2", text="Home Care").find_next("div", class_="section-body")
        data["home_care"] = home_care_section.get_text(" ", strip=True)
    except AttributeError:
        data["home_care"] = None

    # Extract alternative names
    try:
        alternative_names = soup.select_one("#section-Alt p")
        data["alternative_names"] = alternative_names.text.strip() if alternative_names else None
    except AttributeError:
        data["alternative_names"] = None

    return data


# Example for a disease
if diseases:
    disease_data = scrape_disease_page(diseases[0]["link"])
    print(disease_data)

def scrape_all_diseases():
    """Scrape all diseases from A-Z pages and save to CSV."""
    all_data = []
    for letter_link in letter_links:
        print(f"Scraping diseases for: {letter_link}")
        diseases = get_disease_links(letter_link)
        print(f"Found {len(diseases)} diseases on page {letter_link}")
        for disease in diseases:
            print(f"Scraping disease: {disease['name']} ({disease['link']})")
            data = scrape_disease_page(disease["link"])
            all_data.append(data)
            time.sleep(random.uniform(2,6))  # Rate limit
    return all_data

# Scrape all data
data = scrape_all_diseases()

# Save to CSV
df = pd.DataFrame(data)
df.to_csv("medlineplus_diseases.csv", index=False)
print("Data saved to medlineplus_diseases.csv")

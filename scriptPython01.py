import requests
from bs4 import BeautifulSoup
import csv
import time
import random
import datetime

BASE_URL = "https://kulinski.bg"
MANUFACTURERS_URL = f"{BASE_URL}/index.php?route=product/manufacturer"

HEADERS_LIST = [
    {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117 Safari/537.36'},
    {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15 Safari/605.1.15'},
    {'User-Agent': 'Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117 Mobile Safari/537.36'},
]

def random_headers():
    return random.choice(HEADERS_LIST)

def human_delay():
    time.sleep(random.uniform(1.5, 4.0))

def get_soup(url):
    response = requests.get(url, headers=random_headers())
    response.raise_for_status()
    return BeautifulSoup(response.text, 'html.parser')

def get_manufacturers():
    soup = get_soup(MANUFACTURERS_URL)
    links = soup.select('div.manufacturer a.image-card')
    manufacturer_urls = []

    for link in links:
        href = link.get('href')
        if href and href.startswith(BASE_URL):
            manufacturer_urls.append(href)

    return manufacturer_urls

def extract_product_data(product_url):
    products = []
    visited_pages = set()
    page_number = 1

    while True:
        paged_url = f"{product_url}?page={page_number}"
        if paged_url in visited_pages:
            break  # Avoid infinite loops
        visited_pages.add(paged_url)

        try:
            soup = get_soup(paged_url)
        except Exception as e:
            print(f"❌ Failed to load page {paged_url}: {e}")
            break

        product_cards = soup.select('div.product-thumb')
        if not product_cards:
            break  # No products = done

        for card in product_cards:
            image = card.select_one('img')
            model = None

            # Extract model from <span class="stats-label">Модел:</span>
            model_label = card.select_one('span.stats-label')
            if model_label and model_label.get_text(strip=True) == 'Модел:':
                model_span = model_label.find_next_sibling('span')
                if model_span:
                    model = model_span.get_text(strip=True)

            if image and model:
                img_url = image.get('src')
                products.append((img_url, model))

        # Check if next page exists by looking for page numbers
        pagination = soup.select('ul.pagination li a')
        page_numbers = [int(a.get_text(strip=True)) for a in pagination if a.get_text(strip=True).isdigit()]
        if (page_number + 1) in page_numbers:
            page_number += 1
            human_delay()
        else:
            break

    return products

def main():
    manufacturers = get_manufacturers()
    print(f"📦 Found {len(manufacturers)} manufacturers.")
    print(manufacturers)

    filename = f'kulinski_products_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'

    with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Image URL', 'Model'])

        for idx, manu_url in enumerate(manufacturers):
            print(f"\n🔍 Processing manufacturer {idx + 1}/{len(manufacturers)}: {manu_url}")
            try:
                products = extract_product_data(manu_url)
                writer.writerows(products)
                print(f"✅ Found {len(products)} products.")
            except Exception as e:
                print(f"❌ Error processing {manu_url}: {e}")
            human_delay()

    print(f"\n✅ Done! Data saved to: {filename}")

if __name__ == "__main__":
    main()

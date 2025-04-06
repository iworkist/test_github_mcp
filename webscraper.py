#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Simple Web Scraper

This script demonstrates a basic web scraper using BeautifulSoup4 and requests.
It fetches a web page, parses its HTML content, and extracts useful information.
"""

import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime
import os


class WebScraper:
    """A simple web scraper class to fetch and parse web content"""
    
    def __init__(self, url):
        """Initialize the scraper with a URL
        
        Args:
            url (str): The URL to scrape
        """
        self.url = url
        self.soup = None
        self.response = None
    
    def fetch_page(self):
        """Fetch the web page content
        
        Returns:
            bool: True if the page was successfully fetched, False otherwise
        """
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            self.response = requests.get(self.url, headers=headers, timeout=10)
            self.response.raise_for_status()  # Raise an exception for 4XX/5XX responses
            self.soup = BeautifulSoup(self.response.text, 'html.parser')
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error fetching the page: {e}")
            return False
    
    def get_page_title(self):
        """Extract the page title
        
        Returns:
            str: The page title or None if not found
        """
        if not self.soup:
            return None
        
        title_tag = self.soup.find('title')
        return title_tag.text.strip() if title_tag else None
    
    def get_all_links(self):
        """Extract all links from the page
        
        Returns:
            list: List of dictionaries containing link text and href
        """
        if not self.soup:
            return []
        
        links = []
        for link in self.soup.find_all('a', href=True):
            href = link['href']
            # Convert relative URLs to absolute URLs
            if href.startswith('/'):
                base_url = '/'.join(self.url.split('/')[:3])  # http(s)://domain.com
                href = base_url + href
            
            links.append({
                'text': link.text.strip(),
                'href': href
            })
        
        return links
    
    def get_all_images(self):
        """Extract all images from the page
        
        Returns:
            list: List of dictionaries containing image info
        """
        if not self.soup:
            return []
        
        images = []
        for img in self.soup.find_all('img', src=True):
            src = img['src']
            # Convert relative URLs to absolute URLs
            if src.startswith('/'):
                base_url = '/'.join(self.url.split('/')[:3])  # http(s)://domain.com
                src = base_url + src
            
            alt = img.get('alt', '')
            
            images.append({
                'src': src,
                'alt': alt
            })
        
        return images
    
    def extract_text_content(self):
        """Extract the main text content from the page
        
        Returns:
            str: The main text content
        """
        if not self.soup:
            return ""
        
        # Remove script and style elements
        for script in self.soup(["script", "style"]):
            script.extract()
        
        # Get text
        text = self.soup.get_text()
        
        # Break into lines and remove leading and trailing space on each
        lines = (line.strip() for line in text.splitlines())
        
        # Break multi-headlines into a line each
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        
        # Drop blank lines
        text = '\n'.join(chunk for chunk in chunks if chunk)
        
        return text
    
    def save_to_csv(self, data, filename):
        """Save data to a CSV file
        
        Args:
            data (list): List of dictionaries with the same keys
            filename (str): Name of the CSV file
        
        Returns:
            bool: True if the data was successfully saved, False otherwise
        """
        if not data:
            return False
        
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
                fieldnames = data[0].keys()
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                
                writer.writeheader()
                for row in data:
                    writer.writerow(row)
            
            return True
        except Exception as e:
            print(f"Error saving to CSV: {e}")
            return False


def main():
    """Main function to demonstrate the scraper"""
    url = "https://news.ycombinator.com/"  # Example: Hacker News
    scraper = WebScraper(url)
    
    print(f"Fetching content from {url}...")
    if scraper.fetch_page():
        print("Page fetched successfully!")
        
        title = scraper.get_page_title()
        print(f"\nPage title: {title}")
        
        print("\nExtracting links...")
        links = scraper.get_all_links()
        print(f"Found {len(links)} links")
        
        # Display first 5 links
        for i, link in enumerate(links[:5]):
            print(f"{i+1}. {link['text']} - {link['href']}")
        
        # Save links to CSV
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"links_{timestamp}.csv"
        if scraper.save_to_csv(links, filename):
            print(f"\nLinks saved to {filename}")
        
        # Get images
        images = scraper.get_all_images()
        print(f"\nFound {len(images)} images")
        
        # Display first 3 images
        for i, img in enumerate(images[:3]):
            print(f"{i+1}. {img['alt']} - {img['src']}")
    else:
        print("Failed to fetch the page.")


if __name__ == "__main__":
    main()

from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=False)
url_communitech = "https://www1.communitech.ca/jobs"

page = browser.new_page()
page.goto(url_communitech)

time.sleep(2) # Waits for 2 seconds
page.get_by_placeholder("Location").click()
print("Click Location")

time.sleep(2)
page.get_by_placeholder("Type to search").fill("Waterloo Region")
print("Fill Location")

time.sleep(2)
page.click(".sc-beqWaB.kQSjka:first-of-type") # Selects the first item - "Waterloo Region"
print("Select option")

time.sleep(5)

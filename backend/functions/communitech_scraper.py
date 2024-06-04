import asyncio
from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

def is_scroll_at_bottom(page):
    scroll_height = page.evaluate('(document.documentElement || document.body).scrollHeight')
    client_height = page.evaluate('(window.innerHeight || document.documentElement.clientHeight)')
    scroll_top = page.evaluate('(document.documentElement || document.body).scrollTop')

    return scroll_height - client_height <= scroll_top + 1

def communictech_scraper():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        url_communitech = "https://www1.communitech.ca/jobs"

        page = browser.new_page()
        page.goto(url_communitech)

        time.sleep(2) # Waits for 2 seconds
        page.get_by_placeholder("Location").click()

        time.sleep(2)
        page.get_by_placeholder("Type to search").fill("Waterloo Region")

        time.sleep(2)
        page.click(".sc-beqWaB.kQSjka:first-of-type") # Selects the first item - "Waterloo Region"

        time.sleep(2)
        page.get_by_placeholder("Job title, company or keyword").fill("test")

        # Load more if needed
        '''
        while True:
            button = page.query_selector('[data-testid="load-more"]')
            if button:
                button.click()
                time.sleep(5)                
                page.keyboard.down("End")

                while not is_scroll_at_bottom(page):
                    loading = page.query_selector('[class="sc-beqWaB dCSNrJ"]')
                    if loading:
                        time.sleep(3)          
                    page.keyboard.down("End")
                    loading.scroll_into_view_if_needed()
            else:
                break
        '''

        time.sleep(2)
        content = page.content()
        job_list = []

        browser.close()

        soup = BeautifulSoup(content, "html.parser")
        jobs = soup.find_all("div", class_="job-card")

        for job in jobs:
            company = job.find("div", itemprop="hiringOrganization").find("meta", itemprop="name")["content"]
            title = job.find('div', itemprop='title').text.strip()
            location_tags = job.find("div", itemprop="jobLocation").find_all("span")
            locations = []
            for tag in location_tags:
                locations.append(tag.text)
            url = f"https://www1.communitech.ca{job.find("div", class_="job-info").find("a")["href"]}"

            job_list.append({
                "title":title,
                "company": company,
                "location": locations,
                "url":url
            })

            print(company, title, locations, url)
            print("=============================")

        print(f"Total {len(job_list)} jobs!")

communictech_scraper()
import asyncio
from playwright.async_api import async_playwright, Playwright
import time
from bs4 import BeautifulSoup
import tracemalloc

async def communitech_scraper(keyword):
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        page = await browser.new_page()
        url_communitech = "https://www1.communitech.ca/jobs"
        await page.goto(url_communitech)

        # time.sleep(2) # Waits for 2 seconds
        await page.get_by_placeholder("Location").click()
        await page.get_by_placeholder("Type to search").fill("Waterloo Region")
        await page.click(".sc-beqWaB.kQSjka:first-of-type")
        time.sleep(2)

        await page.get_by_placeholder("Job title, company or keyword").fill(keyword)
        time.sleep(2)

        element = await page.query_selector("div.sc-beqWaB.iJyEXG > div > div > div > div > b")
        if element:
            total = await element.text_content()
        print(total)

        time.sleep(3)
        await page.keyboard.press("End")



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

        time.sleep(3)
        content = await page.content()
        soup = BeautifulSoup(content, "html.parser")
        jobs = soup.find_all("div", class_="job-card")

        job_list = []

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

            # print(company, title, locations, url)
            # print("=============================")

        print(f"Total {len(job_list)} jobs!")

        await browser.close()

        return job_list
        

asyncio.run(communitech_scraper("python"))


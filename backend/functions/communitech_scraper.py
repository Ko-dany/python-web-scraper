import asyncio
from playwright.async_api import async_playwright, Playwright
import time
from bs4 import BeautifulSoup
import tracemalloc

def page_of_results(number_of_result):
    full_page = number_of_result //20
    remainder = number_of_result % 20

    return full_page  if remainder > 0 else full_page - 1

async def communitech_scraper(keyword):
    async with async_playwright() as playwright:
        try:
            browser = await playwright.chromium.launch(headless=False)
            page = await browser.new_page()
            url_communitech = "https://www1.communitech.ca/jobs"
            await page.goto(url_communitech)

            # time.sleep(2) # Waits for 2 seconds
            await page.get_by_placeholder("Location").click()
            await page.get_by_placeholder("Type to search").fill("Waterloo Region")
            await page.click(".sc-beqWaB.qIsge:first-of-type")
            time.sleep(2)

            await page.get_by_placeholder("Job title, company or keyword").fill(keyword)
            time.sleep(2)

            # Focus out of searching input
            await page.locator("#content > div.sc-beqWaB.eFnOti > div.sc-beqWaB.sc-gueYoa.krgmev.MYFxR > div.sc-beqWaB.iJyEXG > div > div").click()

            button = await page.query_selector("#content > div.sc-beqWaB.eFnOti > div.sc-beqWaB.sc-gueYoa.krgmev.MYFxR > div.sc-beqWaB.jfIxNQ > button")
            if button:
                button.click()

            element = await page.query_selector("div.sc-beqWaB.iJyEXG > div > div > div > div > b")
            if element:
                total = await element.text_content()
                for x in range(page_of_results(int(total))):
                    time.sleep(3)
                    await page.keyboard.press("End")
                    print("Scrolling! => ", x)
            
            time.sleep(3)
            content = await page.content()
            soup = BeautifulSoup(content, "html.parser")
            jobs = soup.find_all("div", class_="job-card")
            print(jobs)

            job_list = []

            '''
            for job in jobs:
                company = job.find("div", itemprop="hiringOrganization").find("meta", itemprop="name")["content"]
                print("company")
                print(company)

                title = job.find('div', itemprop='title').text.strip()
                print("title")
                print(title)

                location_tags = job.find("div", itemprop="jobLocation").find_all("span")
                print("location_tags")
                print(location_tags)

                locations = []
                for tag in location_tags:
                    locations.append(tag.text)
                url = f"https://www1.communitech.ca{job.find('div', class_='job-info').find('a')['href']}"


                job_list.append({
                    "title":title,
                    "company": company,
                    "location": locations,
                    "url":url
                })
            '''
                
            print(f"Total {len(job_list)} jobs!")

            await browser.close()

            return job_list
        except Exception as e:
            print(f"Error occurred: {e}")
            raise e

# ***** Testing *****
# asyncio.run(communitech_scraper("test"))


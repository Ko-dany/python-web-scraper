import asyncio
from playwright.async_api import async_playwright, Playwright
import time
from bs4 import BeautifulSoup
import tracemalloc

async def communitech_scraper(keyword):
    async with async_playwright() as playwright:
        try:
            browser = await playwright.chromium.launch(headless=False)
            page = await browser.new_page()
            url_communitech = "https://www1.communitech.ca/jobs"
            await page.goto(url_communitech)

             # Searching for jobs in Waterloo Region
            await page.get_by_placeholder("Location").click()
            await page.get_by_placeholder("Type to search").fill("Waterloo Region")
            await page.click(".sc-beqWaB.qIsge:first-of-type")
            await asyncio.sleep(3)

            # Enter the keyword for job search
            await page.get_by_placeholder("Job title, company or keyword").fill(keyword)
            await asyncio.sleep(3)

            # Focus out of searching input
            await page.locator("#content > div.sc-beqWaB.eFnOti > div.sc-beqWaB.sc-gueYoa.krgmev.MYFxR > div.sc-beqWaB.iJyEXG > div > div > div > div").click()


            button = await page.query_selector("#content > div.sc-beqWaB.eFnOti > div.sc-beqWaB.sc-gueYoa.krgmev.MYFxR > div.sc-beqWaB.jfIxNQ > button")
            job_counts = await page.query_selector("div.sc-beqWaB.iJyEXG > div > div > div > div > b")
            footer = await page.query_selector("#wlc-main > div.sc-beqWaB.sc-gueYoa.kVZzjT.MYFxR.powered-by-footer")

            if button:
                await button.click()

            if job_counts:
                total = await job_counts.text_content()
                total_count = int(total)
                pages = total_count // 20 + (1 if total_count % 20 != 0 else 0)

                for x in range(pages):
                    await footer.scroll_into_view_if_needed()
                    print("Scrolling! => ", x)
                    await asyncio.sleep(5)
                    

            await asyncio.sleep(10)
            
            content = await page.content()
            soup = BeautifulSoup(content, "html.parser")
            jobs = soup.find_all("div", class_="job-card")
            # print(jobs)

            job_list = []
            
            for job in jobs:
                company = job.find("div", itemprop="hiringOrganization").find("meta", itemprop="name")["content"]
                # print("company")
                # print(company)

                title = job.find('div', itemprop='title').text.strip()
                # print("title")
                # print(title)

                location_tags = job.find("div", itemprop="jobLocation").find_all("span")
                # print("location_tags")
                # print(location_tags)

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
            
                
            print(f"Total {len(job_list)} jobs!")

            await browser.close()

            return job_list
        except Exception as e:
            print(f"Error occurred: {e}")
            raise e

# ***** Testing *****
# asyncio.run(communitech_scraper("test"))


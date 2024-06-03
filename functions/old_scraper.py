from bs4 import BeautifulSoup
import requests
from urllib.parse import quote

def commitech_scraper(search_keyword):
    encoded_search_keyword = quote(search_keyword)
    url = f"https://www1.communitech.ca/jobs?q={encoded_search_keyword}"
    request = requests.get(url)

    search_results = []

    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        jobs = soup.find_all("div", class_="job-card")

        for job in jobs:
            title = job.find("div", itemprop="title")
            company = job.find("a", attrs={"data-testid": "link"})
            link = f'https://www1.communitech.ca/{job.find("a", attrs={"data-testid": "read-more"}).get("href").strip()}'

            if title:
                title = title.string.strip()
            if company:
                company = company.string.strip()

            print(f"{title} | {company} | {link}")
            print("================================================")
    else:
        print("Can't access the website.")
        print(request.status_code)

    return search_results

commitech_scraper("python")
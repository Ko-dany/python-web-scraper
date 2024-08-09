import csv

def export_to_file(file_name, jobs):
    with open(f"{file_name}.csv", "w", encoding="utf-8-sig", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Company", "Location", "Link"])
        for job in jobs:
            writer.writerow([job["title"], job["company"], job["location"], job["url"]])

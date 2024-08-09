def export_to_file(file_name, jobs):
    file = open(f"{file_name}.csv", "w", encoding="utf-8-sig")

    file.write("Title,Company,Location,Link\n")
    for job in jobs:
        file.write(f"{job["title"]},{job["company"]},{job["location"]},{job["url"]}\n")
    
    file.close()
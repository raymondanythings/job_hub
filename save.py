import csv


def save_to_file(jobs):
    """_summary_

    Args:
        jobs (_type_): _description_
    """
    file = open("jobs.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["title", "company",  "link", "time"])
    for job in jobs:
        writer.writerow(list(job.values()))
    return

import requests
from bs4 import BeautifulSoup


def get_last_page(URL):
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    try:
        pages = soup.find("div", class_="s-pagination").find_all("a")
        last_page = pages[-2].get_text(strip=True)
    except:
        last_page = 0
    return int(last_page)


def extract_job(html):
    title = html.find("h2").find("a")["title"]
    company, location = html.find("h3").find_all("span", recursive=False)
    company = company.get_text(strip=True)
    location = location.get_text(strip=True).strip(
        "-").strip(" \r").strip("\n")
    job_id = html["data-jobid"]
    time_re = html.find(
        "ul", class_="mt4 fs-caption fc-black-500 horizontal-list").find("span").text
    time = time_re.replace("ago", "").strip()
    if time == "yesterday":
        time = "1d"
    return {
        "title": title,
        "company": company,
        "link": f"https://stackoverflow.com/jobs/{job_id}",
        "time": time
    }


def extract_jobs(last_page, URL, name):
    jobs = []
    for page in range(last_page):
        print(f"SOF - {name} Page {page+1} scrapping")
        if page+1 == 1:
            result = requests.get(f"{URL}")
        else:
            result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", class_="-job")
        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs


def get_sof(job):
    URL = f"https://stackoverflow.com/jobs?tl={job}&sort=p"
    last_page = get_last_page(URL)
    jobs = extract_jobs(last_page, URL, job)
    return jobs


'''
url = "https://stackoverflow.com/jobs?tl=python&sort=p&pg=1"
print("======New=======")
re = requests.get(url)
soup = BeautifulSoup(re.text, "html.parser")
result = soup.find_all("div", class_="-job")
for x in result:
    title = x.find("h2").find("a")["title"]
    job_id = f"https://stackoverflow.com/jobs/{x['data-jobid']}"
    print(title)
    print(job_id)

pages = soup.find("div", class_="s-pagination").find_all("a")
last_page = pages[-2].get_text(strip=True)
'''

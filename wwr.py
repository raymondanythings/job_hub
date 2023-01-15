import requests
from bs4 import BeautifulSoup
from time_compile import time_compile


def get_wwr(job):
    url = f"https://weworkremotely.com/remote-jobs/search?term={job}"

    re = requests.get(url)
    soup = BeautifulSoup(re.text, "html.parser")

    section = soup.find_all(class_="jobs")

    result = []
    print(f"WWR - {job} scrapping...")
    for i in section:
        a = i.find_all("li", class_="feature")
        for x in a:
            company = x.find("span", class_="company").text
            title = x.find("span", class_="title").text
            link = x.find_all("a")
            link = link[1]["href"]
            time_get = x.find("time")
            if time_get == None:
                time_get = "Featured"
            else:
                time_get = time_get["datetime"]
            time = time_compile(time_get)
            list = {
                "title": title,
                "company": company,
                "link": f"https://weworkremotely.com{link}",
                "time": time
            }
            result.append(list)
        return result

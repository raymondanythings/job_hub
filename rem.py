'''
d
'''
import requests
from bs4 import BeautifulSoup


def get_rem(job):
    '''
    Get Remote Ok Jobs
    '''
    result = []
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
    url = f"https://remoteok.io/remote-{job}-jobs"

    re = requests.get(url, headers=headers, timeout=5000)
    soup = BeautifulSoup(re.text, "html.parser")
    try:
        li = soup.find("div", class_="container").find(
            "table", id="jobsboard").find_all("tr", class_="job")
        print(f"REM - {job} scrapping...")
        for i in li:
            company = i.find("span", class_="companyLink").text
            title = i.find("h2", itemprop="title").text
            link = i.find("a")["href"]
            time = i.find("td", class_="time").text
            list = {
                "title": title,
                "company": company,
                "link": f"https://remoteok.io{link}",
                "time": time
            }
            result.append(list)
    except:
        result = []
    return result

import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt


class Histogram():

    def __init__(self):
        self.dict = {}

    def add(self, key):
        if key not in self.dict.keys():
            self.dict[key] = 1
        else:
            self.dict[key] += 1

    def count(self, key):
        if key not in self.dict.keys():
            return None
        return self.dict[key]

    def items(self):
        lst = []
        for key in self.dict.keys():
            lst.append((key, self.dict[key]))
        return lst

    def get_dict(self):
        return self.dict


def make_request(histogram, url_prefix, url_suffix):
    headers = {}
    headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
    r = requests.head(url_prefix + url_suffix, headers=headers, allow_redirects=True, timeout=5)
    histogram.add(r.headers["Server"])
    print(r.headers["Server"])


def crawl_website(histogram, url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    for link in soup.find_all('a'):
        try:
            make_request(histogram, url, link.get('href'))
        except Exception:
            pass


def consolidate_servers(all_dict):
    consolidated = {"nginx": 0, "IIS": 0, "Apache": 0, "lighttpd": 0}
    for key in all_dict.keys():
        for most_common in consolidated.keys():
            if most_common in key:
                consolidated[most_common] += all_dict[key]
    return consolidated

h = Histogram()
crawl_website(h, "http://register.start.bg/")
consolidated = consolidate_servers(h.get_dict())

keys = list(consolidated.keys())
values = list(consolidated.values())

X = list(range(len(keys)))

plt.bar(X, list(consolidated.values()), align="center")
plt.xticks(X, keys)

plt.title(".bg servers")
plt.xlabel("Server")
plt.ylabel("Count")

plt.savefig("histogram.png")

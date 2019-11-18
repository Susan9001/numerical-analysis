import re
import requests
import matplotlib as plt
import numpy as np
import time
import json
from bs4 import BeautifulSoup


class UniversityWebsiteAnalyser:
    valid_url_pattern = re.compile(
        'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')  # static

    def __init__(self, target_website="https://uci.edu"):
        self.target_website = "http://"+target_website.split("://")[1].strip()

    def get_all_url_on_page(self, curr_url:str):
        response = None
        try:
            response = requests.get(curr_url)
        except:
            return None
        page_soup = BeautifulSoup(response.content, 'html.parser')
        url_list = []
        link_list = page_soup.find_all('a')
        for link in link_list:
            link = str(link.get('href')).strip("/")
            if re.match(UniversityWebsiteAnalyser.valid_url_pattern, link):
                if (link.startswith("https")):
                    link = "http://"+link.split("://")[1] # unitize: https=>http
                url_list.append(link)
        # print(url_list)
        return list(set(url_list))

    def set_target_website(self, target_website):
        self.target_website = target_website

    def get_new_adj_matrix(self, n=500):
        A = [[0 for j in range(n)] for i in range(n)]
        all_url_list = [None for _ in range(n)]
        all_url_list[0] = self.target_website
        k = 1 # url index in all_url_list currently
        for i in range(n):
            if all_url_list[i] is None:
                break  # when all url is done
            new_url_list = self.get_all_url_on_page(all_url_list[i])
            if new_url_list is None:
                continue
            m = len(new_url_list)
            for j in range(m):
                try: # link to a url that appeared before
                    pos = all_url_list.index(new_url_list[j])
                except ValueError as e: # link to a new url
                    if k >= n:
                        continue
                    A[i][k] = 1
                    all_url_list[k] = new_url_list[j]
                    k += 1
                else:
                    A[i][pos] = 1
            print("ok! no. %d: %s " % (i, all_url_list[i]), end="")
            print(A[i])
        return (all_url_list, A)


if __name__ == '__main__':
    analyser = UniversityWebsiteAnalyser()
    (urls, A) = analyser.get_new_adj_matrix()
    url_adj_dict = dict(zip(urls, A))
    with open("adj_dict.json", "w") as f:
        json.dump(url_adj_dict, f)

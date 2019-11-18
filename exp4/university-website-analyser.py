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

    def __init__(self, target_website="http://uci.edu"):
        self.target_website = target_website

    def get_all_url_on_page(self, curr_url):
        response = None
        try:
            response = requests.get(curr_url)
        except:
            return None
        else:
            time.sleep(0.5)
        page_soup = BeautifulSoup(response.content, 'html.parser')
        url_list = []
        link_list = page_soup.find_all('a')
        for link in link_list:
            link = str(link.get('href'))
            if re.match(UniversityWebsiteAnalyser.valid_url_pattern, link):
                url_list.append(link)
        # print(url_list)
        return url_list

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
                if k >= n:
                    break
                try: # link to a url appeared before
                    pos = all_url_list.index(new_url_list[j])
                except ValueError as e: # link to a new url
                    A[i][k] = 1
                    all_url_list[k] = new_url_list[j]
                    k += 1
                else:
                    A[i][pos] = 1
            with open("./urls.json", "w") as f:
                json.dump(all_url_list, f)
            with open("./A.json", "w") as f:
                json.dump(A, f)
        return (all_url_list, A)


if __name__ == '__main__':
    analyser = UniversityWebsiteAnalyser()
    (urls, A) = analyser.get_new_adj_matrix(300)
    print(urls)
    print(A)
    with open("./urls.json", "w") as f:
        json.dump(urls, f)
    with open("./A.json", "w") as f:
        json.dump(A, f)

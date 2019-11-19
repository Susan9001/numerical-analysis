import re
import requests
import matplotlib as plt
import numpy as np
import time
import json
import datetime
from bs4 import BeautifulSoup


class UniversityWebsiteAnalyser:
    valid_url_pattern = re.compile(
        "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")  # static

    def __init__(self, target_website="https://uci.edu"):
        self.target_website = "http://"+target_website.split("://")[1].strip()

    def get_url(self, url:str, conn_timeout=5, read_timeout=10, reconnect=2):
        '''return: response'''
        for i in range(reconnect):
            try: response = requests.get(url, timeout=(conn_timeout, read_timeout)) # (conn_timeout, read_timeout)
            except: continue
            else: return response
        return None

    def get_all_url_on_page(self, curr_url:str):
        response = self.get_url(curr_url)
        if response is None:
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
        error = [0 for _ in range(n)] # 1--urls that birngs error in method get; 0--normal

        for i in range(n):
            if i >= n:
                break  # when all url is done
            print("no. %d prdocessing %s" %(i, all_url_list[i]))
            starttime = datetime.datetime.now()
            new_url_list = self.get_all_url_on_page(all_url_list[i])
            time_diff = (datetime.datetime.now() - starttime).seconds
            print("used %ds" % time_diff, end=" ")
            if new_url_list is None:
                error[i] = 1
                print("ops! ")
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
            print("done!", end=" ")
            print(A[i])

        # to exclude erroneous urls
        res_dict = {"url_list": [], "adj_matrix": [] }
        for i in range(n):
            if error[i] == 1:
                continue
            res_dict["url_list"].append(all_url_list[i])
            res_dict["adj_matrix"].append([])
            for j in range(n):
                if error[j] == 1:
                    continue
                res_dict["adj_matrix"][-1].append(A[i][j])
        return res_dict


if __name__ == '__main__':
    # analyser = UniversityWebsiteAnalyser()
    # res_dict = analyser.get_new_adj_matrix(500)
    # with open("adj_dict.json", "w", encoding='utf-8') as f:
    #     json.dump(res_dict, f)

    res_dict = {}
    with open("adj_dict.json", "r", encoding='utf-8') as f:
        res_dict =json.load(f)
    url_list = res_dict.get("url_list")
    adj_matrix = res_dict.get("adj_matrix")
    for i in range(len(url_list)):
        print("%s: %d" %(url_list[i], sum(adj_matrix[i])))
    print(res_dict)


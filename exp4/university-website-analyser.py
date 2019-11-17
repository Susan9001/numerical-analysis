import re
import requests
import matplotlib as plt
import numpy as np
import time
from bs4 import BeautifulSoup

class UniversityWebsiteAnalyser:
    valid_url_pattern = re.compile('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*(),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+') # static

    def __init__(self, target_website="http://www.uci.edu"):
        self.target_website = target_website

    def get_all_url_on_page(self, curr_url):
        page_soup = BeautifulSoup(requests.get(curr_url).content, 'html.parser')
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

    # TODO: 求G

if __name__ == '__main__':
    analyser = UniversityWebsiteAnalyser();
    url_list = analyser.get_all_url_on_page("http://www.uci.edu")
    print(url_list)




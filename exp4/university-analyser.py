import re
import requests
import matplotlib as plt
import numpy as np
import time
from bs4 import BeautifulSoup


if __name__ == '__main__':
    page_soup = BeautifulSoup(requests.get("http://www.uci.edu").content, 'html.parser')
    # web_pattern_1 = re.compile('http?://(.*?\.uci?.*?)/?[\'\"]')
    # web_pattern_2 = re.compile("<a href=[\'\"]/(.*?)/?[\"\']")
    url_list = []
    link_list = page_soup.find_all('a')
    for link in link_list:
        # TODO: 检查URL合法性
        url_list.append(link)





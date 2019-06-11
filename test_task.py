#!/usr/bin/env python
# coding: utf-8
"""Please run one by one"""

import requests
import urllib3

import pandas as pd
import datetime

from threading import Thread


def get_namefake():
    """Call the site with names"""
    while len(req) < 100:
        if len(req) >= 100:
            break
        responce_url = requests.get(url=url_namefaker, verify=False, timeout=None)
        data = responce_url.json()
        req.append(1)
        words.extend(data['name'].split(" "))


def most_common_words(words, number_show_word):
    """Generate .csv file with most common words"""
    s = pd.Series(words)
    s.value_counts().head(number_show_word).to_csv(path_or_buf="result.csv", header=False)


th1, th2, th3, th4 = Thread(target=get_namefake), Thread(target=get_namefake), Thread(target=get_namefake), Thread(
    target=get_namefake)
th5, th6, th7, th8 = Thread(target=get_namefake), Thread(target=get_namefake), Thread(target=get_namefake), Thread(
    target=get_namefake)

if __name__ == "__main__":
    urllib3.disable_warnings()  # ignore not secure requests
    url_namefaker = "http://api.namefake.com"  # site api's url address
    words = []  # collect words from name string
    req = []  # counting the number of request
    start = datetime.datetime.now()
    th1.start(), th2.start(), th3.start(), th4.start()
    th5.start(), th6.start(), th7.start(), th8.start()
    th1.join(), th2.join(), th3.join(), th4.join()
    th5.join(), th6.join(), th7.join(), th8.join()
    most_common_words(words, 10)
    finish = datetime.datetime.now()
    print((finish - start).seconds)

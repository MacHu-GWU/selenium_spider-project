#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Because Google Chrome is my favorite webbrower. So in this tutorial we use Chrome.
To use google chrome via webdriver, you have to download one first. Here it is
https://sites.google.com/a/chromium.org/chromedriver/. Usually the version 
should be matched. But you could always use the lastest one in general.
"""

import time
from selenium_tutorial import driver


def open_and_visit():
    """Let's open a browser and vist some sites.
    """
    url_list = [
        "https://www.python.org/", 
        "https://www.google.com/",
        "https://www.apple.com/",
    ]
    
    for url in url_list:
        driver.get(url)
        time.sleep(1.0)
    driver.close() # 关闭Driver
    driver.quit() # 关闭进程
    
open_and_visit()


def get_html():
    driver.get("https://www.python.org/")
    html = driver.page_source # 获得Html
    driver.quit()
    
get_html()
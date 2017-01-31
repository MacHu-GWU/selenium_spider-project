#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium_spider import ChromeSpider

spider = ChromeSpider(executable_path="chromedriver.exe")
with spider as spider:
    html = spider.get_html("https://www.python.org/")
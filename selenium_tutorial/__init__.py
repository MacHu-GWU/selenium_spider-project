#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
selenium-python doc: http://selenium-python.readthedocs.org/
"""

from selenium import webdriver

chrome_executable_path = __file__.replace("__init__.py", "chromedriver.exe")
driver = webdriver.Chrome(executable_path=chrome_executable_path)
driver.set_page_load_timeout(10.0)
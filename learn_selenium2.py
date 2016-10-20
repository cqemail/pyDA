# !/usr/bin/python
# -*- coding: utf-8 -*-
# __author__ = c08762

"""learning selenium2"""

from selenium import webdriver


# driver = webdriver.Firefox(executable_path = '/home/c08762/ProgramFiles/drivers/geckodriver')
driver = webdriver.Firefox()
driver.get('https://www.baidu.com')
driver.find_element_by_id('kw').send_keys('selenium2')
driver.find_element_by_id('su').click()
driver.quit()

#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2021/7/14 0014 17:30
# @File: base_page.py
# @Poject: Work_Project
from appium.webdriver.webdriver import WebDriver
from Coded_UI_Test.unit.read_element import ReadInit

class BasePage:
	driver: WebDriver

	def __init__(self, driver: WebDriver = None):
		self.driver = driver
		self.readini = ReadInit()

	def find(self, locator, value: str = None):
		if isinstance(locator, tuple):
			return self.driver.find_element(*locator)
		else:
			return self.driver.find_element(locator, value)
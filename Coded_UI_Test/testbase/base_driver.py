#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2021/7/14 0014 18:27
# @File: base_driver.py
# @Poject: Work_Project
from selenium.webdriver.remote.webdriver import WebDriver
from Coded_UI_Test.unit.read_element import ReadInit


class BaseDriver:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.readini = ReadInit()
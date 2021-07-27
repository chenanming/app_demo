#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2019/11/18 0018 16:48
# @File: search_page.py
# @Poject: Work_Project
from Coded_UI_Test.page.base_page import BasePage


class SearchPage(BasePage):

	def search_icon(self):
		self.driver.find_element_by_xpath("//*[@recource-id, 'com.youshuge.happybook:id/ivSearch']").click()
		return self

	def search(self, keyword):
		self.driver.find_element_by_xpath("//*[@resource-id, 'com.youshuge.happybook:id/etSearch']").send_keys(keyword)
		# self.driver.find_element(By.ID, self.readini.get_value("search_input")).send_keys(keyword)
		return self

	def select(self, index):
		# 关键字，联想列表
		# self.driver.find_element_by_xpath("//*[@resource-id, 'com.youshuge.happybook:id/tvTitle']").click()
		self.driver.find_elements_by_xpath("//*[@resource-id, 'com.youshuge.happybook:id/rvSearch']")[index].click()
		return self
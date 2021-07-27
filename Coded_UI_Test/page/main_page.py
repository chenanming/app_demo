#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2021/7/14 0014 17:32
# @File: main.py
# @Poject: Work_Project
import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Coded_UI_Test.page.base_page import BasePage
from Coded_UI_Test.page.search_page import SearchPage
from Coded_UI_Test.page.user_page import UserPage

class MainPage(BasePage):
	_search_but = 'com.youshuge.happybook:id/ivSearch'

	def book_details(self):
		pass

	def bookcase_page(self):
		pass

	def user_page(self):
		''' 点击我的，“我的”页面
		'''
		self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
		# self.driver.find_element_by_android_uiautomator(self.value.get_value('UserPage', '我的')).click()
		return UserPage(self.driver)

	def search_page(self):
		''' 点击搜索，进入搜索页面
		'''
		self.driver.find_element(By.ID, self._search_but).click()
		return SearchPage(self.driver)

	def get_toast(self, message):
		''' 验证弹窗提示
		'''
		try:
			toast_loc = ("xpath", ".//*[contains(@text,'%s')]" % message)
			WebDriverWait(self.driver, 100, 0.5).until(EC.presence_of_element_located(toast_loc))
			return True
		except:
			return False

	def get_attribute(self):
		# print(self.driver.find_element_by_id("clickArea").get_attribute("class"))
		print(self.driver.find_element_by_id("com.youshuge.happybook:id/inputPhone").get_attribute("class"))

	def get_page_source(self):
		''' 获取页面信息
		'''
		try:
			text = self.driver.page_source
			logging.info("get page source success")
			return text
		except:
			logging.info("get page source is 'fail'")

	def swipeLeft(self, t=500, n=1):
		''' 向左滑动屏幕
		'''
		l = self.driver.get_window_size()
		x1 = l['width'] * 0.75
		y1 = l['height'] * 0.5
		x2 = l['width'] * 0.25
		for i in range(n):
			self.driver.swipe(x1, y1, x2, y1, t)

	def swipeRight(self, t=500, n=1):
		''' 向右滑动屏幕
		'''
		l = self.driver.get_window_size()
		x1 = l['width'] * 0.25
		y1 = l['height'] * 0.5
		x2 = l['width'] * 0.75
		for i in range(n):
			self.driver.swipe(x1, y1, x2, y1, t)

	def swipeDown(self, t=500, n=1):
		''' 向下滑动屏幕
		'''
		l = self.driver.get_window_size()
		x1 = l['width'] * 0.5
		y1 = l['height'] * 0.35
		y2 = l['height'] * 0.65
		for i in range(n):
			self.driver.swipe(x1, y1, x1, y2, t)

	def swipeUp(self, t=500, n=1):
		''' 向上滑动屏幕
		'''
		l = self.driver.get_window_size()
		x1 = l['width'] * 0.5
		y1 = l['height'] * 0.65
		y2 = l['height'] * 0.35
		for i in range(n):
			self.driver.swipe(x1, y1, x1, y2, t)
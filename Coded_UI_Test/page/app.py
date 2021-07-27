#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2021/7/14 0014 17:27
# @File: app.py
# @Poject: Work_Project
from appium import webdriver
from Coded_UI_Test.page.base_page import BasePage
from Coded_UI_Test.page.main_page import MainPage


class App(BasePage):
	_device = "2507c541"
	# _device = "127.0.0.1:62001"
	_package = "com.youshuge.happybook"
	_activity = "com.youshuge.happybook.ui.SplashActivity"

	def start(self):
		if self.driver is None:
			caps = {}
			caps["platformName"] = "Android"
			caps["deviceName"] = self._device
			caps["appPackage"] = self._package
			caps["appActivity"] = self._activity
			caps["automationName"] = "Uiautomator2"
			caps["autoGrantPermissions"] = True
			caps["noReset"] = True
			caps["unicodeKeyboard"] = True  # 使用unicode编码方式发送字符串
			caps["resetKeyboard"] = True  # 绕过软键盘
			self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
			self.driver.implicitly_wait(15)
		else:
			print(self.driver)
			self.driver.start_activity(self._package, self._activity)
		return self

	def restart(self):
		pass

	def stop(self):
		self.driver.quit()
		return self

	def main(self) -> MainPage:
		return MainPage(self.driver)
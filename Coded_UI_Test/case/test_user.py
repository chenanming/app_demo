#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2021/7/14 0014 17:41
# @File: test_user.py
# @Poject: Work_Project
import allure
from Coded_UI_Test.page.app import App

@allure.feature("测试-登录、退出流程")
class TestLogin:
	'''启动App'''
	def setup(self):
		self.main = App().start().main()

	def teardown(self):
		self.main.user_page().click_set_button(4).click_logout_button()
		self.main.driver.quit()

	def test_wechat_login(self):
		self.main.user_page().click_login_avatar().login_for_wechat()
		assert self.main.get_toast('登录成功') == True

	@allure.story("测试-QQ登录方式")
	def test_qq_login(self):
		''' 测试02：QQ登录'''
		self.main.user_page().click_login_avatar().login_for_qq()
		assert self.main.get_toast('登录成功') == True

	@allure.story("测试-手机号登录方式")
	def test_phone_login(self):
		''' 测试03：手机号验证登录'''
		self.main.user_page().click_login_avatar().phone_input_text('18888888888').code_input_text('666666').check_the_agreement().click_login_button()
		assert self.main.get_toast('登录成功') == True
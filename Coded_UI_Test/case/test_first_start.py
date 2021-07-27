#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2021/7/16 0016 10:44
# @File: test_first_start.py
# @Poject: Work_Project
from Coded_UI_Test.page.app import App

class TestFirstStart:
	def setup(self):
		self.main = App().start().main()

	def teardown(self):
		pass

	def test_first_start_application(self):
		pass
#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2021/7/14 0014 17:40
# @File: test_serch.py
# @Poject: Work_Project
from Coded_UI_Test.page.app import App

class TestSearch:
	def setup(self):
		self.main = App().start().main()

	def teardown(self):
		pass

	def test_search(self):
		self.main.search_page().search_icon().search("超级").select(1)
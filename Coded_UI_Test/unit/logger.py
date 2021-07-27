#!/usr/bin/env python3
# _*_ coding: utf-8 _*_
# @Author: ChenAnming
# @Time: 2020/11/4 0004 10:40
# @File: logger.py
# @Poject: Work_Project
import os
import logging
from datetime import datetime

BASE_PATH = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

class Logger:
    def __init__(self):
        self.logger = logging.getLogger()
        if not self.logger.handlers:
            self.logger.setLevel(logging.INFO)

            # 创建一个handler，用于写入日志文件
            fh = logging.FileHandler(self.log_path, encoding='utf-8')
            fh.setLevel(logging.INFO)

            # 创建一个handler，用于输出到控制台
            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)

            # 定义handler的输出格式
            formatter = logging.Formatter(self.fmt)
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            # 给logger添加handler
            # self.logger.addHandler(fh)
            self.logger.addHandler(ch)  # debug输出到控制台

    @property
    def log_path(self):
        logs_path = os.path.join(BASE_PATH, 'logs')
        if not os.path.exists(logs_path):
            os.makedirs(logs_path)
        now_month = datetime.now().strftime("%Y%m")
        return os.path.join(logs_path, '{}.log'.format(now_month))

    @property
    def fmt(self):
        return '%(levelname)s %(asctime)s %(filename)s:%(lineno)d %(message)s'

log = Logger().logger
if __name__ == '__main__':
    log.info("你好")
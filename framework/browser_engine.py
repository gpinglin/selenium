# -*- coding:utf-8 -*-
"""
封装浏览器的搜索引擎
"""
import configparser
import os
from selenium import webdriver
from framework.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()


class BrowserEngine(object):

    #设置基本路径
    dir = os.path.dirname(os.path.abspath('.'))
    chrrome_driver_path = dir + '/path/chromedriver.exe'

    def __init__(self,driver):
        self.driver = driver

    # 从config中读取browser的类型
    def open_browser(self,driver):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.'))+'/config/config.ini'
        config.read(file_path)

        browser = config.get("browserType","browserName")
        logger.info("You had select %s browser."% browser)
        url = config.get("testServer", "URL")
        logger.info("The test server url is: %s" % url)

        if browser == "FireFox":
            driver = webdriver.Firefox()
            logger.info("Starting firefox browser.")
        elif browser == "Chrome":
            driver = webdriver.Chrome(self.chrrome_driver_path)
            logger.info("Starting Chrome browser.")
        elif browser == "IE":
            driver = webdriver.Ie()
            logger.info("Starting IE browser.")

        driver.get(url)
        logger.info("Open url: %s" % url)
        driver.maximize_window()
        logger.info("Maximize the current window.")
        driver.implicitly_wait(10)
        logger.info("Set implicitly wait 10 seconds.")
        return driver

    #关闭浏览器
    def quit_browser(self):
        logger.info("Now, Close and quit the browser.")
        self.driver.quit()




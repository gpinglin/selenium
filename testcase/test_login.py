# coding = UTF-8
import time
import unittest

from framework.browser_engine import BrowserEngine
from pageobjects.index_page import IndexPage


class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        browser = BrowserEngine(cls)
        cls.driver = browser.open_browser(cls)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_01(self):
        indexpage = IndexPage(self.driver)
        indexpage.login_page('xxxxxxx','xxxxxx')


#if __name__ == '__main__':
    #unittest.main()




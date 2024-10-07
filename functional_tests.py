from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


# test that Django page opens
class BasicInstallTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_home_page_title(self):
        # В браузе открылся сайт по адресу (...)
        # В заголовке написано "NeDorazymenue"  
        self.browser.get('http://127.0.0.1:8000/')
        self.assertIn('Site NeDorazymenue', self.browser.title)
    
    def test_home_page_header(self):
        # В браузе открылся сайт по адресу (...)
        # В заголовке написано "NeDorazymenue" 
        self.browser.get('http://127.0.0.1:8000/')
        header = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertIn('NeDorazymenue', header.text)

    def test_home_page_blog(self):
        self.browser.get('http://127.0.0.1:8000/')
        article_list = self.browser.find_element(By.CLASS_NAME, 'article_list')
        self.assertTrue(article_list)

    def test_home_page_articles_look_correct(self):
        self.browser.get('http://127.0.0.1:8000/')
        article_title = self.browser.find_element(By.CLASS_NAME,
                                                  'article_title')
        article_summary = self.browser.find_element(By.CLASS_NAME,
                                                    'article_summary')
        self.assertTrue(article_title)
        self.assertTrue(article_summary)

    def test_home_page_article_link_opens_article(self):
        self.browser.get('http://127.0.0.1:8000/')
        article_title = self.browser.find_element(By.CLASS_NAME,
                                                  'article_title')
        article_title_text = article_title.text
        article_link = article_title.find_element(By.TAG_NAME, 'a')
        self.browser.get(article_link.get_attribute('href'))
        article_page_title = self.browser.find_element(By.CLASS_NAME,
                                                       'article_title')
        self.assertEqual(article_title_text, article_page_title.text)

       
if __name__ == '__main__':
    unittest.main()

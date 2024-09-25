from selenium import webdriver
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
        self.assertIn('Сайт NeDorazymeune', self.browser.title)
    
    def test_home_page_header(self):
        # В браузе открылся сайт по адресу (...)
        # В заголовке написано "NeDorazymenue" 
        self.browser.get('http://127.0.0.1:8000/')
        header = self.browser.find_elements_by_tag_name('h1')[0]
        self.assertIn('NeDorazymeune', header)


if __name__ == '__main__':
    unittest.main()

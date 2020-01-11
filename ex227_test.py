import unittest
from selenium import webdriver
import page

class TestAutomationpractice(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://automationpractice.com")
    
    def tearDown(self):
        self.driver.quit()
        
    def test_ex227(self):
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches(), "Problème dans le titre de la page"
        main_page.search_txt("chiffon")
        search_results_page = page.SearchResultsPage(self.driver)
        assert search_results_page.is_title_matches(), "Problème dans le titre de la page"
        
if __name__ == "__main__":
    unittest.main()
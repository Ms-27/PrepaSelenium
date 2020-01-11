from locators import MainPageLocators, SearchResultsLocators

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver
    
    def search_txt(self, value):
        field = self.driver.find_element(*MainPageLocators.SEARCH_FIELD)
        field.clear()
        field.send_keys(value)
        button = self.driver.find_element(*MainPageLocators.SEARCH_BUTTON)
        button.click()
        
        
class MainPage(BasePage):
    def is_title_matches(self):
        return "My Store" in self.driver.title
    
class SearchResultsPage(BasePage):
    def is_title_matches(self):
        return "Search" in self.driver.title
    
    def add_in_cart(self):
        element = self.driver.find_element(*SearchResultsLocators.FIRST_ELT_ADD_BUTTON)
        element.click()
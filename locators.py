from selenium.webdriver.common.by import By

class MainPageLocators(object):
    SEARCH_FIELD = (By.ID, 'search_query_top')
    SEARCH_BUTTON = (By.NAME, 'submit_search')
    
class SearchResultsLocators(object):
    FIRST_ELT_ADD_BUTTON = (By.XPATH, "//a[contains(@href,'7&token')]")
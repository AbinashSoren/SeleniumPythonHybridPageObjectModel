from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class SearchPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    valid_hp_product='HP LP3065'
    no_product_message_xpath="//input[@id='button-search']/following-sibling::p"

    def valid_HP_product_is_displayed(self):
        return self.driver.find_element(By.LINK_TEXT,self.valid_hp_product).is_displayed()

    def retieve_no_product_message(self):
        return self.driver.find_element(By.XPATH,self.no_product_message_xpath).text
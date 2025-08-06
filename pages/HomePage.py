from selenium.webdriver.common.by import By

from pages.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.RegisterPage import RegisterPage
from pages.SearchPage import SearchPage


class HomePage(BasePage):
    def __init__(self,driver):
        super().__init__(driver)

    search_box_field_name='search'
    search_button_xpath="//button[contains(@class,'btn-default')]"
    my_account_drop_menu="//span[text()='My Account']"
    register_link_text = "Register"
    login_link_text='Login'

    def enter_product_into_search_box_field(self,product_name):
        self.driver.find_element(By.NAME, self.search_box_field_name).click()
        self.driver.find_element(By.NAME, self.search_box_field_name).clear()
        self.driver.find_element(By.NAME,self.search_box_field_name).send_keys(product_name)

    def click_on_search_button(self):
        self.driver.find_element(By.XPATH,self.search_button_xpath).click()
        return SearchPage(self.driver)

    def click_on_my_account_drop_menu(self):
        self.driver.find_element(By.XPATH,self.my_account_drop_menu).click()

    def click_on_register_link_text(self):
        self.driver.find_element(By.LINK_TEXT, self.register_link_text).click()
        return RegisterPage(self.driver)

    def click_on_login_link_text(self):
        self.driver.find_element(By.LINK_TEXT,self.login_link_text).click()
        return LoginPage(self.driver)
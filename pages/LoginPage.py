from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class LoginPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    input_email_ID='input-email'
    input_password_ID='input-password'
    login_btn_XPATH="//input[@value='Login']"
    edit_account_LINK_TEXT='Edit your account information'
    login_page_error_message='//div[@id="account-login"]/div[1]'

    def enter_credentials_for_login(self,user_id,user_password):
        self.driver.find_element(By.ID,self.input_email_ID).send_keys(user_id)
        self.driver.find_element(By.ID,self.input_password_ID).send_keys(user_password)

    def click_on_login_button(self):
        self.driver.find_element(By.XPATH,self.login_btn_XPATH).click()

    def display_edit_account_link(self):
        return self.driver.find_element(By.LINK_TEXT,self.edit_account_LINK_TEXT).is_displayed()

    def get_login_page_error_message(self):
        return self.driver.find_element(By.XPATH,self.login_page_error_message).text
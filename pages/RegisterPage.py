from selenium.webdriver.common.by import By

from pages.BasePage import BasePage


class RegisterPage(BasePage):

    def __init__(self,driver):
        super().__init__(driver)

    first_name_id="input-firstname"
    last_name_id="input-lastname"
    email_id="input-email"
    telephone_id="input-telephone"
    password_id="input-password"
    confirm_password_id="input-confirm"
    agreed_name="agree"
    continue_btn_xpath="//input[@value='Continue']"
    news_letter_yes_xpath='//input[@value="1"][@name="newsletter"]'
    account_created_message='//div[@id="content"]/h1'

    def enter_first_name(self,first_name):
        self.driver.find_element(By.ID,self.first_name_id).send_keys(first_name)

    def enter_last_name(self,last_name):
        self.driver.find_element(By.ID,self.last_name_id).send_keys(last_name)

    def enter_email_id(self, email):
        self.driver.find_element(By.ID, self.email_id).send_keys(email)

    def enter_telephone(self, phn_number):
        self.driver.find_element(By.ID, self.telephone_id).send_keys(phn_number)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_id).send_keys(password)

    def enter_confirm_password(self, cnf_password):
        self.driver.find_element(By.ID, self.confirm_password_id).send_keys(cnf_password)

    def click_agreed(self):
        self.driver.find_element(By.NAME, self.agreed_name).click()

    def click_continue_btn(self):
        self.driver.find_element(By.XPATH,self.continue_btn_xpath).click()

    def click_yes_new_letter(self):
        self.driver.find_element(By.XPATH,self.news_letter_yes_xpath).click()

    def return_account_created_message(self):
        return self.driver.find_element(By.XPATH,self.account_created_message).text
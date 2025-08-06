from datetime import datetime

import pytest
from selenium.webdriver.common.by import By

from Utilities import ExcelReader
from pages.HomePage import HomePage
from pages.LoginPage import LoginPage
from tests.BaseTest import BaseTest


class Test_Login(BaseTest):

    @pytest.mark.parametrize('email,password',ExcelReader.get_data_from_excel('ExcelFiles/DataDriven.xlsx','TEST'))
    def test_login_with_valid_credentials(self,email,password):

        homePage=HomePage(self.driver)
        homePage.click_on_my_account_drop_menu()
        loginPage=homePage.click_on_login_link_text()
        loginPage.enter_credentials_for_login(email,password)
        loginPage.click_on_login_button()
        assert loginPage.display_edit_account_link()



    def test_login_with_invalid_email_valid_password(self):

        homePage = HomePage(self.driver)
        homePage.click_on_my_account_drop_menu()
        loginPage = homePage.click_on_login_link_text()
        loginPage.enter_credentials_for_login(self.generate_email_time_stamp(),'12345')
        loginPage.click_on_login_button()
        expected_warning_message="Warning: No match for E-Mail Address and/or Password."
        assert loginPage.get_login_page_error_message().__contains__(expected_warning_message)


    def test_login_with_valid_email_invalid_password(self):
        homePage = HomePage(self.driver)
        homePage.click_on_my_account_drop_menu()
        loginPage = homePage.click_on_login_link_text()
        loginPage.enter_credentials_for_login(self.generate_email_time_stamp(), '22323')
        loginPage.click_on_login_button()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert loginPage.get_login_page_error_message().__contains__(expected_warning_message)


    def test_login_without_any_credentials(self):
        homePage = HomePage(self.driver)
        homePage.click_on_my_account_drop_menu()
        loginPage = homePage.click_on_login_link_text()
        loginPage.enter_credentials_for_login("", '')
        loginPage.click_on_login_button()
        expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
        assert loginPage.get_login_page_error_message().__contains__(expected_warning_message)



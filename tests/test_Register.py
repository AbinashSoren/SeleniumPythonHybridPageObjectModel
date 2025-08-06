import time
from datetime import datetime

import pytest
from selenium.webdriver.common.by import By

from pages.HomePage import HomePage
from pages.RegisterPage import RegisterPage
from tests.BaseTest import BaseTest


class Test_Register(BaseTest):
    def test_create_account_with_mandatory_fields(self):

        homePage = HomePage(self.driver)
        homePage.click_on_my_account_drop_menu()

        register=homePage.click_on_register_link_text()
        register.enter_first_name('Abinash')
        register.enter_last_name('Soren')
        register.enter_email_id(self.generate_email_time_stamp())
        register.enter_telephone('1234567890')
        register.enter_password('12345')
        register.enter_confirm_password('12345')
        register.click_agreed()
        register.click_continue_btn()
        assert register.return_account_created_message().__eq__('Your Account Has Been Created!')



    def test_create_account_with_all_fields(self):
        homePage = HomePage(self.driver)
        homePage.click_on_my_account_drop_menu()


        register = homePage.click_on_register_link_text()
        register.enter_first_name('Abinash')
        register.enter_last_name('Soren')
        register.enter_email_id(self.generate_email_time_stamp())
        register.enter_telephone('1234567890')
        register.enter_password('12345')
        register.enter_confirm_password('12345')
        register.click_yes_new_letter()
        register.click_agreed()
        register.click_continue_btn()
        assert register.return_account_created_message().__eq__('Your Account Has Been Created!')

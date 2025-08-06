import pytest
from selenium.webdriver.common.by import By

from pages.HomePage import HomePage
from pages.SearchPage import SearchPage
from tests.BaseTest import BaseTest


class Test_Search(BaseTest):
    def test_search_for_a_valid_product(self):

        home_page= HomePage(self.driver)
        home_page.enter_product_into_search_box_field('HP')
        searchpg=home_page.click_on_search_button()
        assert searchpg.valid_HP_product_is_displayed()



    def test_search_for_a_invalid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field('Honda')
        searchpg =home_page.click_on_search_button()
        expectedTextMessage='There is no product that matches the search criteria'
        assert searchpg.retieve_no_product_message().__contains__(expectedTextMessage)



    def test_search_without_a_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_box_field('')
        searchpg = home_page.click_on_search_button()
        expectedTextMessage = 'There is no product that matches the search criteria'
        assert searchpg.retieve_no_product_message().__contains__(expectedTextMessage)

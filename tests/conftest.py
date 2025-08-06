import pytest
from selenium import webdriver

from Utilities import ReadConfigurations


@pytest.fixture()
def setup_and_teardown(request):
    # global driver
    if ReadConfigurations.read_configurations('basic info','browser').__eq__('chrome'):
        driver=webdriver.Chrome()
    else:
        driver = webdriver.Edge()
    driver.maximize_window()
    app_url=ReadConfigurations.read_configurations('basic info','url')
    # print("----"*20+app_url+"----"*20)
    driver.get(app_url)
    request.cls.driver=driver
    yield
    driver.quit()
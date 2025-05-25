import allure
import pytest
from selenium import webdriver


@pytest.fixture
def browser():
    with allure.step("Открыть браузер"):
        driver = webdriver.Chrome()
    yield driver
    with allure.step("Закрыть браузер"):
        driver.quit()

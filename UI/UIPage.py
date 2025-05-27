import allure
from config import UI_URL
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class UIPage:
    def __init__(self, driver):
        self._driver = driver
        self._driver.get(UI_URL)
        self._driver.maximize_window()

    # Заголовок на главной страницы
    def home_page(self):
        title_hp = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '.kinopoisk-header-logo__img'))
                ).get_attribute('alt')
        return title_hp

    # Ввести названия фильма Мастер и Маргарита
    def name_film(self):
        film = WebDriverWait(self._driver, 20).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '[name="kp_query"]')))
        film.send_keys("Мастер и Маргарита")
        return film

    # Просмотреть результат поиска фильма Мастер и Маргарита
    def result_film(self):
        seach_film = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '#suggest-item-film-1115471'))).text
        return seach_film

    # Нажать кнопку Войти
    def click_button_login(self):
        login = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '.styles_loginButton__LWZQp')))
        login.click()
        self.screenshot("click_button_login")

    # Найти заголовок страницы Войти
    def search_title_login(self):
        button_login = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '.passp-add-account-page-title'))).text
        return button_login

    # Нажать кнопку "Смотреть кино бесплатно"
    def click_film_free(self):
        film_free = WebDriverWait(self._driver, 15).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, '.style_buttonLight____6ma')))
        film_free.click()
        self.screenshot("click_film_free")

    # Найти заголовок страницы "Смотреть кино бесплатно"
    def search_film_free(self):
        title_film_free = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '.passp-add-account-page-title'))).text
        return title_film_free

    # Нажать кнопку "Лупа"
    def click_random_search(self):
        random_search = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((
                By.CSS_SELECTOR, '.search-form-submit-button__icon')))
        random_search.click()

    # Нажать кнопку "Случайный фильм"
    def click_random_film(self):
        button_random_film = WebDriverWait(self._driver, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#search')))
        button_random_film.click()
        self.screenshot("click_random_film")

    # Сделать скриншот результата заданного шага
    def screenshot(self, test_name: str):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshots/{test_name}_{timestamp}.png"
        self._driver.save_screenshot(filename)
        allure.attach.file(
            filename,
            name=f"Screenshot: {test_name}",
            attachment_type=allure.attachment_type.PNG
        )


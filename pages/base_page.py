import time

import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .main_functions import проверка_ссылки
from .main_settings import MAIN_URL


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url.get("link_page").strip()

        проверка_ссылки(MAIN_URL + self.url)
        self.open_url()

        self.ожидание_прогрузки_страницы()
        with allure.step("Открытие страницы"):
            allure.attach(MAIN_URL + self.url,
                          name="Ссылка")
            allure.attach(self.browser.get_screenshot_as_png(),
                          name='screenshot',
                          attachment_type=AttachmentType.PNG)

    def open_url(self):
        """
        открывает ссылку внутри (авторизированному пользователю)
        :return:
        """

        url = MAIN_URL + self.url
        self.browser.get(url)
        self.ожидание_прогрузки_страницы()

    def is_element_present(self, how, what, timeout=5):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
            # self.browser.find_element(how, what)
        except:
            return False
        return True

    def ожидание_прогрузки_страницы(self):
        loadind = True
        try:
            while loadind:
                self.browser.find_element(By.CSS_SELECTOR, ".loading")
                time.sleep(0.5)
        except:
            pass

    def проверка_url_в_адресной_строке(self, url):
        self.ожидание_прогрузки_страницы()
        current_url = self.browser.current_url
        assert url == current_url, \
            f"""Не та страница
            ♦Ожидалось: {url}
            ♦Открылось: {current_url}"""

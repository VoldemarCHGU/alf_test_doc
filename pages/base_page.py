from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .main_settings import MAIN_URL
import time
from .main_functions import f_logging

class BasePage():
    def __init__(self, browser, url, tariff):
        self.browser = browser
        self.url = url.get("link_page").strip()
        # self.tariff = tariff
        self.авторизация(tariff)

        # self.browser.implicitly_wait(timeout)

    def авторизация(self, tariff):
        f_logging(self.browser, tariff)

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
                time.sleep(1)
        except:
            pass





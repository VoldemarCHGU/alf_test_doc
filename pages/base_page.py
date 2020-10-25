import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from .main_settings import MAIN_URL


class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url.get("link_page").strip()
        self.open_url()

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

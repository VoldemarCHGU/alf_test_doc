from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException

from .base_page import BasePage
from .knowledge_locators import KnowledgeLocators
import urllib.request
import time
from .knowledge.knowledge_functions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class KnowledgePageBeforeMoving(BasePage):

    def есть_синяя_плашка(self):
        assert self.is_element_present(
            *KnowledgeLocators.HELP_CONTAINER), "Нет синей плашки"

    def есть_текст_в_плашке(self):
        assert self.is_element_present(
            *KnowledgeLocators.HELP_TEXT), "Нет текста в синей плашке"

    def ссылка_в_синей_плашке(self):
        assert self.is_element_present(
            *KnowledgeLocators.HELP_LINK), "Не найдена кнопка для 'Перехода в Базу знаний'"

    def работоспособность_ссылки(self):
        help_link = self.browser.find_element(*KnowledgeLocators.HELP_LINK)
        zapros = urllib.request.urlopen(help_link.get_attribute("href")).getcode()
        assert zapros == 200, f"Запрос вернул код {zapros}"

    def переход_в_базу_знаний(self, data):
        type_page = data.get("type_page")
        zagolovok_in_knowledge_in_json = data.get("zagolovok_in_knowledge")

        self.browser, current_window = переход_на_вкладку_с_БЗ(self.browser, *KnowledgeLocators.HELP_LINK)
        zagolovok_in_knowledge = получить_заголовок_в_базе_знаний(self.browser, KnowledgeLocators)

        assert zagolovok_in_knowledge == zagolovok_in_knowledge_in_json, \
            f"в БЗ и json не совпадают: \n" \
            f"{zagolovok_in_knowledge}\n" \
            f"{zagolovok_in_knowledge_in_json}"

        self.browser.close()
        self.browser.switch_to.window(current_window)

        if type_page == "step_page":
            need_text = получить_заголовок_до_перехода_в_базу_знаний(self.browser, KnowledgeLocators)
            self.проверить_заголовок_в_базе_знаний_с_шагом_на_странице(need_text, zagolovok_in_knowledge)
        elif type_page == "simple_page":
            pass
        else:
            assert False, "В данных отсутствует тип страницы: simple or step"

    def проверить_заголовок_в_базе_знаний_с_шагом_на_странице(self, need_text, zagolovok_in_knowledge):
        assert need_text in zagolovok_in_knowledge, \
            f"Заголовок в БЗ не совпадает с полученным результатом:\n " \
            f"{need_text} \n {zagolovok_in_knowledge}"

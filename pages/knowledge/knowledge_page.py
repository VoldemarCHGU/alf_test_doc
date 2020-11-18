from pages.base_page import BasePage
from pages.knowledge.knowledge_functions import *
from .knowledge_locators import KnowledgeLocators
from pages.main_functions import проверка_ссылки
from pages.main_settings import MAIN_URL


class KnowledgePageBeforeMoving(BasePage):

    def есть_синяя_плашка(self, data):
        assert self.is_element_present(
            *KnowledgeLocators.HELP_CONTAINER), f"Нет синей плашки \n {data}"

    def есть_текст_в_плашке(self):
        assert self.is_element_present(
            *KnowledgeLocators.HELP_TEXT), "Нет текста в синей плашке"

    def ссылка_в_синей_плашке(self):
        assert self.is_element_present(
            *KnowledgeLocators.HELP_LINK), "Не найдена кнопка для 'Перехода в Базу знаний'"

    def работоспособность_ссылки(self, data, тариф_для_проверки):
        """
        + проверка соответствия ссылки для перехода в БЗ с json
        + проверка запроса на ссылку (ожидается 200)
        """
        bttn_help_link = self.browser.find_element(*KnowledgeLocators.HELP_LINK)
        help_link = bttn_help_link.get_attribute("href")
        data_tariff = data.get(тариф_для_проверки)
        help_link_in_json = (MAIN_URL + data_tariff.get("link_bz")).strip()
        assert help_link == help_link_in_json, f"Cсылка в кнопке не совпадает с json (link_bz) \n " \
                                               f"{help_link}\n" \
                                               f"{help_link_in_json}\n" \
                                               f"{data}"
        проверка_ссылки(help_link)

    def переход_в_базу_знаний(self, data, тариф_для_проверки):
        """
        + проверка заголовка в БЗ с json
        + проверка заголовка с шагом с БЗ (если step_page)

        """
        type_page = data.get("type_page")
        need_data = data.get(тариф_для_проверки)
        self.browser, zagolovok_in_knowledge = self.проверить_заголовок_в_базе_знаний_с_заголовком_в_json(self.browser,
                                                                                                          need_data)
        if type_page == "step_page":
            need_text = получить_заголовок_до_перехода_в_базу_знаний(self.browser, KnowledgeLocators)
            self.проверить_заголовок_в_базе_знаний_с_шагом_на_странице(need_text, zagolovok_in_knowledge)

        self.проверить_список_страниц_этого_раздела()

    def проверить_заголовок_в_базе_знаний_с_шагом_на_странице(self, need_text, zagolovok_in_knowledge):
        assert need_text in zagolovok_in_knowledge, \
            f"Заголовок в БЗ не совпадает с полученным результатом:\n " \
            f"{need_text} \n {zagolovok_in_knowledge}"

    def проверить_заголовок_в_базе_знаний_с_заголовком_в_json(self, browser, data):
        zagolovok_in_knowledge_in_json = data.get("zagolovok_in_knowledge")
        browser, current_window = переход_на_вкладку_с_БЗ(browser, KnowledgeLocators.HELP_LINK)
        zagolovok_in_knowledge = получить_заголовок_в_базе_знаний(browser, KnowledgeLocators)
        assert zagolovok_in_knowledge == zagolovok_in_knowledge_in_json, \
            f"заголовок в БЗ и json не совпадают: \n" \
            f"{zagolovok_in_knowledge}\n" \
            f"{zagolovok_in_knowledge_in_json}" \
            f"\n{data}"
        browser.close()
        browser.switch_to.window(current_window)
        return browser, zagolovok_in_knowledge

    def проверить_список_страниц_этого_раздела(self):
        try:
            self.browser.find_element(*KnowledgeLocators.SPISOK_PAGES_THIS_RAZDEL)
            pages = self.browser.find_elements(*KnowledgeLocators.PAGES_THIS_RAZDEL)
            for page in pages:
                link = page.get_attribute("href")
                проверка_ссылки(link)
        except:
            pass

import allure
import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver

from pages.knowledge.knowledge_functions import проверка_на_skip_test
from pages.knowledge.knowledge_locators import KnowledgeLocators
from pages.knowledge.knowledge_page import KnowledgePageBeforeMoving


@pytest.mark.AFD_5840
@pytest.mark.knowledge1
@allure.epic("Прверка БЗ")
@allure.feature("Проверка БЗ для ПДН.БЮДЖЕТ.ЭКСПЕРТ")
@allure.severity('minor')
class TestKnowledge1():
    @pytest.mark.parametrize('data1', KnowledgeLocators.DATA_TARIFF_ПДН_БЮДЖЕТ_ЭКСПЕРТ)
    def test_проверка_перехода_в_базу_знаний_ПДН_БЮДЖЕТ_ЭКСПЕРТ(self, browser_ПДН_БЮДЖЕТ_ЭКСПЕРТ, data1):
        browser_ПДН_БЮДЖЕТ_ЭКСПЕРТ: WebDriver
        тариф_для_проверки = (data1, "ПДН.БЮДЖЕТ.ЭКСПЕРТ")
        page = KnowledgePageBeforeMoving(browser_ПДН_БЮДЖЕТ_ЭКСПЕРТ, data1)
        page.есть_синяя_плашка(data1)
        page.есть_текст_в_плашке()
        page.ссылка_в_синей_плашке()
        page.работоспособность_ссылки_в_кнопке_бз(*тариф_для_проверки)
        page.переход_в_базу_знаний(*тариф_для_проверки)


@pytest.mark.AFD_5840
@pytest.mark.knowledge2
@allure.epic("Прверка БЗ")
@allure.feature("Проверка БЗ для КИИ.СТАНДАРТ")
@allure.severity('minor')
class TestKnowledge2():
    @pytest.mark.parametrize('data2', KnowledgeLocators.DATA_TARIFF_КИИ_СТАНДАРТ)
    def test_проверка_перехода_в_базу_знаний_КИИ_СТАНДАРТ(self, browser_КИИ_СТАНДАРТ, data2):
        browser_ПДН_БЮДЖЕТ_ЭКСПЕРТ: WebDriver
        тариф_для_проверки = (data2, "КИИ.СТАНДАРТ")
        page = KnowledgePageBeforeMoving(browser_КИИ_СТАНДАРТ, data2)
        page.есть_синяя_плашка(data2)
        page.есть_текст_в_плашке()
        page.ссылка_в_синей_плашке()
        page.работоспособность_ссылки_в_кнопке_бз(*тариф_для_проверки)
        page.переход_в_базу_знаний(*тариф_для_проверки)


@pytest.mark.AFD_5840
@pytest.mark.knowledge3
@allure.epic("Прверка БЗ")
@allure.feature("Проверка БЗ для КИИ.ГИС.ПДН.БЮДЖЕТ.ЭКСПЕРТ")
@allure.severity('minor')
class TestKnowledge3():
    @pytest.mark.parametrize('data3', KnowledgeLocators.DATA_TARIFF_КИИ_ГИС_ПДН_БЮДЖЕТ_ЭКСПЕРТ)
    def test_проверка_перехода_в_базу_знаний_КИИ_ГИС_ПДН_БЮДЖЕТ_ЭКСПЕРТ(self, browser_КИИ_ГИС_ПДН_БЮДЖЕТ_ЭКСПЕРТ,
                                                                        data3):
        тариф_для_проверки = (data3, "КИИ.ГИС.ПДН.БЮДЖЕТ.ЭКСПЕРТ")
        проверка_на_skip_test(*тариф_для_проверки)
        page = KnowledgePageBeforeMoving(browser_КИИ_ГИС_ПДН_БЮДЖЕТ_ЭКСПЕРТ, data3)
        page.есть_синяя_плашка(data3)
        page.есть_текст_в_плашке()
        page.ссылка_в_синей_плашке()
        page.работоспособность_ссылки_в_кнопке_бз(*тариф_для_проверки)
        page.переход_в_базу_знаний(*тариф_для_проверки)


@pytest.mark.AFD_5840
@pytest.mark.knowledge4
@allure.epic("Прверка БЗ")
@allure.feature("Проверка БЗ для КИИ.ПДН.ЭКСПЕРТ")
@allure.severity('minor')
class TestKnowledge4():
    @pytest.mark.parametrize('data4', KnowledgeLocators.DATA_TARIFF_КИИ_ПДН_ЭКСПЕРТ)
    def test_проверка_перехода_в_базу_знаний_КИИ_ПДН_ЭКСПЕРТ(self, browser_КИИ_ПДН_ЭКСПЕРТ, data4):
        тариф_для_проверки = (data4, "КИИ.ПДН.ЭКСПЕРТ")
        проверка_на_skip_test(*тариф_для_проверки)
        page = KnowledgePageBeforeMoving(browser_КИИ_ПДН_ЭКСПЕРТ, data4)
        page.есть_синяя_плашка(data4)
        page.есть_текст_в_плашке()
        page.ссылка_в_синей_плашке()
        page.работоспособность_ссылки_в_кнопке_бз(*тариф_для_проверки)
        page.переход_в_базу_знаний(*тариф_для_проверки)


@pytest.mark.AFD_5840
@pytest.mark.knowledge5
@allure.epic("Прверка БЗ")
@allure.feature("Проверка БЗ для ГИС.ЭКСПЕРТ")
@allure.severity('minor')
class TestKnowledge5():
    @pytest.mark.parametrize('data5', KnowledgeLocators.DATA_TARIFF_ГИС_ЭКСПЕРТ)
    def test_проверка_перехода_в_базу_знаний_ГИС_ЭКСПЕРТ(self, browser_ГИС_ЭКСПЕРТ, data5):
        тариф_для_проверки = (data5, "ГИС.ЭКСПЕРТ")
        проверка_на_skip_test(*тариф_для_проверки)
        page = KnowledgePageBeforeMoving(browser_ГИС_ЭКСПЕРТ, data5)
        page.есть_синяя_плашка(data5)
        page.есть_текст_в_плашке()
        page.ссылка_в_синей_плашке()
        page.работоспособность_ссылки_в_кнопке_бз(*тариф_для_проверки)
        page.переход_в_базу_знаний(*тариф_для_проверки)


@pytest.mark.AFD_5840
@pytest.mark.knowledge6
@allure.epic("Прверка БЗ")
@allure.feature("Проверка БЗ для ГИС.ПДН.БЮДЖЕТ.ЭКСПЕРТ")
@allure.severity('minor')
class TestKnowledge6():
    @pytest.mark.parametrize('data6', KnowledgeLocators.DATA_TARIFF_ГИС_ПДН_БЮДЖЕТ_ЭКСПЕРТ)
    def test_проверка_перехода_в_базу_знаний_ГИС_ПДН_БЮДЖЕТ_ЭКСПЕРТ(self, browser_ГИС_ПДН_БЮДЖЕТ_ЭКСПЕРТ, data6):
        тариф_для_проверки = (data6, "ГИС.ПДН.БЮДЖЕТ.ЭКСПЕРТ")
        проверка_на_skip_test(*тариф_для_проверки)
        page = KnowledgePageBeforeMoving(browser_ГИС_ПДН_БЮДЖЕТ_ЭКСПЕРТ, data6)
        page.есть_синяя_плашка(data6)
        page.есть_текст_в_плашке()
        page.ссылка_в_синей_плашке()
        page.работоспособность_ссылки_в_кнопке_бз(*тариф_для_проверки)
        page.переход_в_базу_знаний(*тариф_для_проверки)

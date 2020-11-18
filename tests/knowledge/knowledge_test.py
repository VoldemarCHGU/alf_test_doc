import pytest

from pages.knowledge.knowledge_functions import проверка_на_skip_test
from pages.knowledge.knowledge_locators import KnowledgeLocators
from pages.knowledge.knowledge_page import KnowledgePageBeforeMoving

@pytest.mark.AFD_5840
@pytest.mark.knowledge1
@pytest.mark.parametrize('data', KnowledgeLocators.DATA_TARIFF_ПДН_БЮДЖЕТ_ЭКСПЕРТ, )
class TestKnowledge1():
    def test_проверка_перехода_в_базу_знаний_ПДН_БЮДЖЕТ_ЭКСПЕРТ(self, browser1, data):
        тариф_для_проверки = (data, "ПДН.БЮДЖЕТ.ЭКСПЕРТ")
        page = KnowledgePageBeforeMoving(browser1, data)
        page.есть_синяя_плашка()
        page.есть_текст_в_плашке()
        page.ссылка_в_синей_плашке()
        page.работоспособность_ссылки(*тариф_для_проверки)
        page.переход_в_базу_знаний(*тариф_для_проверки)

@pytest.mark.AFD_5840
@pytest.mark.knowledge2
class TestKnowledge2():
    @pytest.mark.parametrize('data', KnowledgeLocators.DATA_TARIFF_КИИ_СТАНДАРТ)
    def test_проверка_перехода_в_базу_знаний_КИИ_СТАНДАРТ(self, browser2, data):
        тариф_для_проверки = (data, "КИИ.СТАНДАРТ")
        page = KnowledgePageBeforeMoving(browser2, data)
        page.есть_синяя_плашка()
        page.есть_текст_в_плашке()
        page.ссылка_в_синей_плашке()
        page.работоспособность_ссылки(*тариф_для_проверки)
        page.переход_в_базу_знаний(*тариф_для_проверки)

@pytest.mark.AFD_5840
@pytest.mark.knowledge3
class TestKnowledge3():
    @pytest.mark.parametrize('data', KnowledgeLocators.DATA_TARIFF_КИИ_ГИС_ПДН_БЮДЖЕТ_ЭКСПЕРТ)
    def test_проверка_перехода_в_базу_знаний_КИИ_ГИС_ПДН_БЮДЖЕТ_ЭКСПЕРТ(self, browser_КИИ_ГИС_ПДН_БЮДЖЕТ_ЭКСПЕРТ, data):
        тариф_для_проверки = (data, "КИИ.ГИС.ПДН.БЮДЖЕТ.ЭКСПЕРТ")
        проверка_на_skip_test(*тариф_для_проверки)
        page = KnowledgePageBeforeMoving(browser_КИИ_ГИС_ПДН_БЮДЖЕТ_ЭКСПЕРТ, data)
        page.есть_синяя_плашка(data)
        page.есть_текст_в_плашке()
        page.ссылка_в_синей_плашке()
        page.работоспособность_ссылки(*тариф_для_проверки)
        # page.переход_в_базу_знаний(*тариф_для_проверки)


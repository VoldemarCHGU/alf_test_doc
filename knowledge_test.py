import pytest
from .pages.knowledge_locators import KnowledgeLocators
from .pages.knowledge_page import KnowledgePageBeforeMoving


@pytest.mark.knowledge
class TestKnowledge1():
    @pytest.mark.parametrize('data', KnowledgeLocators.DATA_TARIFF_ПДН_БЮДЖЕТ_ЭКСПЕРТ, )
    def test_проверка_перехода_в_базу_знаний_ПДН_БЮДЖЕТ_ЭКСПЕРТ(self, browser1, data):
        тариф_для_проверки = (data, "ПДН.БЮДЖЕТ.ЭКСПЕРТ")
        page = KnowledgePageBeforeMoving(browser1, data)
        page.open_url()
        page.есть_синяя_плашка()
        page.есть_текст_в_плашке()
        page.ссылка_в_синей_плашке()
        page.работоспособность_ссылки(*тариф_для_проверки)
        page.переход_в_базу_знаний(*тариф_для_проверки)

@pytest.mark.knowledge
class TestKnowledge2():
    @pytest.mark.parametrize('data', KnowledgeLocators.DATA_TARIFF_КИИ_СТАНДАРТ)
    def test_проверка_перехода_в_базу_КИИ_СТАНДАРТ(self, browser2, data):
        тариф_для_проверки = (data, "КИИ.СТАНДАРТ")
        page = KnowledgePageBeforeMoving(browser2, data)
        page.open_url()
        page.есть_синяя_плашка()
        page.есть_текст_в_плашке()
        page.ссылка_в_синей_плашке()
        page.работоспособность_ссылки(*тариф_для_проверки)
        page.переход_в_базу_знаний(*тариф_для_проверки)





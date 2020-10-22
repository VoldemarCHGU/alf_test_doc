import pytest
from .pages.knowledge_page import KnowledgePageBeforeMoving
from .pages.knowledge_locators import KnowledgeLocators

@pytest.mark.knowledge
class TestKnowledge():


    @pytest.mark.parametrize('data', KnowledgeLocators.DATA_TARIFF_ПДН_БЮДЖЕТ_ЭКСПЕРТ)
    def test_проверка_перехода_в_базу_знаний_ПДН_БЮДЖЕТ_ЭКСПЕРТ(self, browser, data):
        page = KnowledgePageBeforeMoving(browser, data.get("link_page").strip())
        page.open_url()
        page.есть_синяя_плашка()
        page.есть_текст_в_плашке()
        page.ссылка_в_синей_плашке()
        page.работоспособность_ссылки()
        page.переход_в_базу_знаний(data)

    @pytest.mark.parametrize('data', KnowledgeLocators.DATA_TARIFF_КИИ_СТАНДАРТ)
    def test_проверка_перехода_в_базу_КИИ_СТАНДАРТ(self, browser, data):
        page = KnowledgePageBeforeMoving(browser, data.get("link_page").strip())
        page.open_url()
        page.есть_синяя_плашка()
        page.есть_текст_в_плашке()
        page.ссылка_в_синей_плашке()
        page.работоспособность_ссылки()
        page.переход_в_базу_знаний(data)


import pytest
from .pages.knowledge_page import KnowledgePageBeforeMoving
from .pages.knowledge_locators import KnowledgeLocators

@pytest.mark.knowledge
class TestKnowledge():


    @pytest.mark.parametrize('data', KnowledgeLocators.DATA_PDN_TARIFF)
    def test_проверка_перехода_в_базу_знаний_ПДН_тариф(self, browser, data):
        page = KnowledgePageBeforeMoving(browser, data.get("link_page").strip())
        page.open_url()
        page.есть_синяя_плашка()
        page.есть_текст_в_плашке()
        page.ссылка_в_синей_плашке()
        page.работоспособность_ссылки()
        page.переход_в_базу_знаний(data)















    # @pytest.mark.parametrize('data', KnowledgeLocators.DATA_MAX_TARIFF)
    # def test_проверка_перехода_в_базу_знаний_макс_тариф(self,browser, data):
    #     page = KnowledgePageBeforeMoving(browser, data.get("link"))
    #     page.open_url()
    #
    #     page.есть_синяя_плашка()
    #     page.есть_текст_в_плашке()
    #     page.ссылка_в_синей_плашке()
    #     page.работоспособность_ссылки()
    #     page.переход_в_базу_знаний(data.get("type_page"), data.get("zagolovok_in_knowledge"))

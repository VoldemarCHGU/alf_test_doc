from selenium.webdriver.common.by import By
from .knowledge.knowledge_functions import *


class KnowledgeLocators():
    HELP_CONTAINER = (By.CSS_SELECTOR, ".help-wrapper > .help-container")
    HELP_TEXT = (By.CSS_SELECTOR, ".help-container > .alert.alert-info > div:nth-child(1) > p:nth-child(1)")
    HELP_LINK = (By.CSS_SELECTOR, ".help-container > .alert.alert-info > div:nth-child(2) > a")
    # DATA_MAX_TARIFF = get_data_on_tariff("max")
    DATA_PDN_TARIFF = get_data_on_tariff("ПДН")
    ZAGOLOVOK_IN_KNOWLEDGE = (By.CSS_SELECTOR, ".page-content > h3")
    STEP_IN_STEPPAGE = (By.CSS_SELECTOR, "ul.wizard-steps li.active > a span.step-number > span")
    NAME_IN_STEPPAGE = (By.CSS_SELECTOR, "ul.wizard-steps li.active > a span.step-name")

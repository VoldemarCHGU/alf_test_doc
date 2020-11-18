from typing import Union
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver
from pages.main_functions import get_alfadoc_rc_sessionid
from pages.main_settings import Global_Profile, MAIN_URL

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Выберите браузер: 'chrome' or 'firefox'")
    parser.addoption('--language', action='store', default="en",
                     help="Введите язык для запуска теста...'")


def choose_browser(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        print("\nStart chrome browser for test..")
        browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nStart firefox browser for test..")
        browser = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    return browser


def browser_settings(choice, value):
    """
    Настройка браузера перед запуском теста
    request : выбор браузера (по умолчанию хром)
    value : значение для авторизации по сессии/токену
    """
    browser: WebDriver
    browser = choose_browser(choice)
    browser.maximize_window()
    browser.get(MAIN_URL)
    browser.add_cookie(
        {'name': 'alfadoc_rc_sessionid', 'value': value})
    return browser

@pytest.fixture(scope='class')
def browser_ПДН_БЮДЖЕТ_ЭКСПЕРТ(request):
    try:
        print("\n___Start браузера для ПДН.БЮДЖЕТ.ЭКСПЕРТ")
        value = get_alfadoc_rc_sessionid(*Global_Profile("ПДН.БЮДЖЕТ.ЭКСПЕРТ"))
        browser = browser_settings(request, value)
        yield browser
        print("\n___Закрытие браузера для ПДН.БЮДЖЕТ.ЭКСПЕРТ___")
    finally:
        browser.quit()


@pytest.fixture(scope='class')
def browser_КИИ_СТАНДАРТ(request):
    try:
        print("\n___Start браузера для КИИ.СТАНДАРТ")
        value = get_alfadoc_rc_sessionid(*Global_Profile("КИИ.СТАНДАРТ"))
        browser = browser_settings(request, value)
        yield browser
        print("\n___Закрытие браузера для КИИ.СТАНДАРТ___")
    finally:
        browser.quit()


@pytest.fixture(scope='class')
def browser_КИИ_ГИС_ПДН_БЮДЖЕТ_ЭКСПЕРТ(request):
    try:
        print("\n___Start браузера для КИИ.ГИС.ПДН.БЮДЖЕТ.ЭКСПЕРТ")
        value = get_alfadoc_rc_sessionid(*Global_Profile("КИИ.ГИС.ПДН.БЮДЖЕТ.ЭКСПЕРТ"))
        browser = browser_settings(request, value)
        yield browser
        print("\n___Закрытие браузера для КИИ.ГИС.ПДН.БЮДЖЕТ.ЭКСПЕРТ___")
    finally:
        browser.quit()

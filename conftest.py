import pytest
from selenium import webdriver

from .pages.main_functions import f_logging


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


@pytest.fixture(scope='class')
def browser1(request):
    try:
        print("\n___Start браузера для ПДН.БЮДЖЕТ.ЭКСПЕРТ")
        browser = choose_browser(request)
        browser.maximize_window()

        # browser = f_logging(browser, "ПДН.БЮДЖЕТ.ЭКСПЕРТ")
        browser.get('http://rc.alfa-doc.ru/')
        browser.add_cookie(
            {'name': 'alfadoc_rc_sessionid', 'value': '6dalcuafz1cdyyeen7rsbo8heywqp391'})

        yield browser
        print("\n___Quit browser..___")
    finally:
        browser.quit()


@pytest.fixture(scope='class')
def browser2(request):
    try:
        print("\n___Start браузера для КИИ.СТАНДАРТ")
        browser = choose_browser(request)
        browser.maximize_window()

        browser.get('http://rc.alfa-doc.ru/')
        browser.add_cookie(
            {'name': 'alfadoc_rc_sessionid', 'value': '9sfhv3bp65bjbj1xxm437931k9yv5omy'})
        # browser = f_logging(browser, "КИИ.СТАНДАРТ")
        yield browser
        print("\n___Quit browser..___")
    finally:
        browser.quit()



@pytest.fixture(scope='class')
def browser3(request):
    try:
        print("\n___Start браузера для КИИ.ГИС.ПДН.БЮДЖЕТ.ЭКСПЕРТ")
        browser = choose_browser(request)
        browser.maximize_window()

        browser.get('http://rc.alfa-doc.ru/')
        browser.add_cookie(
            {'name': 'alfadoc_rc_sessionid', 'value': '3vlynknadrijypbg03388nlzm4hyw4d2'})
        # browser = f_logging(browser, "КИИ.ГИС.ПДН.БЮДЖЕТ.ЭКСПЕРТ")
        yield browser
        print("\n___Quit browser..___")
    finally:
        browser.quit()
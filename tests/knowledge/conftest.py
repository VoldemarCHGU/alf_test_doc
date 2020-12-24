import json

import pytest
from filelock import FileLock
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.firefox.webdriver import WebDriver

from pages.main_functions import get_alfadoc_rc_sessionid
from pages.main_settings import Global_Profile, MAIN_URL


def завершение_теста(browser):
    # with allure.step("Фрагмент в конце теста"):
    #     allure.attach(browser.get_screenshot_as_png(),
    #                   name='screenshot',
    #                   attachment_type=AttachmentType.PNG)
    browser.close()
    browser.quit()


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
    if MAIN_URL == "https://alfa-doc.ru/":
        browser.add_cookie(
            {'name': 'alfadoc_sessionid', 'value': value})
    elif MAIN_URL == "http://rc.alfa-doc.ru/":
        browser.add_cookie(
            {'name': 'alfadoc_rc_sessionid', 'value': value})
    else:
        print("Для такого URL словия не заданы")
    return browser


"""ПДН.БЮДЖЕТ.ЭКСПЕРТ"""


def sessionid_ПДН_БЮДЖЕТ_ЭКСПЕРТ():
    return get_alfadoc_rc_sessionid(*Global_Profile("ПДН.БЮДЖЕТ.ЭКСПЕРТ"))


@pytest.fixture(scope="session")
def get_sessionid_ПДН_БЮДЖЕТ_ЭКСПЕРТ(tmp_path_factory, worker_id, name="sessionid_ПДН_БЮДЖЕТ_ЭКСПЕРТ"):
    if not worker_id:
        # not executing in with multiple workers, just produce the data and let
        # pytest's fixture caching do its job
        return sessionid_ПДН_БЮДЖЕТ_ЭКСПЕРТ()

    # get the temp directory shared by all workers
    root_tmp_dir = tmp_path_factory.getbasetemp().parent

    fn = root_tmp_dir / "data_ПДН_БЮДЖЕТ_ЭКСПЕРТ.json"
    with FileLock(str(fn) + ".lock"):
        if fn.is_file():
            data = json.loads(fn.read_text())
        else:
            data = sessionid_ПДН_БЮДЖЕТ_ЭКСПЕРТ()
            fn.write_text(json.dumps(data))
    return data


@pytest.fixture(scope='session')
def browser_ПДН_БЮДЖЕТ_ЭКСПЕРТ(request, get_sessionid_ПДН_БЮДЖЕТ_ЭКСПЕРТ):
    try:
        print("\n___Start браузера для ПДН.БЮДЖЕТ.ЭКСПЕРТ")
        value = get_sessionid_ПДН_БЮДЖЕТ_ЭКСПЕРТ
        browser = browser_settings(request, value)
        yield browser
        print("\n___Закрытие браузера для ПДН.БЮДЖЕТ.ЭКСПЕРТ___")
    finally:
        завершение_теста(browser)


"""КИИ.СТАНДАРТ"""


def sessionid_КИИ_СТАНДАРТ():
    return get_alfadoc_rc_sessionid(*Global_Profile("КИИ.СТАНДАРТ"))


@pytest.fixture(scope="session")
def get_sessionid_КИИ_СТАНДАРТ(tmp_path_factory, worker_id, name="sessionid_КИИ_СТАНДАРТ"):
    if not worker_id:
        # not executing in with multiple workers, just produce the data and let
        # pytest's fixture caching do its job
        return sessionid_КИИ_СТАНДАРТ()

    # get the temp directory shared by all workers
    root_tmp_dir = tmp_path_factory.getbasetemp().parent

    fn = root_tmp_dir / "data_kii_standart.json"
    with FileLock(str(fn) + ".lock"):
        if fn.is_file():
            data = json.loads(fn.read_text())
        else:
            data = sessionid_КИИ_СТАНДАРТ()
            fn.write_text(json.dumps(data))
    return data


@pytest.fixture(scope='session')
def browser_КИИ_СТАНДАРТ(request, get_sessionid_КИИ_СТАНДАРТ):
    try:
        print("\n___Start браузера для КИИ.СТАНДАРТ")
        value = get_sessionid_КИИ_СТАНДАРТ
        browser = browser_settings(request, value)
        yield browser
        print("\n___Закрытие браузера для КИИ.СТАНДАРТ___")
    finally:
        завершение_теста(browser)


"""КИИ.ГИС.ПДН.БЮДЖЕТ.ЭКСПЕРТ"""


def sessionid_КИИ_ГИС_ПДН_БЮДЖЕТ_ЭКСПЕРТ():
    return get_alfadoc_rc_sessionid(*Global_Profile("КИИ.ГИС.ПДН.БЮДЖЕТ.ЭКСПЕРТ"))


@pytest.fixture(scope="session")
def get_sessionid_КИИ_ГИС_ПДН_БЮДЖЕТ_ЭКСПЕРТ(tmp_path_factory, worker_id, name="sessionid_КИИ_ГИС_ПДН_БЮДЖЕТ_ЭКСПЕРТ"):
    if not worker_id:
        # not executing in with multiple workers, just produce the data and let
        # pytest's fixture caching do its job
        return sessionid_КИИ_ГИС_ПДН_БЮДЖЕТ_ЭКСПЕРТ()

    # get the temp directory shared by all workers
    root_tmp_dir = tmp_path_factory.getbasetemp().parent

    fn = root_tmp_dir / "data_КИИ_ГИС_ПДН_БЮДЖЕТ_ЭКСПЕРТ.json"
    with FileLock(str(fn) + ".lock"):
        if fn.is_file():
            data = json.loads(fn.read_text())
        else:
            data = sessionid_КИИ_ГИС_ПДН_БЮДЖЕТ_ЭКСПЕРТ()
            fn.write_text(json.dumps(data))
    return data


@pytest.fixture(scope='session')
def browser_КИИ_ГИС_ПДН_БЮДЖЕТ_ЭКСПЕРТ(request, get_sessionid_КИИ_ГИС_ПДН_БЮДЖЕТ_ЭКСПЕРТ):
    try:
        print("\n___Start браузера для КИИ.ГИС.ПДН.БЮДЖЕТ.ЭКСПЕРТ")
        value = get_sessionid_КИИ_ГИС_ПДН_БЮДЖЕТ_ЭКСПЕРТ
        browser = browser_settings(request, value)
        yield browser
        print("\n___Закрытие браузера для КИИ.ГИС.ПДН.БЮДЖЕТ.ЭКСПЕРТ___")
    finally:
        завершение_теста(browser)


"""КИИ.ПДН.ЭКСПЕРТ"""


def sessionid_КИИ_ПДН_ЭКСПЕРТ():
    return get_alfadoc_rc_sessionid(*Global_Profile("КИИ.ПДН.ЭКСПЕРТ"))


@pytest.fixture(scope="session")
def get_sessionid_КИИ_ПДН_ЭКСПЕРТ(tmp_path_factory, worker_id, name="sessionid_КИИ_ПДН_ЭКСПЕРТ"):
    if not worker_id:
        # not executing in with multiple workers, just produce the data and let
        # pytest's fixture caching do its job
        return sessionid_КИИ_ПДН_ЭКСПЕРТ()

    # get the temp directory shared by all workers
    root_tmp_dir = tmp_path_factory.getbasetemp().parent

    fn = root_tmp_dir / "data_КИИ_ПДН_ЭКСПЕРТ.json"
    with FileLock(str(fn) + ".lock"):
        if fn.is_file():
            data = json.loads(fn.read_text())
        else:
            data = sessionid_КИИ_ПДН_ЭКСПЕРТ()
            fn.write_text(json.dumps(data))
    return data


@pytest.fixture(scope='session')
def browser_КИИ_ПДН_ЭКСПЕРТ(request, get_sessionid_КИИ_ПДН_ЭКСПЕРТ):
    try:
        print("\n___Start браузера для КИИ.ПДН.ЭКСПЕРТ")
        value = get_sessionid_КИИ_ПДН_ЭКСПЕРТ
        browser = browser_settings(request, value)
        yield browser
        print("\n___Закрытие браузера для КИИ.ПДН.ЭКСПЕРТ___")
    finally:
        завершение_теста(browser)


"""ГИС.ЭКСПЕРТ"""


def sessionid_ГИС_ЭКСПЕРТ():
    return get_alfadoc_rc_sessionid(*Global_Profile("ГИС.ЭКСПЕРТ"))


@pytest.fixture(scope="session")
def get_sessionid_ГИС_ЭКСПЕРТ(tmp_path_factory, worker_id, name="sessionid_ГИС_ЭКСПЕРТ"):
    if not worker_id:
        # not executing in with multiple workers, just produce the data and let
        # pytest's fixture caching do its job
        return sessionid_ГИС_ЭКСПЕРТ()

    # get the temp directory shared by all workers
    root_tmp_dir = tmp_path_factory.getbasetemp().parent

    fn = root_tmp_dir / "data_ГИС_ЭКСПЕРТ.json"
    with FileLock(str(fn) + ".lock"):
        if fn.is_file():
            data = json.loads(fn.read_text())
        else:
            data = sessionid_ГИС_ЭКСПЕРТ()
            fn.write_text(json.dumps(data))
    return data


@pytest.fixture(scope='session')
def browser_ГИС_ЭКСПЕРТ(request, get_sessionid_ГИС_ЭКСПЕРТ):
    try:
        print("\n___Start браузера для ГИС.ЭКСПЕРТ")
        value = get_sessionid_ГИС_ЭКСПЕРТ
        browser = browser_settings(request, value)
        yield browser
        print("\n___Закрытие браузера для ГИС.ЭКСПЕРТ___")
    finally:
        завершение_теста(browser)


"""ГИС.ПДН.БЮДЖЕТ.ЭКСПЕРТ"""


def sessionid_ГИС_ПДН_БЮДЖЕТ_ЭКСПЕРТ():
    return get_alfadoc_rc_sessionid(*Global_Profile("ГИС.ПДН.БЮДЖЕТ.ЭКСПЕРТ"))


@pytest.fixture(scope="session")
def get_sessionid_ГИС_ПДН_БЮДЖЕТ_ЭКСПЕРТ(tmp_path_factory, worker_id, name="sessionid_ГИС_ПДН_БЮДЖЕТ_ЭКСПЕРТ"):
    if not worker_id:
        # not executing in with multiple workers, just produce the data and let
        # pytest's fixture caching do its job
        return sessionid_ГИС_ПДН_БЮДЖЕТ_ЭКСПЕРТ()

    # get the temp directory shared by all workers
    root_tmp_dir = tmp_path_factory.getbasetemp().parent

    fn = root_tmp_dir / "data_ГИС_ПДН_БЮДЖЕТ_ЭКСПЕРТ.json"
    with FileLock(str(fn) + ".lock"):
        if fn.is_file():
            data = json.loads(fn.read_text())
        else:
            data = sessionid_ГИС_ПДН_БЮДЖЕТ_ЭКСПЕРТ()
            fn.write_text(json.dumps(data))
    return data


@pytest.fixture(scope='session')
def browser_ГИС_ПДН_БЮДЖЕТ_ЭКСПЕРТ(request, get_sessionid_ГИС_ПДН_БЮДЖЕТ_ЭКСПЕРТ):
    try:
        print("\n___Start браузера для ГИС.ПДН.БЮДЖЕТ.ЭКСПЕРТ")
        value = get_sessionid_ГИС_ПДН_БЮДЖЕТ_ЭКСПЕРТ
        browser = browser_settings(request, value)
        yield browser
        print("\n___Закрытие браузера для ГИС.ПДН.БЮДЖЕТ.ЭКСПЕРТ___")
    finally:
        завершение_теста(browser)

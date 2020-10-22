import pytest
from selenium import webdriver



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


@pytest.fixture(scope='class', autouse=False)
def browser(request):
    print("\n___Start browser for test..___")
    browser = choose_browser(request)
    # browser.implicitly_wait(3)
    browser.maximize_window()


    yield browser
    print("\n___Quit browser..___")
    browser.quit()

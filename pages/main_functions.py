import time
import requests, urllib.request
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .main_settings import Global_Profile, MAIN_URL


def f_logging(driver, tariff):
    try:
        driver.get(MAIN_URL)
        driver.find_element_by_link_text("Войти").click();
        # print(step, ") С лендинга нажали на 'Войти");step += 1
        driver.find_element_by_link_text("Войти через сервис авторизации Charon").click()
        # print(step, ") Нажали на Войти через сервис авторизации");step += 1

        login, password = Global_Profile(tariff)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "id_password")))
        time.sleep(0.5)
        driver.find_element_by_id("id_username").send_keys(login)

        time.sleep(0.5)

        driver.find_element_by_id("id_password").send_keys(password)
        time.sleep(0.5)
        # print(step,") Ввели логин и пароль");step += 1
        driver.find_element_by_class_name("btn").click()
        # print(step,") Нажали на кнопку 'Войти'");step += 1
        # print("+++++Yes Connect =)\t")
        time.sleep(0.5)

    except Exception as err:
        print(err, "\n")
    finally:
        return driver


def get_alfadoc_rc_sessionid(USERNAME,PASSWORD):
    LOGIN_URL = "https://login.npc-ksb.ru/account/login/"
    ENDPOINT_URL = 'http://rc.alfa-doc.ru/accounts/charon/authenticate/'

    client = requests.session()
    client.get(LOGIN_URL)
    csrftoken = client.cookies['alfalogin_csrftoken']

    login_data = {'username': USERNAME, 'password': PASSWORD, 'csrfmiddlewaretoken': csrftoken}
    headers = {
        'Host': 'login.npc-ksb.ru',
        'Origin': 'https://login.npc-ksb.ru',
        'Referer': 'https://login.npc-ksb.ru/account/login/',
    }
    r1 = client.post(LOGIN_URL, data=login_data, headers=headers)
    client.get(ENDPOINT_URL)
    # site_update = client.get("http://rc.alfa-doc.ru/")
    session_id =client.cookies.get('alfadoc_rc_sessionid')
    return session_id



def проверка_ссылки(link):
    zapros = urllib.request.urlopen(link).getcode()
    assert zapros == 200, f"Запрос вернул код {zapros} \n {link}"

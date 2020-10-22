from .main_settings import Global_Profile
from .main_settings import MAIN_URL
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
        print(err,"\n")
    finally:
        return driver

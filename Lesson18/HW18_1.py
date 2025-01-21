import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_site_new():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Перейти на страницу сайта
        driver.get("https://omayo.blogspot.com/")
        # Найти текстовое поле
        text_field = driver.find_element(By.ID, "textbox1")
        # Очистить поле
        text_field.clear()
        # Ввести значение в текстовое поле
        text_field.send_keys("Selenium test")
        # Отображение текста
        assert text_field.get_attribute("value") == "Selenium test", "Text field value does not match expected"


    finally:
        driver.quit()


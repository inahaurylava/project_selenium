import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager


def test_site2():
    options = Options()
    options.add_argument("--start-maximized")
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    try:
        # Открыть сайт
        driver.get("https://omayo.blogspot.com/")

        # Найти элемент
        dropdown = driver.find_element(By.ID, "drop1")

        # Открыть дропдаун
        select = Select(dropdown)
        # Выбрать значение "doc 3"
        select.select_by_visible_text("doc 3")
        # Проверить что опция установлена
        selected_option = select.first_selected_option
        assert selected_option.text == "doc 3", f"Ожидаемый результат 'doc 3', получили: {selected_option.text}"



    finally:
        driver.quit()



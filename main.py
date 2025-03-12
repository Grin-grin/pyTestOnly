import logging

from selenium import webdriver
from testFooter import test_footer
from settingLog import setting_log

setting_log("footer")

driver = webdriver.Chrome()

pages = [
    "https://only.digital/",
    "https://only.digital/projects",
    "https://only.digital/fields"
]

try:
    for page in pages:
        driver.get(page)
        logging.info(f"Тест страницы: {page}")
        test_footer(driver)
        logging.info("#" * 10)

finally:
    driver.quit()
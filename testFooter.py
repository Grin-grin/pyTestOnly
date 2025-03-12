from seleniumUtils import By, WebDriver, WebElement, NoSuchElementException
from findPhone import find_phone
from findEmail import find_email
import logging

def test_footer(driver: WebDriver):
    """Поиск футера на странице и поск элементов в футере"""

    try:
        # Поиск футера
        footer: WebElement = driver.find_element(By.TAG_NAME, "footer")
        logging.info("Футер на странице найден")
    except NoSuchElementException:
        logging.error("Футер не найден")
        return

    # Поиск телефона в футере
    phone = find_phone(footer)
    if phone:
        logging.info(f"Найден телефон: {phone}")
    else:
        logging.warning("Телефон не найден")

    # Поиск Email в футере
    email = find_email(footer)
    if phone:
        logging.info(f"Найден Email: {email}")
    else:
        logging.warning("Email не найден")
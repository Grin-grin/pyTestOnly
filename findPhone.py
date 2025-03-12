from seleniumUtils import By, WebElement, NoSuchElementException

def find_phone(parent: WebElement) -> str | None:
    """
    Поиск телефона в parent.
    :param parent объект HTML
    """
    try:
        # Поиск телефона по ссылке
        phoneElement: WebElement = parent.find_element(By.CSS_SELECTOR, "a[href^='tel:']")
        return phoneElement.get_attribute("href").replace("tel:", "")
    except NoSuchElementException:
        return None


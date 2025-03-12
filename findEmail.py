from seleniumUtils import By, WebElement, NoSuchElementException

def find_email(parent: WebElement) -> str | None:
    """
    Поиск Email в parent.
    :param parent объект HTML
    """
    try:
        # Поиск Email по ссылке
        emailElement: WebElement = parent.find_element(By.CSS_SELECTOR, "a[href^='mailto:']")
        return emailElement.get_attribute("href").replace("mailto:", "")
    except NoSuchElementException:
        return None


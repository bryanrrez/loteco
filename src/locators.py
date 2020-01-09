from selenium.webdriver.common.by import By

class HomeLocators:
    """Localizadores de la página Home."""

    resultados_anteriores_input = (By.ID, 'datepicker')
    premio_span = (By.XPATH, '//div[div[1]/div[2]/a/span[text()="{loteria}"]]/div[2]/span[{no_premio}]')
    loteria_premio_fecha_span = (By.XPATH, '//div[contains(@class, "game-block") and ./div[1]/div[2 and ./a/span[contains(text(), "{loteria}")]]/div/span[contains(text(), "{fecha}")]]/div[2]/span[{no_premio}]')
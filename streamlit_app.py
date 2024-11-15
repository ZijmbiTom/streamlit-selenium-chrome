import streamlit as st
import time 

# Titel van de applicatie
st.title("Afbeelding downloader")

# Invoerveld voor de URL
url = st.text_input("Geef de URL van VW configurator op:")

with st.echo():
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from webdriver_manager.chrome import ChromeDriverManager
    from webdriver_manager.core.os_manager import ChromeType

    @st.cache_resource
    def get_driver():
        return webdriver.Chrome(
            service=Service(
                ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
            ),
            options=options,
        )

    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--headless")

    driver = get_driver()
    driver.get(url)

    # Wacht een paar seconden zodat de pagina volledig kan laden
    time.sleep(5)

    st.code(driver.page_source)



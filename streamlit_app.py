import streamlit as st

# Titel van de applicatie
st.title("Afbeelding downloader")

# Invoerveld voor de URL
url = st.text_input("Geef de URL van VW configurator op:")

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType

@st.cache_resource
def get_driver():
    options = Options()
    options.add_argument("--disable-gpu")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    return webdriver.Chrome(
        service=Service(
            ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
        ),
        options=options,
    )

# Knop om het downloaden te starten
if st.button("Download Afbeeldingen"):
    if url:
        st.write("Downloadproces gestart...")
        
        driver = get_driver()
        driver.get(url)
    
        # Toon de HTML van de pagina
        st.code(driver.page_source)
        driver.quit()
    else:
        st.warning("Voer een geldige URL in voordat je op 'Download Afbeeldingen' klikt.")

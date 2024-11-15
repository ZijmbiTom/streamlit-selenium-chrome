import streamlit as st

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

    # Knop om het downloaden te starten
    if st.button("Download Afbeeldingen"):
        if url:
            st.write("Downloadproces gestart...")
            
            driver = get_driver()
            driver.get(url)
        
            st.code(driver.page_source)

    else:
        st.warning("Voer een geldige URL in voordat je op 'Download Afbeeldingen' klikt.")

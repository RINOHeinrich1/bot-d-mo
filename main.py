from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configurer et lancer le navigateur
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Optionnel : lance en plein écran

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

try:
    # Aller sur YouTube
    driver.get("https://www.youtube.com")

    # Accepter les cookies si besoin (YouTube peut afficher un popup selon l'emplacement)
    time.sleep(2)
    try:
        consent_button = driver.find_element(By.XPATH, "//button[contains(., 'Accepter tout')]")
        consent_button.click()
    except:
        pass  # Pas de popup

    # Rechercher "Aerosmith"
    search_input = driver.find_element(By.NAME, "search_query")
    search_input.send_keys("Aerosmith")
    search_input.send_keys(Keys.RETURN)

    # Attendre le chargement des résultats
    time.sleep(30)

    # Récupérer le lien de la première vidéo
    first_video = driver.find_element(By.ID, "video-title")
    video_title = first_video.get_attribute("title")
    video_url = first_video.get_attribute("href")

    print(f"🎵 Première vidéo trouvée : {video_title}")
    print(f"🔗 Lien : {video_url}")

finally:
    # Fermer le navigateur
    time.sleep(2)
    driver.quit()

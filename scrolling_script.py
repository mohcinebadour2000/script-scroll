import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
from fake_useragent import UserAgent
import random

# Installer automatiquement la version compatible de ChromeDriver
chromedriver_autoinstaller.install()

def create_driver():
    # Générer un User-Agent aléatoire (PC ou mobile)
    ua = UserAgent()
    user_agent = ua.random  # Choix aléatoire d’un User-Agent

    # Configurer les options pour le navigateur
    chrome_options = Options()
    chrome_options.add_argument(f"user-agent={user_agent}")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    
    # Ajouter une option pour exécuter en arrière-plan (tête invisible)
    chrome_options.add_argument("--headless")

    # Créer l'instance du driver avec les options
    driver = webdriver.Chrome(options=chrome_options)
    return driver

# Lancer le navigateur
driver = create_driver()

# Accéder au site
driver.get("https://almowadafe.com")

# Scroll pendant 2 minutes
end_time = time.time() + 120  # Durée en secondes
while time.time() < end_time:
    # Scroll vers le bas puis vers le haut de manière aléatoire
    driver.execute_script("window.scrollBy(0, 500);")
    time.sleep(random.uniform(1, 3))  # Pause aléatoire pour un comportement humain
    driver.execute_script("window.scrollBy(0, -500);")
    time.sleep(random.uniform(1, 3))

# Fermer le navigateur après le scroll
driver.quit()


# import chromedriver_autoinstaller
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import random
# import time

# # Installer automatiquement la bonne version de chromedriver
# chromedriver_autoinstaller.install()

# # Options pour exécuter Chrome en mode sans affichage
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")
# user_agents = [
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15",
#     "Mozilla/5.0 (Linux; Android 10; SM-G973F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Mobile Safari/537.36"
# ]
# chrome_options.add_argument(f"user-agent={random.choice(user_agents)}")

# # Lancer le navigateur avec les options définies
# driver = webdriver.Chrome(options=chrome_options)

# try:
#     # Accéder au site
#     driver.get("https://almowadafe.com")

#     # Durée de scrolling (2 minutes)
#     scrolling_duration = 120
#     start_time = time.time()

#     while time.time() - start_time < scrolling_duration:
#         scroll_length = random.randint(200, 1000)
#         driver.execute_script(f"window.scrollBy(0, {scroll_length});")
#         time.sleep(random.uniform(0.5, 2))

# finally:
#     # Fermer le navigateur
#     driver.quit()

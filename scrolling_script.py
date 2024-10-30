import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import chromedriver_autoinstaller

# Installer automatiquement la version compatible de ChromeDriver
chromedriver_autoinstaller.install()

# Liste des User Agents pour différents appareils
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; Pixel 3 XL Build/QQ3A.200805.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Linux; Android 11; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Mobile Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
]

# Liste des proxys
proxies_list = [
    "47.74.226.8:5001", "20.233.44.207:80", "43.134.68.153:3128", "41.204.53.27:80",
    "116.125.141.115:80", "8.221.138.111:2000", "34.81.72.31:80", "64.38.135.183:80",
    "27.254.46.194:80", "185.65.254.161:8081"  # Ajoutez d'autres proxys ici
]

def create_driver():
    # Choisir un User-Agent et un proxy aléatoires
    user_agent = random.choice(user_agents)
    proxy = random.choice(proxies_list)

    # Configurer les options pour le navigateur
    chrome_options = Options()
    chrome_options.add_argument(f"user-agent={user_agent}")
    chrome_options.add_argument(f"--proxy-server=http://{proxy}")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--headless")  # Exécuter en mode sans tête

    # Créer l'instance du driver
    driver = webdriver.Chrome(options=chrome_options)
    return driver

try:
    # Lancer le navigateur
    driver = create_driver()

    # Accéder au site
    driver.get("https://almowadafe.com/")
    print("Accès au site réussi.")

    # Scroll pendant 2 minutes
    end_time = time.time() + 120  # Durée en secondes
    while time.time() < end_time:
        # Scroll vers le bas
        driver.execute_script("window.scrollBy(0, 500);")
        time.sleep(random.uniform(1, 3))  # Pause aléatoire

    # Cliquer sur les publications
    publications = driver.find_elements(By.CSS_SELECTOR, ".item-title a")
    if publications:
        # Choisir un élément aléatoire parmi les publications
        publication_a_cliquer = random.choice(publications)

        # Scroller jusqu'à l'élément
        driver.execute_script("arguments[0].scrollIntoView();", publication_a_cliquer)

        # Attendre que l'élément soit cliquable
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".item-title a")))

        # Clic sur la publication
        publication_a_cliquer.click()
        print("Clic sur une publication réussi.")
        
        time.sleep(random.uniform(2, 5))  # Attendre que la page se charge
        print("Entré dans la publication avec succès.")

        # Retour à la page principale, si nécessaire
        driver.back()  # Retourner à la page précédente

        # Re-scroll après avoir cliqué
        for _ in range(5):  # Scroll encore plusieurs fois
            driver.execute_script("window.scrollBy(0, 500);")
            time.sleep(random.uniform(1, 3))

    else:
        print("Aucune publication trouvée.")

    print("Script exécuté avec succès.")

except Exception as e:
    print(f"Erreur lors de l'exécution du script : {e}")

finally:
    # Fermer le navigateur après le scroll et le clic
    driver.quit()
    print("Le navigateur a été fermé.")




# import time
# import random
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import chromedriver_autoinstaller

# # Installer automatiquement la version compatible de ChromeDriver
# chromedriver_autoinstaller.install()

# # Liste des User Agents pour différents appareils
# user_agents = [
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',  # PC
#     'Mozilla/5.0 (Linux; Android 10; Pixel 3 XL Build/QQ3A.200805.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36',  # Android
#     'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',  # iOS
#     'Mozilla/5.0 (Linux; Android 11; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Mobile Safari/537.36',  # Android Samsung
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'  # PC
# ]

# def create_driver():
#     # Choisir un User-Agent aléatoire
#     user_agent = random.choice(user_agents)

#     # Configurer les options pour le navigateur
#     chrome_options = Options()
#     chrome_options.add_argument(f"user-agent={user_agent}")
#     chrome_options.add_argument("--disable-blink-features=AutomationControlled")
#     chrome_options.add_argument("--headless")  # Exécuter en mode sans tête

#     # Créer l'instance du driver
#     driver = webdriver.Chrome(options=chrome_options)
#     return driver

# try:
#     # Lancer le navigateur
#     driver = create_driver()

#     # Accéder au site
#     driver.get("https://almowadafe.com/")
#     print("Accès au site réussi.")

#     # Scroll pendant 2 minutes
#     end_time = time.time() + 120  # Durée en secondes
#     while time.time() < end_time:
#         # Scroll vers le bas
#         driver.execute_script("window.scrollBy(0, 500);")
#         time.sleep(random.uniform(1, 3))  # Pause aléatoire

#     # Cliquer sur les publications (exemple avec un sélecteur CSS)
#     publications = driver.find_elements(By.CSS_SELECTOR, ".item-title a")  # Sélecteur des titres des publications
#     if publications:
#         # Choisir un élément aléatoire parmi les publications
#         publication_a_cliquer = random.choice(publications)

#         # Scroller jusqu'à l'élément
#         driver.execute_script("arguments[0].scrollIntoView();", publication_a_cliquer)

#         # Attendre que l'élément soit cliquable
#         WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".item-title a")))
        
#         # Clic sur la publication
#         publication_a_cliquer.click()  # Clic sur la publication
#         print("Clic sur une publication réussi.")  # Message de succès
        
#         time.sleep(random.uniform(2, 5))  # Attendre que la page se charge
#         print("Entré dans la publication avec succès.")  # Message de succès pour l'entrée dans la publication

#         # Retour à la page principale, si nécessaire
#         driver.back()  # Cela retourne à la page précédente

#         # Re-scroll après avoir cliqué
#         for _ in range(5):  # Scroll encore plusieurs fois
#             driver.execute_script("window.scrollBy(0, 500);")
#             time.sleep(random.uniform(1, 3))

#     else:
#         print("Aucune publication trouvée.")

#     print("Script exécuté avec succès.")

# except Exception as e:
#     print(f"Erreur lors de l'exécution du script : {e}")

# finally:
#     # Fermer le navigateur après le scroll et le clic
#     driver.quit()
#     print("Le navigateur a été fermé.")




##############################3

# import time
# import random
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import chromedriver_autoinstaller

# # Installer automatiquement la version compatible de ChromeDriver
# chromedriver_autoinstaller.install()

# # Liste des User Agents pour différents appareils
# user_agents = [
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',  # PC
#     'Mozilla/5.0 (Linux; Android 10; Pixel 3 XL Build/QQ3A.200805.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36',  # Android
#     'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',  # iOS
#     'Mozilla/5.0 (Linux; Android 11; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Mobile Safari/537.36',  # Android Samsung
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'  # PC
# ]

# def create_driver():
#     # Choisir un User-Agent aléatoire
#     user_agent = random.choice(user_agents)

#     # Configurer les options pour le navigateur
#     chrome_options = Options()
#     chrome_options.add_argument(f"user-agent={user_agent}")
#     chrome_options.add_argument("--disable-blink-features=AutomationControlled")
#     chrome_options.add_argument("--headless")  # Exécuter en mode sans tête

#     # Créer l'instance du driver
#     driver = webdriver.Chrome(options=chrome_options)
#     return driver

# try:
#     # Lancer le navigateur
#     driver = create_driver()

#     # Accéder au site
#     driver.get("https://almowadafe.com/")
#     print("Accès au site réussi.")

#     # Scroll pendant 2 minutes
#     end_time = time.time() + 120  # Durée en secondes
#     while time.time() < end_time:
#         # Scroll vers le bas
#         driver.execute_script("window.scrollBy(0, 500);")
#         time.sleep(random.uniform(1, 3))  # Pause aléatoire

#     # Cliquer sur les publications (exemple avec un sélecteur CSS)
#     publications = driver.find_elements(By.CSS_SELECTOR, ".item-title a")  # Sélecteur des titres des publications
#     if publications:
#         # Choisir un élément aléatoire parmi les publications
#         publication_a_cliquer = random.choice(publications)

#         # Scroller jusqu'à l'élément
#         driver.execute_script("arguments[0].scrollIntoView();", publication_a_cliquer)

#         # Attendre que l'élément soit cliquable
#         WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".item-title a")))
        
#         # Clic sur la publication
#         publication_a_cliquer.click()  # Clic sur la publication
#         time.sleep(random.uniform(2, 5))  # Attendre que la page se charge
#         print("Clic sur une publication réussi.")

#         # Retour à la page principale, si nécessaire
#         driver.back()  # Cela retourne à la page précédente

#         # Re-scroll après avoir cliqué
#         for _ in range(5):  # Scroll encore plusieurs fois
#             driver.execute_script("window.scrollBy(0, 500);")
#             time.sleep(random.uniform(1, 3))

#     else:
#         print("Aucune publication trouvée.")

#     print("Script exécuté avec succès.")

# except Exception as e:
#     print(f"Erreur lors de l'exécution du script : {e}")

# finally:
#     # Fermer le navigateur après le scroll et le clic
#     driver.quit()
#     print("Le navigateur a été fermé.")




# import time
# import random
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# import chromedriver_autoinstaller

# # Installer automatiquement la version compatible de ChromeDriver
# chromedriver_autoinstaller.install()

# # Liste des User Agents pour différents appareils
# user_agents = [
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',  # PC
#     'Mozilla/5.0 (Linux; Android 10; Pixel 3 XL Build/QQ3A.200805.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36',  # Android
#     'Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1',  # iOS
#     'Mozilla/5.0 (Linux; Android 11; Samsung Galaxy S21 Ultra) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Mobile Safari/537.36',  # Android Samsung
#     'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'  # PC
# ]

# def create_driver():
#     # Choisir un User-Agent aléatoire
#     user_agent = random.choice(user_agents)

#     # Configurer les options pour le navigateur
#     chrome_options = Options()
#     chrome_options.add_argument(f"user-agent={user_agent}")
#     chrome_options.add_argument("--disable-blink-features=AutomationControlled")
#     chrome_options.add_argument("--headless")  # Exécuter en mode sans tête

#     # Créer l'instance du driver
#     driver = webdriver.Chrome(options=chrome_options)
#     return driver

# try:
#     # Lancer le navigateur
#     driver = create_driver()

#     # Accéder au site
#     driver.get("https://almowadafe.com/")
#     print("Accès au site réussi.")

#     # Scroll pendant 2 minutes
#     end_time = time.time() + 120  # Durée en secondes
#     while time.time() < end_time:
#         # Scroll vers le bas
#         driver.execute_script("window.scrollBy(0, 500);")
#         time.sleep(random.uniform(1, 3))  # Pause aléatoire

#     # Cliquer sur les publications (exemple avec un sélecteur CSS)
#     publications = driver.find_elements(By.CSS_SELECTOR, ".item-title a")  # Sélecteur des titres des publications
#     if publications:
#         # Choisir un élément aléatoire parmi les publications
#         publication_a_cliquer = random.choice(publications)
#         publication_a_cliquer.click()  # Clic sur la publication
#         time.sleep(random.uniform(2, 5))  # Attendre que la page se charge
#         print("Clic sur une publication réussi.")

#         # Retour à la page principale, si nécessaire
#         driver.back()  # Cela retourne à la page précédente

#         # Re-scroll après avoir cliqué
#         for _ in range(5):  # Scroll encore plusieurs fois
#             driver.execute_script("window.scrollBy(0, 500);")
#             time.sleep(random.uniform(1, 3))

#     else:
#         print("Aucune publication trouvée.")

#     print("Script exécuté avec succès.")

# except Exception as e:
#     print(f"Erreur lors de l'exécution du script : {e}")

# finally:
#     # Fermer le navigateur après le scroll et le clic
#     driver.quit()
#     print("Le navigateur a été fermé.")



# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# import chromedriver_autoinstaller
# from fake_useragent import UserAgent
# import random

# # Installer automatiquement la version compatible de ChromeDriver
# chromedriver_autoinstaller.install()

# def create_driver():
#     # Générer un User-Agent aléatoire (PC ou mobile)
#     ua = UserAgent()
#     user_agent = ua.random  # Choix aléatoire d’un User-Agent

#     # Configurer les options pour le navigateur
#     chrome_options = Options()
#     chrome_options.add_argument(f"user-agent={user_agent}")
#     chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    
#     # Ajouter une option pour exécuter en arrière-plan (tête invisible)
#     chrome_options.add_argument("--headless")

#     # Créer l'instance du driver avec les options
#     driver = webdriver.Chrome(options=chrome_options)
#     return driver

# # Lancer le navigateur
# driver = create_driver()

# # Accéder au site
# driver.get("https://almowadafe.com")

# # Scroll pendant 2 minutes
# end_time = time.time() + 120  # Durée en secondes
# while time.time() < end_time:
#     # Scroll vers le bas puis vers le haut de manière aléatoire
#     driver.execute_script("window.scrollBy(0, 500);")
#     time.sleep(random.uniform(1, 3))  # Pause aléatoire pour un comportement humain
#     driver.execute_script("window.scrollBy(0, -500);")
#     time.sleep(random.uniform(1, 3))

# # Fermer le navigateur après le scroll
# driver.quit()





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

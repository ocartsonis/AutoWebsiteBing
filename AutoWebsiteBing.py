from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

s = Service("F:/ChromeDriver/chromedriver-win64/chromedriver.exe")
email = "jcartsonis@email.arizona.edu"
password = "nopcuc-mizse1-vUznuf"
isDone = False
options = Options()
#options.add_argument("--headless=new")
options.add_argument("--window-size=%s" % "1920, 1080")

driver = webdriver.Chrome(service=s, options=options)
driver.get("https://mytipreport.org/arizona.phoenix/medschool")

#initialize wait
wait = WebDriverWait(driver, 30)

#wait for email label to appear
wait.until(EC.visibility_of(driver.find_element(By.XPATH, """/html/body/div/div/div[1]/div/div[1]/form/div[1]/label""")))

#enter email
email_box = driver.find_element(By.XPATH, """//*[@id="email"]""")
email_box.send_keys(email)

#click submit button
driver.find_element(By.XPATH, """//*[@id="submit"]""").click()

#wait for password label to appear
wait.until(EC.visibility_of(driver.find_element(By.XPATH, """/html/body/div/div/div[1]/div/div[1]/form/div[2]/label""")))

#enter password
password_box = driver.find_element(By.XPATH, """/html/body/div/div/div[1]/div/div[1]/form/div[2]/div/input""")
password_box.send_keys(password)

#click submit button
driver.find_element(By.XPATH, """//*[@id="submit"]""").click()

print("here")
wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@id="navigation-menu"]/a[1]"""))).click()

#wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "ui divider")))
time.sleep(2)

print("cooked")

tasks = driver.find_elements(By.CLASS_NAME, "ui fluid raised card")

print(tasks)

while isDone == False:
    wait.until(EC.element_to_be_clickable((By.XPATH, """//*[@id="e67d52b6-9336-4465-8b79-65c5e56e08a6"]/div/div[1]/div/div[2]/div[3]/div[2]/div[2]/a[1]"""))).click()
    #somehow need to get the id of the top card

print(EC.element_to_be_clickable((By.XPATH, """/html/body/section/main/div[1]/button[1]""")))

print("done")


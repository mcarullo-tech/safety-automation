from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Edge()
driver.get('https://ipassm/NetForms/#/new/ROAM-Online')

try:
    # Wait for iframe to be present
    iframe = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "iframe"))
    )
    print("Iframe found!")

    # Switch to iframe
    driver.switch_to.frame(iframe)

    # Wait for the header to load inside the iframe
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//div[@class='panelHeader']"))
    )
    print("Page loaded successfully inside iframe!")

except Exception as e:
    print("Error:", e)

# Specify the location of your observation
exact_location = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[4]/div[1]/div/div[2]/form/div[3]/div/div[2]/div/div[28]/input")
exact_location.send_keys("Third floor")
print("Exact location specified")


# Describe the observation
observation_description = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[4]/div[1]/div/div[2]/form/div[3]/div/div[2]/div/div[43]/input")
observation_description.send_keys("I noticed a spillage on the floor.")
print("Observation described")

# Describe the action you took
immediate_action = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[4]/div[1]/div/div[2]/form/div[3]/div/div[2]/div/div[44]/input")
immediate_action.send_keys("I placed a wet floor sign over the slippage hazard.")
print("Action taken")

# Specify where you are working from
working_from = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[4]/div[1]/div/div[2]/form/div[3]/div/div[2]/div/div[23]/div[1]/div[2]/div[1]/input")
working_from.click()
# Lets say we are working from office
hatch_office = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[text()='Hatch office']"))
)
hatch_office.click()
print("cool bro")

time.sleep(15)  # Just to see the result before quitting

driver.quit()


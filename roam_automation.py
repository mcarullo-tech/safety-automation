from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

def load_webpage():
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

def click_button(xpath):
    button = driver.find_element(By.XPATH, xpath)
    button.click()

def select_from_dropdown(xpath):
    selection = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, xpath))
    )
    selection.click()

def write_in_box(xpath, text):
    exact_location = driver.find_element(By.XPATH, xpath)
    exact_location.send_keys(text)

driver = webdriver.Edge()
driver.get('https://ipassm/NetForms/#/new/ROAM-Online')

load_webpage()

# Specify safety observation was NOT observed by a contractor because we dont snitch
click_button("/html/body/div[1]/div[4]/div[1]/div[4]/div[1]/div/div[2]/form/div[3]/div/div[2]/div/div[19]/table/tbody/tr/td[2]/label/input")
print("Observation was not observed by contractor")

# Specify where you are working from
click_button("/html/body/div[1]/div[4]/div[1]/div[4]/div[1]/div/div[2]/form/div[3]/div/div[2]/div/div[23]/div[1]/div[2]/div[1]/input")
# Lets say we are working from office
select_from_dropdown("//div[text()='Hatch office']")

print("Working from office")

# Specify observation occured during working hours
click_button("/html/body/div[1]/div[4]/div[1]/div[4]/div[1]/div/div[2]/form/div[3]/div/div[2]/div/div[24]/table/tbody/tr/td[1]/label/input")
print("Observation during working hours")

# Specify at which office the incident occured
click_button("/html/body/div[1]/div[4]/div[1]/div[4]/div[1]/div/div[2]/form/div[3]/div/div[2]/div/div[27]/div[1]/div/div[3]/div[1]/input")
# Lets just choose the Amherst office
select_from_dropdown("//div[text()='100 Sylvan Parkway, Amherst']")

print("Amherst Office")

# Specify the location of your observation
write_in_box("/html/body/div[1]/div[4]/div[1]/div[4]/div[1]/div/div[2]/form/div[3]/div/div[2]/div/div[28]/input", "Third floor")
print("Exact location specified")

# Choose either behavior or condition
click_button("/html/body/div[1]/div[4]/div[1]/div[4]/div[1]/div/div[2]/form/div[3]/div/div[2]/div/div[39]/div[1]/div[2]/div[1]/input")
# Lets choose behavior
select_from_dropdown("//div[text()='Behaviour']")

print("Observation is related to a behavior")

# Specify safe or at risk
click_button("/html/body/div[1]/div[4]/div[1]/div[4]/div[1]/div/div[2]/form/div[3]/div/div[2]/div/div[40]/div[1]/div[2]/div[1]/input")
# Lets choose safe
select_from_dropdown("//div[text()='Safe']")

print("Observation is safe")

# Describe the observation
write_in_box("/html/body/div[1]/div[4]/div[1]/div[4]/div[1]/div/div[2]/form/div[3]/div/div[2]/div/div[43]/input", "I noticed a spillage on the floor.")
print("Observation described")

# Describe the action you took
write_in_box("/html/body/div[1]/div[4]/div[1]/div[4]/div[1]/div/div[2]/form/div[3]/div/div[2]/div/div[44]/input", "I placed a wet floor sign over the slippage hazard.")
print("Action taken")

# Choose an observation category
click_button("/html/body/div[1]/div[4]/div[1]/div[4]/div[1]/div/div[2]/form/div[3]/div/div[2]/div/div[47]/div[1]/div[2]/div[1]/input")
# Lets assume it was an access breach
select_from_dropdown("//div[text()='Access Breach']")

print("Access breach detected")

# Choose an observation type (Green, Yellow, Orange Card)
click_button("/html/body/div[1]/div[4]/div[1]/div[4]/div[1]/div/div[2]/form/div[3]/div/div[2]/div/div[48]/div[1]/div/div[3]/div[1]/input")
# Lets assume green card
select_from_dropdown("//div[text()='VFL- Office Safety Audit Card, Green Card']")

print("Green card")

# Save the ROAM
save_observation = driver.find_element(By.ID, "buttonABMgs6hKb6m3zQAAAAAA3otvABVdAhrQPUEvaAjYosttac7t")
save_observation.click()
print("Observation saved!")


driver.quit()


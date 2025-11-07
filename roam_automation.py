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

# Specify safety observation was NOT observed by a contractor because we dont snitch
work_by_contractor = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[4]/div[1]/div/div[2]/form/div[3]/div/div[2]/div/div[19]/table/tbody/tr/td[2]/label/input")
work_by_contractor.click()
print("Observation was not observed by contractor")

# Specify where you are working from
working_from = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[4]/div[1]/div/div[2]/form/div[3]/div/div[2]/div/div[23]/div[1]/div[2]/div[1]/input")
working_from.click()
# Lets say we are working from office
hatch_office = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[text()='Hatch office']"))
)
hatch_office.click()
print("Working from office")

# Specify observation occured during working hours
during_working_hours = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[4]/div[1]/div/div[2]/form/div[3]/div/div[2]/div/div[24]/table/tbody/tr/td[1]/label/input")
during_working_hours.click()
print("Observation during working hours")

# Specify at which office the incident occured
office_or_site = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[4]/div[1]/div/div[2]/form/div[3]/div/div[2]/div/div[27]/div[1]/div/div[3]/div[1]/input")
office_or_site.click()
# Lets just choose the Amherst office
choose_office = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[text()='100 Sylvan Parkway, Amherst']"))
)
choose_office.click()
print("Amherst Office")

# Specify the location of your observation
exact_location = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[4]/div[1]/div/div[2]/form/div[3]/div/div[2]/div/div[28]/input")
exact_location.send_keys("Third floor")
print("Exact location specified")

# Choose either behavior or condition
behavior_condition = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[4]/div[1]/div/div[2]/form/div[3]/div/div[2]/div/div[39]/div[1]/div[2]/div[1]/input")
behavior_condition.click()
# Lets choose behavior
choose_behavior = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[text()='Behaviour']"))
)
choose_behavior.click()
print("Observation is related to a behavior")

# Specify safe or at risk
safe_risk = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[4]/div[1]/div/div[2]/form/div[3]/div/div[2]/div/div[40]/div[1]/div[2]/div[1]/input")
safe_risk.click()
# Lets choose safe
choose_safe = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[text()='Safe']"))
)
choose_safe.click()
print("Observation is safe")

# Describe the observation
observation_description = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[4]/div[1]/div/div[2]/form/div[3]/div/div[2]/div/div[43]/input")
observation_description.send_keys("I noticed a spillage on the floor.")
print("Observation described")

# Describe the action you took
immediate_action = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[4]/div[1]/div/div[2]/form/div[3]/div/div[2]/div/div[44]/input")
immediate_action.send_keys("I placed a wet floor sign over the slippage hazard.")
print("Action taken")

# Choose an observation category
observation_category = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[4]/div[1]/div/div[2]/form/div[3]/div/div[2]/div/div[47]/div[1]/div[2]/div[1]/input")
observation_category.click()
# Lets assume it was an access breach
choose_category = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[text()='Access Breach']"))
)
choose_category.click()
print("Access breach detected")

# Choose an observation type (Green, Yellow, Orange Card)
observation_type = driver.find_element(By.XPATH, "/html/body/div[1]/div[4]/div[1]/div[4]/div[1]/div/div[2]/form/div[3]/div/div[2]/div/div[48]/div[1]/div/div[3]/div[1]/input")
observation_type.click()
# Lets assume green card
choose_card = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//div[text()='VFL- Office Safety Audit Card, Green Card']"))
)
choose_card.click()
print("Green card")

# Save the ROAM
save_observation = driver.find_element(By.ID, "buttonABMgs6hKb6m3zQAAAAAA3otvABVdAhrQPUEvaAjYosttac7t")
save_observation.click()
print("Observation saved!")


driver.quit()


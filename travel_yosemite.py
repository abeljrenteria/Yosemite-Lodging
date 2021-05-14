from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from send_email import send_email

checkin_date_static = "05/26/2021"
checkout_date_static = "05/27/2021"

path = "/Users/abelrenteria/Documents/Dependencies/chromedriver"
driver = webdriver.Chrome(path)

driver.get("https://travelyosemite.com")

link = driver.find_element_by_id("book-drop")
link.click()

try:
	element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.ID, "box-widget_InitialProductSelection"))
	)
	element.click()

	select = Select(driver.find_element_by_id("box-widget_InitialProductSelection"))
	select.select_by_visible_text("Housekeeping Camp")

	checkin_date = driver.find_element_by_id("box-widget_ArrivalDate")
	checkin_date.send_keys(checkin_date_static)

	checkin_date = driver.find_element_by_id("box-widget_DepartureDate")
	checkin_date.send_keys(checkout_date_static)

	submit = driver.find_element_by_name("wxa-form-search")
	submit.submit()

	try:
		element = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.ID, "box-results-empty-outer"))
		)
		print("Not Available")
		driver.quit()

	except:
		subject = "Housekeeping Yosemite: {} Available".format(checkin_date_static)
		message = "https://travelyosemite.com"

		send_email(subject, message)

		print("Available")
		driver.quit()

except:
	print(element)
	driver.quit()


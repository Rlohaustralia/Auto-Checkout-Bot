from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

# Initialize the webdriver
wd = webdriver.Chrome()
wd.implicitly_wait(10)

# Open the webpage
wd.get("https://8division.com/")
wd.maximize_window()

navigate_to_online_store = wd.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]/div[1]/ul/li[2]/a")
navigate_to_online_store.click()

# Click on the product
target_product = wd.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[3]/div[4]/ul/li[8]/div[1]/a/img")
target_product.click()

# Select size
select_size = wd.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[2]/ul/li[1]/div/select")
select_size.click()
Select(select_size).select_by_value("M")

# Click order button
order = wd.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[2]/div[2]/div[1]/div[4]/a[2]")
order.click()

# Click Non-member login
member = wd.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div/div[2]/a")
member.click()

# Fill in the form fields
name = wd.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div/div[2]/ul/li[1]/input")
name.send_keys("System")
time.sleep(0.7)

phone_2 = wd.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div/div[2]/ul/li[5]/input[1]")
phone_2.send_keys("2044")

phone_3 = wd.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div/div[2]/ul/li[5]/input[2]")
phone_3.send_keys("2339")
time.sleep(0.7)

email_1 = wd.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div/div[2]/ul/li[6]/input[1]")
email_1.send_keys("helloworld")

email_2 = wd.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div/div[2]/ul/li[6]/input[2]")
email_2.send_keys("gmail.com")
time.sleep(0.7)

password_1 = wd.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div/div[3]/ul/li[1]/input")
password_1.send_keys("helloworld111!")

password_2 = wd.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div/div[3]/ul/li[2]/input")
password_2.send_keys("helloworld111!")
time.sleep(0.7)

sendTo = wd.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div/div[4]/ul/li[1]/input")
sendTo.send_keys("System")
time.sleep(0.7)

mail = wd.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div/div[4]/ul/li[2]/a")
mail.click()

# Switch to the iframe for address search
iframe = wd.find_element(By.XPATH, "/html/body/div[16]/iframe")
wd.switch_to.frame(iframe)

select_button = wd.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/ul/li[2]/a")
select_button.click()

# Interact with elements inside the iframe
address = wd.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/table/tbody/tr/td/input")
address.send_keys("행당동 37-16")
time.sleep(0.7)

enter = wd.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/table/tbody/tr/td/a/img")
enter.click()

select_address = wd.find_element(By.XPATH, "/html/body/div/div[1]/div[3]/div[2]/div/table/tbody/tr[2]/td[1]/a[1]/span")
select_address.click()
time.sleep(0.7)

second_address = wd.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div/div[4]/ul/li[3]/input[2]")
second_address.send_keys("Republic of Korea")
time.sleep(0.7)

home_number_1 = wd.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div/div[4]/ul/li[4]/input[1]")
home_number_1.send_keys("2044")

home_number_2 = wd.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div/div[4]/ul/li[4]/input[2]")
home_number_2.send_keys("2339")

mobile_number_1 = wd.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div/div[4]/ul/li[5]/input[1]")
mobile_number_1.send_keys("2044")

mobile_number_2 = wd.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div/div[4]/ul/li[5]/input[2]")
mobile_number_2.send_keys("2339")
time.sleep(0.7)

message = wd.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div/div[4]/ul/li[7]/textarea")
message.send_keys("Hello World")
time.sleep(0.7)

select_payment = wd.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div/div[12]/ul/li[2]/span[4]/label")
select_payment.click()

account_name = wd.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/form/div/div[12]/div[3]/ul/li/input")
account_name.send_keys("System")

time.sleep(60)
wd.quit()

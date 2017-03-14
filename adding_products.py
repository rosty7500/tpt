__author__ = 'SJI-Dev-9'


import csv
import time
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome('C:\\Users\\Administrator\\Desktop\\chrome\\chromedriver.exe')
base_url = 'https://www.teacherspayteachers.com/My-Products/New/Digital'
driver.get(base_url)
driver.maximize_window()
time.sleep(5)
driver.find_element_by_id('UserUsername').send_keys("royston@sjinnovation.com")
driver.find_element_by_id('UserPassword').send_keys("rash0207")
driver.find_element_by_xpath("//form[@id='UserLoginForm']/div[2]/div[3]/a[1]").click()
time.sleep(10)
driver.find_element_by_xpath("//form[@id='UserUpdatePaymentForm']/div[5]/button").click()
time.sleep(10)

user_input = input("Number of products:")
user_input1 = input("Start number: ")
user_input2 = input("End number:")

for i in range(0, len(user_input2)):
    driver.get(base_url)
    file_input = driver.find_element_by_xpath("//div[@id='upload-product']/input[2]")
    file_input.send_keys('C:\\Users\\Administrator\\Desktop\\test.txt')
    time.sleep(15)
    driver.find_element_by_id('ItemName').send_keys("QA Testing: Test Product -" +user_input1)
    driver.find_element_by_id('ItemDescription').send_keys("Test data")
    driver.find_element_by_xpath("//select[@id='ItemResourcetypeSource']/option[1]").click()
    driver.find_element_by_xpath("//form[@id='ItemAddForm']/div[7]/div[2]/div[1]/div[2]/input[1]").click()
    driver.find_element_by_xpath("//input[@id='GradeGrade1']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//select[@id='ItemSubjectareaSource1']/option[2]").click()
    driver.find_element_by_xpath("//form[@id='ItemAddForm']/div[9]/div[2]/div[1]/div[2]/input[1]").click()
    driver.find_element_by_xpath("//div[@class='yui3-g form_item'][9]/div[2]/div/select").click()
    driver.find_element_by_xpath("//div[@class='yui3-g form_item'][9]/div[2]/div/select/option[1]").click()

    driver.find_element_by_xpath("//input[@id='ItemGenerateThumbnail3']").click()
    driver.find_element_by_xpath("//form[@id='ItemAddForm']/div[20]/div/input").click()

    i =i + 1

driver.quit()

from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import yaml
from steps.webelement_functions import *

data = load_yaml(f"{ROOT_DIR}/data/config.yml")
# file_location = f"C:/DEV/week7/screenshots/"

web_url = data['scenario1']['web_url']
username = data['scenario1']['username']
pswd = data['scenario1']['password']


# 1.) ********* Scenario with correct steps
# launch_website("https://letskodeit.teachable.com/p/practice")
# find_elements_tag('button')
# web_driver_properties_switch_to_tab()
# close_browser()
#
# 2.) ********* Scenario for go back, forward, refresh
# launch_website("http://automationpractice.com/index.php")
# women_tab = "//a[@class='sf-with-ul'][contains(text(),'Women')]"
# click_element_by_xpath(women_tab)
# go_back_to_previous_page()
# refresh_browser()
# go_next_page()
# close_browser()
#
# # 3.) *********** Scenario: Login to "http://automationpractice.com/index.php"
# Prerequisite: create an account:
# username: helo@email.com, have strong password: "612345"
# identify all locators by inspecting on browser (xpath, optional: id, css selector):
#
# web_url = "http://automationpractice.com/index.php"
# username = "helo@email.com"
# paswd = "612345"







# login_to_automation_practice(web_url, username, pswd)# keeps orders parameters
# login_to_automation_practice(email=username, url=web_url,password=pswd)
#
#
# data1 = {
#     'scenario1': {'web_url': 'http..', 'username': 'hello', 'password': 'yourpass'},
#     'scenario2': {'web_url': 'http..', 'username': 'hello', 'password': 'yourpass'}
#              }
# #
# web_url = data['scenario1']['web_url']
# username = data['scenario1']['username']
# pswd = data['scenario1']['password']
# close_browser()


# login_to_automation_practice(web_url, username, pswd)
# login_to_automation_practice(email=username, password=pswd, url=web_url)

# sign_in_link = "//a[@class='login']"
# # sign_in_link = "//a[@class='login'" # this is incorrect XPATH, to see Try Except
# email_input = "//input[@id='email']"
# password_input = "//input[@id='passwd']"
# sign_in_button = "//button[@id='SubmitLogin']"
# sign_out_link = "//a[@class='logout']"
# #
# # Steps:
# launch_website("http://automationpractice.com/index.php")
# click_element_by_xpath(sign_in_link)
# time.sleep(2)
# enter_text_by_xpath(email_input, "helo@email.com")
# enter_text_by_xpath(password_input, "612345")
# click_element_by_xpath(sign_in_button)
# time.sleep(10)
# print("successfully signed in ")
# print("signing out now...")
# click_element_by_xpath(sign_out_link)
# close_browser()

# newid = driver.find_element_by_xpath('').get_attribute('id')
#     dynamic_xpath = "//span[@id=obj123456]"
#     dynamic_xpath = f"//span[@id=obj1{newid}]"
#     dynamic_xpath = "//span[contains(@id, 'j1')]"
#     dynamic_xpath = "//span[ends-with(@id, '56')]"
#     dynamic_xpath = "//span[starts-with(@id, 'obj')]"
#     import re
#
#     def get_xpath(id_num):
#         return "//span[@id='" + id_num + "']"


# H/W : Sign In> enter email> click on Create Account > Fill the forms
# finding all elements (xpath, id, name)

# Scenario: Right click
# TODO: find out right way to retrieve chrome right click options, which is not Element property


# test_right_click()
# test_drag_and_drop()
# test_get_attribute()
#test_radio_button_is_displayed_selected()




# sign_in_link = "//a[@class='login']"
# launch_website("http://automationpractice.com/index.php")
# sign_in_element = driver.find_element_by_xpath(sign_in_link)
# actions = ActionChains(driver)
# actions.context_click(sign_in_element).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).build().perform()
# actions.send_keys(Keys.ARROW_DOWN).perform()
# actions.send_keys(Keys.ENTER).perform()

# Scenario: Drag and Drop
# # locators:
# item1_xpath = "//div[@id='todrag']//span[contains(text(),'Draggable 1')]"
# item2_xpath = "//div[@id='todrag']//span[contains(text(),'Draggable 2')]"
# drop_zone_xpath = "//div[@id='mydropzone']"
# dropped_item1_xpath = "//div[@id='droppedlist']//span[contains(text(),'Draggable 1')]"
# dropped_item2_xpath = "//div[@id='droppedlist']//span[contains(text(),'Draggable 2')]"
#
# # Step:
# # start the website
# # drag and drop item 1
# # verify item 1 is under dropped list
# # drag and drop item 2
# # verify item 2 is under dropped list
#
# # launch_website("https://www.seleniumeasy.com/test/drag-and-drop-demo.html")
# # launch_website("https://artoftesting.com/samplesiteforselenium")
# launch_website("http://testautomationpractice.blogspot.com/")
# item1 = driver.find_element_by_xpath("//div[@id='draggable']")
# time.sleep(3)
# drop_zone = driver.find_element_by_xpath("//div[@id='droppable']")
# #
# actions = ActionChains(driver)
# actions.drag_and_drop(item1, drop_zone). pause(3).perform()
# # actions.move_to_element(item1, drop_zone).perform() # hover over element (mouse movement)
# print("drag and drop finished.")
# close_browser()

# Scenario: is_displayed(), is_selected(), is_enabled()

# launch_website("https://letskodeit.teachable.com/p/practice")
#
# xpath1 = "//div[@id='radio-btn-example']"
# radio_button_example = driver.find_element_by_xpath(xpath1)
# print(f"Radio button example is displayed: {radio_button_example.is_displayed()}")
#
# bmw_option = None
# if radio_button_example.is_displayed():
#     bmw_option = driver.find_element_by_xpath("//input[@id='bmwradio']")
#     bmw_option.click()
#     time.sleep(1)
# else:
#     print("Radio button example is not displayed")
#
# print('bwm option is clicked')
# print(f"Is bmw option selected: {bmw_option.is_selected()}")
# assert bmw_option.is_selected(), "bmw Option is not selected "
# print("Yeaah it is selected. Test Passed")
#
# print("getting the attribute of the element")
# button = driver.find_element_by_xpath("//button[@id='openwindow']")
# value1 = button.get_attribute("onclick")
# value2 = button.get_attribute("class")
# print(f"Attributes of the element: onlick: {value1} , class: {value2}")
# print(f"Text of the button : {button.text}")



# ======= ==== ======  week8 09/19/2020
# Class project1:
#H/W : Creating an account in automationpractice.com
# Sign in> enter email> click on Create Account > Fill the forms
# finding all elements (xpath,id, name)
# verify that account is created, by message, Logout button


#Class project: 2
# uploading a file
# open browser, Launch the "https://www.facebook.com/marketplace/"
# login to facebook
# create new listing, choose item for sale, verify the url: "https://www.facebook.com/marketplace/"
# upload_xpath = "//input[@type='file' and contains(@accept, 'image')]"
# price_input = "//label[@aria-label='Price']//input[contains(@id, 'jsc_c_')]"
# title_input = "//label[@aria-label=['Title']//input[contains(@id, 'jsc_c_')]"
# category_list = "//label[@aria-label='Category']//spain"
# category_item = "//spain[contains(text(),'Electronics')]"
# category_sub_item = "//spain[contains(text(),'Blank Media')]"
# condition_list = "//spain[contains(text(),'Condition')]"
# condition_option = "//div[contains(text(),'Used - Like New')]"
# next_button = "//div[@aria-label='Next']"
#
#
#
# image_path = "C:\\Users\\anvar\Downloads\\thinkkorswim-simulated-tranding.png"
# #image_path = "C:/Users/anvar/Downloads/thinkkorswim-simulated-tranding.png"
# image_upload = driver.find_element_by_xpath(upload_xpath)
# image_upload.send_keys(image_path)
#
# # to check next button is enabled
# next_button = driver.find_element_by_xpath(next_button)
# if next_button.is_enabled():
#     next_button.click()
#     print("Next button is clicked.")


# after listing is published verify url=
# verify item is listed
# title = 'TestItem' # this is from Akmal Facebook, you should give it your name for it.
# active_item1_xpath = f"//span[conatins(text(), '{title}')]"
# active_item1 = driver.find_element_by_xpath(active_item1_xpath)
# assert active_item1.is_displayed()
# print("Test is succesefully executed!!")


# 09/19/2020 -week 8
# Instruction to Class Project1 and Class Project 2
# organize the test
# CheckBox is the same as Radio button - try is your self
# drop down list
#test_drop_down_list()
# hw/ try on automationpractice.com on Women tab, sort by

# Agenda for 09/20/2020 ******************
# alert (confirm,  cancel) - java script
# drop down list
# test_drop_down_list()
# alert (confirm, cancel) - java script
# hover over element

#test_alerts()

# == hover over element.
# test_mouse_hovering()
# close_browser()


# commit,  push to github, and submit with google form (send to akmal this form in the chat)

# CheckBox is the same as Radio button - try it your self

# Agenda for next class:
#  explicit waits , and difference between implicit_wait()
# used in enter_text_by_xpath


# print(get_str_day())
# print(get_str_seconds())



# logger = create_logger()
# logger.info("This is the in message")
# logger.debug("Debug message....")
# logger.error("I am an exception case.")
# logger.warn(" something does not seem to be right, but not an error.")
# logger.critical("WOUUW WOOUW STOP NOW< CAN NOT RUN ANYTHING AT THIS POINT!!!!")
#
#
















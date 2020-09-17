

import time

from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# === Initializing a new browser ====
driver = webdriver.Chrome() # starts browser
driver.maximize_window()
driver.implicitly_wait(20) # read more about this !
# or specify the path: driver = webdriver.Chrome('/path/to/chromedriver')
# print("opened the browser and google website")


driver.get("https://letskodeit.teachable.com/p/practice")
print("opened the browser and google website")
time.sleep(1) # thread.sleep() in JAVA

#============  1. == find all buttons, working with list of elements
buttons = driver.find_elements_by_xpath('//button')
for button in buttons:
    print('text of button: ', button.text)

# ================ 2. == == find by link text
open_tab = driver.find_element_by_link_text('Open Tab')
open_tab2 = driver.find_element_by_partial_link_text('en Tab')
# open_tab.click() # this will open a new tab but does not switches to it
time.sleep(5)


# driver.close()
# print("closed the current tab")
# time.sleep(5)
# driver.quit()
# print("browser is closed")

#================ 3. ====== using WebDriver Class Properties ======
url1 = driver.current_url
title1 = driver.title
win_handle1 = driver.current_window_handle
name1 = driver.name
print('Current url:', url1)
print('Current title1:', title1)
print('Current win_handle1:', win_handle1)
print('Current name1:', name1)



# === after getting all details of the current tab, we are opening new tab
open_tab.click() # this will open new tab but not switch to it

# == switch to anew tab, WebDriver Method - switch_to.window(new_handle)
handles = driver.window_handles
print(handles)
url2 = ""
title2 = ""
win_handle2 = ""


# === driver.switch_to.window(handles[1]) - might work but not guarantied


for handle in handles:
    if handle != win_handle1:
        driver.switch_to.window(handle)

    url2 = driver.current_url
    title2 = driver.title
    win_handle2 = driver.current_window_handle


print('Current url2:', url2)
print('Current title2:', title2)
print('Current win_handle2:', win_handle2)
assert url2 == 'https://letskodeit.teachable.com/courses'
assert title2 == "Let's Kode It"


# ==== 3. closing tabs vs closing a browser
driver.close()
print("current tab is closed")
time.sleep(3)





# switch back to initial window handle (initial browser tab)
driver.switch_to.window(win_handle1)

print('Title after closing a new tab: ', driver.title)
print('current_url after closing a new tab: ', driver.current_url)
print('current_window_handle after closing a new tab: ', driver.current_window_handle)
driver.quit()  # this will close the browser
print("browser is closed")




# driver.get("https://google.com")
# driver2 = webdriver.Chrome() # starts browser
# driver2.maximize_window()
# driver2.implicitly_wait(20)

# search_text_box = driver.find_element_by_name("q") # finding(locating) search box element in the HTML DOM
# print("identified google search box")
# time.sleep(3)
#
# search_text_box.clear()    # just in case clearing the search field
# search_text_box.send_keys("python selenium ")
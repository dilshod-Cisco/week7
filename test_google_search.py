# Google search scenario
# 1. Open the browser, Launch the website google.com (Given condition in Gherkin scenario)
# 2. type 'selenium python' in the search and hit Enter (Actions - When)
# 3. Verify the results is more 20 mln (Test here, check point - Then)
# 4. Verify that it take less than a second for the search ( Test here, check point - Then)
# 5. close the browser

# - keywords HTML, (DOM),
# locator: xpath(querying), id, cssSelector(querying) can be customized using tags and attributes
# locator on html: can be provide by id, name, link_name, partial_link_name, class_name

import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome() # starts browser
# or specify the path: driver = webdriver.Chrome('/path/to/chromedriver')
driver.get("https://google.com")
print("opened the browser and google website")
time.sleep(3)


search_text_box = driver.find_element_by_name("q") # finding(locating) search box element in the HTML DOM
print("identified google search box")
time.sleep(3)

search_text_box.clear()    # just in case clearing the search field
search_text_box.send_keys("python selenium ") # enter provided text in the search box
print("cleared the search box the typed 'python selenium' words in it")
time.sleep(3)

search_text_box.send_keys(Keys.RETURN) # simulates hitting the Enter key on your browser
print("hit the inter button")
time.sleep(3)

result_msg = driver.find_element_by_xpath("//div[@id='result-stats']").text
print(result_msg)
#"About 27,800,000 results (0.41 seconds) "
# verify the result num is > 20 mln
result_msg_list = result_msg.split() # split give you the list.
result_num_str = result_msg_list[1].replace(',', '') # replace the comma !
result_num = int(result_num_str) # convert to 'integer'
assert result_num > 20000000, "Result num is less than 20 mln "# convert integer to integer # assert using instead of 'if'
print("Verifying result number Passed.")



# Verifying the performance, less than a second
result_time_str = result_msg_list[3]
result_time_str = result_msg_list[3].replace('(', '')
result_time = float(result_time_str)
assert result_time < 1, "Search took more than a second!"
print("Verifying search performance Passed.")


print("now closing the browser  .....")
#driver.close()
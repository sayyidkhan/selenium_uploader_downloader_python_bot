from selenium import webdriver

# Create a webdriver instance
driver = webdriver.Chrome()

# Navigate to the webpage with the file upload button
website_name = "https://ps.uci.edu/~franklin/doc/file_upload.html"
driver.get(website_name)

# Find the file upload button and click it
#upload_button = driver.find_element_by_id('upload_button') # can choose to use to find by id
upload_button = driver.find_element_by_xpath('/html/body/form/input[1]') # or can choose to use find by xpath 
upload_button.click()

# Use the send_keys() method to attach the file to the input field
file_input = driver.find_element_by_id('file_input')
file_input.send_keys('/path/to/file.txt')

# Submit the form
submit_button = driver.find_element_by_id('submit_button')
submit_button.click()

# Close the webdriver instance
driver.close()
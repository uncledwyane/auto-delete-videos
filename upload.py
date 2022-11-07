# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# driver = webdriver.Chrome()
# driver.set_window_size(1000, 600)
#
# driver.get('https://www.youtube.com/')
#
# login_btn = driver.find_element(By.XPATH, '/html/body/ytd-app/div[1]/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-button-renderer/yt-button-shape/a')
# login_btn.click()
#
# driver.implicitly_wait(3)
#
# user_account = driver.find_element(By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[1]/div')
# user_account.click()
#
# driver.implicitly_wait(3)
# next_step = driver.find_element(By.XPATH, '//*[@id="passwordNext"]/div/button/div[3]')
#
# driver.implicitly_wait(5)
# user_header = driver.find_element(By.XPATH, '//*[@id="avatar-btn"]')
#
# driver.implicitly_wait(2)
# your_channel_btn = driver.find_element(By.XPATH, '//*[@id="primary-text-container"]')
#
# channel_setting_btn = driver.find_element(By.XPATH, '//*[@id="endpoint"]')
# channel_setting_btn.click()
#
# channel_status_and_func_btn = driver.find_element(By.XPATH, '//*[@id="options"]/ytd-channel-options-renderer/yt-formatted-string[1]/a')

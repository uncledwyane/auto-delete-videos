# import undetected_chromedriver as uc
#
# # from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from time import sleep
#
# config = {
#     'account': '',
#     'account_rec': '',
#     'password': '',
#     'website': ''
# }
#
#
# class Browser:
#     def __init__(self):
#         self.chrome_options = None
#         self.wait = None
#         self.driver = None
#         self.log('browser __init__ finished')
#         self.open_browser_window()
#
#     def open_browser_window(self):
#         self.log('正在打开浏览器窗口')
#         self.driver = uc.Chrome(use_subprocess=True, executable_path='C:/Program Files/Google/Chrome/Application/chromedriver.exe')
#         self.driver.set_window_size(1100, 600)
#         self.wait = WebDriverWait(self.driver, 100)
#         self.chrome_options = uc.ChromeOptions()
#         self._init_options()
#
#         self.log('浏览器窗口打开成功')
#
#         self.login_rumble()
#
#     def _init_options(self):
#         self.log('给浏览器添加启动参数')
#         self.chrome_options.add_argument("--ignore-certificate-errors")
#         self.chrome_options.add_experimental_option('detach', True)
#         self.chrome_options.add_argument('--no-default-browser-check')
#         self.chrome_options.add_argument(
#             "--user-data-dir=C:/Users/{userName}/AppData/Local/Google/Chrome/User Data/Profile {#}/")
#
#     def open_link_in_browser(self, link):
#         self.log('正在打开' + link)
#         self.driver.get(link)
#
#     def login_google(self):
#         self.open_link_in_browser('https://google.com')
#
#         sleep(3)
#         # 找到登录按钮并点击
#         self.log('找到登录按钮并点击')
#         login_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="gb"]/div/div[2]/a')))
#         login_btn.click()
#         self.log('登录按钮已点击')
#
#         # 输入邮箱
#         self.log('输入邮箱：' + config.get('account'))
#         email_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="identifierId"]')))
#         email_input.send_keys(config.get('account'))
#         self.log('输入邮箱完成')
#
#         # 点击下一步
#         self.log('下一步')
#         email_next_step = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="identifierNext"]')))
#         email_next_step.click()
#         self.log('已点击下一步')
#
#         # 输入密码
#         self.log('输入密码')
#         password_input = self.wait.until(
#             EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
#         password_input.send_keys(config.get('password'))
#         self.log('输入密码完成')
#
#         # 点击下一步
#         self.log('下一步')
#         pass_next_step = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="passwordNext"]')))
#         pass_next_step.click()
#         self.log('已点击下一步')
#
#         self.log('google登录完成，即将打开rumble')
#
#         recovery_email = self.wait.until(EC.visibility_of_element_located((By.XPATH,
#                                                                            '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/ul/li[3]')))
#         if recovery_email is not None:
#             self.log('需要验证辅助邮箱')
#             recovery_email.click()
#             recovery_email_input = self.wait.until(
#                 EC.visibility_of_element_located((By.XPATH, '//*[@id="knowledge-preregistered-email-response"]')))
#             print('输入辅助邮箱')
#             self.log('输入辅助邮箱')
#             recovery_email_input.send_keys(config.get('account_rec'))
#             self.log('下一步')
#             recovery_next_step = self.wait.until(EC.visibility_of_element_located(
#                 (By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')))
#             recovery_next_step.click()
#             sleep(5)
#             self.login_rumble()
#
#         self.login_rumble()
#
#     def login_rumble(self):
#         sleep(1)
#         self.open_link_in_browser('https://rumble.com')
#
#         sleep(1)
#
#         # 登录按钮
#         rumble_login_btn = self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/header/div/button[3]')))
#         rumble_login_btn.click()
#         self.log('点按钮登录rumble')
#
#         sleep(1)
#         google_login_btn = self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div/section/div[3]/button[2]')))
#         google_login_btn.click()
#         self.log('谷歌登录点击')
#
#         sleep(2)
#         # 打开google的iframe页面，进行登录
#         google_login_iframe = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'iframe')))
#         self.driver.switch_to.frame(google_login_iframe)
#         self.log('iframe')
#
#         # 点击iframe的已登录账户进行登录
#         already_login_account = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="identifierId"]')))
#         already_login_account.send_keys(config.get('account'))
#         self.log('already_login_account')
#
#         sleep(1)
#         already_login_account.click()
#
#         # 返回rumble页面
#         sleep(9999)
#
#     def delete_videos(self):
#         print('5秒后开始检测并删除视频')
#         sleep(5)
#         video_list = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="-v2"]/div[2]/div[2]')))
#         if video_list is not None:
#             print('视频列表不为空， 长度：', len(video_list))
#             self.start_delete()
#
#         else:
#             print('没找到视频列表,代表删除完毕，10秒后退出程序')
#             sleep(1000)
#
#     def start_delete(self):
#         video_title = self.wait.until(EC.presence_of_element_located(
#             (By.XPATH, '//*[@id="8_107669550_1phklg_item"]/article/div[1]/div/header/h2')))
#         if video_title is not None:
#             print('即将删除：' + video_title.text)
#
#         sleep(1)
#         more_btn = self.wait.until(
#             EC.presence_of_element_located((By.XPATH, '//*[@id="8_107669550_1phklg_item"]/article/div[2]/div/a')))
#         more_btn.click()
#         print('点击了三点')
#
#         sleep(1)
#         delete_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="delete"]')))
#         delete_btn.click()
#         print('点击了删除')
#
#         sleep(2)
#         confirm_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="0"]')))
#         confirm_btn.click()
#         print('点击了确定')
#
#         sleep(10)
#         self.driver.refresh()
#         print('刷新页面')
#
#     def log(self, text):
#         print('log: ' + text)
#
#
# # 按间距中的绿色按钮以运行脚本。
# if __name__ == '__main__':
#     Browser()
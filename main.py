import logging
import undetected_chromedriver.v2 as uc

# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from time import sleep

config = {
    'account': 'glavern89@gmail.com',
    'account_rec': 'meBBlznz2071@outlook.com',
    'password': 'dzEF5wUNb',
    'website': ''
}

logging.basicConfig(level=logging.INFO)


class Browser:
    def __init__(self):
        self.chrome_options = None
        self.wait = None
        self.driver = None
        self.delete_times = int(0)
        self.all_waiting_delete_videos_count = 0
        logging.info('browser __init__ finished')
        self.open_browser_window()

    def open_browser_window(self):
        logging.info('正在打开浏览器窗口')
        self.driver = uc.Chrome(
            use_subprocess=True,
            version_main=107,  # 指定版本
            executable_path='C:/Program Files/Google/Chrome/Application/chromedriver.exe'
        )
        self.driver.set_window_size(1100, 600)
        self.wait = WebDriverWait(self.driver, 100)
        self.chrome_options = uc.ChromeOptions()
        self._init_options()

        print('浏览器窗口打开成功', self.delete_times)

        self.login_google()

    def _init_options(self):
        logging.info('给浏览器添加启动参数')
        self.chrome_options.add_argument("--ignore-certificate-errors")
        self.chrome_options.add_experimental_option('detach', True)
        self.chrome_options.add_argument('--no-default-browser-check')
        self.chrome_options.add_argument("--user-data-dir=C:/Users/{userName}/AppData/Local/Google/Chrome/User Data/Profile {#}/")

    def open_link_in_browser(self, link):
        logging.info('正在打开' + link)
        self.driver.get(link)

    def login_google(self):
        self.open_link_in_browser('https://google.com')

        # 找到登录按钮并点击
        logging.info('找到登录按钮并点击')
        login_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="gb"]/div/div[2]/a')))
        login_btn.click()
        logging.info('登录按钮已点击')

        # 输入邮箱
        logging.info('输入邮箱：' + config.get('account'))
        email_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="identifierId"]')))
        email_input.send_keys(config.get('account'))
        logging.info('输入邮箱完成')

        # 点击下一步
        logging.info('下一步')
        email_next_step = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="identifierNext"]')))
        email_next_step.click()
        logging.info('已点击下一步')

        # 输入密码
        logging.info('输入密码')
        password_input = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
        password_input.send_keys(config.get('password'))
        logging.info('输入密码完成')

        # 点击下一步
        logging.info('下一步')
        pass_next_step = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="passwordNext"]')))
        pass_next_step.click()
        logging.info('已点击下一步')
        sleep(10)
        try:
            rec_email_confirm = self.driver.find_element(By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/ul/li[3]')
            rec_email_confirm.click()

            rec_email_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="knowledge-preregistered-email-response"]')))
            rec_email_input.send_keys(config.get('account_rec'))

            rec_email_next_step = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')))
            rec_email_next_step.click()
        except exceptions.NoSuchElementException:
            logging.info('google登录完成，即将打开rumble')
            # sleep(5999)
            self.login_rumble()

    def login_rumble(self):
        self.open_link_in_browser('https://rumble.com')

        # 登录按钮
        rumble_login_btn = self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/header/div/button[3]')))
        rumble_login_btn.click()
        logging.info('点按钮登录rumble')

        google_login_btn = self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div/section/div[3]/button[2]')))
        google_login_btn.click()
        logging.info('谷歌登录点击')

        sleep(10)

        user_info_text = self.driver.find_element(By.XPATH, '/html/body/header/div/button[3]')
        user_info_text.click()
        logging.info('点击rumble头像')

        sleep(2)
        my_content = self.driver.find_element(By.XPATH, '//*[@id="header-user-menu"]/a[3]')
        my_content.click()
        logging.info('进入视频页面')
        sleep(5)

        videos_count = len(self.driver.find_elements(By.CSS_SELECTOR, '.my-videos-nav .activate-dd'))
        if videos_count > 0:
            print('当前有', videos_count, '条可删除的视频')
            self.all_waiting_delete_videos_count = videos_count
            self.delete_videos()
        else:
            logging.info('没有可删除的视频，即将退出')
            sleep(5)
            self.driver.quit()

    def delete_videos(self):
        logging.info('开始删除视频')
        sleep(2)
        videos_more = self.driver.find_elements(By.CSS_SELECTOR, '.my-videos-nav .activate-dd')
        if len(videos_more) > 0:
            self.delete_times += 1
            print('开始删除第', self.delete_times, '条视频')
            first_video_more = self.driver.find_elements(By.CSS_SELECTOR, '.my-videos-nav .activate-dd')[0]
            first_video_more.click()
            logging.info('点击更多')

            sleep(2)
            delete_btn = self.driver.find_element(By.XPATH, '//*[@id="delete"]')
            delete_btn.click()
            logging.info('点击删除')

            sleep(2)
            delete_confirm = self.driver.find_element(By.XPATH, '//*[@id="0"]')
            delete_confirm.click()
            logging.info('确认删除点击')

            sleep(10)
            logging.info('确认删除完成，即将刷新并重新检测')

            self.driver.refresh()
            self.delete_videos()
        else:
            logging.info('没有可删除的视频，即将退出')
            sleep(5)
            self.driver.quit()


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    Browser()
import undetected_chromedriver as uc
import tkinter as tk

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

config = {
    'account': '',
    'account_rec': '',
    'password': '',
    'website': ''
}


class Browser:
    def __init__(self):
        self.driver = uc.Chrome(use_subprocess=True, executable_path='C:/Program Files/Google/Chrome/Application/chromedriver.exe')
        self.wait = WebDriverWait.Wait(self.driver, 20)
        self.chrome_options = uc.ChromeOptions()
        self._init_options()

    def _init_options(self):
        self.chrome_options.add_argument("--ignore-certificate-errors")
        self.chrome_options.add_experimental_option('detach', True)
        self.chrome_options.add_argument('--no-default-browser-check')
        self.chrome_options.add_argument("--user-data-dir=C:/Users/{userName}/AppData/Local/Google/Chrome/User Data/Profile {#}/")

    def open_link_in_browser(self, link):
        self.driver.set_window_size(1100, 600)
        self.driver.get(link)

    def login(self):
        # # 找到登录按钮并点击
        # login_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="gb"]/div/div[2]/a')))
        # login_btn.click()
        sleep(1)
        # 输入邮箱
        print('输入邮箱：' + config.get('account'))
        email_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="identifierId"]')))
        email_input.send_keys(config.get('account'))

        # 点击下一步
        print('下一步')
        email_next_step = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="identifierNext"]')))
        email_next_step.click()

        # 输入密码
        print('输入密码')
        password_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
        password_input.send_keys(config.get('password'))

        # 点击下一步
        print('下一步')
        pass_next_step = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="passwordNext"]')))
        pass_next_step.click()
        print('google登录完成，即将打开rumble')

        recovery_email = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/ul/li[3]')))
        if recovery_email is not None:
            print('需要验证辅助邮箱')
            recovery_email.click()
            recovery_email_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="knowledge-preregistered-email-response"]')))
            print('输入辅助邮箱')
            recovery_email_input.send_keys(config.get('account_rec'))

            print('下一步')
            recovery_next_step = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button')))
            recovery_next_step.click()
            sleep(5)
            self.login_rumble()

    def login_rumble(self):
        sleep(1)
        print('打开rumble')
        self.driver.get('https://rumble.com')

        rumble_login_btn = self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/header/div/button[3]')))
        rumble_login_btn.click()

        sleep(2)
        google_login_btn = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, '/html/body/div[2]/div/div[2]/div/section/div[3]/button[2]')))
        google_login_btn.click()

        # sleep(2)
        # # 打开google的iframe页面，进行登录
        # google_login_iframe = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'iframe')))
        # driver.switch_to.frame(google_login_iframe)
        #
        # sleep(2)
        # # 点击iframe的已登录账户进行登录
        # already_login_account = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/div/ul/li[1]')))
        # already_login_account.click()
        # sleep(1)
        # already_login_account.click()
        # sleep(1)
        # already_login_account.click()


        # 返回rumble页面
        sleep(5)

        # 点击头像
        user_header = self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/header/div/button[3]')))
        if user_header is not None:
            user_header_btn = self.wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/header/div/button[3]')))
            print('点击头像框')
            user_header_btn.click()

            # 点击MyContent
            my_content = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="header-user-menu"]/a[3]')))
            my_content.click()

            # 点击All Videos
            all_videos = self.wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="-v2"]/div[1]/div[2]/ul[2]/li[2]')))
            all_videos.click()

            # 持久化
            sleep(3)
            self.delete_videos()

    def delete_videos(self):
        print('5秒后开始检测并删除视频')
        sleep(5)
        video_list = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="-v2"]/div[2]/div[2]')))
        if video_list is not None:
            print('视频列表不为空， 长度：', len(video_list))
            self.start_delete()

        else:
            print('没找到视频列表,代表删除完毕，10秒后退出程序')
            sleep(1000)


    def start_delete(self):
        video_title = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="8_107669550_1phklg_item"]/article/div[1]/div/header/h2')))
        if video_title is not None:
            print('即将删除：' + video_title.text)

        sleep(1)
        more_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="8_107669550_1phklg_item"]/article/div[2]/div/a')))
        more_btn.click()
        print('点击了三点')

        sleep(1)
        delete_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="delete"]')))
        delete_btn.click()
        print('点击了删除')

        sleep(2)
        confirm_btn = self.wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="0"]')))
        confirm_btn.click()
        print('点击了确定')

        sleep(10)
        self.driver.refresh()
        print('刷新页面')


class App:
    def __init__(self):
        self.root_window = tk.Tk()
        self.root_window.title('自动删除Rumble已上传视频')
        self.root_window.geometry('500x600')

        tk.Label(self.root_window, text='谷歌邮箱：', font=('XHei', 15), padx=3, pady=5).pack()
        tk.Label(self.root_window, text='谷歌邮箱(恢复)：', font=('XHei', 15), padx=3, pady=20).pack()
        tk.Label(self.root_window, text='谷歌密码：', font=('XHei', 15), padx=3, pady=35).pack()

        self.account_entry = tk.Entry(self.root_window)
        self.account_entry.insert(0, 'tarfinhasan65@gmail.com')

        self.account_recovery_entry = tk.Entry(self.root_window)
        self.account_recovery_entry.insert(0, 'DeltsiiaEftefeeva@mail.ru')

        self.password_entry = tk.Entry(self.root_window)
        self.password_entry.insert(0, 'atiati90')

        tk.Button(self.root_window, text='开始', command=self.get_info, padx=5, pady=70).pack()
        tk.Button(self.root_window, text='退出', command=self.quit, padx=20, pady=70).pack()

        self.account_entry.pack(padx=10, pady=5)
        self.account_recovery_entry.pack(padx=10, pady=20)
        self.password_entry.pack(padx=10, pady=35)
        self.root_window.mainloop()

    def get_info(self):
        info = {
            'account': self.account_entry.get(),
            'recovery_account': self.account_recovery_entry.get(),
            'password': self.password_entry.get()
        }
        print('get_info, account: ' + info.get('account'))
        print('get_info, recovery_account: ' + info.get('recovery_account'))
        print('get_info, password: ' + info.get('password'))
        return info

    def quit(self):
        self.root_window.quit()


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    app = App()



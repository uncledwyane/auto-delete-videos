from selenium import webdriver
from selenium.webdriver.common.by import By


eg_option = webdriver.ChromeOptions()
config = {
    # chrome不弹出的“是否接受xxx通知”
    'profile.default_content_setting_values.notifications': 2,
    # chrome开启麦克风--重点
    "profile.default_content_setting_values.media_stream_mic": 1,
    # chrome开启摄像头--重点
    "profile.default_content_setting_values.media_stream_camera": 1
}
eg_option.add_experimental_option('prefs', config)
# 忽略证书错误
eg_option.add_argument('--ignore-certificate-errors')

# 创建一个webdriver
driver = webdriver.Edge(options=eg_option)

# 打开页面
# driver.get('https://avd.nice2meet.cn:9889/demo/demo4.0.4.5/sdk_guide.html')

# 设置窗口大小
# driver.set_window_size(1300, 800)

# waiting time
# driver.implicitly_wait(3)

# find a element by xpath rule
# joinBtn = driver.find_element(By.XPATH, '/html/body/input[11]')


def delete_videos():
    # 拿到所有视频的三个点的元素
    more_links = driver.find_element(By.CLASS_NAME, 'activate-dd')
    if len(more_links) > 0:
        # 取第一个视频的三个点的元素
        more_link = more_links[0]
        # 点击三个点
        more_link.click()

        delete_link = driver.find_element(By.ID, 'delete')
        delete_link.click()
        # 等待1秒
        driver.implicitly_wait(1)



import os


from selenium import webdriver
from selenium.webdriver.common.by import By


def seltest():
    cur_dir = os.path.dirname(__file__)
    text_file = os.path.join(cur_dir, 'text.txt')
    driver = webdriver.Chrome()
    driver.get('https://suninjuly.github.io/file_input.html')
    driver.find_element(
        By.CSS_SELECTOR, '[name=\'firstname\']'
        ).send_keys('a')
    driver.find_element(
        By.CSS_SELECTOR, '[name=\'lastname\']'
        ).send_keys('a')
    driver.find_element(By.CSS_SELECTOR, '[name=\'email\']').send_keys('a')
    file_box = driver.find_element(By.CSS_SELECTOR, '#file')
    file_box.send_keys(text_file)
    driver.find_element(By.CSS_SELECTOR, '.btn, .btn-primary').click()
    driver.quit()


if __name__ == '__main__':
    seltest()

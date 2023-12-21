from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    with Chrome() as driver:
        driver.get('https://justinfarnsworth.io')
        assert 'Justin Farnsworth' in driver.title
        assert 'Contact Me' in driver.page_source

        form = driver.find_element(By.TAG_NAME, 'form')
        name = form.find_element(By.NAME, 'name')
        name.send_keys('Selenium Tutorial')
        email = form.find_element(By.NAME, 'email')
        email.send_keys('selenium@tutorial.com')
        subject = form.find_element(By.NAME, 'subject')
        subject.send_keys('Test Via Selenium')
        message = form.find_element(By.NAME, 'message')
        message.send_keys('This was a test on Selenium!\nHooray!')
        form.submit()

        button = form.find_element(By.TAG_NAME, 'button')
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(button))


if __name__ == '__main__':
    main()

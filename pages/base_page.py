from selenium.common.exceptions import NoSuchElementException as NE


class BasePage:
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        answer = True
        try:
            self.browser.find_element(how, what)
        except NE:
            answer = False
        return answer

from selenium import webdriver


def scrape():
    browser = webdriver.Chrome()
    browser.get('http://inventwithpython.com')


if __name__ == "__main__":
    scrape()
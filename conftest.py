import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', default='en-gb')  # добавляем параметр, с которым будет запускаться тест


@pytest.fixture(scope='function')
def browser(request):
    browser_language = Options()
    browser_language.add_experimental_option(
        'prefs',
        {'intl.accept_languages':
             request.config.getoption('language')})  # присваиваем browser-language значение из командной строки
    browser = webdriver.Chrome(options=browser_language)
    yield browser
    browser.quit()

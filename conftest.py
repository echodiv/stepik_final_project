import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help='Enter language. default "en"')


@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language })
    print('\nstart browser...')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser...')
    browser.quit()
#

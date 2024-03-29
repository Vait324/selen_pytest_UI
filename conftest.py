import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        '--language',
        action='store',
        default='en',
        help='Choose language',
        choices=('en', 'ru', 'es', 'fr'),)


@pytest.fixture
def browser(request):
    """Fixture that start Chrome webdriver with choosed browser language."""
    user_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language}
        )
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

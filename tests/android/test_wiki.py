from allure_commons._allure import step
from selene import have
from selene.support.shared import browser


def test_search_browserstack():
    with step('Проверить что "BrowserStack" найден'):
        browser.element('Search Wikipedia').click()
        browser.element('#search_src_text').type('BrowserStack')
        browser.all('#page_list_item_title').should(have.size_greater_than(0))


def test_search_youtube():
    with step('Проверить что "YouTube" найден'):
        browser.element('#search_src_text').clear()
        browser.element('#search_src_text').type('YouTube')
        browser.all('#page_list_item_title').should(have.size_greater_than(0))


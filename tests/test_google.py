
from selene import by, be, have
from selene.support.shared import browser


def test_search():
    browser.open('https://google.com/')

    browser.element(by.name('q')).should(be.blank)\
        .type('python selene').press_enter()

    browser.all('#search .g').should(have.size_greater_than_or_equal(6))\
        .first.should(have.text('Concise API for Selenium'))\
        .element('.r>a').click()

    browser.should(have.title_containing('yashaka/selene'))
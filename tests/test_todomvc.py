from selene import by, be, have
from selene.support.shared import browser

def test_complete_task():
    # open TodoMVC page
    browser.open('http://todomvc.com/examples/emberjs/')

    # add tasks: 'a', 'b', 'c'
    browser.element(by.id('new-todo')).type('a').press_enter()
    browser.element(by.id('new-todo')).type('b').press_enter()
    browser.element(by.id('new-todo')).type('c').press_enter()

    # tasks should be 'a', 'b', 'c'
    browser.all('#todo-list>li').should(have.exact_texts('a', 'b', 'c'))

    # toggle 'b'
    browser.all('#todo-list>li').should(have.exact_texts('b')).element('.toggle').click()
    # completed tasks should be 'b'
    browser.all('#todo-list>li').filtered_by(have.css_class('completed')).should(have.exact_texts('b'))
    # active tasks should be 'a', 'c'
    browser.all('#todo-list>li').filtered_by(have.no.css_class('completed')).should(have.exact_texts('a', 'c'))
    pass

test_complete_task()
from selenium import webdriver
import time

driver = webdriver.Chrome()

def test_setup():
    driver.get('http://localhost:8000/')
    time.sleep(5)

def test_add_todo():
    input_text = driver.find_element_by_id('formGroupExampleInput')
    input_text.send_keys('first task')
    time.sleep(2)
    add_button = driver.find_elements_by_css_selector(".btn-danger")[0]
    add_button.click()
    time.sleep(1)
    assert driver.find_elements_by_css_selector(".todo_title")[0].text == "first task"
    assert driver.find_elements_by_css_selector(".todo_id")[0].text == "1"

def test_add_second():
    input_text = driver.find_element_by_id('formGroupExampleInput')
    input_text.send_keys('second task')
    time.sleep(2)
    add_button = driver.find_elements_by_css_selector(".btn-danger")[0]
    add_button.click()
    time.sleep(1)
    assert driver.find_elements_by_css_selector(".todo_title")[1].text == "second task"
    assert driver.find_elements_by_css_selector(".todo_id")[1].text == "2"

def test_delete_first_todo():
    add_button = driver.find_elements_by_css_selector(".btn-danger")[1]
    add_button.click()
    time.sleep(1)
    assert driver.find_elements_by_css_selector(".todo_title")[0].text == "second task"
    assert driver.find_elements_by_css_selector(".todo_id")[0].text == "1"

def test_adelete_second_todo():
    add_button = driver.find_elements_by_css_selector(".btn-danger")[1]
    add_button.click()
    time.sleep(1)
    assert len(driver.find_elements_by_css_selector(".todo_title")) == 0
    assert len(driver.find_elements_by_css_selector(".todo_id")) == 0


def test_done():
    driver.quit()

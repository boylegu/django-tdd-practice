# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time # 为了调试,可用time.sleep


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path='../chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 打开首页
        self.browser.get('http://127.0.0.1:8000')

        # 确定断网页的标题和头部都包含了'TO-DO'这个词
        self.assertIn('To-Do', self.browser.title)
        head_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', head_text)

        # 输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 然后输入一个任务项
        inputbox.send_keys("Buy peacock feathers")

        # 按回车键之后,页面更新了
        # 并且办事项显示了相应的信息
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1: Buy peacock feathers')

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.fail('Finish the test')


if __name__ in '__main__':
    unittest.main(warnings='ignore')

'''
browser = webdriver.Chrome(executable_path='./chromedriver')
browser.get('http://127.0.0.1:8000')

assert 'Django' in browser.title
'''

# coding: utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path='../chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 打开首页
        self.browser.get('http://127.0.0.1:8000')

        # 确定断网页的标题和头部都包含了'TO-DO'这个词
        self.assertIn('To-Do', self.browser.title)
        head_text = self.browser.find_element_by_id('h1').text
        self.assertIn('To-Do', head_text)

        # 输入一个待办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # 然后输入一个任务项
        inputbox.send_keys("1: Buy peacock feathers")

        # 按回车键之后,页面更新了
        # 并且办事项显示了相应的信息
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows) # any() ?
        )

        # 此后页面中又显示了一个文本框,可以输入其他的待办事项,接着她又输入了......

        self.fail('Finish the test')

if __name__ in '__main__':
    unittest.main(warnings='ignore')


'''
browser = webdriver.Chrome(executable_path='./chromedriver')
browser.get('http://127.0.0.1:8000')

assert 'Django' in browser.title
'''
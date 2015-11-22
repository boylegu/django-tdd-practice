# coding: utf-8
from .base import FunctionalTest
from unittest import skip


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # 伊迪丝访问首页,不小心提交了一个空待办事项
        # 输入框中没输入内容,她就按下了回车键

        # 首页刷新了,显示一个错误消息
        # 提示待办事项不能为空

        # 她输入一些文字,然后再次提交,这次没问题了

        # 她有点调皮,又提交了一个空代办事项

        # 再清淡页面她看到了一个类似的错误消息

        # 输入文字之后就没有问题了

        self.fail('write me')

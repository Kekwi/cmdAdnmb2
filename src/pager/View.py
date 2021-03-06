# coding=utf-8
from abc import abstractmethod, ABCMeta

from src.out import OutPutUtil


class View(metaclass=ABCMeta):
    #  请求的数据
    data = None
    # 模板
    template = None
    # content
    content = None

    def __init__(self, template):
        self.template = template
        self.on_creat()

    @abstractmethod
    def on_creat(self):
        """
        创建回调
        :return:
        """
        pass

    def init_data(self):
        """
       初始化数据
       :return:
       """
        self.data = self.get_data()

    def on_show(self):
        """
        # 显示回调
        :return:
        """
        if not self.data:
            self.init_data()
        self.print_pager()

    def refresh(self):
        """
        # 强制刷新
        :return:
        """
        self.init_data()


    # 销毁回调
    def on_destroy(self):
        # 销毁数据
        self.data = None
        # 销毁模板
        self.template = None

    @abstractmethod
    def get_data(self):
        """
        请求网络的方法 返回值会被设置 成 self.data
        :return:
        """

        pass

    def bind_template(self, template):
        """
        绑定模板
        :param template:
        :return:
        """
        self.template = template

    def print_pager(self):
        """
        打印页面
        :return:
        """
        if not self.template:
            raise RuntimeError('template is  Unbound')
        self.print_text(self.template.generate_all(self.data))

    def print_header(self):
        """
        打印头
        :return:
        """
        OutPutUtil.singleton.log(self.template.generate_header(self.data))

    def print_footer(self):
        """
        打印脚
        :return:
        """
        OutPutUtil.singleton.log(self.template.generate_footer(self.data))

    def print_content(self):
        OutPutUtil.singleton.log(self.template.generate_content(self.data))

    def print_text(self, text):
        """
        打印 text
        :param text:
        :return:
        """
        OutPutUtil.singleton.log(text)

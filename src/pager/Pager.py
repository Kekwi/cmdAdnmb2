from src.pager.View import *
from abc import ABC


class Pager(View, ABC):

    def init_data(self):
        """
        初始化数据
        :return:
        """
        pass

    def on_destroy(self):
        self.data = None

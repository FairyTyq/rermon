# coding:utf-8

"""
rmon.views.index
视图首页
"""

from flask import render_template
from flask.views import MethodView

class IndexView(MethodView):
    """
    首页视图函数
    """
    def get(self):
        """
        渲染模版
        """
        return render_template('index.html')

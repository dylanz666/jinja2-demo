#!/usr/local/bin/python3
# -*- coding:utf-8 -*-

__author__ = "diren"
__date__ = "2021-01-03 15:50"

import os
import time

from jinja2 import Environment, PackageLoader


class ReportUtil:
    def __init__(self):
        pass

    def write_output_html(self, template_name, html):
        current_dir = os.getcwd()
        output_dir = os.path.join(current_dir, "../resources/output/")
        if not os.path.exists(output_dir):
            os.mkdir(output_dir)
        os.chdir(output_dir)

        fo = open(template_name, "w")
        fo.writelines(html)
        fo.close()
        os.chdir(current_dir)
        print(f"create {template_name}:", "完成")

    def create_jinja2_demo_1_html(self):
        index = 1
        status = "成功"
        message = "这是一个测试文本"
        created_when = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        env = Environment(loader=PackageLoader('resources', 'templates'))
        template_name = "jinja2_demo_1.html"
        template = env.get_template(template_name)
        html = template.render(index=index, message=message, created_when=created_when, status=status)

        self.write_output_html(template_name, html)

    def create_jinja2_demo_2_html(self):
        title = "测试报告"
        status = "失败"
        created_when = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        details = [{
            "status": "成功",
            "message": "测试文本1",
            "created_when": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        }, {
            "index": 2,
            "status": "失败",
            "message": "测试文本2",
            "created_when": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        }, {
            "index": 3,
            "status": "成功",
            "message": "测试文本2",
            "created_when": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        }]

        env = Environment(loader=PackageLoader('resources', 'templates'))
        template_name = 'jinja2_demo_2.html'
        template = env.get_template(template_name)
        html = template.render(title=title, status=status, created_when=created_when, details=details)

        self.write_output_html(template_name, html)

    def create_jinja2_demo_3_html(self):
        title = "人员信息"
        status = "采集成功"
        created_when = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        test_dict = {
            "name": "dylanz",
            "gender": "male",
            "age": 18,
            "professional": "TA"
        }

        env = Environment(loader=PackageLoader('resources', 'templates'))
        template_name = 'jinja2_demo_3.html'
        template = env.get_template(template_name)
        html = template.render(title=title, status=status, created_when=created_when, test_dict=test_dict)

        self.write_output_html(template_name, html)

    def create_jinja2_macro_demo_1_html(self):
        env = Environment(loader=PackageLoader('resources', 'templates'))
        template_name = 'jinja2_macro_demo_1.html'
        template = env.get_template(template_name)
        html = template.render(user_name='dylanz', pass_word='123')

        self.write_output_html(template_name, html)

    def create_jinja2_macro_demo_2_html(self):
        env = Environment(loader=PackageLoader('resources', 'templates'))
        template_name = 'jinja2_macro_demo_2.html'
        template = env.get_template(template_name)
        html = template.render(user_name='dylanz', pass_word='123')

        self.write_output_html(template_name, html)

    def create_child_html(self):
        env = Environment(loader=PackageLoader('resources', 'templates'))
        template_name = 'child.html'
        template = env.get_template(template_name)
        html = template.render()

        self.write_output_html(template_name, html)


if __name__ == "__main__":
    ReportUtil().create_jinja2_demo_1_html()
    ReportUtil().create_jinja2_demo_2_html()
    ReportUtil().create_jinja2_demo_3_html()
    ReportUtil().create_jinja2_macro_demo_1_html()
    ReportUtil().create_jinja2_macro_demo_2_html()
    ReportUtil().create_child_html()

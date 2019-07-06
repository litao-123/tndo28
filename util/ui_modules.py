from  tornado.web import UIModule


class TestModule(UIModule):
    def render(self, *args, **kwargs):
        return 'ui_modules'

class Advertisement(UIModule):
    def render(self, *args, **kwargs):
        return self.render_string('06ad.html') #返回页面需要使用render_string

    def javascript_files(self):
        return [        #需要返回多个是需要使用列表
            'js/jquery_1_7.js',
            'js/King_Chance_Layer.js',
            'js/King_layer_test.js'
        ]

    def css_files(self):
        return 'css/King_Chance_Layer7.css'
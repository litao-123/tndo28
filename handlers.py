import glob

import os
import tornado.web
from PIL import Image

from handlers.main import BaseHandler
from util.mod_file import Calculation


class IndexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        # self.write("aa Hello, world nihao")
        self.render('01in_out.html')

class PictureHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        os.chdir('static')
        names = glob.glob('upload/*jpg')
        os.chdir('..')
        print(os.getcwd())
        self.render('08picture.html',names=names)

class TemplateHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        # self.write('templates page')
        # self.render('01in_out.html')
        atga = """
        <a href="http://www.qq.com">__QQ__</a><br>
        """
        name=self.get_argument('name','')
        self.render('02-templates.html',username=name,atga=atga)

    def post(self):
        user = self.get_argument('name','no')
        self.render('02-templates.html',username=user)


class ExtendHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self):
        name=self.get_argument('name','')
        self.render('04-extend.html',username=self.current_user,
                    haha=self.haha,
                    cacul =Calculation
        )

    def haha(self):
        return 'thisis test'

class SubmitHandler(BaseHandler):
    def get(self):
        username = ''
        if not self.session.get('tudo_cookie'):
            print('your cookie was not set yet!')
        else:
            print(self.session.get('todo_cookie'))
            # print(self.get_cookie('todo_cookie'))
            username = self.session.get('tudo_cookie')
        next_url =self.get_argument('next','')
        self.render('submit.html',username=username,next_url=next_url)

    def post(self):
        username=self.get_argument('username','')
        password=self.get_argument('password','')
        next_url = self.get_argument('next','')

        print('username:{},password:{}'.format(username,password))
        print('next url:{}'.format(next_url))

        if not username.strip() or not password.strip():
            self.redirect('/temp')
        else:
            if username == 'qq' and password == 'qq':
                # self.set_secure_cookie('tudo_cookie','qq')
                self.session.set('tudo_cookie','qq')
                if next_url:
                    self.redirect(next_url)
                else:
                    self.redirect('/pic')
            else:
                self.redirect('/temp')

class UploadHandler(BaseHandler):
    def get(self):
        self.render('07upload.html')
    def post(self):
        pics = self.request.files.get('picture','[]')
        print(pics[0]['filename'])
        for p in pics:
            save_path = 'static/upload/{}'.format(p['filename'])
            print(save_path)
            # print(p['body'])
            print(p['content_type'])
            with open(save_path,'wb') as fh:
                fh.write(p['body'])

            im = Image.open(save_path)
            im.thumbnail((200,200))
            im.save('static/upload/{}_thumb.jpg'.format(p['filename']),'JPEG')

        self.redirect('/pic')


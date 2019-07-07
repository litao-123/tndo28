import hashlib

from models.auth import User,Session,Post
from models.db import Session

db_session = Session()
def hashed(text):
    return hashlib.md5(text.encode('utf8')).hexdigest()

def authenticate(username,password):
    # session = Session()
    # user = session.query(User).filter_by(name=username).first()
    return User.get_password(username) == hashed(password)


def register(username,password):
    session = Session()
    session.add(User(name=username,password=hashed(password)))
    session.commit()
    session.close()


def add_post(image_url,thumb_url,username):
    session = Session()
    user = session.query(User).filter_by(name=username).first()
    post = Post(image_url=image_url,thumb_url=thumb_url,user=user)
    session.add(post)
    session.commit()
    post_id = post.id
    session.close()

    return post_id

def get_all_posts():
    posts = db_session.query(Post).all()
    return posts

def get_posts_for(username):
    user = db_session.query(User).filter_by(name=username).first()
    posts = db_session.query(Post).filter_by(user=user).all()
    return posts

def get_post(post_id):
    post = db_session.query(Post).filter_by(id=post_id).first()
    return post
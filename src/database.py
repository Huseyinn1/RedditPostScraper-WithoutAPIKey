from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker,Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class RedditPost(Base):
    __tablename__ = 'reddit_posts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    author = Column(String)
    likes = Column(Integer)
    date = Column(String)
    content = Column(String)
    url = Column(String)
    comment = Column(String)

# Veritabanı bağlantısı oluştur
engine = create_engine('sqlite:///reddit_posts.db')
Session = sessionmaker(bind=engine)
session = Session()

def create_table():
    Base.metadata.create_all(engine)

def is_post_exists(url):
    post = session.query(RedditPost).filter_by(url=url).first()
    return post is not None

def insert_post(title, author, likes, date, content, url, comment):
    if not is_post_exists(url):
        post = RedditPost(title=title, author=author, likes=likes, date=date, content=content, url=url, comment=comment)
        session.add(post)
        session.commit()
        print(f"Post with title '{title}' added successfully!")
    #else:
      #  print(f"Post with URL '{url}' already exists!")
def delete_post(title):
    post = session.query(RedditPost).filter_by(title=title).first()
    if post:
        session.delete(post)
        session.commit()
        print(f"Post with title '{title}' deleted successfully!")
    else:
        print(f"Post with title '{title}' not found!")
        
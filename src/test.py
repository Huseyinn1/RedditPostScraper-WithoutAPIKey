

import unittest
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from src.database import Base, RedditPost, delete_post, insert_post


class TestRedditCrawler(unittest.TestCase):

    def setUp(self):
        engine = create_engine('sqlite:///reddit_posts.db')
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def tearDown(self):
        self.session.close()

    
    def test_insert_post(self):
        
        insert_post('Test Title3', 'Test Author', 10, '2023-07-10', 'Test Content', 'https://example.com', 'Test Comment')
        print("insert post başarılı")


if __name__ == '__main__':
    unittest.main()
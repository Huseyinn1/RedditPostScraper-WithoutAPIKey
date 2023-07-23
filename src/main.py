from reddit_scraping import get_post_details
from database import create_table
from flask import Flask

app = Flask(__name__)


if __name__ == '__main__':
    
    create_table()
    get_post_details()
    


    app.run()
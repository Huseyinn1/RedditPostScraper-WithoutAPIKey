from database import insert_post
from playwright.sync_api import sync_playwright
import time
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv
def login_reddit(page,username,password):
    page.goto("https://www.reddit.com/login")
    page.fill('input[name="username"]', username)
    page.fill('input[name="password"]', password)
    page.click('button[type="submit"]')
    page.wait_for_load_state('networkidle', timeout=60000)
    
    
def parse_time_string(time_string):
    if 'minute' in time_string:
        minutes_ago = int(time_string.split()[0])
        time_ago = datetime.now() - timedelta(minutes=minutes_ago)
    elif 'hour' in time_string:
        hours_ago = int(time_string.split()[0])
        time_ago = datetime.now() - timedelta(hours=hours_ago)
    elif 'day' in time_string:
        if 'yesterday' in time_string:
            time_ago = datetime.now() - timedelta(days=1)
        else:
            days_ago = int(time_string.split()[0])
            time_ago = datetime.now() - timedelta(days=days_ago)
    else:
        time_ago = None

    return time_ago


def create_post_page_Cookies(browser, cookies, local_storage):
    post_context = browser.new_context()
    post_context.add_cookies(cookies)
    post_context.add_init_script(f"window.localStorage={local_storage}")
    post_page = post_context.new_page()
    return post_page


# Playwright ile bir tarayıcı başlat
def get_post_details():
    with sync_playwright() as p:

        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        print("Login işlemi başladı ")
        # Subreddit sayfasına git
        subreddit = 'nasa'
        load_dotenv()
        username=os.getenv("REDDİT_USERNAME")
        password=os.getenv("REDDİT_PASSWORD")
        print(username)
        login_reddit(page,username, password)
        print("Login olundu ")
        page.goto(f"https://www.reddit.com/r/{subreddit}/new")
        # Son 10 postun seçicilerini bul
        print("Subreddite yönlendirildi ")
                
        while True:
            posts = page.query_selector_all(".Post")
            print("postlar alınıyorr")
            
            # Her post için başlık, yazar ,içerik ,yorum,beğeni,tarih ve url ilgilerini al ve konsola yazdır
            for post in posts:
                    
                    title_element = post.query_selector('h3._eYtD2XCVieq6emjKBH3m').text_content()
                    author_element = post.query_selector('a[data-testid="post_author_link"]').text_content()
                    url_element = post.query_selector('a[data-click-id="body"]').get_attribute('href')
                    date_element = post.query_selector('span[data-testid="post_timestamp"]').text_content()
                    date_time = parse_time_string(date_element)
                    likes_element = post.query_selector('div._1rZYMD_4xY3gRcSS3p8ODO._25IkBM0rRUqWX5ZojEMAFQ').text_content()

                   # content_element =post.query_selector('div._292iotee39Lmt0MkQZ2hPV.RichTextJSON-root')
                    cookies = page.context.cookies()
                    local_storage = page.evaluate("() => Object.assign({},window.localStorage)")
                    post_page = create_post_page_Cookies(browser,cookies,local_storage)
                    
                    post_page_url=f"https://www.reddit.com{url_element}"
                    post_page.goto(post_page_url)
                   
                    #Contenti alır
                    content_element =post_page.query_selector('div._292iotee39Lmt0MkQZ2hPV.RichTextJSON-root').text_content()
                    if not content_element :
                        content_element="No text content"
                    #image_element = post_page.query_selector('img[class="_1dwExqTGJH2jnA-MYGkEL-"]').get_attribute('src')
                   
                    #Yorumları alır   
                    comments = post_page.query_selector_all('[data-testid="comment"]')
                    comment = [ post_comment_element.inner_text() for post_comment_element in comments]
                    comment_string = '\n'.join(comment)
                    
                    #comments_author = post_page.query_selector_all('[data-testid="comment_author_link"]')
                    insert_post(title_element, author_element, likes_element, date_time, content_element,post_page_url,comment_string)
                # Tarayıcıyı kapat
            page.reload()
            time.sleep(3)   
            




# RedditPostScraper-WithoutAPI

RedditScraper is a simple Reddit post scraper project written in Python. This project fetches new posts by scraping the desired Reddit web page and saves the title, content, date, author,
likes, and comments of these posts to the database. Playwright library is used to directly fetch content from Reddit web pages without using the PRAW library or Reddit API.


## Installation

Follow the steps below to install the required dependencies for the project:

1.Ensure that Python is installed on your system.

2.Clone this repository or download it as a ZIP.

3.Navigate to the main directory and run the following command: pip install -r requirements.txt

## How to Use

1. Add your Reddit account username and password to the .env file: 
REDDIT_USERNAME=your_username
REDDIT_PASSWORD=your_password
2. Run the command in the project's main directory to fetch Reddit posts and save them to the database:
    python main.py
3. You can customize the project to examine the posts in the database and perform other tasks
## API Usage

RedditScraper provides an API to fetch and save Reddit posts to the database. The API can be used with HTTP GET or POST requests and returns data in JSON format.

### Endpoints:

1. `/posts`

   - Method: GET
   -Description:Fetches all Reddit posts.
   - Example Usage: `http://127.0.0.1:8000/posts`


2. `/post/{post_id}`

   - Method: GET
   - Description:Fetches a specific Reddit post using post_id.
   - Example Usage: `http://127.0.0.1:8000/post/5`
![posts2](https://github.com/Huseyinn1/RedditPostScraper-WithoutAPI/assets/88551122/26ed50c1-cbc9-4e45-863a-e12b63fae56c)

## Screen Shots
![termianl](https://github.com/Huseyinn1/RedditPostScraper-WithoutAPI/assets/88551122/2f77f3ce-fae5-4412-91f0-3d04cfa1a510)

![redditdb](https://github.com/Huseyinn1/RedditPostScraper-WithoutAPI/assets/88551122/ca956c10-c6e3-4b0d-90ff-0adceb78b03f)
Comments =>>
![redditcomments](https://github.com/Huseyinn1/RedditPostScraper-WithoutAPI/assets/88551122/1f7e0992-f411-46af-9ec9-d0082dc83efb)


## Notes

-This project may be subject to changes due to the structure of the Reddit web pages. If necessary, the code should be edited to keep the project up to date and functional.
## Contribution

-We welcome all kinds of contributions and suggestions. Please fork this repository and make your contributions. Then create a Pull Request to share the changes.  

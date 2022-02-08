import requests
from bs4 import BeautifulSoup

# connects to the steam forum page 
# and scrapes titles and dates of the first page posts
def scraper(url):

    # cfg 
    URL = url

    # end cfg

    # GET url
    res = requests.get(URL)

    # instance and parse data from GET request
    soup = BeautifulSoup(res.text)

    # get only the posts from the page
    posts = soup.find_all(class_="forum_topic unread")

    # create list of posts
    posts_list = []

    for post in posts:
        posts_list.append({
            "date": str.strip(post.find(class_="forum_topic_lastpost").get_text()),
            "thread": str.strip(post.find(class_="forum_topic_name").get_text()),
            "link": str.strip(post.find(class_="forum_topic_overlay")["href"])
        })


    return posts_list

from bin.date_converter import convert_date
from bin.date_comparer import date_comparer
from bin.steam_scraper import scraper
from bin.email_sender import send_emails
from bin.store_pass import set_pass
from datetime import datetime
import json

CURR_YEAR = str(datetime.today().year - 1)

# init config
with open('config.json', 'r') as f:
    config = json.load(f)

# if this is first run, then gather some data;
if config["APP"]["first_run"] == "true":
    config["APP"]["first_run"] = "false"
    config["MAIL"]["login"] = set_pass()                        # this calls keyring module and stores the pass
    config["MAIL"]["service"] = "scraper"                       # this sets fixed value for the keyring service
    latest_post = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # set time to current time for the first run
else:
    # set latest post date as variable
    latest_post = config['APP']['date']

# init scraper
# receive list of posts
unfiltered_posts = scraper(config['APP']['URL'])

# filter post from the current year from scraped list
posts = []
for i in unfiltered_posts:
    if CURR_YEAR in i['date']:
        pass
    else:
        posts.append(i)

# convert all of the posts date to standard
converted_posts = []
for i in posts:
    converted_posts.append(convert_date(i))

# overwrite the date for the latest post (in json)
config["APP"]["date"] = converted_posts[0]['date']

# update json
with open('config.json', 'w') as f:
    json.dump(config, f)

# check if there are any new posts, if so - proceed
if posts:
    filtered_posts = date_comparer(converted_posts, latest_post)    #compare posts' date with the date stored in cfg
    send_emails(filtered_posts)                                     #send only the recent posts 
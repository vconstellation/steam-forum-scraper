# this app takes the time from the scraper
# converts the timezone 
from datetime import datetime, timedelta

def convert_date(post):
    try:
        # get date out of argument's dictionary
        compare_against = post['date']

        # edge case when last post is X hours ago
        if 'hours ago' in compare_against:
            hours_ago = compare_against.split(" ", 1)[0]

            final = datetime.today() - timedelta(hours=int(hours_ago))

            post['date'] = final.strftime("%Y-%m-%d %H:%M:%S")

            return post
        else:     
            datetime_object = datetime.strptime(compare_against, "%d %b @ %I:%M%p")

            post_datetime = datetime_object.replace(year=datetime.now().year)
    
            # convert datetime obj to string:
            post['date'] = str(post_datetime)

            return post
    except UnboundLocalError as e:
        print(e)

from datetime import datetime

# runs through all of the posts,
# checks if they are new / fresh, appends to the new list
# which then is returned to the main
def date_comparer(posts, last_date):

    new_posts = []

    # convert last_date from str to datetime object
    last_date = datetime.strptime(last_date, "%Y-%m-%d %H:%M:%S")

    for i in posts:
        post_date = i['date']

        # convert iterated's post date to datetime obj
        post_date = datetime.strptime(post_date, "%Y-%m-%d %H:%M:%S")

        if post_date > last_date:
            new_posts.append(i)

    return new_posts
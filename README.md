# steam-forum-scraper

## Description
This is a simple scraper for the Steam's Forum, which checks whether there are any new posts in the forum selected by the User. If there are new posts, the scraper will list all of them (along with urls) and send a newsletter-like email with that information.
Sole purpose of this application is to simplify the process of keeping up to date with small, indie and upcoming games released on steam, by tracking any new activities on each project's steam forum. 

In detail: 

When the 'First Run' flag is set as true, the application will ask for the User's email and password - that will be used for sending the notification mail. While email address itself is stored in json, in plain text, the password is being stored inside system's keyring service (via python's keyring module).
Each time the application is executed it will scrape all threads from the first page of a steam forum, convert every thread's latest post date (from '5 Feb @ 7:44am' to '2022-02-05 07:44:00'), compare it, and if there are any new posts - the appliaction will format an email message with notification.

## Further development
As this application has been written with a small scope in mind, I don't personally intend on expanding upon it's features. 

Hypothetical further development could include additional scraper functionality, as in - sraping other social media platforms related to the game project (twitter, developer's own website, etc.).

## Technology

Besides Python's 3.9.6 standard library:

* BeautifulSoup4 ver. 4.10.0
* Keyring ver. 23.5.0

## Setup and Launch

Packages listed above are required.

Manually editing the config.json file is required - User needs to provide following keys:

* "URL": this is where the steam's forum url should go
* "recipients": this is a list which stores full email addresses of notification's recipients

Executing main.py in python will run the application.

If the "first_run" flag is set as true, during the first run application will ask the user for email address and credentials - this email will be used for sending notifications.
Since the application uses smtp library to send emails, depending on the email service provider, it may be necessary to allow 'less secure apps' to connect to it.  

## License
This project is licensed under the terms of the MIT license.

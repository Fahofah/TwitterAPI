from user import User
from database import Database
from twitter_utils import get_request_token
from twitter_utils import get_oauth_pin
from twitter_utils import get_access_token

Database.initialise(user='postgres', password='f1a2h3r4i5', host='localhost', database='Learning')


user_email = input('What is you e-mail address: ')

user = User.load_from_db_by_email(user_email)

if not user:
    first_name = input('first name: ')
    last_name = input('last name: ')

    request_token = get_request_token()

    oauth_pin = get_oauth_pin(request_token)

    access_token = get_access_token(request_token, oauth_pin)

    user = User(user_email, first_name, last_name, access_token['oauth_token'], access_token['oauth_token_secret'])
    user.save_to_db()


tweets = user.tweeter_request('https://api.twitter.com/1.1/search/tweets.json?q=computers+filter:images')

for tweet in tweets['statuses']:
    print(tweet['text'])



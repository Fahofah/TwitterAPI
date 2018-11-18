import oauth2
import constants
import urllib.parse as urlparse

consumer = oauth2.Consumer(constants.API_key, constants.API_key_secret)


def get_request_token():
    # Create a consumer, which uses CONSUMER_KEY and CONSUMER_KEY to identify our app uniquely
    client = oauth2.Client(consumer)

    # Use the client to perform a request for the request token
    response, content = client.request(constants.request_token_url, 'POST')
    if response.status != 200:
        print(f"A error {response.status} has occurred")

    # Get the request token parsing the query string returned
    return dict(urlparse.parse_qsl(content.decode('utf-8')))


def get_oauth_pin(request_token):
    # Ask the user to authorise our and give us the pin code
    print('Go tho the following address in your browser:')
    print(get_oauth_pin(request_token))

    return input('What is the PIN ?\n')


def get_oauth_verifier_url(request_token):
    return '{}?oauth_token={}'.format(constants.authorisation_url, request_token['oauth_token'])


def get_access_token(request_token, oauth_pin):
    # Create a token object which contains the request object and the verifier
    token = oauth2.Token(request_token['oauth_token'], request_token['oauth_token_secret'])
    token.set_verifier(oauth_pin)

    # Create a client with our consumer (our app) and the newly created (and verified) token
    client = oauth2.Client(consumer, token)

    # Ask Twitter for an access token and Twitter know it should give us it because we've verified the request token
    response, content = client.request(constants.access_token_url, 'POST')
    return dict(urlparse.parse_qsl(content.decode('utf-8')))

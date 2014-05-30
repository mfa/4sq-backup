import foursquare

# import credentials from extra file:
from credentials import CLIENT_ID, CLIENT_SECRET

client = foursquare.Foursquare(client_id=CLIENT_ID,
                               client_secret=CLIENT_SECRET,
                               redirect_uri='a.madflex.de')
auth_uri = client.oauth.auth_url()
print('Please authorize: ' + auth_uri)

# insert code from redirect url
code = raw_input('The code: ').strip()
access_token = client.oauth.get_token(code)

# Apply the returned access token to the client
client.set_access_token(access_token)

print("Your access token is: " + access_token)

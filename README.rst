============
 4sq-backup
============

dump all checkins in foursquare from logged in user as json


Setup
=====

1) get an API APP key on the foursquare page: https://foursquare.com/developers/apps
2) write a credentials.py with the following content (of course insert your data)

::

  CLIENT_ID = ''
  CLIENT_SECRET = ''

3) authorize your app for your account using 
   get_user_key.py

4) add to credentials.py

::

  USER_TOKEN

4) run backup.py

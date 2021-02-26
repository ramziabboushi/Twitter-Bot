import gspread
from twitter import *

consumer_key = '####################'
consumer_secret = '########################################'
token = '########################################'
token_secret = '############################################################'

gc = gspread.service_account('credentials.json')
t = Twitter(
    auth=OAuth(token, token_secret, consumer_key, consumer_secret))


# Open a sheet from a spreadsheet in one go
wks = gc.open("quotesfromhell").sheet1

# Update a range of cells using the top left corner address
next_tweet = wks.acell('A2').value

#post tweet through twitter API
t.statuses.update(
    status=next_tweet)

#delete row on success
wks.delete_rows(2)



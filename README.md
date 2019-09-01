# BurgerBot
A bot based on [BurgerBot 4545](https://www.facebook.com/BurgerBot4545/) created for fun

## Requirements

- Firebase Admin 
`pip install firebase-admin`

## Setting up

###  Firebase
In order to run the bot, you'll first need a Firebase project to work with. Download your service account key and place it in the root of the project.
In `firebase.py`, change `cred = credentials.Certificate("[Your Certificate Name Here]")`

### Facebook
If you intend to post the burgers to Facebook, you'll also need a Facebook app registered with your Facebook developer account and a page to post to.
Grab your access token and app id from the [Graph API Explorer](https://developers.facebook.com/tools/explorer/) and create a file titled `config.py`.
Add the `access_token` and `id` keys with their appropriate values. Also ensure that you have the `post_pages` permission enabled.

## Running BurgerBot

```
Usage: python BurgerBot.py [-options]
where options include:
    -c --create     Create a random burger and post it to Facebook
    -b              Create a new bun and add it to the database
    -f              Create a new filling and add it to the database
```

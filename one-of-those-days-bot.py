#!/usr/bin/env python3

import os
import tweepy
import random
import argparse

messages = [
    "It's one of those days.",
    "It's just one of those days.",
    "*sigh* Just one of those days, I guess.",
    "One of them days.",
    "Just one of those days.",
    "It is one of those days."
]

def main():
    ap = argparse.ArgumentParser(description="It's one of those days.")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    if not args.dry_run:

        api_key = os.environ.get('API_KEY')
        api_secret = os.environ.get('API_SECRET')
        access_token = os.environ.get('ACCESS_TOKEN')
        access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

        auth = tweepy.OAuthHandler(api_key, api_secret)
        auth.set_access_token(access_token, access_token_secret)

        api = tweepy.API(auth)

        try:
            api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")
            exit

    # TODO: Make it say "It's the LORD's day" on Sundays
    message = random.choice(messages)

    if args.dry_run:
        print(message)
    else:
        api.update_status(message)

if __name__ == "__main__":
    main()

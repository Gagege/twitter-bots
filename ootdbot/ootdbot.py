#!/usr/bin/env python3

import sys
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
    ap.add_argument("--api-key", required=True)
    ap.add_argument("--api-secret", required=True)
    ap.add_argument("--access-token", required=True)
    ap.add_argument("--access-token-secret", required=True)
    args = ap.parse_args()

    auth = tweepy.OAuthHandler(args.api_key, args.api_secret)
    auth.set_access_token(args.access_token, args.access_token_secret)

    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Authentication OK")
    except:
        print("Error during authentication")
        exit

    message = random.choice(messages)

    print(message)
        # api.update_status("It's one of those days.")

if __name__ == "__main__":
    main()

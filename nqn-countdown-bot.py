#!/usr/bin/env python3

import tweepy
import argparse

def main():
    ap = argparse.ArgumentParser(description="No Quarter November Countdown Bot")
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

if __name__ == "__main__":
    main()

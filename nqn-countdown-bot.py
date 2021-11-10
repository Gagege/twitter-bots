#!/usr/bin/env python3

import tweepy
import argparse
import datetime

def main():
    ap = argparse.ArgumentParser(description="No Quarter November Countdown Bot")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--api-key")
    ap.add_argument("--api-secret")
    ap.add_argument("--access-token")
    ap.add_argument("--access-token-secret")
    args = ap.parse_args()

    if not args.dry_run:
        auth = tweepy.OAuthHandler(args.api_key, args.api_secret)
        auth.set_access_token(args.access_token, args.access_token_secret)

        api = tweepy.API(auth)

        try:
            api.verify_credentials()
            print("Authentication OK")
        except:
            print("Error during authentication")
            exit

    today = datetime.date.today()
    # today = datetime.date(year=2023, month=10, day=31)

    current_month = today.month
    if current_month != 11:
        next_november_1 =  datetime.date(year = today.year if today.month < 11 else today.year + 1, month=11, day=1)
        date_diff = next_november_1 - today
        pluralized_day = "day" if date_diff.days == 1 else "days"
        print(f"{date_diff.days} {pluralized_day} left until No Quarter November.")
    else:
        # Subtract the current day from 31 instead of 30 (the number of days in November) so days_left will include the current day
        days_left = 31 - today.day
        pluralized_day = "day" if days_left == 1 else "days"
        print(f"{days_left} {pluralized_day} left in No Quarter November.")

if __name__ == "__main__":
    main()

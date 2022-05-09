#!/usr/bin/env python3
import argparse
import datetime
import re
import sys

with open('wordle-original.txt') as originalfile:
    originalwordlist =  originalfile.readlines()

with open('wordle-nyt-ko.txt') as nytopenfile:
    nytwordlist = nytopenfile.readlines()


def get_date_difference(date, basedate="2021-06-19"):
    base  = datetime.datetime.strptime(basedate,   "%Y-%m-%d")
    date = datetime.datetime.strptime(date, "%Y-%m-%d")
    return abs((date - base).days)


def get_word_of_the_day(day=datetime.datetime.today(), wordlist=originalwordlist):
    if type(day) != datetime.datetime:
        day = datetime.datetime.strptime(day, "%Y-%m-%d")
    #day = day + datetime.timedelta(days=1)
    formatteddate = f'{day.year}-{day.month}-{day.day}'
    s = get_date_difference(date=formatteddate)
    # formula is days  since 2021-6-19 00:00:00
    # (s) modulo wordlist length = 2315
    a = s % len(wordlist)
    return wordlist[a]


if __name__ == "__main__":
    wordlist = originalwordlist
    # pattern is valid from dates 2000-01-01-9999-12-31
    pattern = "^(?!2000)(?!2001)(?!2002)(?!2003)(?!2004)(?!2005)(?!2006)(?!2007)(?!2008)(?!2009)(?!2010)(?!2011)(?!2012)(?!2013)(?!2014)(?!2015)(?!2016)(?!2017)(?!2018)(?!2019)(?!2020)([2-9])\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"
    parser = argparse.ArgumentParser(description="Wordle Solver",
                                     add_help=True,
                                     epilog="If no argument is passed, we use today's date.")
    parser.add_argument("--date", "-d", action="store", dest="date",
                        type=str,
                        help="date in the format YYYY-MM-DD")
    parser.add_argument("--nyt", type=bool, dest="nyt",
                        const=True, default=False, nargs='?',
                        help="new york times version")
    args = parser.parse_args()
    if (not args.date) and (args.nyt== False):
        print(get_word_of_the_day(wordlist=wordlist))
    elif (args.nyt) and (not args.date):
         wordlist = nytwordlist
         print(get_word_of_the_day(wordlist=wordlist))
    else:
        if args.nyt:
            wordlist = nytwordlist
        if (re.match(pattern, args.date)):
            # No longer needed because of my dirty negative lookahead
            # hack: checks if the given date is less than 2021-06-19
            # because I suck at writing valid regex.
            # I know this is bad, thank you.
            #intdate = int(args.date.replace('-', ""))
            #if intdate < 20210619:
            #    print("Error: Valid dates are from 2021-06-19 to 9999-12-31")
            #    sys.exit(1)
            #else:
            #   pass
            print(get_word_of_the_day(day=args.date, wordlist=wordlist))
        else:
            print("Error: Valid dates are from 2021-06-19 to 9999-12-31")
            sys.exit(1)




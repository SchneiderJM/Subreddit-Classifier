#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 16:17:55 2020

@author: jason
"""

import pandas as pd
import os
import praw

#Client ID, secret, user agent in that order
credentials = list(pd.read_csv(os.getcwd()+'/credentials.csv').columns)

reddit = praw.Reddit(client_id=credentials[0],
                     client_secret=credentials[1],user_agent=credentials[2])

#I want:
#Title, text, link (if applicable), top comments, author


r = reddit.subreddit('politics').top(limit=100,time_filter='day')
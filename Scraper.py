#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 16:17:55 2020

@author: jason
"""

import pandas as pd
import os

#Client ID, secret, user agent in that order
credentials = list(pd.read_csv(os.getcwd()+'/credentials.csv').columns)
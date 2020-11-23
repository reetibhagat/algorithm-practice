#
# The elements of campaigns.csv are defined as follows
# 1. campaignId – integer Primary-Key for of campaign
# 2. name – campaign Name; String of maximum 256 character length
# 3. startDate – campaign start date in yyyy-MM-dd format
# 4. endDate – campaign end-date in yyyy-MM-dd format
# 5. advertiserId – an id representing an advertiser
# 6. active – 1 if a campaign is Active. 0 if it is inactive
# 7. priority – integer, higher number represents higher priority
#
# The attributes in banners.json are defined as follows
# 1. bannerId – integer Primary-Key for banners
# 2. campaignId – integer Foreign-Key to Campaigns
# 3. url – URL that represents the Ad Image; string can be indefinitely long
# 4. startDate – the date the banner starts
# 5. endDate – the date the banner ends
#
# Requirements : ( only do 1,  2, 2.b , 3)
# 1. Read the campaigns and banners files into memory
# 2. Choose 10 Active campaigns using the following rules
# a. (don't do this) Campaign must be active by status and date, as of today’s date.
# b. No more than 2 active banners for each campaign should be selected.
# c. OPTIONAL - Highest priority campaigns should be selected first.
# d. OPTIONAL - No more than 2 Campaigns with the same priority should
# be selected
# 3. Print out all the selected Campaign ids with their associated banner id and
# url using the standard JDK Logger.

import json



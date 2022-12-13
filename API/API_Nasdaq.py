from dotenv import load_dotenv
import os
import requests
import json

load_dotenv()

# note: the following function (solver) will only work on stocks that have an individual stock price lower than
# 10,000,000. This will practically work because the most expensive stock in the world is
# Berkshire Hathaway, currently at 429,200 a share.
# https://www.gobankingrates.com/investing/stocks/most-expensive-stock/

# note dates entered in the "start_date" and "end_date" variables must be entered in year-month-day format
# etc 2020-04-31

def solver(start_date, end_date):

    API_KEY = os.getenv("API_KEY")

    nasdaq = requests.get(
        f"https://data.nasdaq.com/api/v3/datasets/XFRA/SES.json?&start_date={start_date}&end_date={end_date}&api_key={API_KEY}").text

    data_dict = json.loads(nasdaq)

    dd_simplified = data_dict["dataset"]

    ddss = dd_simplified["data"]

    highest_value = 0

    lowest_value = 10000000

    summm = 0

    for i in ddss:
        if i[4] > highest_value:
            highest_value = i[4]
        if i[4] < lowest_value:
            lowest_value = i[4]

        summm+=i[5]

    rdelta = (highest_value - lowest_value)

    av_vol = summm/len(ddss)

    return rdelta, av_vol


print("The largest difference between closing prices over this interval",
      "and the average volume is", solver("2010-05-01", "2010-05-05"),
      "respectively.")

import datetime

today = datetime.datetime.now()
DD = datetime.timedelta(days=30)
earlier = today - DD
earlier_str = earlier.strftime("%Y%m%d")

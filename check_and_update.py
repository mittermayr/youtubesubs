import datetime
now = datetime.datetime.now()
subscriber_count = f"{now.minute}{now.second}"
f = open("subscriber_count.txt", "w+")
f.write(subscriber_count)
f.close()

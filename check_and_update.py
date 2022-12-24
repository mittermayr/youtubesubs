import urllib.request, json, sys
if len(sys.argv) != 3:
    sys.exit("Giving up: you likely forgot to set up the Channel ID and API Key in Github Settings / Actions / Secrets.")
channel_id = sys.argv[1]
api_key = sys.argv[2]
api_url = f"https://www.googleapis.com/youtube/v3/channels?part=statistics&id={channel_id}&key={api_key}"

with urllib.request.urlopen(api_url) as url:
    data = json.load(url)
    if "items" in data:
        if len(data["items"]) > 0:
            if "statistics" in data["items"][0]:
              subscriber_count = data["items"][0]["statistics"]["subscriberCount"]
              view_count = data["items"][0]["statistics"]["viewCount"]
              f = open("subscriber_count.txt", "w+")
              f.write(subscriber_count)
              f.close()
              f = open("view_count.txt", "w+")
              f.write(view_count)
              f.close()
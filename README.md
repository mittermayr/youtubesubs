# A YouTube Subscriber Counter

A YouTube subscriber counter that self-publishes via Github Actions. This can be pulled from an ESP32, Raspberry PI, Grafana, or pretty much any other UI you can get to run an HTTP GET call for you.

At midnight, this Github action automatically fetches your latest subscriber count (and view count) and (if it changed), commits the latest data as a pure and simple number to a file that can be publicly accessed by your display devices.

## Requirements: 

You will need to set up an account with Google API to get the API key. This is free (if you don't overdo it) and only needs to be done once. Make sure you enable the Youtube Data API to generate a key here. DO NOT put the key into the file and accidentally upload it, you've been warned. Read the next step:

### Github Actions / Secrets

You need to head into your repository settings, find a menu called Github Actions / Secrets, and create two new secrets there. Call them `YOUTUBE_CHANNEL_ID` and `YOUTUBE_API_KEY` — insert the appropriate values and save it. 

To determine your channel ID, take a channel like this one: https://www.youtube.com/channel/UCBPiXP06rZHXAGCQ0Yzh1PQ (like and subscribe, thanks) — and extract only the key on the very right of the URL. So the channel ID here would be `UCBPiXP06rZHXAGCQ0Yzh1PQ`. Use that.

### Schedule

You can fine-tune the schedule by editing the workflow file. See `.github/workflows/update_subscribers.yml` for details (the cron line is what you're after).

### Disclaimer

I take no liability on any of these experiments, so if you're making mistakes and overusing Github Actions or the Google API — you're on your own, sorry.

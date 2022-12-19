import requests
import json
import datetime
import time
import threading


#with open('twitter_results.json', 'r') as openfile:

    # Reading from json file
    #data = json.load(openfile)
while True:
  tic = time.perf_counter()
  data = []
  with open('results.json', "r+") as file:
    data3 = json.load(file)
    last_time = data3[0]["postTime"]
    last_id = data3[0]["id"]

  ## Twitter
  user_ids = ["1175086049195909121", "1311393885806100481", "1404603419101306881",
  "1447265265134223360", "1357259205191766016", "3195799826", "94261044",
  "1493226085815025664", "1423031747432783872", "1199465444597477379",
  "1285954300712308737", "4357416197", "5768872", "295218901", "12", "993595279545982976",
  "3434609596", "25787685", "1108435779234287616", "1321502344660439040",
  "1356434353623093249", "1378291440770408514", "1467867844264316937", "2652239532",
  "1498857371547828224", "313275062", "1493130176087080967", "94261044",
  "1479141522041937925", "96770474", "986900699366604800", "904700529988820992",
  "1478109975406858245", "1388487332093997057", "745273", "244647486",
  "1287576585353039872", "574032254", "47805001", "14841047", "2362854624", "2425151",
  "1423031747432783872", "808513538", "16168217", "657863", "980935731794403328",
  "1457443615542636545", "347831597", "1367095024069062657", "3369243892", "2621412174",
  "62418232", "1583853585540030464", "1468860643600175106", "130778116", "2478217117",
  "1379053041995890695", "1587013112422604800", "34097500", "1542856831168544769",
  "44196397", "1433121559057559555", "1432583226707484676", "1427759853498298369",
  "1441835930889818113", "1182339769914855430", "1508498431907557376", "295218901",
  "1393859359839604737", "1357749263632109570", "1381699264011771906",
  "1502099166822113283", "62418232", "1494856957471113219", "1362625187489976321",
  "399412477", "1427557319500472325", "2371575838", "1232540254457847808",
  "1516490048375607296", "1490319920260956164", "1544277054895661058",
  "1401536806978457602", "1444937781441187842", "1412256674115686402",
  "1387497871751196672", "904700529988820992", "361289499", "1424994036293586947",
  "2298174714", "902926941413453824", "877807935493033984", "1522696538211991554",
  "1491285218422300673", "1369348853414178822", "1323747353308835840", "5768872",
  "1457443615542636545", "1432583226707484676", "1317828734913753090",
  "1405701429646430212", "1395553778187718657,", "14379660"]
  def task1 ():
    global author_name
    global author_avatar
    global hasImage

    for user_id in user_ids[0:5]:
      #print(user_id + "BU 1DEN")

      url = "https://api.twitter.com/2/users/" + user_id + "/tweets?tweet.fields=created_at,attachments&expansions=author_id,attachments.media_keys&media.fields=url&exclude=retweets,replies&user.fields=profile_image_url"
      payload = {}
      headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAMSAjQEAAAAAHG%2FH8wMqgPG74itKqF3LYX0xu4s%3D7yFFUHLeLAl0LduBr9w7pOE7649g6hIXxgAVMJ6M2ERvFWzfpC',
        'Cookie': 'guest_id=v1%3A167014144542504276'
      }

      response = requests.request("GET", url, headers=headers, data=payload)

      # print(json.loads(response.text))
      result_twitter = json.loads(response.text)
      # res_count = result_twitter['meta']['result_count']
      if 'data' in result_twitter:

        tweets_info = result_twitter['data']
        users_info = result_twitter['includes']['users']

        for user_info in users_info:
          author_name = user_info['username']
          author_avatar = user_info['profile_image_url']

        if 'media' in result_twitter['includes']:
          media_infos = result_twitter['includes']['media']
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            if (postTime < last_time or last_id == id):
              continue

            if "attachments" in tweet:

              if "media_keys" in tweet['attachments']:
                media_keys = tweet['attachments']['media_keys']
                for key in media_keys:
                  for media in media_infos:
                    media_key = media['media_key']
                    if key == media_key:
                      media_type = media['type']
                      if media_type == "photo":
                        image.append(media['url'])
                        hasImage = True
                      else:
                        image.append("")
                        hasImage = False

            else:
              hasImage = False
              image.append("")

            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)



        else:
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            hasImage = False
            image.append("")
            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)



          else:
            for tweet in tweets_info:
              description = tweet['text']
              postTime = tweet['created_at']

              # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
              id = tweet['id']
              image = []
              hasImage = False
              image.append("")
              if (postTime < last_time or last_id == id):
                continue
              else:
                entry = {
                  "author": {"name": author_name, "author_avatar": author_avatar},
                  "description": description,
                  "postTime": postTime,
                  "hasImage": hasImage,
                  "image": image,
                  "id": id
                }
                data.append(entry)




    #print(author_name)
    #print(author_avatar)


  def task2():
    global author_name
    global author_avatar
    global hasImage

    for user_id in user_ids[5:10]:
      #print(user_id+ "BU 2DEN")
      url = "https://api.twitter.com/2/users/" + user_id + "/tweets?tweet.fields=created_at,attachments&expansions=author_id,attachments.media_keys&media.fields=url&exclude=retweets,replies&user.fields=profile_image_url"
      payload = {}
      headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAMSAjQEAAAAAHG%2FH8wMqgPG74itKqF3LYX0xu4s%3D7yFFUHLeLAl0LduBr9w7pOE7649g6hIXxgAVMJ6M2ERvFWzfpC',
        'Cookie': 'guest_id=v1%3A167014144542504276'
      }

      response = requests.request("GET", url, headers=headers, data=payload)

      # print(json.loads(response.text))
      result_twitter = json.loads(response.text)
      # res_count = result_twitter['meta']['result_count']
      if 'data' in result_twitter:

        tweets_info = result_twitter['data']
        users_info = result_twitter['includes']['users']

        for user_info in users_info:
          author_name = user_info['username']
          author_avatar = user_info['profile_image_url']

        if 'media' in result_twitter['includes']:
          media_infos = result_twitter['includes']['media']
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            if (postTime < last_time or last_id == id):
              continue

            if "attachments" in tweet:

              if "media_keys" in tweet['attachments']:
                media_keys = tweet['attachments']['media_keys']
                for key in media_keys:
                  for media in media_infos:
                    media_key = media['media_key']
                    if key == media_key:
                      media_type = media['type']
                      if media_type == "photo":
                        image.append(media['url'])
                        hasImage = True
                      else:
                        image.append("")
                        hasImage = False

            else:
              hasImage = False
              image.append("")

            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)



        else:
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            hasImage = False
            image.append("")
            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)
  def task3():
    global author_name
    global author_avatar
    global hasImage

    for user_id in user_ids[10:15]:
      #print(user_id+ "BU 3DEN")
      url = "https://api.twitter.com/2/users/" + user_id + "/tweets?tweet.fields=created_at,attachments&expansions=author_id,attachments.media_keys&media.fields=url&exclude=retweets,replies&user.fields=profile_image_url"
      payload = {}
      headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAMSAjQEAAAAAHG%2FH8wMqgPG74itKqF3LYX0xu4s%3D7yFFUHLeLAl0LduBr9w7pOE7649g6hIXxgAVMJ6M2ERvFWzfpC',
        'Cookie': 'guest_id=v1%3A167014144542504276'
      }

      response = requests.request("GET", url, headers=headers, data=payload)

      # print(json.loads(response.text))
      result_twitter = json.loads(response.text)
      # res_count = result_twitter['meta']['result_count']
      if 'data' in result_twitter:

        tweets_info = result_twitter['data']
        users_info = result_twitter['includes']['users']

        for user_info in users_info:
          author_name = user_info['username']
          author_avatar = user_info['profile_image_url']

        if 'media' in result_twitter['includes']:
          media_infos = result_twitter['includes']['media']
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            if (postTime < last_time or last_id == id):
              continue

            if "attachments" in tweet:

              if "media_keys" in tweet['attachments']:
                media_keys = tweet['attachments']['media_keys']
                for key in media_keys:
                  for media in media_infos:
                    media_key = media['media_key']
                    if key == media_key:
                      media_type = media['type']
                      if media_type == "photo":
                        image.append(media['url'])
                        hasImage = True
                      else:
                        image.append("")
                        hasImage = False

            else:
              hasImage = False
              image.append("")

            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)



        else:
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            hasImage = False
            image.append("")
            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)
  def task4():
    global author_name
    global author_avatar
    global hasImage

    for user_id in user_ids[15:20]:
      #print(user_id+ "BU 4DEN")
      url = "https://api.twitter.com/2/users/" + user_id + "/tweets?tweet.fields=created_at,attachments&expansions=author_id,attachments.media_keys&media.fields=url&exclude=retweets,replies&user.fields=profile_image_url"
      payload = {}
      headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAMSAjQEAAAAAHG%2FH8wMqgPG74itKqF3LYX0xu4s%3D7yFFUHLeLAl0LduBr9w7pOE7649g6hIXxgAVMJ6M2ERvFWzfpC',
        'Cookie': 'guest_id=v1%3A167014144542504276'
      }

      response = requests.request("GET", url, headers=headers, data=payload)

      # print(json.loads(response.text))
      result_twitter = json.loads(response.text)
      # res_count = result_twitter['meta']['result_count']
      if 'data' in result_twitter:

        tweets_info = result_twitter['data']
        users_info = result_twitter['includes']['users']

        for user_info in users_info:
          author_name = user_info['username']
          author_avatar = user_info['profile_image_url']

        if 'media' in result_twitter['includes']:
          media_infos = result_twitter['includes']['media']
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            if (postTime < last_time or last_id == id):
              continue

            if "attachments" in tweet:

              if "media_keys" in tweet['attachments']:
                media_keys = tweet['attachments']['media_keys']
                for key in media_keys:
                  for media in media_infos:
                    media_key = media['media_key']
                    if key == media_key:
                      media_type = media['type']
                      if media_type == "photo":
                        image.append(media['url'])
                        hasImage = True
                      else:
                        image.append("")
                        hasImage = False

            else:
              hasImage = False
              image.append("")

            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)



        else:
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            hasImage = False
            image.append("")
            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)


  def task5():
    global author_name
    global author_avatar
    global hasImage

    for user_id in user_ids[20:25]:
      # print(user_id+ "BU 4DEN")
      url = "https://api.twitter.com/2/users/" + user_id + "/tweets?tweet.fields=created_at,attachments&expansions=author_id,attachments.media_keys&media.fields=url&exclude=retweets,replies&user.fields=profile_image_url"
      payload = {}
      headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAMSAjQEAAAAAHG%2FH8wMqgPG74itKqF3LYX0xu4s%3D7yFFUHLeLAl0LduBr9w7pOE7649g6hIXxgAVMJ6M2ERvFWzfpC',
        'Cookie': 'guest_id=v1%3A167014144542504276'
      }

      response = requests.request("GET", url, headers=headers, data=payload)

      # print(json.loads(response.text))
      result_twitter = json.loads(response.text)
      # res_count = result_twitter['meta']['result_count']
      if 'data' in result_twitter:

        tweets_info = result_twitter['data']
        users_info = result_twitter['includes']['users']

        for user_info in users_info:
          author_name = user_info['username']
          author_avatar = user_info['profile_image_url']

        if 'media' in result_twitter['includes']:
          media_infos = result_twitter['includes']['media']
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            if (postTime < last_time or last_id == id):
              continue

            if "attachments" in tweet:

              if "media_keys" in tweet['attachments']:
                media_keys = tweet['attachments']['media_keys']
                for key in media_keys:
                  for media in media_infos:
                    media_key = media['media_key']
                    if key == media_key:
                      media_type = media['type']
                      if media_type == "photo":
                        image.append(media['url'])
                        hasImage = True
                      else:
                        image.append("")
                        hasImage = False

            else:
              hasImage = False
              image.append("")

            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)



        else:
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            hasImage = False
            image.append("")
            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)


  def task6():
    global author_name
    global author_avatar
    global hasImage

    for user_id in user_ids[25:30]:
      # print(user_id+ "BU 4DEN")
      url = "https://api.twitter.com/2/users/" + user_id + "/tweets?tweet.fields=created_at,attachments&expansions=author_id,attachments.media_keys&media.fields=url&exclude=retweets,replies&user.fields=profile_image_url"
      payload = {}
      headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAMSAjQEAAAAAHG%2FH8wMqgPG74itKqF3LYX0xu4s%3D7yFFUHLeLAl0LduBr9w7pOE7649g6hIXxgAVMJ6M2ERvFWzfpC',
        'Cookie': 'guest_id=v1%3A167014144542504276'
      }

      response = requests.request("GET", url, headers=headers, data=payload)

      # print(json.loads(response.text))
      result_twitter = json.loads(response.text)
      # res_count = result_twitter['meta']['result_count']
      if 'data' in result_twitter:

        tweets_info = result_twitter['data']
        users_info = result_twitter['includes']['users']

        for user_info in users_info:
          author_name = user_info['username']
          author_avatar = user_info['profile_image_url']

        if 'media' in result_twitter['includes']:
          media_infos = result_twitter['includes']['media']
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            if (postTime < last_time or last_id == id):
              continue

            if "attachments" in tweet:

              if "media_keys" in tweet['attachments']:
                media_keys = tweet['attachments']['media_keys']
                for key in media_keys:
                  for media in media_infos:
                    media_key = media['media_key']
                    if key == media_key:
                      media_type = media['type']
                      if media_type == "photo":
                        image.append(media['url'])
                        hasImage = True
                      else:
                        image.append("")
                        hasImage = False

            else:
              hasImage = False
              image.append("")

            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)



        else:
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            hasImage = False
            image.append("")
            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)


  def task7():
    global author_name
    global author_avatar
    global hasImage

    for user_id in user_ids[30:35]:
      # print(user_id+ "BU 4DEN")
      url = "https://api.twitter.com/2/users/" + user_id + "/tweets?tweet.fields=created_at,attachments&expansions=author_id,attachments.media_keys&media.fields=url&exclude=retweets,replies&user.fields=profile_image_url"
      payload = {}
      headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAMSAjQEAAAAAHG%2FH8wMqgPG74itKqF3LYX0xu4s%3D7yFFUHLeLAl0LduBr9w7pOE7649g6hIXxgAVMJ6M2ERvFWzfpC',
        'Cookie': 'guest_id=v1%3A167014144542504276'
      }

      response = requests.request("GET", url, headers=headers, data=payload)

      # print(json.loads(response.text))
      result_twitter = json.loads(response.text)
      # res_count = result_twitter['meta']['result_count']
      if 'data' in result_twitter:

        tweets_info = result_twitter['data']
        users_info = result_twitter['includes']['users']

        for user_info in users_info:
          author_name = user_info['username']
          author_avatar = user_info['profile_image_url']

        if 'media' in result_twitter['includes']:
          media_infos = result_twitter['includes']['media']
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            if (postTime < last_time or last_id == id):
              continue

            if "attachments" in tweet:

              if "media_keys" in tweet['attachments']:
                media_keys = tweet['attachments']['media_keys']
                for key in media_keys:
                  for media in media_infos:
                    media_key = media['media_key']
                    if key == media_key:
                      media_type = media['type']
                      if media_type == "photo":
                        image.append(media['url'])
                        hasImage = True
                      else:
                        image.append("")
                        hasImage = False

            else:
              hasImage = False
              image.append("")

            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)



        else:
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            hasImage = False
            image.append("")
            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)


  def task8():
    global author_name
    global author_avatar
    global hasImage

    for user_id in user_ids[35:40]:
      # print(user_id+ "BU 4DEN")
      url = "https://api.twitter.com/2/users/" + user_id + "/tweets?tweet.fields=created_at,attachments&expansions=author_id,attachments.media_keys&media.fields=url&exclude=retweets,replies&user.fields=profile_image_url"
      payload = {}
      headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAMSAjQEAAAAAHG%2FH8wMqgPG74itKqF3LYX0xu4s%3D7yFFUHLeLAl0LduBr9w7pOE7649g6hIXxgAVMJ6M2ERvFWzfpC',
        'Cookie': 'guest_id=v1%3A167014144542504276'
      }

      response = requests.request("GET", url, headers=headers, data=payload)

      # print(json.loads(response.text))
      result_twitter = json.loads(response.text)
      # res_count = result_twitter['meta']['result_count']
      if 'data' in result_twitter:

        tweets_info = result_twitter['data']
        users_info = result_twitter['includes']['users']

        for user_info in users_info:
          author_name = user_info['username']
          author_avatar = user_info['profile_image_url']

        if 'media' in result_twitter['includes']:
          media_infos = result_twitter['includes']['media']
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            if (postTime < last_time or last_id == id):
              continue

            if "attachments" in tweet:

              if "media_keys" in tweet['attachments']:
                media_keys = tweet['attachments']['media_keys']
                for key in media_keys:
                  for media in media_infos:
                    media_key = media['media_key']
                    if key == media_key:
                      media_type = media['type']
                      if media_type == "photo":
                        image.append(media['url'])
                        hasImage = True
                      else:
                        image.append("")
                        hasImage = False

            else:
              hasImage = False
              image.append("")

            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)



        else:
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            hasImage = False
            image.append("")
            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)


  def task9():
    global author_name
    global author_avatar
    global hasImage

    for user_id in user_ids[40:45]:
      # print(user_id+ "BU 4DEN")
      url = "https://api.twitter.com/2/users/" + user_id + "/tweets?tweet.fields=created_at,attachments&expansions=author_id,attachments.media_keys&media.fields=url&exclude=retweets,replies&user.fields=profile_image_url"
      payload = {}
      headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAMSAjQEAAAAAHG%2FH8wMqgPG74itKqF3LYX0xu4s%3D7yFFUHLeLAl0LduBr9w7pOE7649g6hIXxgAVMJ6M2ERvFWzfpC',
        'Cookie': 'guest_id=v1%3A167014144542504276'
      }

      response = requests.request("GET", url, headers=headers, data=payload)

      # print(json.loads(response.text))
      result_twitter = json.loads(response.text)
      # res_count = result_twitter['meta']['result_count']
      if 'data' in result_twitter:

        tweets_info = result_twitter['data']
        users_info = result_twitter['includes']['users']

        for user_info in users_info:
          author_name = user_info['username']
          author_avatar = user_info['profile_image_url']

        if 'media' in result_twitter['includes']:
          media_infos = result_twitter['includes']['media']
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            if (postTime < last_time or last_id == id):
              continue

            if "attachments" in tweet:

              if "media_keys" in tweet['attachments']:
                media_keys = tweet['attachments']['media_keys']
                for key in media_keys:
                  for media in media_infos:
                    media_key = media['media_key']
                    if key == media_key:
                      media_type = media['type']
                      if media_type == "photo":
                        image.append(media['url'])
                        hasImage = True
                      else:
                        image.append("")
                        hasImage = False

            else:
              hasImage = False
              image.append("")

            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)



        else:
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            hasImage = False
            image.append("")
            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)


  def task10():
    global author_name
    global author_avatar
    global hasImage

    for user_id in user_ids[45:50]:
      # print(user_id+ "BU 4DEN")
      url = "https://api.twitter.com/2/users/" + user_id + "/tweets?tweet.fields=created_at,attachments&expansions=author_id,attachments.media_keys&media.fields=url&exclude=retweets,replies&user.fields=profile_image_url"
      payload = {}
      headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAMSAjQEAAAAAHG%2FH8wMqgPG74itKqF3LYX0xu4s%3D7yFFUHLeLAl0LduBr9w7pOE7649g6hIXxgAVMJ6M2ERvFWzfpC',
        'Cookie': 'guest_id=v1%3A167014144542504276'
      }

      response = requests.request("GET", url, headers=headers, data=payload)

      # print(json.loads(response.text))
      result_twitter = json.loads(response.text)
      # res_count = result_twitter['meta']['result_count']
      if 'data' in result_twitter:

        tweets_info = result_twitter['data']
        users_info = result_twitter['includes']['users']

        for user_info in users_info:
          author_name = user_info['username']
          author_avatar = user_info['profile_image_url']

        if 'media' in result_twitter['includes']:
          media_infos = result_twitter['includes']['media']
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            if (postTime < last_time or last_id == id):
              continue

            if "attachments" in tweet:

              if "media_keys" in tweet['attachments']:
                media_keys = tweet['attachments']['media_keys']
                for key in media_keys:
                  for media in media_infos:
                    media_key = media['media_key']
                    if key == media_key:
                      media_type = media['type']
                      if media_type == "photo":
                        image.append(media['url'])
                        hasImage = True
                      else:
                        image.append("")
                        hasImage = False

            else:
              hasImage = False
              image.append("")

            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)



        else:
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            hasImage = False
            image.append("")
            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)
  def task11 ():
    global author_name
    global author_avatar
    global hasImage

    for user_id in user_ids[50:55]:
      #print(user_id + "BU 1DEN")

      url = "https://api.twitter.com/2/users/" + user_id + "/tweets?tweet.fields=created_at,attachments&expansions=author_id,attachments.media_keys&media.fields=url&exclude=retweets,replies&user.fields=profile_image_url"
      payload = {}
      headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAMSAjQEAAAAAHG%2FH8wMqgPG74itKqF3LYX0xu4s%3D7yFFUHLeLAl0LduBr9w7pOE7649g6hIXxgAVMJ6M2ERvFWzfpC',
        'Cookie': 'guest_id=v1%3A167014144542504276'
      }

      response = requests.request("GET", url, headers=headers, data=payload)

      # print(json.loads(response.text))
      result_twitter = json.loads(response.text)
      # res_count = result_twitter['meta']['result_count']
      if 'data' in result_twitter:

        tweets_info = result_twitter['data']
        users_info = result_twitter['includes']['users']

        for user_info in users_info:
          author_name = user_info['username']
          author_avatar = user_info['profile_image_url']

        if 'media' in result_twitter['includes']:
          media_infos = result_twitter['includes']['media']
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            if (postTime < last_time or last_id == id):
              continue

            if "attachments" in tweet:

              if "media_keys" in tweet['attachments']:
                media_keys = tweet['attachments']['media_keys']
                for key in media_keys:
                  for media in media_infos:
                    media_key = media['media_key']
                    if key == media_key:
                      media_type = media['type']
                      if media_type == "photo":
                        image.append(media['url'])
                        hasImage = True
                      else:
                        image.append("")
                        hasImage = False

            else:
              hasImage = False
              image.append("")

            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)



        else:
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            hasImage = False
            image.append("")
            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)



          else:
            for tweet in tweets_info:
              description = tweet['text']
              postTime = tweet['created_at']

              # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
              id = tweet['id']
              image = []
              hasImage = False
              image.append("")
              if (postTime < last_time or last_id == id):
                continue
              else:
                entry = {
                  "author": {"name": author_name, "author_avatar": author_avatar},
                  "description": description,
                  "postTime": postTime,
                  "hasImage": hasImage,
                  "image": image,
                  "id": id
                }
                data.append(entry)




    #print(author_name)
    #print(author_avatar)


  def task12():
    global author_name
    global author_avatar
    global hasImage

    for user_id in user_ids[55:60]:
      #print(user_id+ "BU 2DEN")
      url = "https://api.twitter.com/2/users/" + user_id + "/tweets?tweet.fields=created_at,attachments&expansions=author_id,attachments.media_keys&media.fields=url&exclude=retweets,replies&user.fields=profile_image_url"
      payload = {}
      headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAMSAjQEAAAAAHG%2FH8wMqgPG74itKqF3LYX0xu4s%3D7yFFUHLeLAl0LduBr9w7pOE7649g6hIXxgAVMJ6M2ERvFWzfpC',
        'Cookie': 'guest_id=v1%3A167014144542504276'
      }

      response = requests.request("GET", url, headers=headers, data=payload)

      # print(json.loads(response.text))
      result_twitter = json.loads(response.text)
      # res_count = result_twitter['meta']['result_count']
      if 'data' in result_twitter:

        tweets_info = result_twitter['data']
        users_info = result_twitter['includes']['users']

        for user_info in users_info:
          author_name = user_info['username']
          author_avatar = user_info['profile_image_url']

        if 'media' in result_twitter['includes']:
          media_infos = result_twitter['includes']['media']
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            if (postTime < last_time or last_id == id):
              continue

            if "attachments" in tweet:

              if "media_keys" in tweet['attachments']:
                media_keys = tweet['attachments']['media_keys']
                for key in media_keys:
                  for media in media_infos:
                    media_key = media['media_key']
                    if key == media_key:
                      media_type = media['type']
                      if media_type == "photo":
                        image.append(media['url'])
                        hasImage = True
                      else:
                        image.append("")
                        hasImage = False

            else:
              hasImage = False
              image.append("")

            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)



        else:
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            hasImage = False
            image.append("")
            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)
  def task13():
    global author_name
    global author_avatar
    global hasImage

    for user_id in user_ids[60:65]:
      #print(user_id+ "BU 3DEN")
      url = "https://api.twitter.com/2/users/" + user_id + "/tweets?tweet.fields=created_at,attachments&expansions=author_id,attachments.media_keys&media.fields=url&exclude=retweets,replies&user.fields=profile_image_url"
      payload = {}
      headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAMSAjQEAAAAAHG%2FH8wMqgPG74itKqF3LYX0xu4s%3D7yFFUHLeLAl0LduBr9w7pOE7649g6hIXxgAVMJ6M2ERvFWzfpC',
        'Cookie': 'guest_id=v1%3A167014144542504276'
      }

      response = requests.request("GET", url, headers=headers, data=payload)

      # print(json.loads(response.text))
      result_twitter = json.loads(response.text)
      # res_count = result_twitter['meta']['result_count']
      if 'data' in result_twitter:

        tweets_info = result_twitter['data']
        users_info = result_twitter['includes']['users']

        for user_info in users_info:
          author_name = user_info['username']
          author_avatar = user_info['profile_image_url']

        if 'media' in result_twitter['includes']:
          media_infos = result_twitter['includes']['media']
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            if (postTime < last_time or last_id == id):
              continue

            if "attachments" in tweet:

              if "media_keys" in tweet['attachments']:
                media_keys = tweet['attachments']['media_keys']
                for key in media_keys:
                  for media in media_infos:
                    media_key = media['media_key']
                    if key == media_key:
                      media_type = media['type']
                      if media_type == "photo":
                        image.append(media['url'])
                        hasImage = True
                      else:
                        image.append("")
                        hasImage = False

            else:
              hasImage = False
              image.append("")

            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)



        else:
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            hasImage = False
            image.append("")
            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)
  def task14():
    global author_name
    global author_avatar
    global hasImage

    for user_id in user_ids[65:70]:
      #print(user_id+ "BU 4DEN")
      url = "https://api.twitter.com/2/users/" + user_id + "/tweets?tweet.fields=created_at,attachments&expansions=author_id,attachments.media_keys&media.fields=url&exclude=retweets,replies&user.fields=profile_image_url"
      payload = {}
      headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAMSAjQEAAAAAHG%2FH8wMqgPG74itKqF3LYX0xu4s%3D7yFFUHLeLAl0LduBr9w7pOE7649g6hIXxgAVMJ6M2ERvFWzfpC',
        'Cookie': 'guest_id=v1%3A167014144542504276'
      }

      response = requests.request("GET", url, headers=headers, data=payload)

      # print(json.loads(response.text))
      result_twitter = json.loads(response.text)
      # res_count = result_twitter['meta']['result_count']
      if 'data' in result_twitter:

        tweets_info = result_twitter['data']
        users_info = result_twitter['includes']['users']

        for user_info in users_info:
          author_name = user_info['username']
          author_avatar = user_info['profile_image_url']

        if 'media' in result_twitter['includes']:
          media_infos = result_twitter['includes']['media']
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            if (postTime < last_time or last_id == id):
              continue

            if "attachments" in tweet:

              if "media_keys" in tweet['attachments']:
                media_keys = tweet['attachments']['media_keys']
                for key in media_keys:
                  for media in media_infos:
                    media_key = media['media_key']
                    if key == media_key:
                      media_type = media['type']
                      if media_type == "photo":
                        image.append(media['url'])
                        hasImage = True
                      else:
                        image.append("")
                        hasImage = False

            else:
              hasImage = False
              image.append("")

            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)



        else:
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            hasImage = False
            image.append("")
            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)


  def task15():
    global author_name
    global author_avatar
    global hasImage

    for user_id in user_ids[70:75]:
      # print(user_id+ "BU 4DEN")
      url = "https://api.twitter.com/2/users/" + user_id + "/tweets?tweet.fields=created_at,attachments&expansions=author_id,attachments.media_keys&media.fields=url&exclude=retweets,replies&user.fields=profile_image_url"
      payload = {}
      headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAMSAjQEAAAAAHG%2FH8wMqgPG74itKqF3LYX0xu4s%3D7yFFUHLeLAl0LduBr9w7pOE7649g6hIXxgAVMJ6M2ERvFWzfpC',
        'Cookie': 'guest_id=v1%3A167014144542504276'
      }

      response = requests.request("GET", url, headers=headers, data=payload)

      # print(json.loads(response.text))
      result_twitter = json.loads(response.text)
      # res_count = result_twitter['meta']['result_count']
      if 'data' in result_twitter:

        tweets_info = result_twitter['data']
        users_info = result_twitter['includes']['users']

        for user_info in users_info:
          author_name = user_info['username']
          author_avatar = user_info['profile_image_url']

        if 'media' in result_twitter['includes']:
          media_infos = result_twitter['includes']['media']
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            if (postTime < last_time or last_id == id):
              continue

            if "attachments" in tweet:

              if "media_keys" in tweet['attachments']:
                media_keys = tweet['attachments']['media_keys']
                for key in media_keys:
                  for media in media_infos:
                    media_key = media['media_key']
                    if key == media_key:
                      media_type = media['type']
                      if media_type == "photo":
                        image.append(media['url'])
                        hasImage = True
                      else:
                        image.append("")
                        hasImage = False

            else:
              hasImage = False
              image.append("")

            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)



        else:
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            hasImage = False
            image.append("")
            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)


  def task16():
    global author_name
    global author_avatar
    global hasImage

    for user_id in user_ids[75:80]:
      # print(user_id+ "BU 4DEN")
      url = "https://api.twitter.com/2/users/" + user_id + "/tweets?tweet.fields=created_at,attachments&expansions=author_id,attachments.media_keys&media.fields=url&exclude=retweets,replies&user.fields=profile_image_url"
      payload = {}
      headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAMSAjQEAAAAAHG%2FH8wMqgPG74itKqF3LYX0xu4s%3D7yFFUHLeLAl0LduBr9w7pOE7649g6hIXxgAVMJ6M2ERvFWzfpC',
        'Cookie': 'guest_id=v1%3A167014144542504276'
      }

      response = requests.request("GET", url, headers=headers, data=payload)

      # print(json.loads(response.text))
      result_twitter = json.loads(response.text)
      # res_count = result_twitter['meta']['result_count']
      if 'data' in result_twitter:

        tweets_info = result_twitter['data']
        users_info = result_twitter['includes']['users']

        for user_info in users_info:
          author_name = user_info['username']
          author_avatar = user_info['profile_image_url']

        if 'media' in result_twitter['includes']:
          media_infos = result_twitter['includes']['media']
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            if (postTime < last_time or last_id == id):
              continue

            if "attachments" in tweet:

              if "media_keys" in tweet['attachments']:
                media_keys = tweet['attachments']['media_keys']
                for key in media_keys:
                  for media in media_infos:
                    media_key = media['media_key']
                    if key == media_key:
                      media_type = media['type']
                      if media_type == "photo":
                        image.append(media['url'])
                        hasImage = True
                      else:
                        image.append("")
                        hasImage = False

            else:
              hasImage = False
              image.append("")

            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)



        else:
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            hasImage = False
            image.append("")
            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)


  def task17():
    global author_name
    global author_avatar
    global hasImage

    for user_id in user_ids[80:85]:
      # print(user_id+ "BU 4DEN")
      url = "https://api.twitter.com/2/users/" + user_id + "/tweets?tweet.fields=created_at,attachments&expansions=author_id,attachments.media_keys&media.fields=url&exclude=retweets,replies&user.fields=profile_image_url"
      payload = {}
      headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAMSAjQEAAAAAHG%2FH8wMqgPG74itKqF3LYX0xu4s%3D7yFFUHLeLAl0LduBr9w7pOE7649g6hIXxgAVMJ6M2ERvFWzfpC',
        'Cookie': 'guest_id=v1%3A167014144542504276'
      }

      response = requests.request("GET", url, headers=headers, data=payload)

      # print(json.loads(response.text))
      result_twitter = json.loads(response.text)
      # res_count = result_twitter['meta']['result_count']
      if 'data' in result_twitter:

        tweets_info = result_twitter['data']
        users_info = result_twitter['includes']['users']

        for user_info in users_info:
          author_name = user_info['username']
          author_avatar = user_info['profile_image_url']

        if 'media' in result_twitter['includes']:
          media_infos = result_twitter['includes']['media']
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            if (postTime < last_time or last_id == id):
              continue

            if "attachments" in tweet:

              if "media_keys" in tweet['attachments']:
                media_keys = tweet['attachments']['media_keys']
                for key in media_keys:
                  for media in media_infos:
                    media_key = media['media_key']
                    if key == media_key:
                      media_type = media['type']
                      if media_type == "photo":
                        image.append(media['url'])
                        hasImage = True
                      else:
                        image.append("")
                        hasImage = False

            else:
              hasImage = False
              image.append("")

            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)



        else:
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            hasImage = False
            image.append("")
            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)


  def task18():
    global author_name
    global author_avatar
    global hasImage

    for user_id in user_ids[85:90]:
      # print(user_id+ "BU 4DEN")
      url = "https://api.twitter.com/2/users/" + user_id + "/tweets?tweet.fields=created_at,attachments&expansions=author_id,attachments.media_keys&media.fields=url&exclude=retweets,replies&user.fields=profile_image_url"
      payload = {}
      headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAMSAjQEAAAAAHG%2FH8wMqgPG74itKqF3LYX0xu4s%3D7yFFUHLeLAl0LduBr9w7pOE7649g6hIXxgAVMJ6M2ERvFWzfpC',
        'Cookie': 'guest_id=v1%3A167014144542504276'
      }

      response = requests.request("GET", url, headers=headers, data=payload)

      # print(json.loads(response.text))
      result_twitter = json.loads(response.text)
      # res_count = result_twitter['meta']['result_count']
      if 'data' in result_twitter:

        tweets_info = result_twitter['data']
        users_info = result_twitter['includes']['users']

        for user_info in users_info:
          author_name = user_info['username']
          author_avatar = user_info['profile_image_url']

        if 'media' in result_twitter['includes']:
          media_infos = result_twitter['includes']['media']
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            if (postTime < last_time or last_id == id):
              continue

            if "attachments" in tweet:

              if "media_keys" in tweet['attachments']:
                media_keys = tweet['attachments']['media_keys']
                for key in media_keys:
                  for media in media_infos:
                    media_key = media['media_key']
                    if key == media_key:
                      media_type = media['type']
                      if media_type == "photo":
                        image.append(media['url'])
                        hasImage = True
                      else:
                        image.append("")
                        hasImage = False

            else:
              hasImage = False
              image.append("")

            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)



        else:
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            hasImage = False
            image.append("")
            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)


  def task19():
    global author_name
    global author_avatar
    global hasImage

    for user_id in user_ids[90:93]:
      # print(user_id+ "BU 4DEN")
      url = "https://api.twitter.com/2/users/" + user_id + "/tweets?tweet.fields=created_at,attachments&expansions=author_id,attachments.media_keys&media.fields=url&exclude=retweets,replies&user.fields=profile_image_url"
      payload = {}
      headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAMSAjQEAAAAAHG%2FH8wMqgPG74itKqF3LYX0xu4s%3D7yFFUHLeLAl0LduBr9w7pOE7649g6hIXxgAVMJ6M2ERvFWzfpC',
        'Cookie': 'guest_id=v1%3A167014144542504276'
      }

      response = requests.request("GET", url, headers=headers, data=payload)

      # print(json.loads(response.text))
      result_twitter = json.loads(response.text)
      # res_count = result_twitter['meta']['result_count']
      if 'data' in result_twitter:

        tweets_info = result_twitter['data']
        users_info = result_twitter['includes']['users']

        for user_info in users_info:
          author_name = user_info['username']
          author_avatar = user_info['profile_image_url']

        if 'media' in result_twitter['includes']:
          media_infos = result_twitter['includes']['media']
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            if (postTime < last_time or last_id == id):
              continue

            if "attachments" in tweet:

              if "media_keys" in tweet['attachments']:
                media_keys = tweet['attachments']['media_keys']
                for key in media_keys:
                  for media in media_infos:
                    media_key = media['media_key']
                    if key == media_key:
                      media_type = media['type']
                      if media_type == "photo":
                        image.append(media['url'])
                        hasImage = True
                      else:
                        image.append("")
                        hasImage = False

            else:
              hasImage = False
              image.append("")

            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)



        else:
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            hasImage = False
            image.append("")
            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)


  def task20():
    global author_name
    global author_avatar
    global hasImage

    for user_id in user_ids[93:]:
      # print(user_id+ "BU 4DEN")
      url = "https://api.twitter.com/2/users/" + user_id + "/tweets?tweet.fields=created_at,attachments&expansions=author_id,attachments.media_keys&media.fields=url&exclude=retweets,replies&user.fields=profile_image_url"
      payload = {}
      headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAAMSAjQEAAAAAHG%2FH8wMqgPG74itKqF3LYX0xu4s%3D7yFFUHLeLAl0LduBr9w7pOE7649g6hIXxgAVMJ6M2ERvFWzfpC',
        'Cookie': 'guest_id=v1%3A167014144542504276'
      }

      response = requests.request("GET", url, headers=headers, data=payload)

      # print(json.loads(response.text))
      result_twitter = json.loads(response.text)
      # res_count = result_twitter['meta']['result_count']
      if 'data' in result_twitter:

        tweets_info = result_twitter['data']
        users_info = result_twitter['includes']['users']

        for user_info in users_info:
          author_name = user_info['username']
          author_avatar = user_info['profile_image_url']

        if 'media' in result_twitter['includes']:
          media_infos = result_twitter['includes']['media']
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            if (postTime < last_time or last_id == id):
              continue

            if "attachments" in tweet:

              if "media_keys" in tweet['attachments']:
                media_keys = tweet['attachments']['media_keys']
                for key in media_keys:
                  for media in media_infos:
                    media_key = media['media_key']
                    if key == media_key:
                      media_type = media['type']
                      if media_type == "photo":
                        image.append(media['url'])
                        hasImage = True
                      else:
                        image.append("")
                        hasImage = False

            else:
              hasImage = False
              image.append("")

            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)



        else:
          for tweet in tweets_info:
            description = tweet['text']
            postTime = tweet['created_at']

            # print(datetime.datetime.strptime(postTime, "%Y-%m-%dT%H:%M:%S.%fZ"))
            id = tweet['id']
            image = []
            hasImage = False
            image.append("")
            if (postTime < last_time or last_id == id):
              continue
            else:
              entry = {
                "author": {"name": author_name, "author_avatar": author_avatar},
                "description": description,
                "postTime": postTime,
                "hasImage": hasImage,
                "image": image,
                "id": id
              }
              data.append(entry)



  t1 = threading.Thread(target=task1)
  t2 = threading.Thread(target=task2)
  t3 = threading.Thread(target=task3)
  t4 = threading.Thread(target=task4)
  t5 = threading.Thread(target=task5)
  t6 = threading.Thread(target=task6)
  t7 = threading.Thread(target=task7)
  t8 = threading.Thread(target=task8)
  t9 = threading.Thread(target=task9)
  t10 = threading.Thread(target=task10)
  t11 = threading.Thread(target=task11)
  t12 = threading.Thread(target=task12)
  t13 = threading.Thread(target=task13)
  t14 = threading.Thread(target=task14)
  t15 = threading.Thread(target=task15)
  t16 = threading.Thread(target=task16)
  t17 = threading.Thread(target=task17)
  t18 = threading.Thread(target=task18)
  t19 = threading.Thread(target=task19)
  t20 = threading.Thread(target=task20)

  t1.start()
  t2.start()
  t3.start()
  t4.start()
  t5.start()
  t6.start()
  t7.start()
  t8.start()
  t9.start()
  t10.start()
  t11.start()
  t12.start()
  t13.start()
  t14.start()
  t15.start()
  t16.start()
  t17.start()
  t18.start()
  t19.start()
  t20.start()
  t1.join()
  t2.join()
  t3.join()
  t4.join()
  t5.join()
  t6.join()
  t7.join()
  t8.join()
  t9.join()
  t10.join()
  t11.join()
  t12.join()
  t13.join()
  t14.join()
  t15.join()
  t16.join()
  t17.join()
  t18.join()
  t19.join()
  t20.join()

  #toc = time.perf_counter()
  #print(f"Downloaded the tutorial in {toc - tic:0.4f} seconds")
  ## Crytopanic
  url = "https://cryptopanic.com/api/v1/posts/?auth_token=04d277a59a5688bcbb28c56d999fe3fc16bdbba3&metadata=true"

  payload={}
  headers = {}

  response_cryptopanic = requests.request("GET", url, headers=headers, data=payload)

  #print(json.loads(response.text))
  result_cryptopanic = json.loads(response_cryptopanic.text)
  author_avatar = "https://www.obmforall.com"
  posts_info = result_cryptopanic['results']
  for post in posts_info:
    author_name = "Cryptopanic"
    image = []
    description = post['title'] + "\n" + "\n"
    postTime = post['published_at']
    if 'metadata' in post:
      if 'description' in post['metadata']:
        description = description + post['metadata']['description']

      if 'image' in post['metadata']:
          image.append(post['metadata']['image'])
          hasImage = True
      else :
        image.append("")
        hasImage = False
    else:
      hasImage = False
      image.append("")

    id = post['id']
    author_name = author_name + "-" + post['source']['title']
    entry = {
      "author": {"name" : author_name,"author_avatar" : author_avatar},
      "description" : description,
      "postTime" : postTime,
      "hasImage" : hasImage,
      "image" : image,
      "id" : id
    }
    data.append(entry)

  ## Discord
  channel_ids = ["1047197303091495015"]
  channel_names = ["Onurcanın Grubu"]
  for i in range(len(channel_ids)):
    channel_id = channel_ids[i]

    url = "https://discord.com/api/v8/channels/" + channel_id + "/messages"

    payload={}
    headers = {
      'authorization': 'MTA0NTY5NDA4MTU0MTYxNTYyNg.G6IL7x.u8yKA7V8q_AhqDoUW_XCrtatp6mnWGpvHj16vE',
      'Cookie': '__cfruid=c45698fb50534e406a5445fa9357222413ae15ee-1670155889; __dcfduid=c860332473cc11ed8b812a1b98f9d0b9; __sdcfduid=c860332473cc11ed8b812a1b98f9d0b93491dae19efa09296254ab935039c60796786ceaabbcc7a0ef6005dc5c10c453'
    }

    response_discord = requests.request("GET", url, headers=headers, data=payload)

    results_cryptopanic = json.loads(response_discord.text)

    for messages in results_cryptopanic:
      author_name = "Discord" + "-" + channel_names[i]
      image = []
      description = messages['content']
      postTime = messages['timestamp']
      id = messages['id']
      hasImage = False
      author_name = author_name + "-" + messages['author']['username']

      if messages['author']['avatar'] is None:
        author_avatar = "https://www.obmforall.com"
      else:
        author_avatar = "https://cdn.discordapp.com/avatars/" + messages['author']['id'] + "/" + messages['author']['avatar'] + ".png"

      if len(messages['attachments']) != 0:
        media_keys = messages['attachments']
        for key in media_keys:
          image.append(key['url'])
          hasImage = True
      else:
        image.append("")
        hasImage = False
      entry = {
        "author": {"name" : author_name,"author_avatar" : author_avatar},
        "description" : description,
        "postTime" : postTime,
        "hasImage" : hasImage,
        "image" : image,
        "id" : id
      }
      data.append(entry)


  ## sort and append
  with open('results.json', "r+") as file:
    data2 = json.load(file)
    if len(data2) != 0:
      for new_data in data:
        isNotAdded = True
        for i in range(len(data2)):
          old_data = data2[i]
          if old_data["id"] == new_data["id"]:
            isNotAdded = False
            break
          else:
            continue
        if isNotAdded:
          data2.append(new_data)
          file.seek(0)
          data2 = sorted(data2, key=lambda d: d['postTime'],reverse=True)
          json.dump(data2, file,indent=4)
    else:
      for new_data in data:
          data2.append(new_data)
          file.seek(0)
          data2 = sorted(data2, key=lambda d: d['postTime'],reverse=True)
          json.dump(data2, file,indent=4)









    #print(json_object)
  toc = time.perf_counter()
  print(f"Downloaded general the tutorial in {toc - tic:0.4f} seconds")
  time.sleep(300)
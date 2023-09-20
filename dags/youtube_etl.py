# -*- coding: utf-8 -*-

# Sample Python code for youtube.commentThreads.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

from http.client import responses
from ntpath import join
import os
from xmlrpc.client import ResponseError
import googleapiclient.discovery
import pandas as pd

def youtube_etl():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    DEVELOPER_KEY = ""

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part = "snippet",
        videoId = 'O5AsvA9OGhM&t=910s')
    response = request.execute()
    
    data = []
    for text in response["items"]:
        comment_id = text["id"]
        author = text["snippet"]['topLevelComment']["snippet"]["authorDisplayName"]
        text_display = text["snippet"]['topLevelComment']["snippet"]["textDisplay"]
        like_count = text["snippet"]['topLevelComment']["snippet"]["likeCount"]
        publish_at = text["snippet"]['topLevelComment']["snippet"]["publishedAt"]
        update_at = text["snippet"]['topLevelComment']["snippet"]["updatedAt"]
        reply_count = text["snippet"]["totalReplyCount"]
        if publish_at == update_at:
            update_at = "NONE"
        content = {
            "comment_id": comment_id,
            "author": author,
            "comment": text_display,
            "number of like": like_count,
            "publish at": publish_at,
            "update at": update_at,
            "Number of reply": reply_count
        }
        data.append(content)

    df = pd.DataFrame(data)
    df.to_csv("data.csv", index=False)

            
"""def main():
        with open('video_id_list.txt') as f:
            for line in f:
                try: 
                    youtube_etl(line)
                except:
                    print(f"id: {line} occur an error")
                    pass
            f.close()"""



"""{
  "kind": "youtube#commentListResponse",
  "etag": etag,
  "nextPageToken": string,
  "pageInfo": {
    "totalResults": integer,
    "resultsPerPage": integer
  },
  "items": [
    {
  "kind": "youtube#comment",
  "etag": etag,
  "id": string,
  "snippet": {
    "authorDisplayName": string,
    "authorProfileImageUrl": string,
    "authorChannelUrl": string,
    "authorChannelId": {
      "value": string
    },
    "channelId": string,
    "videoId": string,
    "textDisplay": string,
    "textOriginal": string,
    "parentId": string,
    "canRate": boolean,
    "viewerRating": string,
    "likeCount": unsigned integer,
    "moderationStatus": string,
    "publishedAt": datetime,
    "updatedAt": datetime
  }
}
  ]
}"""



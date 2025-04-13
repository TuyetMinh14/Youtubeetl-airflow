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
from airflow.exceptions import AirflowException
from utils.constant import YOUTUBE_API_KEY



def youtube_etl(**context) -> str:
    """
    ETL function to extract YouTube comments
    Returns a string indicating completion status
    
    Args:
        **context: Airflow context variables
        
    Returns:
        str: Status message
        
    Raises:
        AirflowException: If API key is missing or API call fails
    """
    try:
        # Get API key from environment variable
        api_key = YOUTUBE_API_KEY
        if not api_key:
            raise AirflowException("YouTube API key not found in environment variables")

        # Build YouTube API client
        youtube = googleapiclient.discovery.build(
            "youtube", "v3", 
            developerKey=api_key,
            cache_discovery=False
        )

        # API request
        request = youtube.commentThreads().list(
            part="snippet",
            videoId='O5AsvA9OGhM&t=910s',
            maxResults=100  # Adjust as needed
        )
        response = request.execute()
        
        # Process comments
        data = []
        for item in response.get("items", []):
            comment = item["snippet"]["topLevelComment"]["snippet"]
            content = {
                "comment_id": item["id"],
                "author": comment["authorDisplayName"],
                "comment": comment["textDisplay"],
                "number of like": comment["likeCount"],
                "publish at": comment["publishedAt"],
                "update at": comment["updatedAt"] if comment["publishedAt"] != comment["updatedAt"] else "NONE",
                "Number of reply": item["snippet"]["totalReplyCount"]
            }
            data.append(content)

        # Save to CSV
        if data:
            df = pd.DataFrame(data)
            output_path = os.path.join(os.path.dirname(__file__), 'data.csv')
            df.to_csv(output_path, index=False)
            return f"ETL Process Completed - {len(data)} comments processed"
        else:
            return "ETL Process Completed - No comments found"
            
    except Exception as e:
        error_msg = f"YouTube ETL failed: {str(e)}"
        print(error_msg)
        raise AirflowException(error_msg)

if __name__ == "__main__":
    youtube_etl()

            
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



from googleapiclient.discovery import build

class YouTubeClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.service_name = "youtube"
        self.version = "v3"
        self.youtube = build(self.service_name, self.version, developerKey=self.api_key)

    def search_videos(self, query: str, max_results: int = 5):
        """Search YouTube videos by query"""
        request = self.youtube.search().list(
            q=query,
            part="snippet",
            maxResults=max_results,
            type="video"
        )
        response = request.execute()

        results = []
        for item in response.get("items", []):
            results.append({
                "video_id": item["id"]["videoId"],
                "title": item["snippet"]["title"],
                "description": item["snippet"]["description"]
            })
        return results
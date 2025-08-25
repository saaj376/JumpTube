from youtube import YoutubeClient
from config import YOUTUBE_API_KEY

if __name__=="__main__":
    ytclient=YoutubeClient(YOUTUBE_API_KEY)
    
    while True:
        query = input("\nEnter search term (or 'quit' to exit): ")
        
        if query.lower() == 'quit':
            break
            
        if query.strip():
            try:
                videos = ytclient.search(query)
                for idx, v in enumerate(videos, 1):
                    print(f"{idx}. {v['title']} — https://youtu.be/{v['video_id']}")
            except Exception as e:
                print(f"Error: {e}")
    
    print("Goodbye!")
from google import genai
from transcription import YoutubeTranscriber

class videosummarizer:
    def __init__(self,api_key,model_size="tiny.en"):
        self.transcriber=YoutubeTranscriber(model_size=model_size)
        self.client=genai.Client(api_key=api_key)
        
    def summarize(self, video_url,model="gemini-2.5-flash"):
        transcript_text=self.transcriber.transcribe(video_url)
        if transcript_text:
            prompt=("Please provide a concise summary of the following video" f" transcript:\n\n{transcript_text}")
            response=self.client.models.generate_content(model=model,contents=prompt)
            return response.text
        else:
            return "Transcription failed"
if __name__ =="__main__":
    api_key=""
    video_url="https://www.youtube.com/watch?v=b-Pn0yXL9y8"
    summarizer=videosummarizer(api_key=api_key)
    summary=summarizer.summarize(video_url)
    print("Summary")
    print(summary)
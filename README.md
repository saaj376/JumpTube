# JumpTube - YouTube Video Search & Notes Summarizer

A Python application that allows you to search for YouTube videos using the YouTube Data API v3, generate AI-powered summaries of video content, and **jump to specific parts of videos based on natural language prompts**. Available in command-line version.

## Features

- Search YouTube videos by keywords
- Asynchronous processing using celery without disrupting or blocking the UI
- Redis is used to store the cache temporarily and then next time, it gives instant reply
- **Jump to specific video parts using natural language prompts**
- **Voice/audio prompt support** for hands-free navigation
- AI-powered video content summarization and downloading it as PDF
  
## Installation

1. **Clone or download this repository**
2. Install FFMPEG and Redis
3. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure your YouTube API key:**
   - Get a YouTube Data API v3 key from [Google Cloud Console](https://console.cloud.google.com/)
   - Edit `Backend/config.py` and replace `YOUR_YOUTUBE_API_KEY_HERE` with your actual API key
   - Enable the YouTube Data API v3 in your Google Cloud project
   - also make sure google cloud speech to text API is working fine


## Project Structure

```
JumpTube/
├── Backend/
│   ├── config.py          # API configuration
│   ├── youtube.py         # YouTube API client
│   ├── main.py           # Command-line interface
│   ├── summarizer.py      # AI-powered content summarization
│   └── transcription.py   # Video transcript extraction
├── requirements.txt      # Python dependencies
└── README.md            # This file
```


## Core Feature: Jump to Video Parts

JumpTube's main feature allows you to navigate to specific parts of any YouTube video using natural language prompts. Simply describe what you're looking for, and the AI will find the exact timestamp and jump to that part of the video.

### Examples of Prompts

- **"Navigate to part where CNN is first explained"**
- **"Jump to the section about machine learning algorithms"**
- **"Go to where they discuss the main findings"**
- **"Find the part about troubleshooting steps"**
- **"Seek to the conclusion of the presentation"**

### How It Works

1. **Input Prompt**: Provide a text or voice prompt describing what you want to find
2. **AI Analysis**: The system analyzes the video transcript and content
3. **Timestamp Detection**: AI identifies the exact location in the video
4. **Video Navigation**: Automatically seeks to that timestamp and resumes playback
5. **Context Display**: Shows relevant context around the found section

### Input Methods

- **Text Prompts**: Type your request in natural language
- **Voice Commands**: Speak your request for hands-free operation
- **Audio Input**: Upload or record audio prompts

## Notes Summarizer

The application includes an AI-powered notes summarizer that can:

- **Extract Transcripts**: Automatically retrieve video transcripts from YouTube
- **Generate Summaries**: Create concise, structured notes from video content
- **Smart Analysis**: Identify key points, topics, and important information
- **Export Options**: Save summaries in various formats for study or reference

### How It Works

1. Search for a YouTube video using the search functionality
2. Select a video to analyze
3. The system extracts the video transcript
4. AI processes the content to generate structured notes
5. View or export the summarized content

## License

This project is open source and available under the Apache License


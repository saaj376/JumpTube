## Whatever I've implemented so far:

So I've designed a local system which has the following core features:
- uses the youtube api key to fetch videos and display in the UI
- the user can click on the video and play the video
- when the user begins the video, a data processing pipeline transcribes the video even before the audio playback is complete using OpenAI's faster-whisper
- a prompt bar is placed below the video. Let's say the prompt is "navigate to part where CNN is first explained" or "navigate to 5:22 of the video" or a similar prompt like that, it will navigate automatically to that part of the video

Normally to transcribe a youtube video, we have to download the video and then use an external tool to extract the text from the audio of the video file. Or else there is the youtube transcript API which extracts the youtube video transcripts from the video but this only works when the video when uploaded by the user to his/her channel has transcriptions filled in by the user manually, else it won't work. 

But I have created a data processing pipeline which transcribes the youtube video based on the url in two major steps:
- Fetching the audio stream using with yt-dlp
   - The first stage of the pipeline is to obtain a direct, streamable link to the audio of the YouTube video. We use yt-dlp for this task because it is highly efficient and avoids downloading the entire video file.
   - The core idea behind yt-dlp is to stream the audio into ffmpeg without downloading the youtube video and occupying additional space
- Converting the audio using ffmpeg
   - The audio stream obtained from yt-dlp is in a compressed format (like Opus or AAC). The Whisper model, however, requires the audio in a very specific, raw, uncompressed format. This is where ffmpeg, the universal multimedia converter, comes in.
   - The raw audio bytes from ffmpeg are then converted into a NumPy array of 32-bit floating-point numbers, normalized to a range of -1.0 to 1.0.
   - A perfectly formatted NumPy array, ready to be fed into the Whisper model for transcription.

The transcription is then used to seek to different parts of the video based on the prompt given by the user. 
Another feature which is being implemented is the youtube video notes summarizer which uses Gemini API to summarize the given youtube video url based on the transcription provided earlier and then download it as a notes in the form of a PDF.

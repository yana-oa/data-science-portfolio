## Import libraries
from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi as ytapi
########################

## Variables
yt_video = str(input(("Input Youtube Video link: ")))
video_id = yt_video.split("=")[1]
print(video_id)

########################
##Extract transcript in json
transcript = ytapi.get_transcript(video_id) #json object/dict
transcript[0:5]

## Parse json in text
vid_text = ""
for i in transcript:
    vid_text += ' '+ i['text']
print(vid_text)

## Built in summarization pipeline
summarizer = pipeline('summarization')
summarizer(vid_text, max_length = 120, min_length = 10, do_sample=False)

## Creating Summary Text
num_its = int(len(vid_text)/1000)
summary = []
for i in range(0,num_its + 1):
    start = 0
    start = i * 1000
    start = (i+1) * 1000
    out = summarizer(vid_text(start:end)) #summarizes by chunks
    out = out[0]
    out = out['summary_text']
    summary.append(out)
#create chunks and iterations are based off transcript length


print(summary)

#sentences = []
#for sentence in (vid_text):
 #   sentences.append(sentence.replace("[^a-zA-Z]"," ").split(" "))
#sentences.pop()
#print(sentences)




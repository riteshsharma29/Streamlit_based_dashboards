import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
import streamlit.components.v1 as components

st.title("Streamlit YouTube Transcript Extractor")
URL = st.sidebar.text_input("Paste YouTube URL:","https://www.youtube.com/watch?v=zFvoXxeoosI")

if "=" in URL:
    ID = URL.split("=")[1]
    embedurl = "https://www.youtube.com/embed/" + ID
    if "&" in embedurl: embedurl = embedurl.split("&")[0]
try:
    components.iframe(embedurl, width=500, height=250)
except:
    st.error("YouTube URL Required")

try:
    transcript = YouTubeTranscriptApi.get_transcript(ID)
    l = [t['text'] for t in transcript]
    description = " ".join(l)
except:
    pass

try :
    if len(description) > 0:
        output = st.text_area("Extracted Transcript",description,height=200)
        st.download_button(label="Download Transcript",data=description,file_name=str(ID) + ".txt",mime="text/plain")
except Exception as e:
        st.error("Transcript Not available for this video")




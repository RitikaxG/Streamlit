import streamlit as st
import pandas as pd 

st.subheader("Uploading the CSV file")

df = st.file_uploader("Loading the CSV file:",type=['csv','xlsx'])

df = pd.read_csv("iris.csv")
if df is not None:
    st.table(df.head())


st.subheader("Dealing with images directly")
st.image('Ritika.jpeg')


st.subheader("Working with Images")
img_file = st.file_uploader("Upload the Image file:",type=['png','jpeg'])
if img_file is not None:
    st.image(img_file)


st.subheader("Working with Videos")

video_file = st.file_uploader("Upload the video file:",type=['mp4','mkv'])
if video_file is not None:
    st.video(video_file,start_time=0)


st.subheader("Working with Audio")
audio_file = st.file_uploader("Upload the audio file:",type=['mp3','wav'])
if audio_file is not None:
    st.audio(audio_file.read())

import streamlit as st
import json
import requests 
from streamlit_lottie import st_lottie 
from PIL import Image

# GitHub: https://github.com/andfanilo/streamlit-lottie
# Lottie Files: https://lottiefiles.com/
st.set_page_config(
    layout="wide",
    page_icon= "🤖",
    page_title= "InfuGenX"
)

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottiefile("lottiefiles/chatdoc.json")  # replace link to local lottie file
lottie_hello = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_M9p23l.json")

st.title("      WELCOME TO :green[ChatDoc]       ")
st.write("  Seamless Conversations with :green[PDF's] ")
st_lottie(
    lottie_coding,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
    height=500,
    width=1000,
    key=None,
)

st.subheader("💡 Working Model ")
lottie_workingmodel = load_lottiefile("lottiefiles/working.json")
st_lottie(
    lottie_workingmodel,
    speed=1,
    reverse=False,
    loop=True,
    quality="low", # medium ; high
    height=700,
    width=1000,
    key=None,
)


with st.sidebar:
  st.image('chatdoc-logo-black.png', width=150 )

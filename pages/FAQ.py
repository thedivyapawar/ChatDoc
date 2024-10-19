import streamlit as st 
import app_component as au
from PIL import Image

st.set_page_config(
    page_title="AI InfuGenX- FAQ",
    page_icon="https://api.dicebear.com/5.x/bottts-neutral/svg?seed=faq"#,
)

st.markdown(
    "<style>#MainMenu{visibility:hidden;}</style>",
    unsafe_allow_html=True
)

st.title("FAQ")

#st.markdown("---")
au.robo_avatar_component()

st.markdown("#### AI Designs")

with st.expander("What is ChatDoc?"):
    st.markdown("ChatDoc is an innovative web-based platform designed to revolutionize the way users interact with their documents, particularly PDF files. At its core, ChatDoc integrates natural language processing (NLP) capabilities with document analysis, enabling users to engage in conversational queries and prompts to extract specific information and insights from their documents.")

with st.expander("What language models do you support?"):
    st.markdown("""
    We currently support the following Google Gemini: Every model has its own strengths and weaknesses, and the choice of model should be based on your specific use case. You can find detailed information on each model on https://ai.google.dev/ .  \n
    """)

st.markdown("#### General")
with st.expander("What is Google Gemini?"):
    st.markdown("Google Gemini is a family of new AI models from Google. Despite Google being a leader in AI research for almost a decade and developing the transformer architecture—one of the key technologies in large language models (LLMs)—OpenAI and its GPT models are dominating the conversation.")

with st.expander("What is an Google API Key and why do I need one?"):
    st.markdown("An OpenAI API key is a unique credential that allows you to interact with Google AI based models.")

with st.expander("How can I get an GOOGLE API Key?"):
    st.markdown("You can obtain an GOOGLE API Key by creating one on the GOOGLE website for AI Developers: https://ai.google.dev/tutorials/setup")


st.markdown("#### Privacy, Platform Guidelines, and Intellectual Property")

with st.expander("Is my information kept confidential on ChatDoc?"):
    st.markdown("Yes, we take your privacy and confidentiality very seriously. We do not store any personally identifiable.")

with st.expander("Who owns the prompts created in ChatDoc ?"):
    st.markdown("You do! The prompts created by the users in ChatDoc belong to the users themselves. It is a platform that enables users to interact with and create their own AI Designs powered by Google's language models for AI Developers, and the prompts created by the users in the app are the property of the users themselves.ChatDoc does not claim any ownership or rights to the prompts created by the users.")

with st.sidebar:
  st.image('chatdoc-logo-black.png', width=150 )
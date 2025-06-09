import streamlit as st
from PIL import Image
from fashion_myth_utils import get_myth_theme_suggestions, match_image_to_myth
from agent import talk_to_muse

st.set_page_config(page_title="MythosMuse AI", layout="wide")
st.title("🎭 MythosMuse AI – Where Mythology Inspires Modern Design")

st.markdown("Select a myth or upload an image, and let your AI Muse create legendary fashion.")

# Select a Myth Theme
myth = st.selectbox("🔮 Choose a Mythology Theme", ["Greek", "Indian", "Norse", "Egyptian", "Celtic"])

if myth:
    st.subheader(f"🧵 Outfit Concepts Inspired by {myth} Mythology")
    st.markdown(get_myth_theme_suggestions(myth))

# Upload Fabric or Design
st.subheader("📸 Upload Fabric / Accessory Image")
uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Sample", use_column_width=True)
    matched_myth = match_image_to_myth(image)
    st.success(f"This image reminds us of: **{matched_myth}**")

# Ask the AI Agent
st.subheader("🧠 Ask Your Muse")
user_prompt = st.text_input("What fashion idea are you exploring?")
if user_prompt:
    response = talk_to_muse(user_prompt)
    st.markdown(response)

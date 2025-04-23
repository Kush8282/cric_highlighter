import streamlit as st

st.set_page_config(page_title="Cric Highlighter", layout="centered")

st.title("🏏 Cric Highlight Maker")
st.markdown("This is your deployed Streamlit app!")

uploaded_file = st.file_uploader("Upload your cricket video", type=["mp4"])

if uploaded_file:
    st.success("✅ File uploaded successfully!")
    st.video(uploaded_file)
else:
    st.info("Please upload a .mp4 video to continue.")

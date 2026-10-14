import streamlit as st

# पेज का टाइटल और लेआउट सेट करना
st.set_page_config(page_title="AI Flow Studio", page_icon="🎬", layout="wide")

# ऐप का हेडर
st.title("🎬 AI Flow Studio")
st.write("आपका अपना फ्री AI वीडियो और इमेज जनरेटर")

st.divider()

# यूजर इनपुट एरिया
prompt = st.text_area("आप क्या बनाना चाहते हैं? (Prompt दर्ज करें):", placeholder="An astronaut riding a horse on Mars, 4k cinematic style...")

# जनरेट बटन
if st.button("🚀 Generate AI Content"):
    if prompt:
        st.info(f"आपका प्रॉम्प्ट मिला: **'{prompt}'**")
        st.success("Day 1 कम्पलीट! कल हम इसमें फ्री AI API जोड़कर असली इमेज/वीडियो जनरेट करेंगे।")
    else:
        st.warning("कृपया पहले कुछ प्रॉम्प्ट लिखें!")

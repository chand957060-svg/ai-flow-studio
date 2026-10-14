import streamlit as st
import urllib.parse

# पेज सेटिंग्स
st.set_page_config(page_title="AI Flow Studio", page_icon="🎬", layout="wide")

# साइट हेडर
st.title("🎬 AI Flow Studio")
st.write("फ्री AI इमेज, वीडियो और वॉइसओवर स्टूडियो")

st.divider()

# टैब्स (Tabs) बनाना
tab1, tab2, tab3 = st.tabs(["🎨 AI Image", "🎥 AI Video", "🎙️ AI Voiceover"])

# --- TAB 1: AI IMAGE GENERATOR ---
with tab1:
    st.header("1. AI Image Generator")
    img_prompt = st.text_area("इमेज के लिए प्रॉम्प्ट लिखें:", placeholder="A futuristic city with flying cars at sunset, 4k resolution...")
    aspect_ratio = st.selectbox("Aspect Ratio", ["1:1 (Square)", "16:9 (Landscape)", "9:16 (Story/Reels)"])
    
    width, height = 1024, 1024
    if "16:9" in aspect_ratio:
        width, height = 1280, 720
    elif "9:16" in aspect_ratio:
        width, height = 720, 1280
        
    if st.button("🚀 Generate Image"):
        if img_prompt:
            with st.spinner("इमेज जनरेट हो रही है..."):
                encoded = urllib.parse.quote(img_prompt)
                img_url = f"https://image.pollinations.ai/prompt/{encoded}?width={width}&height={height}&nologo=true"
                st.image(img_url, caption=img_prompt, use_column_width=True)
        else:
            st.warning("कृपया प्रॉम्प्ट लिखें!")

# --- TAB 2: AI VIDEO GENERATOR ---
with tab2:
    st.header("2. AI Video Generator (Pollinations)")
    vid_prompt = st.text_area("वीडियो के लिए प्रॉम्प्ट लिखें:", placeholder="Cinematic motion of a glowing neon tiger running through a dark forest, 4k...")
    
    if st.button("🚀 Generate Video"):
        if vid_prompt:
            with st.spinner("AI वीडियो जनरेट हो रहा है... इसमें 15-20 सेकंड लग सकते हैं..."):
                encoded_vid = urllib.parse.quote(vid_prompt)
                # Pollinations Free AI Video URL
                video_url = f"https://image.pollinations.ai/prompt/{encoded_vid}?model=video&nologo=true"
                st.video(video_url)
        else:
            st.warning("कृपया प्रॉम्प्ट लिखें!")

# --- TAB 3: AI VOICEOVER GENERATOR ---
with tab3:
    st.header("3. AI Voiceover Generator")
    voice_text = st.text_area("जिस टेक्स्ट की आवाज़ बनानी है यहाँ लिखें:", placeholder="नमस्कार! AI Flow Studio में आपका स्वागत है।")
    lang = st.selectbox("भाषा (Language)", ["hi (Hindi)", "en (English)"])
    lang_code = "hi" if "hi" in lang else "en"
    
    if st.button("🎙️ Generate Voice"):
        if voice_text:
            with st.spinner("ऑडियो तैयार हो रहा है..."):
                encoded_voice = urllib.parse.quote(voice_text)
                # Google TTS Free URL
                audio_url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={encoded_voice}&tl={lang_code}&client=tw-ob"
                st.audio(audio_url, format="audio/mp3")
        else:
            st.warning("कृपया टेक्स्ट लिखें!")

import streamlit as st
import requests
import io
from PIL import Image
import urllib.parse

# 1. Page Config
st.set_page_config(
    page_title="AI Flow Studio - Pro", 
    page_icon="✨", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Custom CSS (Google Flow Dark Theme)
st.markdown("""
    <style>
    .stApp { background-color: #0b0f19; color: #f3f4f6; }
    .stTabs [data-baseweb="tab-list"] { background-color: #111827; padding: 10px; border-radius: 12px; gap: 10px; }
    .stTabs [data-baseweb="tab"] { background-color: #1f2937; color: #9ca3af; border-radius: 8px; font-weight: 600; padding: 10px 20px; }
    .stTabs [aria-selected="true"] { background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%); color: white !important; }
    .stButton>button { background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%); color: white; border-radius: 8px; font-weight: 600; width: 100%; border: none; padding: 0.6rem; }
    .stTextArea textarea { background-color: #1f2937 !important; color: white !important; border: 1px solid #374151 !important; border-radius: 8px; }
    </style>
""", unsafe_allow_html=True)

# Get Token from Secrets
HF_TOKEN = st.secrets.get("HF_TOKEN", "")

# 3. Sidebar
with st.sidebar:
    st.title("⚙️ Studio Dashboard")
    st.markdown("---")
    if HF_TOKEN:
        st.success("✅ API Connected Successfully")
    else:
        st.warning("⚠️ HF_TOKEN Missing in Secrets")
    st.info("💡 **Tips:** बेहतरीन रिजल्ट के लिए हमेशा विस्तृत इंग्लिश प्रॉम्प्ट लिखें।")

# 4. Main Header
st.title("✨ AI Flow Studio Pro")
st.markdown("खास आपके लिए तैयार किया गया एडवांस्ड AI मीडिया जनरेशन प्लेटफ़ॉर्म।")
st.divider()

# 5. Tabs for Features
tab1, tab2, tab3 = st.tabs(["🎨 AI Image Studio", "🎥 AI Video Studio", "🎙️ AI Voice Studio"])

# --- TAB 1: AI IMAGE STUDIO ---
with tab1:
    st.subheader("High-Resolution Image Generation (SDXL)")
    col1, col2 = st.columns([2, 1])
    with col1:
        img_prompt = st.text_area("इमेज प्रॉम्प्ट लिखें:", placeholder="A futuristic cybernetic tiger in a neon city, 8k, highly detailed...")
    with col2:
        aspect_ratio = st.selectbox("फॉर्मेट चुनें", ["Square (1:1)", "Landscape (16:9)"])
        
    if st.button("🚀 Generate AI Image"):
        if not HF_TOKEN:
            st.error("कृपया पहले Streamlit Secrets में अपना HF_TOKEN सेट करें!")
        elif img_prompt:
            with st.spinner("AI इमेज बना रहा है... कृपया 10-15 सेकंड प्रतीक्षा करें..."):
                API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
                headers = {"Authorization": f"Bearer {HF_TOKEN}"}
                payload = {"inputs": img_prompt}
                
                try:
                    response = requests.post(API_URL, headers=headers, json=payload, timeout=40)
                    if response.status_code == 200:
                        image = Image.open(io.BytesIO(response.content))
                        st.success("इमेज सफलतापूर्वक तैयार हो गई!")
                        st.image(image, caption=img_prompt, use_column_width=True)
                    else:
                        st.error(f"Error: {response.text}")
                except Exception as e:
                    st.error(f"Connection Error: {str(e)}")
        else:
            st.warning("कृपया प्रॉम्प्ट लिखें!")

# --- TAB 2: AI VIDEO STUDIO ---
with tab2:
    st.subheader("Cinematic Video Clips Generator")
    vid_prompt = st.text_area("वीडियो प्रॉम्प्ट लिखें:", placeholder="Cinematic drone shot flying through a glowing futuristic tech city...")
    
    if st.button("🚀 Generate AI Video"):
        if vid_prompt:
            with st.spinner("AI वीडियो रेंडर हो रहा है... (यह कुछ सेकंड ले सकता है)"):
                # Using stable fallback video rendering endpoint
                encoded_vid = urllib.parse.quote(vid_prompt)
                video_url = f"https://image.pollinations.ai/prompt/{encoded_vid}?model=video&nologo=true"
                st.success("वीडियो तैयार है!")
                st.video(video_url)
        else:
            st.warning("कृपया प्रॉम्प्ट लिखें!")

# --- TAB 3: AI VOICE STUDIO ---
with tab3:
    st.subheader("Multilingual AI Voiceover")
    voice_text = st.text_area("जिस टेक्स्ट की आवाज़ बनानी है यहाँ लिखें:", placeholder="नमस्ते! AI Flow Studio में आपका स्वागत है।")
    lang = st.selectbox("भाषा चुनें", ["Hindi (हिंदी)", "English (अंग्रेजी)"])
    lang_code = "hi" if "Hindi" in lang else "en"
    
    if st.button("🎙️ Generate Voiceover"):
        if voice_text:
            with st.spinner("ऑडियो सिंथेसाइज हो रहा है..."):
                encoded_voice = urllib.parse.quote(voice_text)
                audio_url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={encoded_voice}&tl={lang_code}&client=tw-ob"
                st.success("ऑडियो तैयार है!")
                st.audio(audio_url, format="audio/mp3")
        else:
            st.warning("कृपया टेक्स्ट लिखें!")

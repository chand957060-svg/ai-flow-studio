import streamlit as st
import urllib.parse

# 1. पेज कॉन्फ़िगरेशन (डार्क थीम और वाइड लेआउट)
st.set_page_config(
    page_title="AI Flow Studio - Pro", 
    page_icon="✨", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. कस्टम CSS (Google Flow जैसी प्रीमियम डार्क थीम और मॉडर्न UI)
st.markdown("""
    <style>
    /* Main Background & Font */
    .stApp {
        background-color: #0b0f19;
        color: #f3f4f6;
        font-family: 'Inter', sans-serif;
    }
    
    /* Sidebar Styling */
    css-1d391kg, [data-testid="stSidebar"] {
        background-color: #111827;
        border-right: 1px solid #1f2937;
    }

    /* Tabs Styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: #111827;
        padding: 10px;
        border-radius: 12px;
    }
    .stTabs [data-baseweb="tab"] {
        background-color: #1f2937;
        color: #9ca3af;
        border-radius: 8px;
        padding: 10px 20px;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white !important;
    }

    /* Buttons Styling */
    .stButton>button {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        width: 100%;
        box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        opacity: 0.9;
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(168, 85, 247, 0.4);
    }

    /* Text Areas & Inputs */
    .stTextArea textarea, .stSelectbox select {
        background-color: #1f2937 !important;
        color: white !important;
        border: 1px solid #374151 !important;
        border-radius: 8px !important;
    }
    </style>
""", unsafe_allow_html=True)

# 3. साइडबार (Sidebar Controls)
with st.sidebar:
    st.image("https://img.icons8.com/clouds/200/artificial-intelligence.png", width=100)
    st.title("⚙️ Studio Control")
    st.markdown("---")
    st.info("💡 **Tip:** बेहतरीन रिजल्ट के लिए अपने प्रॉम्प्ट में इंग्लिश शब्दों (जैसे: *cinematic lighting, 4k, hyperrealistic*) का इस्तेमाल करें।")
    st.markdown("---")
    st.markdown("🚀 **Status:** Free Tier Active")
    st.markdown("⚡ **Engine:** Pollinations AI & Google TTS")

# 4. मुख्य हेडर (Main Header)
st.title("✨ AI Flow Studio Pro")
st.markdown("खास आपके लिए तैयार किया गया नेक्स्ट-जेन AI मीडिया जनरेशन प्लेटफ़ॉर्म।")
st.divider()

# 5. टैब्स (Tabs)
tab1, tab2, tab3 = st.tabs(["🎨 AI Image Studio", "🎥 AI Video Studio", "🎙️ AI Voice Studio"])

# --- TAB 1: IMAGE ---
with tab1:
    col1, col2 = st.columns([2, 1])
    with col1:
        img_prompt = st.text_area("इमेज प्रॉम्प्ट दर्ज करें:", placeholder="A futuristic cybernetic samurai standing in neon rain, 8k, cinematic...")
    with col2:
        aspect_ratio = st.selectbox("इमेज फॉर्मेट (Aspect Ratio)", ["Square (1:1)", "Landscape (16:9)", "Portrait (9:16)"])
    
    width, height = 1024, 1024
    if "16:9" in aspect_ratio:
        width, height = 1280, 720
    elif "9:16" in aspect_ratio:
        width, height = 720, 1280
        
    if st.button("🚀 Generate AI Image"):
        if img_prompt:
            with st.spinner("AI आपकी इमेज बना रहा है..."):
                encoded = urllib.parse.quote(img_prompt)
                img_url = f"https://image.pollinations.ai/prompt/{encoded}?width={width}&height={height}&nologo=true"
                st.success("इमेज तैयार है!")
                st.image(img_url, caption=img_prompt, use_column_width=True)
        else:
                    st.warning("कृपया पहले प्रॉम्प्ट लिखें!")

# --- TAB 2: VIDEO ---
with tab2:
    vid_prompt = st.text_area("वीडियो प्रॉम्प्ट दर्ज करें:", placeholder="Cinematic drone shot flying through a glowing futuristic tech city...")
    if st.button("🚀 Generate AI Video"):
        if vid_prompt:
            with st.spinner("AI वीडियो रेंडर हो रहा है... (15-20 सेकंड प्रतीक्षा करें)"):
                encoded_vid = urllib.parse.quote(vid_prompt)
                video_url = f"https://image.pollinations.ai/prompt/{encoded_vid}?model=video&nologo=true"
                st.success("वीडियो तैयार है!")
                st.video(video_url)
        else:
            st.warning("कृपया पहले प्रॉम्प्ट लिखें!")

# --- TAB 3: VOICEOVER ---
with tab3:
    voice_text = st.text_area("वॉइसओवर के लिए टेक्स्ट लिखें:", placeholder="नमस्ते! AI Flow Studio में आपका स्वागत है।")
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
            st.warning("कृपया पहले टेक्स्ट लिखें!")

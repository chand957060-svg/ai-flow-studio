import streamlit as st
import requests
import io
from PIL import Image

# पेज कॉन्फ़िगरेशन
st.set_page_config(page_title="AI Flow Studio", page_icon="🎬", layout="wide")

st.title("🎬 AI Flow Studio")
st.write("फ्री में हाई-क्वालिटी AI इमेज और वीडियो बनाएं")

st.divider()

# Streamlit Secrets से API Token लेना
HF_TOKEN = st.secrets.get("HF_TOKEN", "")

# Hugging Face Flux AI Model API Endpoint
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def generate_image(prompt_text):
    payload = {"inputs": prompt_text}
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return Image.open(io.BytesIO(response.content))
    else:
        st.error(f"Error {response.status_code}: API कनेक्ट करने में समस्या आई।")
        return None

# UI Controls
prompt = st.text_area("आप क्या बनाना चाहते हैं? (Prompt दर्ज करें):", 
                      placeholder="A futuristic cybernetic tiger in a neon city, 8k resolution, cinematic lighting...")

if st.button("🚀 Generate AI Image"):
    if not HF_TOKEN:
        st.error("कृपया Streamlit Secrets में अपना HF_TOKEN सेट करें!")
    elif prompt:
        with st.spinner("AI इमेज जनरेट हो रही है... कृपया 10-15 सेकंड प्रतीक्षा करें..."):
            image = generate_image(prompt)
            if image:
                st.success("इमेज सफलतापूर्वक तैयार हो गई!")
                st.image(image, caption=prompt, use_column_width=True)
    else:
        st.warning("कृपया पहले कुछ प्रॉम्प्ट लिखें!")

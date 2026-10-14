import streamlit as st
import requests
import io
from PIL import Image

# पेज सेटिंग्स
st.set_page_config(page_title="AI Flow Studio", page_icon="🎬", layout="wide")

st.title("🎬 AI Flow Studio")
st.write("फ्री में हाई-क्वालिटी AI इमेज जनरेट करें")

st.divider()

# Streamlit Secrets से API Token लेना
HF_TOKEN = st.secrets.get("HF_TOKEN", "")

# वर्किंग मॉडल (Stable Diffusion XL Turbo - बहुत तेज़ और मुफ़्त)
API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def generate_image(prompt_text):
    payload = {"inputs": prompt_text}
    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 200:
            return Image.open(io.BytesIO(response.content)), None
        elif response.status_code == 503:
            return None, "मॉडल अभी लोड हो रहा है, कृपया 10 सेकंड बाद दोबारा बटन दबाएं।"
        elif response.status_code == 401:
            return None, "API Token सही नहीं है! कृपया Streamlit Secrets जांचें।"
        else:
            return None, f"Error {response.status_code}: {response.text}"
            
    except Exception as e:
        return None, f"Connection Error: इंटरनेट या सर्वर की समस्या। ({str(e)})"

# UI
prompt = st.text_area("आप क्या बनाना चाहते हैं? (Prompt दर्ज करें):", 
                      placeholder="A cute robot drinking tea in space, highly detailed, 4k...")

if st.button("🚀 Generate AI Image"):
    if not HF_TOKEN:
        st.error("कृपया Streamlit Secrets में अपना HF_TOKEN सेट करें!")
    elif prompt:
        with st.spinner("AI इमेज जनरेट हो रही है..."):
            image, err = generate_image(prompt)
            if image:
                st.success("इमेज बन गई!")
                st.image(image, caption=prompt, use_column_width=True)
            else:
                st.error(err)
    else:
        st.warning("कृपया पहले कुछ प्रॉम्प्ट लिखें!")

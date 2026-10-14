import streamlit as st

# पेज सेटिंग्स
st.set_page_config(page_title="AI Flow Studio", page_icon="🎬", layout="wide")

st.title("🎬 AI Flow Studio")
st.write("फ्री और फास्ट AI इमेज जनरेटर")

st.divider()

# UI Controls
prompt = st.text_area("आप क्या बनाना चाहते हैं? (Prompt दर्ज करें):", 
                      placeholder="A cute baby in space, cinematic lighting, 4k...")

aspect_ratio = st.selectbox("इमेज साइज़ (Aspect Ratio)", ["Square (1:1)", "Landscape (16:9)", "Portrait (9:16)"])

# साइज़ सेट करना
width, height = 1024, 1024
if "16:9" in aspect_ratio:
    width, height = 1280, 720
elif "9:16" in aspect_ratio:
    width, height = 720, 1280

if st.button("🚀 Generate AI Image"):
    if prompt:
        with st.spinner("AI इमेज जनरेट हो रही है... कृपया कुछ सेकंड प्रतीक्षा करें..."):
            # URL-encode the prompt safely
            import urllib.parse
            encoded_prompt = urllib.parse.quote(prompt)
            
            # Pollinations AI Free URL (बिना किसी API Key या एरर के काम करता है)
            image_url = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width={width}&height={height}&nologo=true"
            
            st.success("इमेज सफलतापूर्वक तैयार हो गई!")
            st.image(image_url, caption=prompt, use_column_width=True)
    else:
        st.warning("कृपया पहले कुछ प्रॉम्प्ट लिखें!")

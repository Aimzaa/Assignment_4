import streamlit as st
from streamlit_lottie import st_lottie
import json
import requests

# Set page config with emoji
st.set_page_config(
    page_title="My First Website", 
    page_icon="🌐", 
    layout="centered"
)

# Load Lottie animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_hello = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_ktwnwv5m.json")

# Stylish title with emoji
st.title("✨ Welcome to My First Python Website! 🎯")

# Colorful sidebar navigation
with st.sidebar:
    st.title("🗺️ Navigation")
    page = st.radio("Go to", ["🏠 Home", "ℹ️ About", "📩 Contact"],index=0)

# Home Page
if page == "🏠 Home":
    st.header("🏡 Home Page")
    st.write("🌟 This is a simple home page built with Python and Streamlit")
    
    name = st.text_input("👋 What's your name?")
    if name:
        st.success(f'🎉 Hello {name}! Thanks for visiting! 🥳')
        st.balloons()  # Celebration animation

# About Page
elif page == "ℹ️ About":
    st.header("📚 About Page")
    st.write("""
    🚀 This website is built entirely using Python and Streamlit in under 15 minutes!
    \n💡 Streamlit makes it super easy to create web apps with just Python code.
    \n🐍 No HTML/CSS/JavaScript required!
    """)
    
    # Skills progress bars
    st.subheader("🛠️ Skills Used")
    st.progress(90, text="Python")
    st.progress(80, text="Streamlit")
    st.progress(70, text="Web Development")

# Contact Page
elif page == "📩 Contact":
    st.header("📬 Contact Us")
    
    with st.form("contact_form"):
        email = st.text_input("📧 Your Email")
        message = st.text_area("💬 Your Message")
        
        submitted = st.form_submit_button("🚀 Submit")
        if submitted:
            st.success("🎊 Thanks for reaching out! We'll contact you soon!")
            st.balloons()

# Lottie animation at the bottom
if lottie_hello:
    st_lottie(
        lottie_hello,
        speed=1,
        reverse=False,
        loop=True,
        quality="high",
        height=300,
        key=None
    )
else:
    st.warning("Couldn't load animation")

# Footer
st.markdown("---")
st.markdown("© 2025 Made with Aiman Khan ❤️ using Streamlit")
import streamlit as st


def footer_home():
    logo_url = "https://i.ibb.co/4r5X1FY/apnacollege.png"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:white;"> Created with ❤️ by </p>  
        <span style="display:inline-block; background:#ffffff22; color:#fff; padding:4px 10px; border-radius:999px; font-weight:700; margin-left:8px;">SONU</span>
        </div>
                
                """, unsafe_allow_html=True)


def footer_dashboard():
    logo_url = "https://i.ibb.co/4r5X1FY/apnacollege.png"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:black;"> Created with ❤️ by </p>  
        <span style="display:inline-block; background:#0000000f; color:#000; padding:4px 10px; border-radius:999px; font-weight:700; margin-left:8px;">SONU</span>
        </div>
                
                """, unsafe_allow_html=True)
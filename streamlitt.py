import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Set page title and icon
st.set_page_config(page_title="Solar SCADA Login", page_icon="☀")

# Add a background image
background_image = Image.open(""C:\Users\91983\Desktop\20200415_154039.jpg"") # Replace with your image
st.image(background_image, use_column_width=True)

# Create a container for the login form
login_container = st.container()
login_container.markdown("<h1 style='text-align: center; color: white;'>Solar SCADA Login</h1>", unsafe_allow_html=True)

# Add the login form
with login_container:
  user_name = st.text_input("User Name", key="username")
  password = st.text_input("Password", type="password", key="password")
  remember_me = st.checkbox("Remember me", key="remember")
  login_button = st.button("Sign in", use_container_width=True, type="primary")

# Add "Forgot password" and "No account" links
with login_container:
  st.markdown("<p style='text-align: center; color: white;'>Forgot Password?</p>", unsafe_allow_html=True)
  st.markdown("<p style='text-align: center; color: white;'>No account? Apply for registration</p>")

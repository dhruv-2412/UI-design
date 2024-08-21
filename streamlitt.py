import streamlit as st
import hashlib

# Create a title for the app
st.title("Solar SCADA Login")

# Add custom CSS for styling
st.markdown("""
    <style>
    .login-box {
        width: 300px;
        margin: auto;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 10px;
        background-color: #f9f9f9;
    }
    .login-box input {
        margin-bottom: 10px;
    }
    .login-box button {
        background-color: green;
        color: white;
        width: 100%;
        padding: 10px;
        border: none;
        border-radius: 5px;
    }
    .login-box a {
        display: block;
        text-align: center;
        margin-top: 10px;
        color: #007bff;
        text-decoration: none;
    }
    .login-box a:hover {
        text-decoration: underline;
    }
    body {
        background-image: url('https://img.staticmb.com/mbcontent/images/crop/uploads/2024/1/solar-panels-for-home_0_1200.jpg');
        background-size: cover;
    }
    </style>
""", unsafe_allow_html=True)

# Create a form for login credentials
with st.form("login_form", clear_on_submit=True):
    st.markdown('<div class="login-box">', unsafe_allow_html=True)
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submit_button = st.form_submit_button("Login")
    st.markdown('<a href="https://example.com/forgot-password">Forgot password?</a>', unsafe_allow_html=True)
    st.markdown('<a href="https://example.com/register">Don\'t have an account? Register here</a>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# Create a dictionary to store usernames and passwords
users = {"admin": "password123", "user1": "password456", "user2": "password789"}

# Create a function to hash passwords
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Create a function to check if the username and password are correct
def check_credentials(username, password):
    if username in users:
        stored_password = users[username]
        hashed_password = hash_password(password)
        if hashed_password == stored_password:
            return True
    return False

# Check if the login credentials are correct
if submit_button:
    if check_credentials(username, password):
        st.success("Login successful! Redirecting to dashboard...")
        # Redirect to the dashboard page
        st.write("You are now logged in. Please wait while we redirect you to the dashboard...")
        # You can add code here to redirect to a new page or perform some action
    else:
        st.error("Invalid username or password")

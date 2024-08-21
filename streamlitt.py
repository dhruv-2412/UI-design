import streamlit as st
import hashlib

# Set the background image
st.markdown("""
<style>
body {
    background-image: url("https://images.unsplash.com/photo-1593642634443-44a065d409b6?ixlib=rb-1.2.1&q=80&fm=jpg&crop=entropy&cs=tinysrgb&w=1080&fit=max");
    background-size: cover;
}
</style>
""", unsafe_allow_html=True)

# Create a title for the app
st.title("Solar SCADA Login")

# Create a form for login credentials
with st.form("login_form"):
    st.write("Login to your Solar SCADA account")
    username = st.text_input("Username", placeholder="Enter your username")
    password = st.text_input("Password", type="password", placeholder="Enter your password")
    st.write("")
    st.write("")
    st.markdown("Forgot password? [Click here](https://example.com/forgot-password)")
    st.markdown("Don't have an account? [Register here](https://example.com/register)")
    submit_button = st.form_submit_button("Login", button_color="green")

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

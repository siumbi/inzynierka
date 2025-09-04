import streamlit as st

# --- USER DATA (in real life, use a database + hashed passwords) ---
users = {
    "alice": {"password": "123", "role": "admin"},
    "bob": {"password": "abc", "role": "admin"},
    "charlie": {"password": "xyz", "role": "user"}
}

# --- SESSION STATE INIT ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = None
    st.session_state.role = None
    st.session_state.page = "login"  # start at login page

# --- PAGE: LOGIN ---
def login_page():
    st.title("🔑 Login Page")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and users[username]["password"] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.session_state.role = users[username]["role"]
            st.session_state.page = "dashboard"  # redirect to dashboard
            st.experimental_rerun()
        else:
            st.error("❌ Invalid username or password")

# --- PAGE: DASHBOARD ---
def dashboard_page():
    role = st.session_state.role
    username = st.session_state.username

    st.sidebar.success(f"Logged in as {username} ({role})")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.session_state.role = None
        st.session_state.page = "login"
        st.experimental_rerun()

    if role == "admin":
        st.title("📊 Admin Dashboard")
        st.write("Welcome, admin! You can manage users and see full reports.")

        st.subheader("Admin tools")
        st.write("- Add/remove users (future feature)")
        st.write("- Full access to sensitive data")

    else:
        st.title("👤 User Dashboard")
        st.write("Welcome, user! You can see only basic information.")

        st.subheader("Basic Information")
        st.write("- Membership status")
        st.write("- Payment overview")

# --- MAIN ROUTER ---
if st.session_state.page == "login":
    login_page()
elif st.session_state.page == "dashboard":
    dashboard_page()


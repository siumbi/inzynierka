import streamlit as st

# --- USER DATA (normally from DB or file) ---
users = {
    "alice": {"password": "123", "role": "admin"},
    "bob": {"password": "abc", "role": "admin"},
    "charlie": {"password": "xyz", "role": "user"}
}

# --- LOGIN ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.username = None

if not st.session_state.logged_in:
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and users[username]["password"] == password:
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"Welcome {username}!")
        else:
            st.error("Invalid username or password")

else:
    # --- AFTER LOGIN ---
    username = st.session_state.username
    role = users[username]["role"]

    st.sidebar.success(f"Logged in as {username} ({role})")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.username = None
        st.experimental_rerun()

    if role == "admin":
        st.title("Admin Dashboard")
        st.write("Full access to reports and data")
    else:
        st.title("User Dashboard")
        st.write("Basic info only")

import streamlit as st
import requests

API_URL = "http://localhost:8000"

st.set_page_config(page_title="Notes Manager", layout="centered")
st.title("📝 Notes Manager")

try:
    response = requests.get(f"{API_URL}/notes")
    notes = response.json()\
    
except :
    notes = []
    st.warning("Backend not runnung")

for note in notes:
    st.markdown(f'**{note["title"]}**: {note["content"]}')
    st.divider()

with st.form("add_note_form"):
    title = st.text_input("Note Title")
    content = st.text_area("Note Content")
    submitted = st.form_submit_button("➕ Add Note")

    if submitted:
        if title and content:
            res = requests.post(
                f"{API_URL}/notes",
                json={"title": title, "content": content}
            )
            if res.status_code == 200:
                st.success("✅ Note added!")
                st.rerun()  # Refresh the page to show new note
            else:
                st.error("❌ Failed to add note")
        else:
            st.warning("⚠️ Please fill in both fields")
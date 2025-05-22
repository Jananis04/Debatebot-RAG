import streamlit as st
from generate_debate import generate_debate

st.set_page_config(page_title="DebateBot", layout="centered")
st.title("DebateBot")

topic = st.text_input("Enter a debate topic:")
if topic:
    with st.spinner("Generating arguments..."):
        output = generate_debate(topic)
    st.markdown("###Debate")
    st.markdown(f"```markdown\n{output}\n```")

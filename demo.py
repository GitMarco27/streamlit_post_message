import streamlit as st

from streamlit_post_message.streamlit_post_message import streamlit_post_message

if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="Streamlit Post Message Demo")

    payload = streamlit_post_message(sleep_time=1.0, message_key="tool-init")
    with st.expander("Payload received from parent window: ", expanded=True):
        st.info(payload)

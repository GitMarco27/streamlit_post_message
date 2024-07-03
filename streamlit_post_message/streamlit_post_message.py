"""
Streamlit Post Message component
"""

import os
import time

import streamlit as st
from streamlit_javascript import st_javascript


def streamlit_post_message(
    sleep_time: float = 1.0, message_key: str = "tool-init"
) -> dict:
    """
    Streamlit component for application embedded in an iFrame.
    The component sends an ackonolgment to the parent window first.
    After that, it waits for a payload from the parent application
    using postMessage via an EventListener.
    When the message is received, the event listener is removed.

    The component continues to relaunch the application,
    with a certain delay, until the message is received.

    Parameters
    ----------

    sleep_time : float, optional
        Time to wait before relaunching the application, in seconds, by default 1.

    message_key: str, optional
        Key for the message, by default "tool-init"

    Returns
    -------
    dict
        The payload received from the parent application.
    """

    # JavaScript code is loaded from file
    js_code_path = os.path.join(os.path.dirname(__file__), "listener.js")
    with open(js_code_path, "r", encoding="utf-8") as f:
        js_code = f.read()

    set_key_code_path = os.path.join(os.path.dirname(__file__), "set_key.js")
    with open(set_key_code_path, "r", encoding="utf-8") as f:
        set_key_code = f.read()

    # Execute the JavaScript code
    if "listener" not in st.session_state:
        st_javascript(set_key_code.replace("{message_key}", message_key))
        st_javascript(js_code)
        st.session_state.listener = True

    if "get_message_code" not in st.session_state:
        st.session_state.get_message_code = "window.parent.externalMessage;"

    payload: dict | int = st_javascript(st.session_state.get_message_code)

    if payload == 0:
        time.sleep(sleep_time)

        # Need to perform this "trick" to force an update in the component.
        # Otherwise, the correct value of externalMessage won't be retrieved.
        if st.session_state.get_message_code == "window.parent.externalMessage;":
            st.session_state.get_message_code = "window.parent.externalMessage; "
        else:
            st.session_state.get_message_code = "window.parent.externalMessage;"

        st.rerun()
        return {}  # Needed by mypy

    else:
        if not isinstance(payload, dict):
            raise TypeError("Payload must be a dictionary")

        return payload

import streamlit as st
from langgraph_backend import chatbot
from langchain_core.messages import HumanMessage


CONFIG = {
    "configurable": {
        "thread_id": "thread-1"
    }
}


# Initialize session state
if "message_history" not in st.session_state:
    st.session_state["message_history"] = []


# Display previous messages
for message in st.session_state["message_history"]:

    with st.chat_message(message["role"]):
        st.text(message["content"])


# Get user input
user_input = st.chat_input("Type here")


if user_input:

    # Display user message
    with st.chat_message("user"):
        st.text(user_input)

    # Store user message
    st.session_state["message_history"].append({
        "role": "user",
        "content": user_input
    })

    # Invoke LangGraph
    response = chatbot.invoke(
        {
            "message": [
                HumanMessage(content=user_input)
            ]
        },
        config=CONFIG
    )

    # Get AI response
    ai_message = response["message"][-1].content

    # Store AI response
    st.session_state["message_history"].append({
        "role": "assistant",
        "content": ai_message
    })

    # Display AI response
    with st.chat_message("assistant"):
        st.text(ai_message)

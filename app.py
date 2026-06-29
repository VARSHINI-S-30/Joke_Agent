import streamlit as st
from main import chat

# --------------------------------
# Page Config
# --------------------------------

st.set_page_config(
    page_title="😂 AI Joke Agent",
    page_icon="😂",
    layout="wide"
)

# --------------------------------
# Custom CSS
# --------------------------------

st.markdown("""
<style>

.main {
    background-color: #F8F9FA;
}

h1 {
    color: #FF6B35;
    text-align: center;
}

.stChatMessage {
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------
# Sidebar
# --------------------------------

with st.sidebar:

    st.title("😂 Joke Agent")

    st.markdown("---")

    st.write("### Features")

    st.success("✅ AI Powered")

    st.success("✅ JokeAPI")

    st.success("✅ Streamlit UI")

    st.success("✅ OpenRouter")

    st.markdown("---")

    st.write("### Try Asking")

    st.info("Tell me a joke")

    st.info("Tell me a programming joke")

    st.info("Tell me a dark joke")

    st.info("Tell me a spooky joke")

    st.info("Tell me a pun")

    st.markdown("---")

    if st.button("🗑 Clear Chat"):

        st.session_state.messages = []

        st.rerun()

# --------------------------------
# Header
# --------------------------------

st.title("😂 AI Joke Generator Agent")

st.markdown(
    """
    Welcome! Ask me for jokes in different categories.
    
    Available categories:
    - Programming 💻
    - Dark 🌑
    - Pun 😆
    - Spooky 👻
    - Random 🎲
    """
)

# --------------------------------
# Session State
# --------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# --------------------------------
# Display Previous Messages
# --------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

# --------------------------------
# Chat Input
# --------------------------------

prompt = st.chat_input("Ask me for a joke...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):

        st.markdown(prompt)

    with st.spinner("Finding a funny joke... 😂"):

        try:

            response = chat(prompt)

        except Exception as e:

            response = f"❌ Error: {str(e)}"

    with st.chat_message("assistant"):

        st.markdown(response)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

# --------------------------------
# Footer
# --------------------------------

st.markdown("---")

st.caption(
    "Built using Python • Streamlit • OpenRouter • JokeAPI"
)
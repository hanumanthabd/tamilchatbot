import streamlit as st # type: ignore
import time
from prompt import firePrompt  # Ensure prompt.py exists and firePrompt is defined

st.set_page_config(
    page_title='Tamil LLM',
    page_icon='💁🏻‍♂️',
    layout='wide',
    initial_sidebar_state='expanded'
)

# Initialize session state variables
if 'messages' not in st.session_state:
    st.session_state.messages = []

if 'temp' not in st.session_state:
    st.session_state.temp = 0.3  # Default temperature value

# Sidebar Configuration
with st.sidebar:
    st.markdown('## எனது கற்பனை திறனை தேர்வு செய்க !', unsafe_allow_html=True)
    st.session_state.temp = st.slider(
        label='Temperature', min_value=0.0, max_value=1.0, step=0.1, value=st.session_state.temp
    )
    st.image('sidebar_logo.png', use_column_width=True)
    st.image('cit_logo_small.png', use_column_width=True)

# Function to get avatar based on role
def getAvatar(role):
    return "tamil-llama-logo2.png" if role == 'assistant' else "cit_logo_small.png"

# Function to build chat context
def getContext():
    return "\n".join(f"role: {msg['role']} content: {msg['content']}" for msg in st.session_state.messages[:-1])

# Header
st.markdown('# :rainbow[Local] 🏠 :rainbow[Private] 🔒 :rainbow[தமிழ் AI Assistant] 🤖', unsafe_allow_html=True)
st.markdown('## :rainbow[Powered by தமிழ் 🦙🦙🦙] ', unsafe_allow_html=True)

# Assistant's initial message
with st.chat_message(name="assistant", avatar='tamil-llama-logo2.png'):
    st.markdown('#### Ask me anything! என்னிடம் தமிழிலும் உரையாடலாம்! 🙏🏻')

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(name=message["role"], avatar=getAvatar(message["role"])):
        st.markdown(f'{message["content"]}')

# User input handling
prompt = st.chat_input(placeholder="Chat with me. என்னிடம் தமிழிலும் உரையாடலாம்!")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message(name="user", avatar='cit_logo_small.png'):
        st.markdown(prompt)
    
    with st.chat_message(name='assistant', avatar='tamil-llama-logo2.png'):
        message_placeholder = st.empty()
        full_response = ""
        
        with st.spinner(text="Thinking... 💭💭💭"):
            raw_response = firePrompt(prompt, temp=st.session_state.temp)
            response = str(raw_response)
            
            # Simulate response typing effect
            for chunk in response.split():
                full_response += chunk + " "
                time.sleep(0.05)
                message_placeholder.markdown(full_response + "▌", unsafe_allow_html=True)
            
            message_placeholder.markdown(f'#### {full_response}', unsafe_allow_html=True)
            st.session_state.messages.append({"role": "assistant", "content": full_response})

#!/usr/bin/env python3
"""
WCC AI Learning Series - Session 1 Live Demo
Progressive Chatbot Building - Uncomment sections step by step!

INSTRUCTIONS FOR LIVE DEMO:
1. Start with SECTION 1 (already active)
2. To activate SECTION 2: Delete the triple quotes
3. To activate SECTION 3: Delete the triple quotes
4. To activate SECTION 4: Delete the triple quotes
5. To activate SECTION 5: Delete the triple quotes

Demo Flow:
1. Basic API call (START HERE - ACTIVE)
2. Add personality with system prompt (SECTION 2)
3. Add conversation memory (SECTION 3)
4. Explore model parameters (SECTION 4)
5. Create web interface (SECTION 5)
"""

import os
import google.generativeai as genai
from datetime import datetime


MODEL_ID = 'gemini-2.5-flash-lite'

# Load .env if available (dev convenience)
try:
    from dotenv import load_dotenv
    load_dotenv()
except Exception:
    pass


# =============================================================================
# SECTION 1: BASIC API CALL (START HERE - ALREADY ACTIVE)
# =============================================================================

print("🚀 WCC AI Learning Series - Session 1 Demo")
print("=" * 50)

# Configure Gemini API
api_key = os.getenv('GEMINI_API_KEY') or 'your-gemini-api-key-here'
genai.configure(api_key=api_key)

# Create the simplest possible model instance
model = genai.GenerativeModel(MODEL_ID)
'''
# Our first AI interaction!
print("STEP 1: Basic API Call")
print("-" * 30)

response = model.generate_content("What is Women Coding Community (WCC)?")
print(f"AI Response: {response.text}")
print("\n🎉 SUCCESS! You just talked to AI! 🎉\n")

# =============================================================================
# SECTION 2: ADD PERSONALITY
# =============================================================================

print("STEP 2: Adding Personality with System Prompts")
print("-" * 45)
'''
# Define WCC knowledge and personality
wcc_system_prompt = '''You are a helpful and enthusiastic assistant for the Women Coding Community (WCC).

ABOUT WCC:
- WCC is a vibrant community supporting women in technology
- We provide mentorship, networking, skill development workshops, and career guidance
- Our mission is to create an inclusive space for women to grow in tech careers
- We host regular events: technical workshops, mentorship sessions, networking meetups

PERSONALITY:
- Friendly, encouraging, and supportive
- Use inclusive language and be welcoming
- Be enthusiastic about WCC's mission
- Always try to connect answers back to community engagement

HOW TO HELP:
- Answer questions about WCC programs and events
- Encourage participation and community involvement
- Provide supportive advice for women in tech
- If you don't know something specific, suggest they check our Slack or website
'''

# Create model with system prompt
model_with_personality = genai.GenerativeModel(
    MODEL_ID,
    system_instruction=wcc_system_prompt
)

# Test questions with personality
test_questions = [
    "What is WCC?",
    "How can I join?", 
    "I'm new to coding, can WCC help me?",
    "What events do you have?"
]

for question in test_questions:
    print(f"\nQ: {question}")
    response = model_with_personality.generate_content(question)
    print(f"A: {response.text}")
    print("-" * 40)

print("\n🌟 PERSONALITY ADDED! Notice how responses are more WCC-focused! 🌟\n")


# =============================================================================
# SECTION 3: ADD CONVERSATION MEMORY
# =============================================================================

"""
print("STEP 3: Adding Conversation Memory")
print("-" * 35)

class WCCChatBot:
    def __init__(self):
        self.model = genai.GenerativeModel(
            MODEL_ID,
            system_instruction=wcc_system_prompt
        )
        self.conversation_history = []
    
    def chat(self, user_input):
        # Add user message to history
        self.conversation_history.append(f"User: {user_input}")
        
        # Create context with conversation history
        context = "\\n".join(self.conversation_history[-10:])  # Keep last 10 messages
        full_prompt = f"Conversation so far:\\n{context}\\n\\nUser: {user_input}\\n\\nAssistant:"
        
        # Generate response
        response = self.model.generate_content(full_prompt)
        
        # Add assistant response to history
        self.conversation_history.append(f"Assistant: {response.text}")
        
        return response.text

# Test conversation memory
chatbot = WCCChatBot()

print("Testing conversation memory:")
print("=" * 30)

response1 = chatbot.chat("Hi, I'm Sarah and I'm new to programming")
print(f"User: Hi, I'm Sarah and I'm new to programming")
print(f"Bot: {response1}\\n")

response2 = chatbot.chat("What programming language should I start with?")
print(f"User: What programming language should I start with?")
print(f"Bot: {response2}\\n")

response3 = chatbot.chat("Do you remember my name?")
print(f"User: Do you remember my name?")
print(f"Bot: {response3}\\n")

print("🧠 MEMORY ADDED! Bot remembers the conversation! 🧠\\n")
"""

# =============================================================================
# SECTION 4: EXPLORE MODEL PARAMETERS
# =============================================================================

"""
print("STEP 4: Understanding Model Parameters")
print("-" * 40)

# Test different temperature settings
def test_parameters():
    question = "Write a creative welcome message for new WCC members"
    
    print("🌡️ TEMPERATURE EXAMPLES:")
    print("=" * 25)
    
    temperatures = [0.0, 0.7, 1.5]
    
    for temp in temperatures:
        print(f"\\nTemperature: {temp}")
        print(f"Expected: {'Deterministic' if temp == 0.0 else 'Balanced' if temp == 0.7 else 'Very Creative'}")
        print("-" * 20)
        
        # Configure generation with specific temperature
        generation_config = genai.types.GenerationConfig(
            temperature=temp,
            max_output_tokens=100,
        )
        
        model_temp = genai.GenerativeModel(
            'gemini-pro',
            generation_config=generation_config
        )
        
        response = model_temp.generate_content(question)
        print(f"Response: {response.text}\\n")
    
    print("🎚️ TOP-P AND TOP-K EXAMPLES:")
    print("=" * 25)
    
    # Test Top-p (nucleus sampling)
    configs = [
        {"top_p": 0.3, "description": "Conservative (focused)"},
        {"top_p": 0.9, "description": "Balanced (recommended)"},
        {"top_k": 5, "description": "Top-5 tokens only"},
        {"top_k": 50, "description": "Top-50 tokens"}
    ]
    
    for config in configs:
        print(f"\\nConfig: {config}")
        print("-" * 30)
        
        generation_config = genai.types.GenerationConfig(
            temperature=0.7,
            max_output_tokens=80,
            **{k: v for k, v in config.items() if k != 'description'}
        )
        
        model_param = genai.GenerativeModel(
            'gemini-pro',
            generation_config=generation_config
        )
        
        response = model_param.generate_content("Describe WCC in one sentence")
        print(f"Response: {response.text}\\n")

# Run parameter tests
test_parameters()

print("⚙️ PARAMETERS EXPLORED! See how they change the responses! ⚙️\\n")
"""

# =============================================================================
# SECTION 5: STREAMLIT WEB INTERFACE
# =============================================================================


import streamlit as st

print("STEP 5: Creating Web Interface with Streamlit")
print("-" * 45)

# Streamlit Web App
def create_streamlit_app():
    '''
    To run this section:
    1. Delete the triple quotes around this entire section
    2. Save this file as 'wcc_demo.py'
    3. Run: streamlit run wcc_demo.py
    '''
    
    st.set_page_config(
        page_title="WCC Info Bot",
        page_icon="🌟",
        layout="centered"
    )
    
    st.title("🌟 WCC Info Bot")
    st.markdown("### Ask me anything about Women Coding Community!")
    
    # Sidebar with parameter controls
    st.sidebar.header("🎛️ Model Settings")
    temperature = st.sidebar.slider("Temperature", 0.0, 2.0, 0.7, 0.1)
    max_tokens = st.sidebar.slider("Max Tokens", 50, 500, 200, 50)
    top_p = st.sidebar.slider("Top-p", 0.1, 1.0, 0.9, 0.1)
    
    # Initialize session state for conversation history
    if "messages" not in st.session_state:
        st.session_state.messages = []
        st.session_state.messages.append({
            "role": "assistant", 
            "content": "Hello! I'm your WCC Info Bot. Ask me anything about the Women Coding Community! 🚀"
        })
    
    # Display conversation history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("What would you like to know about WCC?"):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Generate AI response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                # Configure model with user settings
                generation_config = genai.types.GenerationConfig(
                    temperature=temperature,
                    max_output_tokens=max_tokens,
                    top_p=top_p
                )
                
                model_ui = genai.GenerativeModel(
                    MODEL_ID,
                    generation_config=generation_config,
                    system_instruction=wcc_system_prompt
                )
                
                # Create conversation context
                context = "\\n".join([
                    f"{msg['role']}: {msg['content']}" 
                    for msg in st.session_state.messages[-5:]  # Last 5 messages
                ])
                
                full_prompt = f"Conversation context:\\n{context}\\n\\nUser: {prompt}"
                response = model_ui.generate_content(full_prompt)
                
                st.markdown(response.text)
        
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response.text})
    
    # Display current settings
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Current Settings:**")
    st.sidebar.write(f"🌡️ Temperature: {temperature}")
    st.sidebar.write(f"📝 Max Tokens: {max_tokens}")
    st.sidebar.write(f"🎯 Top-p: {top_p}")
    
    # Usage instructions
    with st.expander("💡 How to use this bot"):
        st.markdown('''
        **Try asking:**
        - What is WCC?
        - How can I join the community?
        - What events do you have?
        - I'm new to coding, can you help?
        - How can I volunteer or mentor?
        
        **Experiment with settings:**
        - 🌡️ **Temperature**: Higher = more creative responses
        - 📝 **Max Tokens**: Longer responses
        - 🎯 **Top-p**: Lower = more focused responses
        ''')

# Instructions for running Streamlit
print('''
🌐 TO CREATE WEB INTERFACE:
========================
1. Delete the triple quotes around SECTION 5 above
2. Save this file as 'wcc_demo.py'  
3. Install Streamlit: pip install streamlit
4. Run: streamlit run wcc_demo.py
5. Your browser will open with the web app!

📱 FEATURES OF THE WEB APP:
- Interactive chat interface
- Adjustable model parameters
- Conversation history
- Mobile-friendly design
''')

# Only run Streamlit if this section is uncommented and file is run with streamlit
if __name__ == "__main__" and "streamlit" in os.environ.get("_", ""):
    create_streamlit_app()


# =============================================================================
# DEMO COMPLETION
# =============================================================================

print("🎓 SESSION 1 DEMO COMPLETE!")
print("=" * 30)
print("""
WHAT WE BUILT TODAY:
✅ Basic API integration with Gemini
✅ AI personality with system prompts  
✅ Conversation memory management
✅ Model parameter experimentation
✅ Web interface with Streamlit

NEXT STEPS:
1. Uncomment sections one by one as you follow along
2. Experiment with different prompts and parameters
3. Customize the WCC knowledge base
4. Deploy your bot and share with the community!

HOMEWORK:
- Enhance your bot with more WCC information
- Try different model parameters
- Add your bot to GitHub
- Come to Session 2 with questions!

Happy coding! 💪🌟
""")

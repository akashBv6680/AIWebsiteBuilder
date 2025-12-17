import streamlit as st
import os
from website_agent import WebsiteAgent

st.set_page_config(
    page_title="AI Website Builder",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🌐 AI Website Builder")
st.markdown("""
### Create Amazing Websites with AI
Powered by Gemini 2.5 Flash & AI Agents
""")

# Initialize session state
if "generated_html" not in st.session_state:
    st.session_state.generated_html = None
if "generation_in_progress" not in st.session_state:
    st.session_state.generation_in_progress = False

# Sidebar configuration
with st.sidebar:
    st.header("⚙️ Configuration")
    st.info("API Key is configured via Streamlit Secrets")
    
    model_choice = st.radio(
        "Select Model:",
        ["Gemini 2.5 Flash"],
        help="Using Gemini 2.5 Flash for optimal performance"
    )

# Main input area
with st.container():
    col1, col2 = st.columns([3, 1])
    
    with col1:
        user_prompt = st.text_area(
            label="Describe your website:",
            placeholder="e.g., Create a modern portfolio website for a AI engineer with dark theme, project showcase, and contact form",
            height=120,
            help="Be specific about design, features, and layout preferences"
        )
    
    with col2:
        st.write("")
        st.write("")
        generate_btn = st.button(
            "🚀 Generate Website",
            use_container_width=True,
            disabled=st.session_state.generation_in_progress or not user_prompt
        )

# Process user request
if generate_btn and user_prompt:
    try:
        st.session_state.generation_in_progress = True
        
        with st.spinner("🤖 AI Agent is generating your website... This may take a minute."):
            # Initialize the website agent
            agent = WebsiteAgent()
            
            # Generate the website
            st.session_state.generated_html = agent.generate_website(user_prompt)
        
        st.session_state.generation_in_progress = False
        st.success("✅ Website generated successfully!")
        
    except Exception as e:
        st.session_state.generation_in_progress = False
        st.error(f"❌ Error generating website: {str(e)}")
        st.info("Please check your API key configuration and try again.")

# Display generated website
if st.session_state.generated_html:
    st.divider()
    st.header("📱 Preview")
    
    # Display the HTML in an iframe
    st.components.v1.html(st.session_state.generated_html, height=800, scrolling=True)
    
    # Download button
    col1, col2 = st.columns(2)
    
    with col1:
        st.download_button(
            label="📥 Download HTML",
            data=st.session_state.generated_html,
            file_name="website.html",
            mime="text/html",
            use_container_width=True
        )
    
    with col2:
        if st.button("🔄 Generate Another Website", use_container_width=True):
            st.session_state.generated_html = None
            st.rerun()

# Footer
st.divider()
st.markdown("""
<div style='text-align: center; color: gray; font-size: 12px;'>
    Powered by Streamlit & Gemini 2.5 Flash API | AI Website Builder v1.0
</div>
""", unsafe_allow_html=True)

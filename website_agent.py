import google.generativeai as genai
import streamlit as st
import re
from typing import Optional

class WebsiteAgent:
    """
    AI Agent for generating beautiful websites using Gemini 2.5 Flash.
    This agent takes user prompts and generates complete HTML/CSS websites.
    """
    
    def __init__(self):
        """Initialize the WebsiteAgent with Gemini API."""
        try:
            # Get API key from Streamlit secrets
            api_key = st.secrets.get("GEMINI_API_KEY")
            
            if not api_key:
                raise ValueError(
                    "GEMINI_API_KEY not found in Streamlit secrets. "
                    "Please add it to .streamlit/secrets.toml or Streamlit Cloud secrets."
                )
            
            genai.configure(api_key=api_key)
            self.model = genai.GenerativeModel(
                model_name="gemini-2.5-flash",
                generation_config=genai.types.GenerationConfig(
                    temperature=0.7,
                    top_p=0.95,
                    top_k=40,
                    max_output_tokens=8000,
                )
            )
        except Exception as e:
            st.error(f"Failed to initialize Gemini API: {str(e)}")
            raise
    
    def _create_system_prompt(self) -> str:
        """Create a comprehensive system prompt for website generation."""
        return """You are an expert web developer and UI/UX designer. Your task is to generate beautiful, modern, and functional HTML5 websites based on user requirements.

IMPORTANT INSTRUCTIONS:
1. Generate ONLY valid HTML5 code with embedded CSS and JavaScript
2. Do NOT include any markdown, explanations, or code blocks (no ```html or backticks)
3. Start directly with <!DOCTYPE html>
4. Include comprehensive styling using <style> tags
5. Make the design modern, responsive, and visually appealing
6. Use CSS Grid or Flexbox for layouts
7. Include smooth animations and transitions
8. Ensure proper color schemes and typography
9. Add interactive elements where appropriate
10. Make it mobile-responsive with media queries
11. Include proper meta tags and structured content
12. Do NOT include external dependencies - everything must be self-contained
13. Use only modern CSS3 features
14. Include proper accessibility features
15. Output ONLY the HTML code, nothing else

Generate a complete, ready-to-use website HTML file."""
    
    def generate_website(self, user_prompt: str) -> Optional[str]:
        """
        Generate a complete website based on user prompt using Gemini 2.5 Flash.
        
        Args:
            user_prompt (str): Description of the website to generate
            
        Returns:
            Optional[str]: Generated HTML code or None if generation fails
            
        Raises:
            ValueError: If the prompt is empty or invalid
        """
        if not user_prompt or not user_prompt.strip():
            raise ValueError("User prompt cannot be empty")
        
        try:
            # Create enhanced prompt with specific instructions
            enhanced_prompt = f"""
            User Request: {user_prompt}
            
            Requirements:
            1. Create a beautiful, modern website based on the above request
            2. Generate ONLY HTML5 code with embedded CSS - no external files
            3. Make it fully responsive and mobile-friendly
            4. Include smooth animations and modern design principles
            5. Use professional color schemes and typography
            6. Ensure all content is properly structured
            7. Start with <!DOCTYPE html> and include all necessary tags
            8. Do NOT include any explanations or markdown - only raw HTML
            9. Make it visually stunning and professional
            10. Include interactive elements if appropriate
            
            Generate the complete HTML code now:
            """
            
            # Call Gemini 2.5 Flash to generate website
            response = self.model.generate_content(
                enhanced_prompt,
                stream=False
            )
            
            if not response or not response.text:
                raise ValueError("No response received from Gemini API")
            
            # Extract HTML from response
            html_content = response.text.strip()
            
            # Remove markdown code blocks if present
            html_content = re.sub(r'^```html\s*', '', html_content)
            html_content = re.sub(r'^```\s*', '', html_content)
            html_content = re.sub(r'\s*```$', '', html_content)
            
            # Validate that it starts with DOCTYPE
            if not html_content.lower().startswith('<!doctype'):
                raise ValueError("Generated content does not appear to be valid HTML")
            
            return html_content
            
        except Exception as e:
            st.error(f"Error generating website: {str(e)}")
            raise
    
    def optimize_html(self, html_content: str) -> str:
        """
        Optimize the generated HTML for better performance.
        
        Args:
            html_content (str): Raw HTML content
            
        Returns:
            str: Optimized HTML content
        """
        try:
            # Add viewport meta tag if missing
            if '<meta name="viewport"' not in html_content:
                html_content = html_content.replace(
                    '<head>',
                    '<head>\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">'
                )
            
            # Add charset if missing
            if '<meta charset' not in html_content:
                html_content = html_content.replace(
                    '<head>',
                    '<head>\n    <meta charset="UTF-8">'
                )
            
            return html_content
        except Exception as e:
            st.warning(f"Could not optimize HTML: {str(e)}")
            return html_content


def get_website_agent() -> WebsiteAgent:
    """
    Factory function to get or create WebsiteAgent instance.
    Uses Streamlit caching for efficiency.
    
    Returns:
        WebsiteAgent: Initialized WebsiteAgent instance
    """
    @st.cache_resource
    def _create_agent():
        return WebsiteAgent()
    
    return _create_agent()

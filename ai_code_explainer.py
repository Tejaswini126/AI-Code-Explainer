import streamlit as st
import requests
import json # Import json to handle JSON serialization/deserialization

# --- Configuration for Gemini API ---
GEMINI_MODEL_NAME = "gemini-1.5-flash"

# !!! SECURITY WARNING !!!
# Pasting your API key directly here is NOT recommended for production or public code.
# This key will be visible to anyone who accesses your code.
# For secure deployment, always use environment variables (e.g., os.getenv("GEMINI_API_KEY"))
# or Streamlit Secrets.
MY_GEMINI_API_KEY = ".." # <<< PASTE YOUR API KEY HERE WHICH IS MENTIONED IN THE DOCUMENT >>>

# --- Gemini API Endpoint ---
# IMPORTANT: Ensure the model name in the URL matches GEMINI_MODEL_NAME
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{GEMINI_MODEL_NAME}:generateContent?key={MY_GEMINI_API_KEY}"

# --- Streamlit UI setup ---
st.set_page_config(page_title="AI Code Explainer", page_icon="🤖", layout="centered")
st.title("🤖 AI Code Explainer")
st.markdown("""
Enter any code snippet and get a beginner-friendly explanation using Gemini AI.
""")

# Language selector
language = st.selectbox(
    "Choose Programming Language:",
    ["Python", "JavaScript", "C++", "Java", "Go", "Ruby", "PHP", "Swift", "Kotlin", "Rust", "TypeScript", "Other"]
)

# Code input area
user_code = st.text_area(
    "Paste your code here",
    height=300,
    placeholder=f"Example for {language}:\n\n"
                     + ("for i in range(5): print(i)" if language == "Python" else "")
                     + ("function greet() { console.log('Hello!'); }" if language == "JavaScript" else "")
                     + ("int main() { std::cout << 'Hello World!'; return 0; }" if language == "C++" else "")
                     + ("class MyClass { public static void main(String[] args) { System.out.println(\"Hello\"); } }" if language == "Java" else "")
)

# Action button
if st.button("Explain Code", use_container_width=True):
    if not user_code.strip():
        st.warning("⚠ Please enter some code to explain.")
    else:
        with st.spinner("Generating explanation..."):
            # Ensure API key is provided
            if not MY_GEMINI_API_KEY or MY_GEMINI_API_KEY == "YOUR_PASTED_GEMINI_API_HERE":
                 st.error("❌ API Key is missing or not replaced. Please paste your Gemini API key in the script.")
                 st.stop()

            # Consolidated system prompt for a single explanation style
            prompt_text = (
                f"Explain this {language} code to a beginner, focusing on clarity and simplicity. "
                "Break down complex parts. Provide an explanation in a friendly and easy-to-understand manner. "
                "Do NOT include the original code or code snippets in your output. "
                "Do NOT include generic introductions about the programming language itself; "
                "jump straight into explaining the provided code:\n\n"
                f"{user_code}\n"
            )

            headers = {
                "Content-Type": "application/json"
            }
            payload = {
                "contents": [
                    {
                        "parts": [
                            {"text": prompt_text}
                        ]
                    }
                ],
                "generationConfig": {
                    "temperature": 0.7, # Adjust creativity
                    "maxOutputTokens": 1000 # Max length of the explanation
                }
            }

            try:
                response = requests.post(GEMINI_API_URL, headers=headers, json=payload, timeout=60) # Increased timeout
                response.raise_for_status() # This will raise an HTTPError for bad responses (4xx or 5xx)

                response_data = response.json()
                explanation = ""
                if "candidates" in response_data and response_data["candidates"]:
                    for candidate in response_data["candidates"]:
                        if "content" in candidate and "parts" in candidate["content"]:
                            for part in candidate["content"]["parts"]:
                                if "text" in part:
                                    explanation += part["text"] + "\n"

                if explanation.strip():
                    st.success("✅ Explanation:")
                    st.markdown(explanation.strip())
                else:
                    st.error("❌ Gemini returned an empty or unparseable explanation. Please try a different code snippet or prompt.")
                    st.json(response_data) # Show raw response for debugging

            except requests.exceptions.RequestException as e:
                # Catch any request-related errors (ConnectionError, HTTPError, Timeout)
                st.error(f"❌ An error occurred during API request: {e}")
                st.info("Please check your internet connection, API key, and the Gemini API status.")
                if hasattr(e, 'response') and e.response is not None:
                    st.code(e.response.text, language="json") # Show API error response if available
            except json.JSONDecodeError as e:
                st.error(f"❌ Error decoding JSON response from API: {e}")
                st.info("The API might have returned malformed data.")
            except Exception as e:
                st.error(f"❌ An unexpected error occurred: {str(e)}")

# Footer or additional info (optional)
st.markdown("---")
st.markdown("Developed with Streamlit and Google Gemini AI (using requests).")

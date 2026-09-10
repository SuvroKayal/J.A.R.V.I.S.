import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Initialize native Gemini client
client = genai.Client(api_key=api_key) if api_key else None

def ask_jarvis(command):
    if not client:
        return "Boss, your Gemini API key is missing."

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=command,
            config=types.GenerateContentConfig(
                system_instruction=(
                    "You are JARVIS, a sophisticated personal AI assistant. "
                    "Address the user as Boss when appropriate. "
                    "Give clear, concise, complete, and direct answers in 2 to 4 sentences. "
                    "Use plain conversational English without asterisks, markdown symbols, or special formatting "
                    "because your responses are spoken aloud using text to speech. "
                    "Never mention ChatGPT, Google, or OpenAI. You are JARVIS."
                ),
                temperature=0.7,
                max_output_tokens=1000,
                # Disables Automatic Function Calling (AFC) to remove the SDK warning
                automatic_function_calling=types.AutomaticFunctionCallingConfig(
                    disable=True
                )
            )
        )

        message = response.text

        if message:
            clean_message = message.replace("*", "").replace("#", "").replace("- ", "").strip()
            return clean_message
        else:
            return "Sorry Boss, I could not generate a response."

    except Exception as e:
        print(f"API Error: {e}")
        return "I encountered an API error, Boss."
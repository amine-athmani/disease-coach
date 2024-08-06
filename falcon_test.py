import openai
from dotenv import load_dotenv
import os

AI71_BASE_URL = "https://api.ai71.ai/v1/"
load_dotenv()
AI71_API_KEY = os.getenv("AI71_API_KEY")

client = openai.OpenAI(
    api_key=AI71_API_KEY,
    base_url=AI71_BASE_URL,
)

# Simple invocation:
print(client.chat.completions.create(
    model="tiiuae/falcon-180b-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"},
    ],
))

# Streaming invocation:
for chunk in client.chat.completions.create(
    messages=[{
      "role": "user", 
      "content": "Write a song about a ginger-colored fish on the moon."
    }],
    model="tiiuae/falcon-180b-chat",
    stream=True,
):
    delta_content = chunk.choices[0].delta.content
    if delta_content:
        print(delta_content, sep="", end="", flush=True)
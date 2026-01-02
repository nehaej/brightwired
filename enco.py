from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENROUTER_API_KEY"),
)
def chat(user_prompt):
    try:
        completion = client.chat.completions.create(
            extra_headers={
                "HTTP-Referer": "", 
                "X-Title": "", 
            },
            model="mistralai/devstral-2512:free",
            max_tokens=120,   
            temperature=0.4,  
            messages=[
                {
                    "role": "user",
                    "content": f"Neurodivergent user says {user_prompt}. Give them motivation. Keep responses SHORT and SIMPLE. NO unsolicited advice"
                }
            ]
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error:{e}")
        return "Something went wrong. Try again later"


from openai import OpenAI
import os

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
def analyze(articles):
   text = ""
   for a in articles:
       text += f"{a['title']} {a['url']}\n"
   prompt = f"""
Analyze these articles and extract
the top 5 technology trends related to:

OS platform
Google Android
Smart TV
Connected TV (CTV)
web engine
Media Stack and Streaming Technology
device platform
AI agents

Articles:
{text}

Return:
Trend
Explanation
Reference link
"""

   response = client.chat.completions.create(
       model="gpt-4o-mini",
       messages=[{"role":"user","content":prompt}]
   )
   return response.choices[0].message.content

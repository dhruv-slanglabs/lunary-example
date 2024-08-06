from fastapi import FastAPI
import openai
import lunary
import google.generativeai as genai
import uuid
from dotenv import load_dotenv
import os




load_dotenv()


GOOGLE_API_KEY=os.environ['GOOGLE_API_KEY']
genai.configure(api_key=GOOGLE_API_KEY)

app = FastAPI()

def call_llm(llm_model: str, user_input: str) -> str:
    run_id = uuid.uuid4()
    lunary.track_event(
      run_type="llm",
      event_name="start",
      run_id=run_id,
      name=llm_model,
      input=user_input
    )
    if llm_model == 'gpt-4o':

        openai_client = openai.OpenAI(
        api_key=os.environ['OPENAI_API_KEY'], 
        )
        # lunary.monitor(openai_client)
        chat_completion = openai_client.chat.completions.create(
            model="gpt-4o", 
            messages=[{"role": "user", "content": user_input}]  
        )
        response = chat_completion.choices[0].message.content
    else:
        model = genai.GenerativeModel('gemini-1.5-flash')

        response = model.generate_content(user_input)
        response = response.text

    lunary.track_event(
      run_type="llm",
      event_name="end",
      run_id=run_id,
      output=response,
    )
    return response

@app.post("/assistants/openai")
async def endpoint1(user_input: str):
    with lunary.tags(["openai"]):
        response = call_llm('gpt-4o', user_input)
    return {"message": response}

@app.post("/assistants/gemini")
async def endpoint2(user_input: str):
    with lunary.identify('user123', user_props={"email": "email@example.org"}):
        response = call_llm('gemini-1.5-flash', user_input)
    return {"message": response}




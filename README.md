# Lunary example

This is a simple FastAPI application with two endpoints to call on openai and the gemini LLM models. The purpose is to show how Lunary can be integrated with this server to monitor all LLM calls. 


# Instructions

To run the script, you will need a .env file with the correct API keys and Lunary information. A sample .env file is shown below

```
OPENAI_API_KEY=...
GOOGLE_API_KEY=...
LUNARY_PUBLIC_KEY=...
LUNARY_API_URL=http://localhost:3333
LUNARY_VERBOSE=True #for debugging
```
This example uses a self hosted version of lunary, with the server running on port 3333.
To self host lunary, follow the instructions here: https://github.com/lunary-ai/lunary


Run the server via:
`uvicorn main:app --host 0.0.0.0 --port 4000 --reload`
Port 4000 is used in this case because the default port 8080 was being used by lunary's frontend

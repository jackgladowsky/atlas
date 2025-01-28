from openai import OpenAI
from pydantic import BaseModel, Field

import os
from dotenv import load_dotenv

load_dotenv()

class ChatModel:
    def __init__(self, model: str, system_prompt: str = "You are a helpful assistant named ATLAS. Respone with text and/or emojis"):
        self.model = model
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        # self.client = OpenAI(api_key=self.api_key, base_url="https://openrouter.ai/api/v1")
        self.client = OpenAI(api_key="none", base_url="http://172.31.128.1:1234/v1")
        self.messages = []

        if not self.messages:
            self.messages = [{"role": "system", "content": system_prompt}]
        

    def __call__(self, request: str):
        try:
            # add the user prompt to the messages list
            self.messages.append({"role": "user", "content": request})

            # create the chat request
            response = self.client.chat.completions.create(model=self.model, messages=self.messages)

            # add the response to the messages list
            self.messages.append({"role": "system", "content": response.choices[0].message.content})
            
            # return the response
            return response.choices[0].message.content
        except Exception as e:
            return f"An error occurred: {e}"
        
    def call(self, request: str):
        return self(request)
    
    def run(self):
        loop = True
        os.system("clear")
        print("Welcome to ATLAS chat. Type 'exit' to quit.")

        while loop:
            user_input = input("> ")
            if user_input == "exit":
                print("Goodbye!")
                loop = False
            else:
                response = self.call(user_input)
                print(f"ATLAS: {response}")
from json import loads
from datetime import datetime
from flask import Flask, request, jsonify
from g4f.client import Client

class Backend_Api:
    def __init__(self, app,config) -> None:
        self.app = app
        self.client = Client(provider="PerplexityLabs")
        self.routes = {
            '/backend-api/v2/conversation': {
                'function': self._conversation,
                'methods': ['POST']
            }
        }

    def _conversation(self):
        try:
            _conversation = request.json['meta']['content']['conversation']
            prompt = request.json['meta']['content']['parts'][0]
            current_date = datetime.now().strftime("%Y-%m-%d")
            system_message = f'You are PerplexityLabs AI ChatBot, a large language model trained by PerplexityLabs. Strictly follow the user’s instructions. Knowledge cutoff: 2021-09-01 Current date: {current_date}'

            history = [
                {'role': 'system', 'content': "Hello! How can I help you today?"},
                {'role': 'system', 'content': "English only please. I am not able to understand other languages."},
                {'role': 'system', 'content': system_message}
            ] + _conversation + [prompt]

            response = self.client.chat.completions.create(
                model="mixtral-8x7b-instruct",
                messages=history
            )
            

            response_content = response.choices[0].message.content
            if '$@$v=undefined-rv2$@' in response_content:
                response_content = response_content.replace('$@$v=undefined-rv2$@', '')
            return (response_content), 200

        except Exception as e:
            print(e)
            return {
                'success': False,
                "error": f"An error occurred: {str(e)}"
            }, 400



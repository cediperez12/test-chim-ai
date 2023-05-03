from flask import Flask, request
import json
import os
from langchain import OpenAI
from llama_index import GPTSimpleVectorIndex

os.environ['OPENAI_API_KEY'] = "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"

ai = GPTSimpleVectorIndex.load_from_disk('index.json')

app = Flask(__name__)

@app.route('/')
def index():
    sample_input = "Say hello to everyone!"
    response = ai.query(sample_input)

    return json.dumps({
      'query': sample_input,
      'response': response.response
    })

@app.route('/askchim', methods=['GET'])
def ask_chim():
    query = request.args.get('query')
    response = ai.query(query)

    print(f"query: {query}")
    print(f"response: {response.response}")

    return json.dumps({
      'query': query,
      'response': response.response
    })

app.run(host='0.0.0.0', port=81)
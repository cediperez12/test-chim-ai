from flask import Flask, request
from flask_cors import CORS
import json
import os
from langchain import OpenAI
from llama_index import StorageContext, load_index_from_storage

# Set your API here.
# os.environ['OPENAI_API_KEY'] = "<PUT YOUR API KEY HERE>"

storage_context = StorageContext.from_defaults(persist_dir="index_storage")
index = load_index_from_storage(storage_context)
ai = index.as_query_engine()

app = Flask(__name__)
CORS(app)

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

    reply = response.response

    return json.dumps({
      'query': query,
      'response': reply[1:len(reply)]
    })
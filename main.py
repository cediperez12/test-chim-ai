from flask import Flask, request
import json
import os
from langchain import OpenAI
from llama_index import StorageContext, load_index_from_storage

os.environ['OPENAI_API_KEY'] = "<ENTER YOUR API KEY HERE>"

storage_context = StorageContext.from_defaults(persist_dir="index_storage")
index = load_index_from_storage(storage_context)
ai = index.as_query_engine()

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
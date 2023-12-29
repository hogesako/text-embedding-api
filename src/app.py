from fastembed.embedding import FlagEmbedding as Embedding
from typing import List
import numpy as np

from flask import Flask, request
from waitress import serve
from werkzeug.exceptions import BadRequest
import os

model_loaded = False
app = Flask(__name__)
model_name = os.environ.get('MODEL_NAME', 'intfloat/multilingual-e5-large')

print("start model loading")
embedding_model = Embedding(model_name, max_length=512) 
model_loaded = True
print("finish model loading")

@app.route('/', methods=["GET"])
def index():
   return 'curl -X POST -H "Content-Type: application/json" -d \'{"sentence":"test-sentence"}\' http://localhost:9500/vectorize'

@app.route('/vectorize', methods=["POST"])
def vectorize():
    sentence = request.json['sentence']
    if sentence == None:
        raise BadRequest
    if model_loaded == False:
        raise BadRequest
    documents: List[str] = [sentence]
    embeddings: List[np.ndarray] = list(embedding_model.embed(documents))
    return embeddings[0].tolist()

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=9500)
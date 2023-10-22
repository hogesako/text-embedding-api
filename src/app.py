from sentence_transformers import SentenceTransformer
from flask import Flask, request
from waitress import serve
from werkzeug.exceptions import BadRequest
import os

app = Flask(__name__)
model_name = os.environ.get('MODEL_NAME', 'intfloat/multilingual-e5-small')

print("start model loading")
model = SentenceTransformer(model_name)
print("finish model loading")

@app.route('/', methods=["GET"])
def index():
   return 'curl -X POST -H "Content-Type: application/json" -d \'{"sentence":"test-sentence"}\' http://localhost:9500/vectorize'

@app.route('/vectorize', methods=["POST"])
def vectorize():
    sentence = request.json['sentence']
    if sentence == None:
        raise BadRequest
    return model.encode(sentence, normalize_embeddings=True).tolist()

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=9500)
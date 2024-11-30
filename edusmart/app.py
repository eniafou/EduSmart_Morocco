from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.utils import *

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

@app.route('/submit', methods=['POST'])
def submit_answers():
    data = request.json
    data = generate_customized_cours(data)
    return jsonify(data)




@app.route('/create_general_qcm', methods=['POST'])
def create_general_qcm():
    data = request.json
    data = mapping_front_back_meta_form(data)
    qcm_data = generate_general_qcm_from_cours_parties(**data)
    return jsonify(qcm_data["data"])

if __name__ == '__main__':
    app.run(debug=True)



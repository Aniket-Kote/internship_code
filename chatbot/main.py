from flask import Flask, request, jsonify
from ai_code import single_message_instruct
import json
from pymongo.errors import PyMongoError
from db import insert_data

app = Flask(__name__)
port = 8080

@app.route('/', methods=['POST'])
@app.route('/question', methods=['POST'])
def ask_question():
    try:
        data = request.get_json()

        # Validate the incoming JSON payload
        question = data.get('question')
        if not question:
            return jsonify({"error": "Invalid JSON payload: 'question' is required"}), 400

        # Process the question using the AI logic
        ai_response = single_message_instruct(question)
        r = json.loads(ai_response)

        # Extract the response content
        response_data = r["choices"][0]["message"]["content"]
        document = {"question": question, "response": response_data}

        # Insert the document into MongoDB
        if not insert_data(document):
            raise Exception("Failed to insert data into MongoDB")
        else:
            # return jsonify({"result": "Data inserted successfully", "answer": {"question": question, "response": response_data}}), 200
            return document,200

    except PyMongoError as e:
        return jsonify({"error": "Database operation failed", "details": str(e)}), 500
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=port, host='0.0.0.0')
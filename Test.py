from flask import Flask, request, jsonify
from generate_questions import generate_question  # Import the function

app = Flask(__name__)

@app.route('/ask', methods=['POST'])
def ask_question():
    data = request.json
    student_input = data.get('input', '')
    
    if not student_input:
        return jsonify({"error": "No input provided"}), 400
    
    question = generate_question(student_input)
    
    return jsonify({"socratic_question": question})

if __name__ == '__main__':
    app.run(debug=True)

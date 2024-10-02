import openai

# Set up OpenAI API key
openai.api_key = 'YOUR_OPENAI_API_KEY'

# Function to generate Socratic questions
def generate_question(student_input):
    prompt = f"You're a Socratic teacher guiding a student on data structures, specifically sorting algorithms. \
    The student has input: '{student_input}'. Guide them to discover the problem by asking insightful, open-ended questions."

    response = openai.Completion.create(
        engine="text-davinci-003",  # GPT-4 API
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )
    
    question = response.choices[0].text.strip()
    return question

# Sample student input
student_input = "My sorting algorithm is timing out on large input."
socratic_question = generate_question(student_input)
print(f"Socratic Question: {socratic_question}")

from flask import Flask, request, jsonify, send_from_directory
from together import Together
import textwrap

app = Flask(__name__)

# Initialize the Together client
client = Together(api_key="e7a501a28a46881b3559d8599dd96cf6bb100fe303fc4cfa67f02c023b193d41")

PROMPT_TEMPLATES = {
    '1': "Provide structured information about the importance of blood donation in 100 words.",
    '2': "Explain the eligibility criteria for donating blood in 100 words, clearly organized.",
    '3': "Describe the step-by-step process of blood donation in 100 words.",
    '4': "Outline pre and post-donation care tips in 100 words, formatted properly.",
    '5': "Summarize different blood groups and their compatibility in 100 words.",
    '6': "List emergency contact details for blood banks in 100 words.",
    '7': "Debunk common myths and provide blood donation facts in 100 words.",
    '8': "Highlight the benefits of regular blood donation in 100 words.",
    '9': "[Custom] User-defined prompt."
}

def generate_response(category, custom_prompt=None):
    """ Generates a structured AI response limited to 100 words. """
    
    # Construct prompt
    if category == '9' and custom_prompt:
        prompt_text = f"Write a structured response in exactly 100 words: {custom_prompt}"
    else:
        prompt_text = PROMPT_TEMPLATES.get(category, "Invalid category")

    messages = [{"role": "user", "content": prompt_text}]
    
    # Call Together API for response generation
    completion = client.chat.completions.create(
        model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
        messages=messages
    )

    response_text = completion.choices[0].message.content.strip() if completion.choices else "No response generated."

    # Ensure response is exactly 100 words
    words = response_text.split()
    if len(words) > 100:
        response_text = " ".join(words[:100])  # Trim to 100 words

    # Format response properly
    return "\n\n".join(textwrap.wrap(response_text, width=80))

@app.route("/")
def serve_frontend():
    """ Serves the frontend UI. """
    return send_from_directory(".", "index.html")

@app.route("/get-response", methods=["POST"])
def get_bot_response():
    """ Handles requests from the frontend and returns AI-generated responses. """
    
    data = request.json
    category = data.get("category")
    custom_prompt = data.get("custom_prompt", "")

    response = generate_response(category, custom_prompt)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True, port=5001)

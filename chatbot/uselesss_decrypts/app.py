from flask import Flask, render_template, jsonify, request
from together import Together

app = Flask(__name__)

# Initialize the Together client
client = Together(api_key='e7a501a28a46881b3559d8599dd96cf6bb100fe303fc4cfa67f02c023b193d41')

# Prompt templates for categories
PROMPT_TEMPLATES = {
    '1': "Write a hilariously absurd excuse for why someone was late to work because of a pet raccoon.",
    '2': "Make up a funny excuse for missing an assignment involving aliens.",
    '3': "Write a ridiculous reason for forgetting an anniversary, preferably involving talking animals or time travel.",
    '4': "Give a silly excuse for not attending a friend's party because of a highly unusual reason.",
    '5': "Create a bizarre reason for avoiding household chores, involving imaginary creatures."
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate-excuse', methods=['POST'])
def generate_excuse():
    try:
        data = request.json
        
        # Handle custom prompt
        if 'customPrompt' in data:
            custom_prompt = data['customPrompt']
            prompt = f"Generate a creative and funny excuse for the following situation: {custom_prompt}.ust use 1 excuse, make it short and crazy,make it more comedy,Generate an excuse that fits into the situation and implement sarcasm"
        # Handle category-based prompt
        elif 'category' in data:
            category = data['category']
            prompt = PROMPT_TEMPLATES.get(category)
        else:
            return jsonify({'error': 'Invalid request. Please provide category or custom prompt.'}), 400

        # Generate excuse using Together API
        messages = [{"role": "user", "content": prompt}]
        
        completion = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
            messages=messages
        )

        if completion and hasattr(completion, 'choices') and len(completion.choices) > 0:
            excuse = completion.choices[0].message.content.strip()
            return jsonify({'excuse': excuse})
        
        return jsonify({'error': 'No excuse generated. Please try again.'}), 500

    except Exception as e:
        print(f"Error: {str(e)}")  # For debugging
        return jsonify({'error': 'An error occurred while generating the excuse.'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)  # Change port to 8080
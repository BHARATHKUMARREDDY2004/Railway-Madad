from flask import Flask, jsonify, render_template, request
import google.generativeai as genai
import os

genai.configure(api_key= "Google API Key")
Problems = {
    'Food': [],
    'Cleanines': [],
    'Electrical': [],
    'Emergency': [],
    'Disterbance': []
}

# Initialize Flask app
app = Flask(__name__)

# Main route for rendering the chat interface
@app.route('/')
def home():
    return render_template('index.html')

# Flask route taking input from user and to give output
@app.route('/chat', methods=['POST'])
def chat():
    # Process user input
    message = request.json['message']
    
    # Set the context for Gemini (the problem domain)
    context = """
    Rail Madad is a platform where passengers file complaints regarding train journeys. The system handles various complaint types including:
    1. Coach cleanliness
    2. Damage to seats, windows, or train infrastructure
    3. Staff behavior and misconduct
    4. Delays or disruptions in service
    5. Safety concerns, accidents, or emergencies

    Users may also submit images, videos, or audio files related to these issues. The AI should automatically categorize complaints, detect urgency, and respond appropriately based on the type of complaint and its content.

    Please provide a response based on the type of complaint the user is making, offer any necessary actions, and ensure the user feels supported and informed.
    if user whishes like thank you or done after complaint filing, please respond with "You're welcome! If you have any other questions or concerns, feel free to ask."
    if user asks irrelevant questions, please respond with "I'm sorry, I can only assist with railway-related problems. If you have any other questions or concerns, feel free to ask."
    if user asks for general information about the railway system, please respond with a brief overview of the services provided by the railway system.
    if user asks for the status of a train, please respond with "I'm sorry, I can't provide real-time train status information. You can check the status of your train on the official railway website or app."
    if user asks for the location of a train, please respond with "I'm sorry, I can't provide real-time train location information. You can check the location of your train on the official railway website or app."
    if user asks for the schedule of a train, please respond with "I'm sorry, I can't provide real-time train schedule information. You can check the schedule of your train on the official railway website or app."

    ask user to describe the problem and train details and coach details and evidence if any and then.

       """

    # Predict response using the context and user message
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(f"{context} {message}")

    say = model.generate_content(f"say user provied problem or not in message : {message} if provide give output as 'yes' else 'no' in simple string format.")

    if say.text == 'yes':
        category = model.generate_content(f"categorize the problem or complaint related to ['Food', 'Cleanines', 'Electrical', 'Emergency', 'Disterbance'] {message} and return the category in simple string format as in list.")
        print("-----------------------------------------------------------------------------")
        print(category.text)

        problem = model.generate_content("Retrive the information from user message, Train No, Coach No, Problem in" + message + "\n and return the information in {'Train No': <tarin no>, 'Coach No': <coach no>, 'Problem': <problem>} with no information not even a single word more, Just return object")

        if category.text in Problems.keys():
            Problems[category].append(problem.text)
    # Return response
    print(Problems)
    return jsonify({'response': response.text})

if __name__ == '__main__':
    app.run(debug=True)

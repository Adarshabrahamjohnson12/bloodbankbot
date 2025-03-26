[

](https://drive.google.com/file/d/11z_Pr8KBwbKc6inN_NfQ6keKgP8ZLzcM/view?usp=sharing)

<img width="1280" alt="readme-banner" src="https://github.com/user-attachments/assets/35332e92-44cb-425b-9dff-27bcf1023c6c">

# Excuse_me 🎯


## Basic Details
### Team Name: Decrypts


### Team Members
- Team Lead: Adarsh_Abraham - TIST
- Member 2: ANAN_M_BINOJ - TIST
- Member 3: ARJUN_T_AKHILESH - TIST

### Project Description
The Peter Griffin Excuse Generator is a humor-driven web app that generates witty, over-the-top excuses for various situations inspired by the iconic character Peter Griffin. Users can choose from preset categories like "Late to Work" or "Missed Assignment," or input a custom prompt to receive a unique, sarcastic excuse. Featuring a playful interface, voice playback, and plenty of comedic flair, this app delivers a quick laugh and a perfect "Peter-approved" excuse for every occasion!

### The Problem (that doesn't exist)
Have you ever found yourself in desperate need of a hilarious, wildly implausible excuse for being late, forgetting an important date, or dodging an event? In a world filled with unimaginative explanations, we're solving the (nonexistent) problem of excuse blandness. With the Peter Griffin Excuse Generator, you’ll never again have to settle for a boring “I forgot.” Instead, let Peter himself supply you with the most outrageous, unforgettable excuses, perfect for when reality just doesn’t cut it!

### The Solution (that nobody asked for)

The Solution (that nobody asked for)
We’re tackling the global epidemic of boring excuses with the Peter Griffin Excuse Generator! Powered by Peter’s unique sense of humor (and some clever code), our app serves up absurd, laugh-out-loud excuses for every occasion. Just pick a category—or get creative with a custom prompt—and let Peter deliver an excuse so hilarious, it might actually work. Need to blame a pet raccoon, a time-travel mishap, or an alien abduction? We've got you covered. This is the ultimate tool for anyone who wants their excuses to leave people both baffled and entertained!

## Technical Details
Technical Details
Technologies/Components Used
Flask: A lightweight Python web framework used to build the server-side logic of the application, handling requests and routing.

Together API: An AI integration that generates witty excuses based on user input, utilizing natural language processing to create contextually appropriate and humorous responses.

HTML/CSS: The backbone of the frontend, where HTML structures the content and CSS styles it to create a vibrant and engaging user interface.

JavaScript: Used to add interactivity to the web application, enabling dynamic features like excuse generation, mode toggling, and text-to-speech functionality.

Speech Synthesis API: A built-in web API that allows the application to convert the generated excuses into spoken words, enhancing user experience.

Responsive Design: The app employs responsive design principles to ensure usability across various devices and screen sizes, making it accessible to all users.

JSON: Data interchange format used for sending requests and responses between the client and server, facilitating smooth communication and data handling.
For Software:
Software
Languages Used:

Python (for backend development)
HTML (for structure of web pages)
CSS (for styling of web pages)
JavaScript (for client-side interactivity)
Frameworks Used:

Flask (for building the web application)
Libraries Used:

Together API (for generating excuses)
Speech Synthesis API (for text-to-speech functionality)
Tools Used:

Visual Studio Code (for code editing)
Git (for version control)
Postman (for testing API requests)
Browser Developer Tools (for debugging and testing frontend features)

For Hardware:
- [List main components]
- [List specifications]
- [List tools required]

### Implementation
For Software:
# Installation
1)Clone the Repository:
git clone https://github.com/Adarshabrahamjohnson12/uselesss_decrypts
cd <repository-directory>
2)Set Up a Virtual Environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Required Packages: Ensure you have pip installed, then run:
pip install flask
pip install together
Set Up Environment Variables: Create a .env file in the root directory to store your API key:
TOGETHER_API_KEY='e7a501a28a46881b3559d8599dd96cf6bb100fe303fc4cfa67f02c023b193d41'


# Run
 Start the Flask server:
 python app.py

Access the App:http://127.0.0.1:5000/


### Project Documentation
Project Overview
The Peter Griffin Excuse Generator is a web application that allows users to create humorous excuses for various situations using a cartoon character's quirky personality. The application leverages natural language processing via the Together API to generate contextually relevant and funny responses.

Features
Excuse Generation: Users can choose from predefined categories or enter custom prompts to generate excuses.
Text-to-Speech: The application can read aloud the generated excuses, enhancing the interactive experience.
Responsive Design: The app is designed to work seamlessly on various devices, ensuring accessibility for all users.
Installation Guide
Clone the Repository:

git clone <repository-url>
cd <repository-directory>
Set Up a Virtual Environment:



python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
Install Required Packages:



pip install flask
pip install together
Set Up Environment Variables: Create a .env file in the root directory and add your Together API key:

TOGETHER_API_KEY='e7a501a28a46881b3559d8599dd96cf6bb100fe303fc4cfa67f02c023b193d41'
Run the Application:
python app.py
Access the Application: Open your browser and go to:

http://127.0.0.1:5000/
Usage Instructions
Select a category or enter a custom prompt in the input area.
Click the "Generate Excuse" button to create your excuse.
Use the "Play Excuse" button to hear the generated excuse spoken aloud.
Code Structure
app.py: The main application file containing Flask routes and logic for excuse generation.
templates/index.html: The HTML structure for the frontend of the application.
static: Contains CSS and JavaScript files for styling and interactivity.
Dependencies
Flask: Web framework for building the application.
Together API: Service for generating text responses.
Speech Synthesis API: For text-to-speech functionality in the browser.
License
This project is licensed under the MIT License. Please see the LICENSE file for details.

Acknowledgments
Thanks to the creators of the Together API for enabling seamless natural language generation.
Special thanks to the community for their ongoing support and feedback.
This documentation provides a comprehensive overview of the Peter Griffin Excuse Generator, ensuring users can effectively install, use, and understand the application. Enjoy generating excuses and sharing laughs!


# Screenshots (Add at least 3)
![Screenshot1]![Front page of the website](https://github.com/user-attachments/assets/95ae92ba-53fc-4ddf-9d37-2bcf6207514e)

This is the front page of the site we can see two types of input Categories and Custom Input.

![Screenshot2]![categories](https://github.com/user-attachments/assets/d513b026-18ae-483e-8675-ebb5f9a68834)

This is the section called categories in this section we can choose a random category for getting excuse.

![Screenshot3]![Custom input](https://github.com/user-attachments/assets/f3a6c943-713a-46f0-ad09-069a1ce67b4f)

This is the section called Custom in this section we can custom prompt the input and get the output

# Diagrams
![Workflow]![excuse_generator_corrected_linear_workflow_diagram (2)](https://github.com/user-attachments/assets/a92dfda0-ee2f-41ec-9d9c-b376a671c5de)

This workflow diagram illustrates the interaction between the user interface, the Flask backend, and the Together API. Users can choose a category or enter a custom prompt, which is sent to the Flask server. The server processes the request, communicates with the Together API to generate an excuse, and then returns the response to the user interface for display. Additionally, the text-to-speech feature allows users to hear the generated excuses

For Hardware:

# Schematic & Circuit
![Circuit](Add your circuit diagram here)
*Add caption explaining connections*

![Schematic](Add your schematic diagram here)
*Add caption explaining the schematic*

# Build Photos
![Components](Add photo of your components here)
*List out all components shown*

![Build](Add photos of build process here)
*Explain the build steps*

![Final](Add photo of final product here)
*Explain the final build*

### Project Demo
# Video
[excuseme_main1.mp4](https://drive.google.com/file/d/11z_Pr8KBwbKc6inN_NfQ6keKgP8ZLzcM/view?usp=sharing)
explain the content and main working of the video in step by step video


## Team Contributions
- Adarsh Abraham Johnson: Frontend, Backend
- Anan M Binoj: Design
- Arjun T Aghilesh: Design

---
Made with ❤️ at TinkerHub Useless Projects 

![Static Badge](https://img.shields.io/badge/TinkerHub-24?color=%23000000&link=https%3A%2F%2Fwww.tinkerhub.org%2F)
![Static Badge](https://img.shields.io/badge/UselessProject--24-24?link=https%3A%2F%2Fwww.tinkerhub.org%2Fevents%2FQ2Q1TQKX6Q%2FUseless%2520Projects)




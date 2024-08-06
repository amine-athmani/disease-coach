
# DAIT Assistant

## Overview
DAIT Assistant is an AI-powered chatbot designed to assist patients with chronic diseases by providing personalized advice and answering questions about their condition. The assistant is built using Streamlit and leverages the Falcon LLM for natural language processing.

## Features
- Collects user information including age, height, weight, sex, disease, activity level, diet, food preferences, and allergies.
- Provides personalized assistance based on the user's chronic disease.
- Suggests relevant questions that the user can ask.
- Dynamically generates new suggested questions after each interaction.

## Requirements
- Python 3.7+
- Streamlit
- OpenAI API key

## Installation
1. Clone the repository:
   \`\`\`bash
   git clone https://github.com/yourusername/dait-assistant.git
   cd dait-assistant
   \`\`\`

2. Create a virtual environment and activate it:
   \`\`\`bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows use \`venv\Scripts\activate\`
   \`\`\`

3. Install the required packages:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. Create a \`.env\` file in the root directory and add your OpenAI API key:
   \`\`\`
   AI71_API_KEY=your_openai_api_key
   \`\`\`

## Usage
1. Run the Streamlit app:
   \`\`\`bash
   streamlit run app.py
   \`\`\`

2. Open your web browser and navigate to \`http://localhost:8501\`.

3. Fill in the required information on the input form and submit.

4. Interact with the chatbot by typing your questions or selecting from the suggested questions.

## Project Structure
- \`app.py\`: Main application file containing the Streamlit code.
- \`requirements.txt\`: List of dependencies required for the project.
- \`.env\`: Environment file containing sensitive information like API keys.

## Example
Here's an example of how the chatbot can be used:
1. User fills in their information on the input form.
2. The chatbot greets the user and presents itself as an expert in their disease.
3. The chatbot suggests three relevant questions that the user can ask.
4. User clicks on one of the suggested questions or types their own question.
5. The chatbot responds with personalized advice and suggests new questions.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License.
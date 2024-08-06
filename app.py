import streamlit as st
import openai
from dotenv import load_dotenv
import os

AI71_BASE_URL = "https://api.ai71.ai/v1/"
load_dotenv()
AI71_API_KEY = os.getenv("AI71_API_KEY")


# Define the color scheme
primary_color = "#022b29"
secondary_color = "#e4c45a"
bg_color = "#f9f7e3"

# Get OpenAI api key
#api_key = st.secrets["OPEN_API_KEY"]

# Apply the color scheme globally
st.set_page_config(
    page_title='DAIT Assistant',
    initial_sidebar_state='auto',
    page_icon="🍽️",
)

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'input'

# Function to display the input form
def show_input_form():
    st.title('Talk to our AI assistant')

    with st.form(key='meal_plan_form'):
        st.write("We just need some vital information about yourself to assist you in your disease.")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            age = st.number_input('Age', min_value=0, value=26)
        with col2:
            height = st.number_input('Height (Centimeters)', min_value=0, value=188)
        with col3:
            weight = st.number_input('Weight (KG)', min_value=0, value=75)

        col4, col5 = st.columns(2)
        with col4:
            sex = st.selectbox('Sex', ['Male', 'Female'], index=0)
            disease = st.selectbox('Disease', ['Type 1 diabetes', 'Type 2 diabetes', 'Gestational'], index=0)
        with col5:
            activity_level = st.selectbox('Activity level', ["No exercise", "Light", "Moderate", "High", "Extreme"], index=2)
            diet = st.selectbox('Diet', ['Anything', 'Vegetarian', 'Vegan', 'Pescatarian'], index=0)
        
        food_pref = st.multiselect('Food Category?', 
                                   ['Mediterranean', "Middle Eastern"],
                                   ["Middle Eastern"])
        
        # country = st.multiselect('Specific country?', 
        #                            ['Algeria', 'Bahrain', 'Egypt', 'France', 'Greece',
        #                             'Iraq', 'Italy', 'Jordan', 'Kuwait', 'Lebanon',
        #                             'Morocoo', 'Oman', 'Palestine', 'Portugal', 'Qatar',
        #                             'Saudi Arabia', 'Spain', 'Syria', 'Tunisia', 'UAE', 'Yemen'],
        #                            ['Saudi Arabia'])

        allergies = st.multiselect('Any allergies or ingredients you have allergies for?', 
                                   ['Nuts', 'Dairy', 'Shellfish', 'Soy', 'Eggs', 'Gluten'])

        submit_button = st.form_submit_button(label='Talk to our AI assistant')

    if submit_button:
        # Save the input data to session state
        st.session_state.user_input = {
            # User infos
            'age': age, 'height': height, 'weight': weight, 'sex': sex,
            'activity_level': activity_level, 
            # User preferences
            'disease': disease,
            'diet': diet,
            'allergies': allergies,
            'food_pref': food_pref,
        }
                
        # Navigate to the meal plan page
        st.session_state.page = 'chatbot'

def regenerate():
    st.session_state.page = 'chatbot'

def back_input():
    st.session_state.page = 'input'

# Function to display the meal plan
def chatbot():
    user_input = st.session_state.user_input
    disease = user_input["disease"]
    st.title(f"💬 Your {disease} Assistant")
    st.caption("🚀 A chatbot powered by Falcon LLM")

    client = openai.OpenAI(
        api_key=AI71_API_KEY,
        base_url=AI71_BASE_URL,
    )
    
    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "system", "content": f"You are an expert assistant specializing in {disease}. Provide tips, advice, and answer questions specifically related to {disease}."}]
        st.session_state["messages"] = [{"role": "assistant", "content": f"Hello! I am your assistant specialized in {disease}. How can I assist you today?"}]
    
    for msg in st.session_state.messages:
        if msg["role"] != "system":
            st.chat_message(msg["role"]).write(msg["content"])
 
    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        st.chat_message("user").write(prompt)
        
        response = client.chat.completions.create(model="tiiuae/falcon-180b-chat",
                                                  messages=st.session_state.messages)
        msg = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)
                
# Page router
if st.session_state.page == 'input':
    show_input_form()
elif st.session_state.page == 'chatbot':
    chatbot()

#_____LOADING_PACKAGES_/_INITIAL_CONFIG:______________________________________
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

from difflib import get_close_matches

import indicators as ind

st.set_page_config(layout='wide', initial_sidebar_state="expanded")


#_____PLOTS_DICT:_____________________________________________________________
charts = {
    'age histogram': lambda: ind.age_histogram(st.session_state['df']),
    'education histogram': lambda: ind.education_histogram(st.session_state['df']),
    'Education Field histogram': lambda: ind.education_field_histogram(st.session_state['df']),
    'Salary Slab histogram': lambda: ind.salary_slab_histogram(st.session_state['df'])
}


#_____MAIN_APP:__________________________________________________________

# main APP
def main():
    st.title('HR - Insights Chatbot')
    
    # initializes the message history
    if 'message_history' not in st.session_state:
        st.session_state['message_history'] = []
    
    # initializes the DataFrame
    if 'df' not in st.session_state:
        st.session_state['df'] = load_data('./data/HR_Analytics.csv')
    
    # assigns the DataFrame locally
    df = st.session_state['df']
    
    # sidebar with insights options
    with st.sidebar:
        st.header('Available indicators')
        
        for key in charts.keys():
            # when the button is clicked, simulates that the user typed the 
            # indicator's name in the chat
            st.button(key, on_click=simulate_interaction, args=(key,))
        
        st.markdown('')
        
        # footer
        st.markdown('____')
        url = 'https://leandrofabioportfolio.streamlit.app/'
        st.markdown(f'[Made by Leandro Fabio with streamlit 💻]({url})')
    
    
    # chat input
    user_input = st.chat_input('Search for the desired indicator...')
    
    if user_input:
        # adds the user's message to the history
        save_reply(role='user', content=user_input)
        
        # Suggests a closer indicator if the user makes a typo
        indicator_suggested = suggest_indicator(user_input)
        
        if indicator_suggested:
            # chat's reply with the indicator suggested
            reply = f'📈 Displaying the indicator: {indicator_suggested}...'
            save_reply(
                role = 'assistant',
                content = reply,
                chart = charts[indicator_suggested]
            )
        else:
            reply = (f'😔 Sorry, but the indicator "{user_input}" was not' +
                     'found. Please try again.')
            save_reply(
                role = 'assistant',
                content = reply
            )
    
    # Exibe o histórico da conversa
    for message in st.session_state['message_history']:
        with st.chat_message(message['role']):
            st.markdown(message['content'])
            if message['chart'] != '':
                message['chart']()


#_____FUNCTION_TO_SUGGEST_INDICATORS__________________________________________
def suggest_indicator(user_input):
    """
    Returns the closest indicator based on the user's input
    """
    suggestions = get_close_matches(
        user_input.lower(),
        charts.keys(),
        n=1,
        cutoff=0.6)
    
    return suggestions[0] if suggestions else None


#_____SAVE_REPLIES____________________________________________________________
def save_reply(role: str, content: str, chart: str = ''):
    """
    Saves the reply in st.session_state based on the provided parameters.
    """
    st.session_state['message_history'].append(
        {'role': role,
         'content': content,
         'chart': chart}
    )


#_____SIMULATE_CHAT_INTERACTION_______________________________________________
def simulate_interaction(indicator):
    # simulates that the user typed in the chat
    save_reply(
        role='user',
        content=indicator
    )
    # chat's reply
    reply = f'📈 Displaying the indicator: {indicator}...'
    save_reply(
        role = 'assistant',
        content = reply,
        chart = charts[indicator]
    )


#_____LOAD_DATA________________________________________________________
@st.cache_data
def load_data(filepath):
    df = pd.read_csv(filepath)
    return df


# loading data
df = load_data('./data/HR_Analytics.csv')

if __name__ == "__main__":
    main()

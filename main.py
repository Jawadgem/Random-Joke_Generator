import streamlit as st
import requests

def get_random_joke():
    """Fetch a random joke from the API"""
    try:
        response = requests.get("https://official-joke-api.appspot.com/random_joke")
        
        if response.status_code == 200:
            joke_data = response.json()
            return f"{joke_data['setup']} \n\n {joke_data['punchline']}"
        else:
            return "Failed to fetch a a joke. Please try again later."
        
    except:
        return f"Looks like this programmer forgot to handle exceptions! 😂"

def main():
    st.title ("Joke-a-Tron: Powered by Laughter 😁")
    st.write ("Click the button below to generate a random Joke")

    if st.button("Tell me a Joke"):
        joke = get_random_joke()
        st.success(joke)
        
    st.divider()

    st.markdown(
        """
    <div style= 'text-align:center;'>
        <p>Joke from Official Joke API</p>
        <p style="font-weight: bold;">Built by 😍 Jawad Nasir</p>
    </div>

""", unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
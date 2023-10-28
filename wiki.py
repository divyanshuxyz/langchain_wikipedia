#import libraries
import streamlit as st
from langchain.tools import WikipediaQueryRun
from langchain.utilities import WikipediaAPIWrapper

# Create a Streamlit app
st.title("Wikipedia LangChain Bot 🦜")
st.write("Enter a question, and I will query Wikipedia for an answer.")

# Create an instance of WikipediaQueryRun with WikipediaAPIWrapper
wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper(),)

# Create a text input field for user input
question = st.text_input("Enter your question:")

if st.button("Search Wikipedia"):
    if question:
        # Run the Wikipedia query
        response = wikipedia.run(question)

        # Display the response
        st.subheader("Wikipedia Answer:")
        st.write(response)
    else:
        st.warning("Please enter a question.")

#to run the code enter
#streamlit run wiki.py
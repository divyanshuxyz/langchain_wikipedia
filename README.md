# langchain_wikipedia
This app demonstrates the power of LangChain, a Python library for natural language processing (NLP) tasks, to create a question answering system powered by Wikipedia. The app uses Streamlit to create a simple and intuitive user interface, where users can ask questions about Wikipedia articles and receive informative answers.

LangChain Wikipedia Streamlit App

This app demonstrates the power of LangChain, a Python library for natural language processing (NLP) tasks, to create a question answering system powered by Wikipedia. The app uses Streamlit to create a simple and intuitive user interface, where users can ask questions about Wikipedia articles and receive informative answers.

Under the hood, the app uses a LangChain chain that combines a Wikipedia retriever with a large language model (LLM). The retriever first retrieves relevant Wikipedia articles for the user query, and then the LLM is used to generate an answer based on the retrieved articles. The app also uses conversational memory to track the user's previous queries and answers, which allows the LLM to generate more informative and relevant responses over time.

This app is a great example of how LangChain can be used to create powerful NLP applications with ease. It is also a valuable tool for anyone who wants to learn more about Wikipedia and its vast knowledge base.

Features:

Answer questions about Wikipedia articles in a comprehensive and informative way
Use conversational memory to track the user's previous queries and answers
Easy to use and install
Powered by LangChain and Streamlit
To use the app:

Clone the repository and install the dependencies:
git clone https://github.com/your-username/langchain-wikipedia-streamlit-app.git
cd langchain-wikipedia-streamlit-app
pip install -r requirements.txt
Start the Streamlit app:
streamlit run wiki.py
Enter your query in the text box and click on the "Answer" button.

The app will generate an answer based on the retrieved Wikipedia articles and your previous queries.


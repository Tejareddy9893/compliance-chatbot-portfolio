import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from semantic import load_embeddings, semantic_answer
from service_now.mock_api import create_ticket, search_kb
import streamlit as st

st.title("Compliance Chatbot Assistant")
query = st.text_input("Ask a compliance question:")

if query:
    index, questions, answers = load_embeddings()
    answer = semantic_answer(query, index, questions, answers)
    st.write("**Answer:**", answer)

    if "breach" in query.lower() or "incident" in query.lower():
        ticket = create_ticket(query)
        st.write("**ServiceNow Ticket Created:**", ticket["link"])
    else:
        kb = search_kb(query)
        st.write("**Knowledge Base Result:**", kb)
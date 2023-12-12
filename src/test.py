import streamlit as st
import st_query_input as input_box

def main():

    st.set_page_config(page_title="test", layout="wide")

    if 'question' not in st.session_state:
        st.session_state["question"] = "enter your question here..."

    st.write("Multiline text input")
    col1, col2, col3 = st.columns([2,8,1])
    with col2:
        value = input_box.query_input(st.session_state["question"], height=38, cols=60, key=1)
    st.write(value)

    if value is not None and 'submit' in value:
        st.session_state["question"] = value['submit']

    if st.button("click to ret-run"):
        st.session_state["question"] = ""
        st.rerun()

if __name__ == "__main__":
    main()


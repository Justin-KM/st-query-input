import streamlit as st
import st_query_input as input_box

def main():

    st.set_page_config(page_title="test", layout="wide")

    st.write("Multiline text input")
    valiue = input_box.query_input("my default valueX", height=20, cols=60)
    st.write(valiue)

if __name__ == "__main__":
    main()


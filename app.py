import streamlit as st
books = "The Hobbit","Harry Potter","To kill a Mockingbird","Theo of Golden"

st.title("Book checker App")
st.write("Enter a book title to check if it exist in the database")
user_input = st.text_input("Book Titles")
if st.button("Check book"):
  if user_input.strip() == "":
    st.warning ("Please enter a book title")
  elif user_input in books:
    st.success("The book exists in the database")
  else:
    st.error("The book is NOT in the database")
    

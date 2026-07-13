import streamlit as st

st.set_page_config(page_title="Databricks Apps Demo")

st.title("🚀 Databricks Apps Demo")

st.write("### Employee Information")

name = st.text_input("Enter Employee Name")

if st.button("Show Details"):
    st.success("Employee Details")
    st.write(f"👤 Employee Name: {name}")
    st.write("🏢 Department: Data Engineering")
    st.write("📍 Location: Bangalore")
    st.write("⭐ Experience: 5+ Years")

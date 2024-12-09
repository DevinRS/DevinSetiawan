import streamlit as st

# -- HERO SECTION --
st.image("assets/teaching_hero.jpg")
st.header("Teaching") 
st.markdown("""This page summarizes my teaching and tutoring experiences. To see more of my work, visit my <a href="https://github.com/DevinRS" target="_self">GitHub page</a> or check out my <a href="http://localhost:8501/about" target="_self">about</a> page.""", unsafe_allow_html=True)

# -- Teaching --
st.write("---")
st.subheader("Teaching Experiences", anchor=False)
st.subheader("2024 - present")
st.markdown("""
- **📚 Graduate Teaching Assistant**: University of Kansas, Department of Mathematics (Calculus I, MATH 115).
""", unsafe_allow_html=True)
st.subheader("2022 - 2024")
st.markdown("""
- **📚 Tutor**: University of Kansas, Kansas Algebra Program (College Algebra, MATH 002 & 101).
""", unsafe_allow_html=True)
import streamlit as st
from forms.contact import contact_form

# -- FUNCTIONS --
@st.dialog("Send me a message!")
def show_contact_form():
    contact_form()

# -- CSS INJECTION -- 
st.markdown(
    """
    <style>
        a {
            text-decoration: none;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# -- HERO SECTION --
col1, col2 = st.columns(2, gap='small', vertical_alignment='center')
with col1:
    st.image("assets/profilepic.png", width=230)
with col2:
    st.title("Hi, I am Devin!", anchor=False)
    st.markdown(
        """
        Check out my <a href="http://devinsetiawan.streamlit.app/research" target="_self">research</a> and 
        <a href="http://devinsetiawan.streamlit.app/projects" target="_self">projects</a> to learn more about me.
        """,
        unsafe_allow_html=True
    )
    col3, col4, col5 = st.columns(3, gap='small', vertical_alignment='center')
    with col3:
        st.markdown("""<a href="https://www.linkedin.com/in/devin-setiawan/" target="_blank">![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)</a>""", unsafe_allow_html=True)
    with col4:
        st.markdown("""<a href="https://github.com/DevinRS" target="_blank">![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)</a>""", unsafe_allow_html=True)
    with col5:
        st.markdown("""<a href="https://www.instagram.com/devin.rs/" target="_blank">![instagram](https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)""", unsafe_allow_html=True)

# -- ABOUT ME SECTION --
st.write("---")
st.subheader("About Me", anchor=False)
st.write("I am an independent ML researcher working on applied machine learning in the field of medicine. With a B.S. degree in Computer Science and a strong passion for solving real-world problems through applied machine learning, I have explored diverse domains to create impactful solutions.")
st.write("Currently, I am a graduate student at the University of Kansas, where I contribute to various research labs and serve as a graduate teaching assistant. My work is driven by a commitment to advancing healthcare through innovative ML applications, and I continually seek to expand my expertise and make meaningful contributions to the field.")
st.write("I love to spend my free time playing golf ⛳, and doing jiu-jitsu 🥋.")

with open('assets/Curriculum Vitae (CV).pdf', 'rb') as f:
    st.download_button(label='🗎 Curriculum Vitae', data=f, file_name='Devin_Setiawan_CV.pdf', mime='application/pdf')

# -- ABOUT THIS WEBSITE SECTION --
st.write("---")
st.subheader("About This Website", anchor=False)
st.write("This website host my portfolio, where I showcase my research projects, personal projects, and teaching materials. Here are some sections you can explore:")
st.markdown(
    """
    - **🔎 <a href="http://devinsetiawan.streamlit.app/research" target="_self">Research</a>**: My recent research projects and publications.
    - **📁 <a href="http://devinsetiawan.streamlit.app/projects" target="_self">Projects</a>**: My personal projects and open-source contributions.
    - **🎓 <a href="http://devinsetiawan.streamlit.app/teaching" target="_self">Teaching</a>**: My teaching experiences.
    """,
    unsafe_allow_html=True
)

# -- CONTACT SECTION --
st.write("---")
st.subheader("Contact", anchor=False)
st.write("Feel free to reach out to me via email or send me a message below. I am always open to new opportunities and collaborations.")
if st.button("📧 Send Message"):
    show_contact_form()



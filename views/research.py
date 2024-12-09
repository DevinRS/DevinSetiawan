import streamlit as st
from forms.cards import show_card1, show_card2

# -- INITIALIZATION --
if "readmore1_toggle" not in st.session_state:
    st.session_state.readmore1_toggle = False

if "readmore2_toggle" not in st.session_state:
    st.session_state.readmore2_toggle = False

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

# -- FUNCTIONS --
@st.fragment
def card1():
    show_card1()

@st.fragment
def card2():
    show_card2()

# -- HERO SECTION --
st.image("assets/research_hero.jpg")
st.header("Research") 
st.markdown("""This page summarizes my recent research projects and publications. My research interests include predictive modeling, interpretable machine learning, and individualized clinical assessments. To see more of my work, visit my <a href="https://github.com/DevinRS" target="_blank">GitHub page</a> or check out my <a href="http://localhost:8501/about" target="_self">about</a> page.""", unsafe_allow_html=True)

# -- HIGHLIGHTED RESEARCH --
st.write("---")
st.subheader("Highlighted Research", anchor=False)
st.markdown("""
Here are some of my recent research projects:
- **🚑 <a href="http://localhost:8501/research#individualized-machine-learning-based-clinical-assessments-recommendation-system-icare" target="_self">iCARE</a>**: An individualized machine-learning based clinical assessments recommendation system.
- **🧠 <a href="http://localhost:8501/research#5d69d084" target="_self">CAFE</a>**: An interpretable scorecard model for early detection and risk calculation of AD development.
         
Scroll down to see more research projects I've been involved in, and click "read more" to see the research abstract.
""", unsafe_allow_html=True)
card1()
card2()

# -- FURTHER RESEARCH --
st.write("---")
st.subheader("Other Research", anchor=False)
st.subheader("2024")
st.markdown("""
- **💻 ConvNeXt Model for Breast Cancer Image
Classification**: A convolutional neural network model for classifying breast cancer images. (Accepted at ICORIS 2024)
- **🩻 Image Segmentation for Teeth Classification**: Use YOLO for segmentation and use similarity matching to find the identity of patient based on their teeth image.
            
""", unsafe_allow_html=True)
st.subheader("2023")
st.markdown("""
- **🧬 In-silico Analysis for Aptamer Selection**: A project with the Whelan Lab to select aptamers for a specific target using in-silico analysis.
""", unsafe_allow_html=True)

import streamlit as st
from forms.cards import show_card3, show_card4

# -- INITIALIZATION --
if "readmore3_toggle" not in st.session_state:
    st.session_state.readmore3_toggle = False

if "readmore4_toggle" not in st.session_state:
    st.session_state.readmore4_toggle = False

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
def card3():
    show_card3()

@st.fragment
def card4():
    show_card4()

# -- HERO SECTION --
st.image("assets/project_hero.jpg")
st.header("Projects") 
st.markdown("""This page summarizes my school and personal project in many domain of Computer Science. To see more of my work, visit my <a href="https://github.com/DevinRS" target="_self">GitHub page</a> or check out my <a href="http://localhost:8501/about" target="_self">about</a> page.""", unsafe_allow_html=True)

# -- HIGHLIGHTED RESEARCH --
st.write("---")
st.subheader("Highlighted Projects", anchor=False)
st.markdown("""
Here are some of my recent projects:
- **🌲 <a href="http://localhost:8501/projects#prose-x-llama-program-synthesis-for-semantically-wrong-code-fixing" target="_self">PROSE x Llama</a>**: Program Synthesis project to fix semantically wrong code through AST-to-AST transformation.
- **💉 <a href="http://localhost:8501/projects#pas-ip-predictive-analysis-scorecard-for-identifying-patients-at-risk-of-diabetes-development" target="_self">PAS-IP</a>**: An interpretable scorecard model for early detection and risk calculation of Diabetes development.
         
Scroll down to see more projects I've been involved in, and click "read more" to see the project description.
""", unsafe_allow_html=True)
card3()
card4()

# -- FURTHER RESEARCH --
st.write("---")
st.subheader("Other Projects", anchor=False)
st.subheader("2024")
st.markdown("""
- **🏭 Air Quality Interpolation**: A project to predict air quality using various interpolation methods using Beijing Air Dataset.
- **📦 ML Sandbox**: Capstone project to create a machine learning web application for non-technical users.
            
""", unsafe_allow_html=True)
st.subheader("2023")
st.markdown("""
- **✈️ JAD**: Involved in data team for Jayhawk Aero Design.
- **➕ Arithmetic ML**: Embedded machine learning project to predict results of arithmetic operations using CNN.
- **🎲 Settlers of Catan**: An analysis report on the game Settlers of Catan.
            
""", unsafe_allow_html=True)
st.subheader("2022")
st.markdown("""
- **🎮 Cuadrado**: Fast paced, puzzle solving game made for 2 players.
""", unsafe_allow_html=True)
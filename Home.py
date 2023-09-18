import streamlit as st
from PIL import Image
from streamlit.components.v1 import html

def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)


st.set_page_config(page_title="Devin Setiawan", page_icon="😎")

st.sidebar.title('Devin Setiawan')
button1 = st.sidebar.button('📧 Email', use_container_width=True, on_click=open_page, args=('mailto:devinryandi.s@gmail.com',))
button2 = st.sidebar.button('💻 GitHub', use_container_width=True, on_click=open_page, args=('https://github.com/DevinRS',))

st.header('Summary')
st.write("I am a senior at the University of Kansas, majoring in Computer Science, expected to graduate in May 2024. My research and interests include data analysis, interpretable machine learning, and personalized machine learning.")

st.header("Research 🔬")
st.write("Personalized Machine Learning for Early Disease Detection")
with st.expander("Learn More"):
    st.success("Lead researcher under the guidance of Dr. Arian Ashourvan of the Brain, Behavior, and Quantitative department. The research aims to find a new personalized framework that allows traditional machine learning model to make individualized predictions.")
st.write("Interpretable Scorecard Model for Alzheimer's Disease")
with st.expander("Learn More"):
    st.success("Joint research to generate a new scorecard model for Alzheimer's disease prediction. The use of scorecard is motivated by the need of an interpretable model for high-risk decision making where explanations are an important part of the decision.")
st.write("In-Silico DNA Aptamer Selection and Molecular Docking")
with st.expander("Learn More"):
    st.success("Volunteer research with Dr. Rebecca Whelan of the Analytical Chemistry department. The research aims to expand understanding of ovarian cancer. During my volunteer research, I learn to work with DNA sequence data to perform candidate selection in a procedure called Aptamer Selection. I also do data cleaning, feature engineering, and using various machine learning model to aid in DNA selection and simulation of molecular docking.")

python_image = Image.open('assets/python.png')
streamlit_image = Image.open('assets/streamlit.png')
plotly_image = Image.open('assets/plotly.png')
matplotlib_image = Image.open('assets/matplotlib.png')
scikitlearn_image = Image.open('assets/scikitlearn.png')
godot_image = Image.open('assets/godot.png')
figma_image = Image.open('assets/figma.png')
svelte_image = Image.open('assets/svelte.png')
weatherapi_image = Image.open('assets/weatherapi.png')
php_image = Image.open('assets/php.png')

st.header("Projects 🛠️")
st.write('JAD Data Science Tool')
col1, col2, col3 = st.columns(3)
with col1:
    st.image(python_image, width=80, caption='Python')
with col2:
    st.image(plotly_image, width=80, caption='Plotly')
with col3:
    st.image(streamlit_image, width=130, caption='Streamlit')
st.write('')
st.write('')
st.write('')
st.write('Settlers of Catan Analysis')
col1, col2, col3 = st.columns(3)
with col1:
    st.image(python_image, width=80, caption='Python')
with col2:
    st.image(matplotlib_image, width=80, caption='Matplotlib')
with col3:
    st.image(scikitlearn_image, width=120, caption='Scikit-learn')
st.write('')
st.write('')
st.write('')
st.write('Cuadrado Puzzle Game')
col1, col2, col3 = st.columns(3)
with col1:
    st.image(godot_image, width=80, caption='Godot Game Engine')
with col2:
    st.image(figma_image, width=60, caption='Figma')
st.write('')
st.write('')
st.write('')
st.write('Find Your Weather')
col1, col2, col3 = st.columns(3)
with col1:
    st.image(weatherapi_image, width=80, caption='Weather API')
with col2:
    st.image(svelte_image, width=60, caption='SvelteKit')    
st.write('')
st.write('')
st.write('')
st.write('Shopping Web Page')
col1, col2, col3 = st.columns(3)
with col1:
    st.image(php_image, width=100, caption='php') 
with col2:
    st.image(figma_image, width=60, caption='Figma')

st.header('Work Experience 🧑‍💼')
st.write('Kansas Algebra Program - UGTA (2022 - now)')

st.header('Education 🏫')
st.write('''
University of Kansas - Computer Science Undergraduate
- Anticipated Graduation: May 2024
- GPA: 3.94  
''')
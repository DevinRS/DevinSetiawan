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

st.sidebar.markdown("<h1 style='text-align: center; color: white;'>Devin Setiawan</h1>", unsafe_allow_html=True)
button1 = st.sidebar.button('📧 Email', use_container_width=True, on_click=open_page, args=('mailto:devinryandi.s@gmail.com',))
button2 = st.sidebar.button('💻 GitHub', use_container_width=True, on_click=open_page, args=('https://github.com/DevinRS',))
with open("assets/Resume 2023-2024.png", "rb") as file:
    btn = st.sidebar.download_button(
            label="📄 Resume",
            data=file,
            file_name="Resume 2023-2024.png",
            mime="image/png",
            use_container_width=True
          )

st.header('Summary')
st.write("I am a senior at the University of Kansas, majoring in Computer Science, expected to graduate in May 2024. My research and interests include data analysis, interpretable machine learning, and personalized machine learning.")

st.markdown("""---""") 

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

st.markdown("""---""") 

st.header("Projects 🛠️")
st.write('[JAD Data Science Tool](https://kujad1.streamlit.app/)')
col1, col2, col3 = st.columns(3)
with col1:
    st.image(python_image, width=80, caption='Python')
with col2:
    st.image(plotly_image, width=80, caption='Plotly')
with col3:
    st.image(streamlit_image, width=130, caption='Streamlit')
with st.expander("Learn More"):
    st.success('''
    This semester my co-worker, who happens to be the president of Jayhawk Aero Design, invited me to JAD. The goal of JAD is to win AIAA plane design competition where we build working rc plane and try to be the best amongst participating universities. Upon this intriguing idea, I decided to join the data science team to help bring KU its long deserved victory. Check out my website that I built to help achieve this goal!
    ''')
st.write('')
st.write('')
st.write('')
st.write('[Settlers of Catan Analysis](https://github.com/DevinRS/Settlers_of_Catan_Analysis)')
col1, col2, col3 = st.columns(3)
with col1:
    st.image(python_image, width=80, caption='Python')
with col2:
    st.image(matplotlib_image, width=80, caption='Matplotlib')
with col3:
    st.image(scikitlearn_image, width=120, caption='Scikit-learn')
with st.expander("Learn More"):
    st.success('''
    My roommate introduced me to this amazing boardgame (RIP Klaus Teuber 1952-2023) that consist of conquering, trading, and a lot more awesome mechanics. This game is played with 4 players where the goal of the game is to be the first to reach 10 points. Being the competitive person that I am, I decided to analyze the game and come up with data-driven strategy that gives me an edge over my roommates. Check out my analysis above and win more games for yourself!! 💪
    ''')
st.write('')
st.write('')
st.write('')
st.write('[Cuadrado Puzzle Game](https://github.com/DevinRS/448_Project)')
col1, col2, col3 = st.columns(3)
with col1:
    st.image(godot_image, width=80, caption='Godot Game Engine')
with col2:
    st.image(figma_image, width=60, caption='Figma')
with st.expander("Learn More"):
    st.success('''
    This is the project I did alongside my 5 teammates for Software Engineering 1 course. Working on the project, I was exposed to the process of agile development and truly experienced how developing a software feels like. I'm the lead programmer and throughout the sprint, I felt the experience of having to learn a totaly new and unfamiliar tool, Godot Game Engine. At the end of the project, we managed to deploy our working puzzle game. Try it out! It's quite fun 😊
    ''')

st.markdown("""---""") 

st.header('Teaching Experience 🧑‍💼')
st.write('''
Throughout my academic journey, rarely, if ever, I find teaching fascinating. I always saw it as just another thing people do, just another boring job, or just one of the many ways to pay the bills. However, ever since I've joined the Kansas Algebra Program, I've discovered a new appreciation and fascination with the art of teaching. That's what teaching really is to me now, an ART 🎨
''')
with st.expander('Kansas Algebra Program (KAP)'):
    st.subheader('What is KAP?')
    st.write('Under the deparment of mathematics in the University of Kansas, KAP manages MATH 002 Intermediate Mathematics and MATH 101 College Algebra. KAP design the classes curriculum and manages all the available resource to help student succeed in learning algebra for their education journey.')
    st.subheader('What\'s my role?')
    st.write('''
Here's my role at KAP:
- Class Assistant
- Algebra Tutor
- Desk Assistant
- Supervisor
             
At KAP, I've learned how to teach, how to manage administration duties, and how to manage people. As a class assistant and tutor, I played an active role in teaching the student one-to-one, tailoring to each individual need to ensure they're able to succeed in learning the material. With the desk assistant position, I ensure documents are updated and where they're suppose to be. I also need to make sure that the communication line between the student and KAP is accessible. As a supervisor, I've learned to manage people and be a leader. 
''')
    st.subheader('Love for Teaching')
    st.write('''
Being a teacher first hand have taught me the true value of teaching. When you have to teach one-on-one, you really need to tailor your approach to the student you're teaching. In my opinion, this is the art in teaching. There's no guidebook or fixed methods to teach someone how to learn a material. Sure, there are some guideline you can follow but ultimately, you'll always need to adapt and adjust in the process.
''')

st.markdown("""---""") 

st.header('Education 🏫')
st.write('''
University of Kansas - Computer Science Undergraduate
- Anticipated Graduation: May 2024
- GPA: 3.94  
''')
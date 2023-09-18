import streamlit as st
from streamlit.components.v1 import html

def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)


st.set_page_config(page_title="Education", page_icon="🏫")

st.sidebar.title('Devin Setiawan')
button1 = st.sidebar.button('📧 Email', use_container_width=True, on_click=open_page, args=('mailto:devinryandi.s@gmail.com',))
button2 = st.sidebar.button('💻 GitHub', use_container_width=True, on_click=open_page, args=('https://github.com/DevinRS',))

st.title('Education 🏫')
st.write('''
As an international student from Indonesia, I embarked on an exciting journey to the University of Kansas to pursue my passion for computer science. I've met a lot of amazing people from different backgrounds and get to experience not only an amazing academic journey, but a journey of self discovery. I've been lucky enough to be able to experience leadership experience, engage in my hobbies, and discover new exciting activities. Here's my story 😄
''')

with st.expander('2020 - 2021:  COVID and Online Classes 😷'):
    st.write('')
with st.expander('2021 - 2022: USA, Snow, and Jiujitsu ⛄'):
    st.write('')
with st.expander('2022 - 2023: Software Engineering, AI and the ChatGPT Boom 💥'):
    st.write('')
with st.expander('2023 - Now: More GPT\'s, More AI, and More JiuJitsu 🤖'):
    st.write('')
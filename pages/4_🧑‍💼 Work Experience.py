import streamlit as st
from streamlit.components.v1 import html

def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)


st.set_page_config(page_title="Work Experience", page_icon="🧑‍💼")

st.sidebar.title('Devin Setiawan')
button1 = st.sidebar.button('📧 Email', use_container_width=True, on_click=open_page, args=('mailto:devinryandi.s@gmail.com',))
button2 = st.sidebar.button('💻 GitHub', use_container_width=True, on_click=open_page, args=('https://github.com/DevinRS',))

st.title('Work Experience 🧑‍💼')
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
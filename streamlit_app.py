import streamlit as st

# -- PAGE CONFIG --
st.set_page_config(
    page_title="Devin's Portfolio",
    page_icon="😎"
)

# -- PAGE SETUP --
about_page = st.Page(
    page="views/about.py",
    title="About",
    icon=":material/home:"
)

projects_page = st.Page(
    page="views/projects.py",
    title="Projects",
    icon=":material/emoji_objects:"
)

research_page = st.Page(
    page="views/research.py",
    title="Research",
    icon=":material/insights:"
)

teaching_page = st.Page(
    page="views/teaching.py",
    title="Teaching",
    icon=":material/school:"
)

# -- NAVIGATION SETUP --
page = st.navigation(pages=[about_page, research_page, projects_page, teaching_page])

# -- SHARED ON ALL PAGES --
st.logo("assets/logo.png")
st.sidebar.text("Made with ❤︎ by Devin")

# -- RUN NAVIGATION --
page.run()

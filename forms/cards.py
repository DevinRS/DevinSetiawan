import streamlit as st

def readmore1():
    st.session_state.readmore1_toggle = not st.session_state.readmore1_toggle

def readmore2():
    st.session_state.readmore2_toggle = not st.session_state.readmore2_toggle

def readmore3():
    st.session_state.readmore3_toggle = not st.session_state.readmore3_toggle

def readmore4():
    st.session_state.readmore4_toggle = not st.session_state.readmore4_toggle

def show_card1():
    with st.container(border=True):
        st.subheader("Individualized Machine-learning Based Clinical Assessments Recommendation System (iCARE)")
        st.image("assets/icare.png")
        st.html("<h4>Highlights</h4>")
        st.markdown(
            """
            - Developed a novel individualized feature selection algorithm for improving diagnostic accuracy.
            - Build a working prototype of the iCARE system using Scikit-Learn and SHAP libraries.
            - Received KU Undergraduate Research Award and Outstanding Presentation Award.
            """
        )
        if st.session_state.readmore1_toggle:
            st.html("<h4>Abstract</h4>")
            st.write("**Background:** Traditional clinical assessments often lack individualization, relying on standardized procedures that may not accommodate the diverse needs of patients, especially in early stages where personalized diagnosis could offer significant benefits. We aim to provide a machine-learning framework that addresses the individualized feature addition problem and enhances diagnostic accuracy for clinical assessments.")
            st.write("**Methods:** Individualized Clinical Assessment Recommendation System (iCARE) employs locally weighted logistic regression and Shapley Additive Explanations (SHAP) value analysis to tailor feature selection to individual patient characteristics. Evaluations were conducted on synthetic and real-world datasets, including early-stage diabetes risk prediction and heart failure clinical records from the UCI Machine Learning Repository. We compared the performance of iCARE with a Global approach using statistical analysis on accuracy and area under the ROC curve (AUC) to select the best additional features.")
            st.write("**Findings:** The iCARE framework enhances predictive accuracy and AUC metrics when additional features exhibit distinct predictive capabilities, as evidenced by synthetic datasets 1-3 and the early diabetes dataset. Specifically, in synthetic dataset 1, iCARE achieved an accuracy of 0·999 and an AUC of 1·000, outperforming the Global approach with an accuracy of 0·689 and an AUC of 0·639. In the early diabetes dataset, iCARE shows improvements of 1·5-3·5% in accuracy and AUC across different numbers of initial features. Conversely, in synthetic datasets 4-5 and the heart failure dataset, where features lack discernible predictive distinctions, iCARE shows no significant advantage over global approaches on accuracy and AUC metrics.")
            st.write("**Interpretation:** iCARE provides personalized feature recommendations that enhance diagnostic accuracy in scenarios where individualized approaches are critical, improving the precision and effectiveness of medical diagnoses.")
        col1, col2, col3 = st.columns(3, vertical_alignment='center')
        with col1:
            if st.session_state.readmore1_toggle:
                st.button("📜 Read Less", on_click=readmore1, key="readmore1", use_container_width=True)
            else:
                st.button("📜 Read More", on_click=readmore1, key="readmore1", use_container_width=True)
        with col2:
            st.link_button("💻 GitHub Repo", url="https://github.com/DevinRS/iCARE", use_container_width=True)
        with col3:
            st.link_button("📕 Paper", url="https://medrxiv.org/cgi/content/short/2024.07.24.24310941v1", use_container_width=True)

def show_card2():
    with st.container(border=True):
        st.subheader("The Cognitive, Age, Functioning, and APOE4 (CAFE) Scorecard to Predict the Development of Alzheimer’s Disease: A White-Box Approach")
        st.image("assets/cafe.png")
        st.html("<h4>Highlights</h4>")
        st.markdown(
            """
            - Implemented an interpretable scorecard model (FasterRisk) for early detection and risk calculation of Alzheimer's disease.
            - Evaluations on the Alzheimer's Disease Neuroimaging Initiative (ADNI) dataset showed an AUC of 0.867 to 0.893.
            - Research was presented in International Neuropsychological Society (INS) conference.
            """
        )
        if st.session_state.readmore2_toggle:
            st.html("<h4>Abstract</h4>")
            st.write("**Objective:** This study aimed to create a scoring system to predict the likelihood of developing Alzheimer’s disease using accessible variables  to address the costliness of the diagnostic process and promote early detection.")
            st.write("**Participants and Methods:** We analyzed 713 participants with normal cognition or mild cognitive impairment from the Alzheimer's Disease Neuroimaging Initiative. We integrated cognitive test scores from various domains, informant-reported daily functioning, APOE4, and demographics to generate the scorecards using the FasterRisk algorithm.")
            st.write("**Results:** Various combinations of 5 features were selected for the ten scorecards with a test area under the curve ranging from 0.867 to 0.893. The best performance scorecard generated the following point assignments: age < 76 (-2 points); no APOE4 alleles (-3 points); Rey Auditory Verbal Learning Test <= 36 items (4 points); Logical Memory delayed <= 3 items (5 points); and Functional Assessment Questionnaire <= 2 (-5 points). The probable Alzheimer’s development risk was 4.3% for a score of -10, 31.5% for a score of -3, 50% for a score of -1, 76.3% for a score of 1, and greater than 95% for a score of > 6.")
            st.write("**Conclusions:** Our findings highlight the potential of these interpretable scorecards to predict the likelihood of developing Alzheimer’s disease using accessible information, allowing for applicability across diverse healthcare environments. While our initial scope centers on Alzheimer’s disease, the foundation we have established paves the way for similar methodologies to be applied to other types of dementia.")
        col1, col2, col3 = st.columns(3, vertical_alignment='center')
        with col1:
            if st.session_state.readmore2_toggle:
                st.button("📜 Read Less", on_click=readmore2, key="readmore2", use_container_width=True)
            else:
                st.button("📜 Read More", on_click=readmore2, key="readmore2", use_container_width=True)
        with col2:
            st.button("💻 GitHub Repo", key="github2", use_container_width=True, disabled=True)
        with col3:
            st.button("📕 Paper", key="paper2", use_container_width=True, disabled=True)

def show_card3():
    with st.container(border=True):
        st.subheader("PROSE x Llama: Program Synthesis for Semantically Wrong Code Fixing")
        st.image("assets/prose.png")
        st.html("<h4>Highlights</h4>")
        st.markdown(
            """
            - Use Microsoft PROSE SDK to generate AST-to-AST transformation for fixing semantically wrong code.
            - Implement a working prototype of the PROSE x Llama system using Python and C#.
            - Inspired by the JIGSAW paper, which aims to improve LLM generated code by fixing semantically wrong code.
            """
        )
        if st.session_state.readmore3_toggle:
            st.html("<h4>Project Description</h4>")
            st.write("This project presents a detailed account of the implementation and evaluation of targeted AST-to-AST transformations aimed at correcting semantic inaccuracies in code generated by Pre-trained Language Models (PTLMs). Our approach utilizes a customized Domain-Specific Language (DSL) developed for structuring abstract syntax trees (ASTs) and a series of predefined transformation rules facilitated by the PROSE synthesis framework. We evaluated the effectiveness of these transformations on common semantic errors identified in PTLM outputs, such as incorrect indexing methods and unnecessary arguments. Our results demonstrate the system\’s capability to significantly enhance the accuracy of the transformed code, underlining the potential of targeted interventions in automated code synthesis. This work not only sheds light on the inherent challenges of semantic correctness in code generation but also sets the stage for further exploration of modular and scalable transformation techniques in programming languages.")
        col1, col2 = st.columns(2, vertical_alignment='center')
        with col1:
            if st.session_state.readmore3_toggle:
                st.button("📜 Read Less", on_click=readmore3, key="readmore3", use_container_width=True)
            else:
                st.button("📜 Read More", on_click=readmore3, key="readmore3", use_container_width=True)
        with col2:
            st.link_button("💻 GitHub Repo", url="https://github.com/bakhbyergyen7/jigsaw-reimplementation", use_container_width=True)


def show_card4():
    with st.container(border=True):
        st.subheader("PAS-IP: Predictive Analysis Scorecard for Identifying Patients at Risk of Diabetes Development")
        st.image("assets/scorecard.png")
        st.html("<h4>Highlights</h4>")
        st.markdown(
            """
            - Implemented an interpretable scorecard model (FasterRisk) for early detection and risk calculation of Diabetes development.
            - Evaluations on the Early Diabetes Dataset showed an AUC of 0.973
            - Inspired by the CAFE paper, which aims to predict the development of Alzheimer's disease using accessible variables.
            """
        )
        if st.session_state.readmore4_toggle:
            st.html("<h4>Project Description</h4>")
            st.write("This project aims to build predictive models to identify individuals at risk of early-stage diabetes based on a variety of health-related features. We leverage multiple machine learning techniques, including simpler models like Logistic Regression and more complex models like Random Forest and Gradient Boosting. Additionally, we focus on generating an interpretable risk scorecard using the FasterRisk algorithm, which can be used by healthcare professionals to make informed decisions.")
        col1, col2 = st.columns(2, vertical_alignment='center')
        with col1:
            if st.session_state.readmore4_toggle:
                st.button("📜 Read Less", on_click=readmore4, key="readmore4", use_container_width=True)
            else:
                st.button("📜 Read More", on_click=readmore4, key="readmore4", use_container_width=True)
        with col2:
            st.link_button("💻 GitHub Repo", url='https://github.com/DevinRS/Interpretable-Scorecard-Model-for-Early-Diabetes-Classification', use_container_width=True)
import streamlit as st

from questions import QUESTIONS
from engine import recommend_majors


st.set_page_config(
    page_title="University Major Advisor",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 University Major Advisor")

st.write(
    "Discover university majors that match "
    "your interests, academic subjects, and skills."
)

st.info("Answer the following questions to discover your top 5 majors.")

with st.form("advisor_form"):

    answers = []

    for index, question in enumerate(QUESTIONS):

        choice = st.radio(
            question["question"],
            options=list(question["options"].keys()),
            format_func=lambda x, q=question: q["options"][x][0],
            key=f"question_{index}"
        )

        answers.append(choice)

    submitted = st.form_submit_button("Get My Recommendations")

if submitted:

    student_data = {
        "interests": [],
        "subjects": [],
        "skills": []
    }

    for question, choice in zip(QUESTIONS, answers):

        category = question["category"]

        selected_value = question["options"][choice][1]

        student_data[category].append(selected_value)

    results = recommend_majors(student_data)

    st.success("Your recommendations are ready!")

    st.subheader("Your Top 5 Recommended Majors")

    for index, result in enumerate(results, start=1):

        st.write(f"### {index}. {result['major']}")

        st.write(f"Category: {result['category']}")

        st.progress(result["score"] / 100)

        st.write(f"Compatibility: {result['score']}%")

        st.divider()

    st.caption("Thank you for using University Major Advisor!")

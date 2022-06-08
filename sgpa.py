import streamlit as st
import pandas as pd
import annotated_text


ba_courses = pd.read_csv("majors/BA.csv")
mis_courses = pd.read_csv("majors/MIS.csv")
cs_courses = pd.read_csv("majors/CS.csv")
ce_courses = pd.read_csv("majors/CE.csV")
ee_courses = pd.read_csv("majors/EE.csv")
me_courses = pd.read_csv("majors/ME.csv")

grades = {"A+": 4.00, "A": 4.00,
          "B+": 3.50, "B": 3.00,
          "C+": 2.50, "C": 2.00,
          "D+": 1.50, "D": 1.00,
          "E": 0.50, "F": 0.00}


def get_credit(course_list, course):
    a = 0
    for i in course_list["Course"]:
        if i == course:
            return course_list["Credit"][a]
        a += 1


def calc_gpa(c, g, crs):
    cds = []
    gps = []
    for i in c:
        cds.append(get_credit(crs, i))
    for k in g:
        gps.append(grades[k])

    ca = 0
    for j in range(len(cds)):
        ca += cds[j] * gps[j]

    return round(ca / sum(cds), 2)


def manipulate(mj, ncs):
    st.markdown("\n\n")
    with st.expander("Calculator"):
        st.markdown("<hr>", unsafe_allow_html=True)

        my_courses = []
        my_grades = []
        for i in range(int(ncs)):
            l, r = st.columns(2)
            course = l.selectbox("Course", sorted(mj["Course"]),
                                 help="Incase of a non-major elective, kindly select 'Non-major elective'",
                                 key=i)
            my_courses.append(course)
            grade = r.selectbox("Select a grade", list(grades.keys()), key=i)
            my_grades.append(grade)

        st.markdown("\n\n")
        l, m, r = st.columns(3)
        confirm = l.button("Calculate GPA")

        if confirm:

            value = calc_gpa(my_courses, my_grades, mj)
            with r:
                if 3.69 >= value >= 3.5:
                    annotated_text.annotated_text(annotated_text.annotation(str(value), "CUM LAUDE 😜", color="black",
                                                                            background="#ccffcc", font_size="22px"))
                elif 3.84 >= value >= 3.70:
                    annotated_text.annotated_text(annotated_text.annotation(str(value), "MAGNA CUM LAUDE 😎", color="black",
                                                                            background="#ccffcc", font_size="22px"))
                elif 4.00 >= value >= 3.85:
                    annotated_text.annotated_text(annotated_text.annotation(str(value), "SUMMA CUM LAUDE 🥳", color="black",
                                                                            background="#ccffcc", font_size="22px"))
                elif 3.49 >= value >= 3.00:
                    annotated_text.annotated_text(annotated_text.annotation(str(value), "CONGRATULATIONS 😁", color="black",
                                                                            background="#ffff99", font_size="22px"))
                elif 2.99 >= value >= 2.50:
                    annotated_text.annotated_text(annotated_text.annotation(str(value), "KEEP PUSHING 💪🏿", color="black",
                                                                            background="#ffcccc", font_size="22px"))
                elif 2.49 >= value >= 2.00:
                    annotated_text.annotated_text(annotated_text.annotation(str(value), "KEEP PUSHING 💪🏿", color="black",
                                                                            background="#ffcccc", font_size="22px"))
                else:
                    annotated_text.annotated_text(annotated_text.annotation(str(value), "KEEP PUSHING 💪🏿", color="black",
                                                                            background="#ffcccc", font_size="22px"))
        st.markdown("\n\n")


def sem_gpa():

    st.title("Semester GPA Calculator")

    ll, rr = st.columns([5, 5])

    major = ll.selectbox("Major", ["📈 Business Administration", "💼 Management Information Systems",
                                   "🧑🏽‍💻 Computer Science", "🤖 Computer Engineering",
                                   "⚡ Electrical Engineering",
                                   "👨🏿‍🔧 Mechanical Engineering"])

    num_courses = rr.number_input("Number of courses taken", min_value=1, max_value=6, step=1)

    if major == "📈 Business Administration":
        manipulate(ba_courses, num_courses)
    elif major == "💼 Management Information Systems":
        manipulate(mis_courses, num_courses)
    elif major == "🧑🏽‍💻 Computer Science":
        manipulate(cs_courses, num_courses)
    elif major == "🤖 Computer Engineering":
        manipulate(ce_courses, num_courses)
    elif major == "⚡ Electrical Engineering":
        manipulate(ee_courses, num_courses)
    elif major == "👨🏿‍🔧 Mechanical Engineering":
        manipulate(me_courses, num_courses)



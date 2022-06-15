import streamlit as st
import annotated_text

sems = {"Year 1 Semester 1": "Semester 1",
        "Year 1 Semester 2": "Semester 2",
        "Year 2 Semester 1": "Semester 3",
        "Year 2 Semester 2": "Semester 4",
        "Year 2 Summer School": "Semester 4.5",
        "Year 3 Semester 1": "Semester 5",
        "Year 3 Semester 2": "Semester 6",
        "Year 3 Summer School": "Semester 6.5",
        "Year 4 Semester 1": "Semester 7",
        "Year 4 Semester 2": "Semester 8"}


def calc_cgpa(gps, cds):
    try:
        return round(sum(gps)/sum(cds), 2)
    except ZeroDivisionError:
        st.warning("👀 Herh! select a semester")


def cum_gpa():

    st.title("Cumulative GPA Calculator")

    sem = st.multiselect("Select Semesters", sems.keys())

    st.markdown("<hr>", unsafe_allow_html=True)
    st.info("Kindly have your transcript opened to get the necessary data to fill out the fields.")
    with st.expander("Calculator"):
        l, m, r = st.columns(3)
        x = 0
        cds = []
        gps = []
        for i in sem:
            l.text_input("Semester", value=i)
            credit = m.slider("Semester Credit(s)", min_value=1.0, max_value=5.5, step=0.5, key=x)
            cds.append(credit)
            gpa = r.number_input("Semester GPA", min_value=0.00, max_value=4.00, step=0.01, key=x)
            gps.append(round(gpa*credit, 2))
            x += 1
        st.markdown("\n\n\n")

        ll, mm, rr = st.columns(3)
        confirm = ll.button("Calculate CGPA")

        if confirm:
            value = calc_cgpa(gps, cds)

            with rr:
                try:
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
                except:
                    st.markdown("")
                    
        st.markdown("\n\n")









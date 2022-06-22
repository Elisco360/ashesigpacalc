import math

import annotated_text
import streamlit as st


def target():
    st.title("Target GPA Calculator")

    st.info("This calculator allows you to set a target and tells you what you need to achieve that target")

    st.markdown("<hr>", unsafe_allow_html=True)

    x, y = st.columns([7, 3])

    major = st.selectbox("Major", ["📈 Business Administration", "💼 Management Information Systems",
                                   "🧑🏽‍💻 Computer Science", "🤖 Computer Engineering",
                                   "⚡ Electrical Engineering",
                                   "👨🏿‍🔧 Mechanical Engineering"])

    required_credits = 0
    if major == "📈 Business Administration" or major == "💼 Management Information Systems" or \
            major == "🧑🏽‍💻 Computer Science":
        pre_c = st.checkbox("Pre-Calculus track")
        if pre_c:
            required_credits = 34.5
        else:
            required_credits = 33.5
        manipulate(required_credits)
    elif major == "🤖 Computer Engineering" or major == "⚡ Electrical Engineering" or major == "👨🏿‍🔧 Mechanical Engineering":
        pre_c = st.checkbox("Calculus track")
        if pre_c:
            required_credits = 36.5
        else:
            required_credits = 35.5
        manipulate(required_credits)


def calc(curr_gpa, curr_cds, r_cds, t_gpa, rm_cds):
    val = ((t_gpa * r_cds) - (curr_gpa * curr_cds)) / rm_cds
    return val


def manipulate(r_cds):
    st.markdown("\n\n\n")
    l, r = st.columns(2)
    curr_gpa = l.number_input("Current CGPA", min_value=0.00, max_value=4.00, step=0.01)
    curr_cds = r.number_input("Number of credits that correspond the provided current CGPA ", min_value=0.0,
                              max_value=34.5, step=0.5)
    t_gpa = l.number_input("Target CGPA", min_value=0.00, max_value=4.00, )
    rm_cds = r.number_input("Remaining Credits till Graduation", value=(r_cds - curr_cds), disabled=True)

    st.markdown("\n\n\n")

    ll, mm, rr = st.columns(3)
    confirm = ll.button("Calculate")

    if confirm:
        value = calc(curr_gpa, curr_cds, r_cds, t_gpa, rm_cds)
        rgpa = value
        st.markdown("\n\n\n")
        with rr:
            annotated_text.annotated_text(annotated_text.annotation(str(round(value, 2)), "REQUIRED GPA OVER " + str(
                rm_cds) + " CREDITS TO ATTAIN " + str(round(t_gpa, 2)), background="#e6ffff",
                                                                    color="black", font_size="22px"))

        if round(value, 2) > 4.00:
            val = round(((rm_cds * 4.0) + (curr_gpa * curr_cds)) / r_cds, 2)
            r_gpa = val
            st.warning("Since the required GPA for your target is out of scale, note that the highest GPA you can "
                       "attain is **" + str(val) + "**")
            st.caption("(Assuming you make straight A/A+ for all your remaining " + str(rm_cds) + " credits)")
        else:
            mini = minim(rm_cds, rgpa)
            st.info("You need a maximum of **"+str(mini[0])+" "+mini[1]+"s** to get the required GPA.")


def minim(rcds, rgpa):
    g = ["B+", "B", "C+", "C", "D+", "D", "E"]
    x = rcds * rgpa
    y = rcds * 4
    z = y - x
    a = z / 0.5

    n = a
    t = 1
    while a > rcds:
        a = n * 0.5 / (t - 0.5)
        t += 1
    return [math.floor(abs(a)), g[(t - 1)]]

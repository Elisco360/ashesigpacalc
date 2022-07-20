import streamlit as st


def use():

    st.header("How to use")

    project = st.tabs(["Semester GPA Calculator", "Cumulative GPA Calculator", "Target GPA Calculator"])

    with project[0]:
        st.markdown("""
        ### Overview
        > This calculator allows a student to select a course depending on their major and select a grade 
        > and calculates their grade point average. Assuming that the user want to compute their GPA for a specific 
        > semester, the **Semester GPA Calculator** restricts the number of courses to six, or a maximum of 5.5 credits, as 
        > mandated by Ashesi. 
                
        ### Usage
        
         - Select your **major**.
         - Enter the **number of courses** you want to calculate for. 
            > *Feel free to use the `plus` and `minus` buttons.*
         - Open the expander below and fill out the fields.
         - Click on the **`Calculate` button** to display your GPA.
        
        ### Some Benefits
        
         - The student can estimate a likely GPA by simulating grades and courses in order to make educated decisions.
         - The student can take a test to determine their expected GPA at the conclusion of the semester based on their expected grades.
         - The student can prepare for a semester with a GPA target in mind in terms of the grades they hope to achieve.
         
        """)

    with project[1]:
        st.markdown("""
                ### Overview
                > This calculator allows the selection of multiple semesters, followed by the entry of the number of 
                > credits earned and gpa for each semester.
                
                ### Usage

                 - Select your **major**.
                 - Enter the **number of courses** you want to calculate for. 
                    > *Feel free to use the `plus` and `minus` buttons.*
                 - Open the expander below and fill out the fields.
                 - Click on the **`Calculate` button** to display your GPA.

                """)

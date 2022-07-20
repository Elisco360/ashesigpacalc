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
            > - Select a course from the dropdown.
            > - Select a grade corresponding to the selected course.
         - Click on the **`Calculate GPA` button** to display your GPA.
         
        """)

    with project[1]:
        st.markdown("""
                ### Overview
                
                > This calculator allows the selection of multiple semesters, followed by the entry of the number of 
                > credits earned and gpa for each semester.
                
                ### Usage

                 - Select as many semesters as from the dropdown.
                    > You can also take out a semester by clicking the `close` attached to the selected semesters.
                 - Open the expander and fill out the fields.
                    > - **Drag** to set the number of credits for the corresponding semester.
                    > - Enter the GPA for the semester.
                 - Click on the **`Calculate CGPA` button** to display your Cumulative GPA.

                """)

        with project[2]:
            st.markdown("""
                ### Overview
                
                > This calculator allows a student to determine what GPA they need to achieve over a specific number of credits
                > in order to reach a desired Cumulative GPA by graduation. The calculator also shows the student the 
                > benchmark of grades that can allow them achieve a the required GPA.
                
                ### Usage

                 - Select your **major**.
                    > Check the box below if it applies to you.
                 - Enter your current **Cumulative GPA**.
                 - Enter your **desired Cumulative GPA by graduation**(`target GPA`).
                    > The disabled field shows the remaining number of credits you need to graduate and cannot be altered.
                 - Click on the **`Calculate` button** to display the required GPA you need to meet your desired GPA.
                 
            """)

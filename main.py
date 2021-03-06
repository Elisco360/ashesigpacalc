import streamlit as st
from streamlit_option_menu import option_menu
from sgpa import sem_gpa
from cgpa import cum_gpa
from predictor import target
from manual import use


def main():
    st.set_page_config(page_icon='🎓', page_title='Ashesi GPA Calculator', layout="wide")
    st.markdown("<h1 style='text-align: center'>ASHESI GPA CALCULATOR</h1>", unsafe_allow_html=True)
    with st.sidebar:
        st.header("Menu")
        option = option_menu('', ['🧮 GPA Calculator', '📊 CGPA Calculator', '🔭 Target GPA Calculator', '🤔 How to use'],
                             icons=["nothing", "nothing", "nothing", "nothing"],
                             menu_icon='nothing',
                             orientation='vertical')
        st.markdown("\n\n\n\n")
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown("\n\n")
        with st.expander("Wanna talk or Need Help?"):
            st.markdown("* [Academic Advisor](mailto:emmanuel.ntow@ashesi.edu.gh)")
            st.markdown("* [Maths Center](mailto:elijah.boateng@ashesi.edu.gh)")
            st.markdown("* [Writing Center](mailto:writing@ashesi.edu.gh)")
            st.markdown("* [Peer Tutorship](https://ashesipeertutors.herokuapp.com/)")

    if option == "🧮 GPA Calculator":
        sem_gpa()
    elif option == "📊 CGPA Calculator":
        cum_gpa()
    elif option == "🔭 Target GPA Calculator":
        target()
    elif option == "🤔 How to use":
        use()


main()

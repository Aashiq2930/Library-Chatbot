import streamlit as st

from streamlit_option_menu import option_menu



import LibGuide_Route,about_book,research


st.set_page_config(page_title="Clara",page_icon="book",layout="wide")



class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        with st.sidebar:        
            app = option_menu(
                menu_title='Main Menu',
                options=["LibGuide Route", 'Know about your Book', 'Research'],
                icons=['chat-fill', 'book', 'trophy-fill', 'chat-fill', 'info-circle-fill'],
                menu_icon='cast',
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": "#F5F5F5"},
                    "icon": {"color": "#6C757D", "font-size": "15px"},
                    "nav-link": {
                        "color": "#495057", 
                        "font-size": "15px",
                        "text-align": "left",
                        "margin": "-1px",
                        "--hover-color": "#E9ECEF", 
                        "font-weight": "bold"  # Make options bold
                    },
                    "nav-link-selected": {"background-color": "#D6E4F0"},
                    "menu-title": {
                        "font-weight": "bold",  # Make the Main Menu title bold
                        "font-size": "18px",  # Optionally adjust the font size
                        "color": "#2C3E50"  # Optional: Set a specific color for the title
                    }
                }
        )

        
        if app == "LibGuide Route":
            LibGuide_Route.guide()
        if app == "Know about your Book":
            about_book.abtbook()
        if app=="Research":
            research.re()
          
             
          
             
    run()            
         
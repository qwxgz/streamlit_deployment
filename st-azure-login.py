"""
streamlit-azure-ad-login https://pypi.org/project/streamlit-azure-ad-login/

pip install streamlit-azure-ad-login

This is a React login component that help you check coonect to an endpoint that make the authentication with Azure Active Director and return the proper token.
This aproach is because the Active Directory authentication requires a lot of certifications that depends on each project.

The component allows you to personalize the following parameters:

header_text: Text that will apear on the header of the login component
authentication_endpoint_url: The active directory url to send the credentials and return the token
logo_uri: a URI with the image of your company
prefix: If you have a prefix for the login, here is where it goes
"""
# To be tested

import streamlit as st

from streamlit_azure_login import login_component

def login():
    with st.expander('Auth', expanded=True):
        token = login_component(
            header_text='Intercement', 
            authentication_endpoint_url=environ.get('AD_ENDPOINT'), 
            logo_uri=environ.get('AD_LOGO_URI'),
            prefix=environ.get('AD_PREFIX'),
        )
        if token:
            return True
        
        return False

if __name__ == '__main__':
    favicon = Image.open('src/favicon/dir.ico')
    st.set_page_config(page_icon=favicon, layout="wide")

    # 1) We start the app without token and we set it to False
    if 'token' not in st.session_state:
        st.session_state.token = False
    
    # 3) We enter to the web logic
    if st.session_state.token:
        # Here goes the dashboard logic
        st.title('Test Azure Login')
    
    # 4) We create a logout button that re run the app
    if st.sidebar.button('Logout', key='logout_1'):
            del st.session_state['token']
            token = False
            st.session_state.token = False
            st.experimental_rerun()

    # 2) We make the login and set the token to True if the login goes ok 
    # or false if goes wrong
    else:
        token = login()
        st.session_state.token = token

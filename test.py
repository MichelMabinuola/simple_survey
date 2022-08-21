import pandas as pd
import streamlit as st
import streamlit_authenticator as stauth
import yaml


st.set_page_config(layout="wide", page_icon="ambulance", page_title="MyANON MetaVerse Counselling")

row0_spacer1, row0_1, row0_spacer3 = st.columns(
    (1, 5, 1))

choice = ["",
    "Does your neck, nose, eyes and ears hurt?", "Does your tooth hurt?","Do you want to consult with a urologist?", "Do you want to consult with a gynecologist?", "Do you want to consult with a dermatologist?","other"
]

choices6 = ["","Getting better", "About the same","Getting worse","Fluctuating"]





def main():
    
    
    CONDITION=[]
    STATUS=[]
    DOB=[]
    
    row0_1.title('Analyzing your answer for better recommendation')
    

    
   
    with st.form(key='Please select an option that best describes your situation', clear_on_submit=True):
        
        condition = st.selectbox("Please select an option that best describes your situation", choice)
        
        
        status = st.selectbox("My symptoms are currently:", choices6)

        
        dob = st.date_input("Date of Birth")

        submit_button = st.form_submit_button(label='Submit')
        
        CONDITION.append(condition)
        STATUS.append(status)
        DOB.append(dob)
        
        if (len(CONDITION)>0 and CONDITION[0]!="") and (len(STATUS)>0 and STATUS[0]!=""):
            
                 
            
            if submit_button:
                for e in STATUS:
                    
                
                    for i in CONDITION:

                        if (i == "Does your neck, nose, eyes and ears hurt?") & (e!=""):

                            st.success("Thank you for filling out the form. Please access this link below to enter meet the recommended consultant")
                            st.markdown("https://zep.us/play/2bqBEd", unsafe_allow_html=True)
    #                         st.write("ENTER THE METAVERSE")

                        elif (i == "Does your tooth hurt?") & (e!=""):
                            st.success("Thank you for filling out the form. Please access this link below to enter meet the recommended consultant")
                            st.markdown("https://zep.us/play/2Yq3vJ", unsafe_allow_html=True)




                        elif (i == "Do you want to consult with a urologist?") & (e!=""):
                            st.success("Thank you for filling out the form. Please access this link below to enter meet the recommended consultant")
                            st.markdown("https://zep.us/play/y1zxWo", unsafe_allow_html=True)


                        elif (i == "Do you want to consult with a gynecologist?") & (e!=""):

                            st.success("Thank you for filling out the form. Please access this link below to enter meet the recommended consultant")
                            st.markdown("https://zep.us/play/ydWQe5", unsafe_allow_html=True)




                        elif (i == "Do you want to consult with a dermatologist?") & (e!=""):

                            st.success("Thank you for filling out the form. Please access this link below to enter meet the recommended consultant")
                            st.markdown("https://zep.us/play/2nYJ5X", unsafe_allow_html=True)


                        elif (i == "Others") & (e!=""):

                            st.success("Thank you for filling out the form. Please access this link below to enter meet the recommended consultant")
                            st.markdown("https://zep.us/play/y1zxZE", unsafe_allow_html=True)
                        
                        

                        
            
        else:
            st.write("Please, fill out the form")
       
            
          
if __name__ == '__main__':
    main()

    

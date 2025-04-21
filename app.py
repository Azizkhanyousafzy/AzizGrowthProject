#streamlit
import streamlit as st

st.set_page_config(page_title= "growth mindset project", prject)
st.title("Growth Mindset Challenge: Web Appwith Streamlit")
st.header("Welcome to Your Growth Journey!") 
st.write("A growth mindset, a term coined by psychologist Carol Dweck, refers to a cognitive and metacognitive framework wherein individuals perceive intelligence, abilities, and talents as malleable traits that can be developed over time through effort, effective strategies, and input from others. This contrasts with a fixed mindset, where such attributes are viewed as static and innate")

#Quote Section
st.header("Today's Growth Mindset Quote")
st.write("Challenges are what make life interesting. Overcoming them is what makes life meaningful")

st.header("What is Your Challenge Today")
user_input = st.text_input("Describe a Challenge You're facing:")

#codition 
if user_input:
    st.success(f" You are facing: {user_input}. Keep pushing forward towards your goal!")

else:
    st.warning("Tell us about youre challange to get started!")

    #reflexing 
    st.header("Reflect on Your Learning")
    reflection = st.text_area("Write youre reflections here")


    if reflection:
        st.success(f"Great Insight! Youre reflection: {reflection}")
    else:
        st.info("Reflecting on past experience help you grow! share youre difficultes")

        #acheivements
        st.header("Celebrate Youre Wins!")
        acheivement = st.text_input("Share Something You Have Accomplished:")

        if acheivement:
            st.success(f"Amazing You Have Acheivement: {acheivement}")

        else:
            st.info("Big or small, every achivement counts! Share one now 💫")

            #footer
            st.write("- - -")
            st.write("☄️Keep believing in yourself. Growth is a journey, not a distination!☪")
            st.write("**𓇻Created by Aziz Ullah Khan Yousafzai**")

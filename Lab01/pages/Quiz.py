
import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Coffee Personality Quiz", page_icon="☕")

st.title("What Type of Coffee Are You? ☕")
st.write("Answer these questions to find out your ideal coffee!")

icedlatte_img = "images/icedlatte.jpg"
cortado_img = "images/cortado.jpg"
espresso_img = "images/espresso.jpg"
coldfoam_img = "images/coldfoam.jpg"

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.image("images/icedlatte.jpg", width=200)
    st.caption("icedlatte")
with col2:
    st.image("images/cortado.jpg", width=200)
    st.caption("cortado")
with col3:
    st.image("images/espresso.jpg", width=200)
    st.caption("espresso")
with col4:
    st.image("images/coldfoam.jpg", width=200)
    st.caption("coldfoam")

st.divider()

icedlatte = 0
cortado = 0
espresso = 0
coldfoam = 0

st.subheader("Question 1")
q1 = st.radio(  #NEW
    "How do you spend your mornings:",
    ["Slow morning/work from home", "Fast paced and productive", "What are mornings? ", "Something different every day"]
)
if q1 == "Slow morning/work from home":
    icedlatte += 2
elif q1 == "Fast paced and productive":
    cortado += 2
elif q1 == "What are mornings?":
    espresso += 2
else:
    coldfoam += 2

st.subheader("Question 2")
q2 = st.multiselect(  #NEW
    "Choose up to 3 things you love:",
    ["Routine", "Workout classes", "Aesthetic vibes", "Trying new things", "Sweet treats", "Drawing/Paiting", "Baking" ],
    max_selections=3
)
if "Routine" in q2 or "Workout classes" in q2:
    icedlatte += 2
if "Trying new things" in q2 or "Drawing/Paiting" in q2:
    cortado += 2
if "Hiking" in q2:
    espresso += 2
if "Sweet treats" in q2 or "Baking" in q2 :
    coldfoam += 2

st.subheader("Question 3")
q3 = st.number_input(  #NEW
    "How many hours of sleep did you get last night?",
    min_value=0,
    max_value=14,
    value=7,
    step=1
)
if q3 <= 5:
    cortado += 2
elif q3 <= 7:
    espresso += 2
else:
    coldfoam += 2

st.subheader("Question 4")
q4 = st.selectbox( 
    "Pick your study spot: ",
    ["Clough 3rd or 4th floor", "Crossland quiet 6 and 7th floor", "My dorm", "Student Center"]
)
if q4 == "Clough 3rd or 4th floor":
    icedlatte += 2
elif q4 == "Crossland quiet 6 and 7th floor":
    cortado += 2
elif q4 == "My dorm":
    espresso += 2
else:
    coldfoam += 2

st.subheader("Question 5")
q5 = st.slider(  #NEW
    "How much do you like trying new flavors?",
    0, 10, 5
)
if q5 >= 7:
    coldfoam += 2
elif q5 <= 3:
    espresso += 2
else:
    icedlatte += 1
    cortado += 1

st.divider()

total = icedlatte + cortado + espresso + coldfoam
st.progress(min(total / 12, 1.0))  #NEW

if st.button("Get my result!"):
    scores = {
        "icedlatte": icedlatte,
        "cortado": cortado,
        "espresso": espresso,
        "coldfoam": coldfoam
    }

    top_score = max(scores.values())
    winners = [k for k, v in scores.items() if v == top_score]
    result = winners[0]

    st.subheader("Your Result ☕")
    st.write("**Your scores:**", scores)

    if len(winners) > 1:
        st.info(f"Tie! You match: **{', '.join(winners)}** (showing the first one)")

    if result == "icedlatte":
        st.image("images/icedlatte.jpg", width=300)
        st.success("**You are an Iced Latte!** Cozy, reliable, and you bring calm energy.")
        st.metric("IcedLatte Points", icedlatte)  
                 
    elif result == "Cortado":
        st.image("images/cortado.jpg", width=300)
        st.success("**You are Cortado!** Chill, fun, and you’re always up for plans.")
        st.metric("Cortado Points", cortado)  
        
    elif result == "Espresso":
        st.image("images/espresso.jpg", width=300)
        st.success("**You are an Espresso!** Bold, intense, and you get things done.")
        st.metric("Espresso Points", espresso) 
    else:
        st.image("images/coldfoam.jpg", width=300)
        st.success("**You are a Coldfoam Latte!** Unique, creative, and you like doing things your own way.")
        st.metric("coldfoam Points", coldfoam)  

    st.balloons()  #NEW

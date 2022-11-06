import pandas as pd
import streamlit as st
import altair as alt
import numpy as np

st.write("Do you like bees?")
yes=st.checkbox("Yes!")
no=st.checkbox("No!")

if yes:
    st.write("Cool! Me too! Let's take a closer look at bees!")
    st.balloons()
if no:
    st.write("That's too bad. Let's take a closer look and learn some more")
#else: "Select Yes or No to continue"


st.write("What do you like best about bees?")
honey=st.checkbox('Honey')
pollination=st.checkbox('Pollination')
bee=st.checkbox('Bees are cool')
no=st.checkbox("I told you I don't like bees")

if honey:
    st.write("Yum! The average honey bee will make ~1/12 of a tsp of honey in its lifetime")
    st.image("honey.jpg")
if pollination:
    st.write("honey bees contribute over $15B to the value of US crop production")
    st.image("flower.jpg")
if bee:
    st.write('They sure are!Bees huddle together and buzz within their hive during the winter to survive')
    #st.info('This is a purely informational message', icon="ℹ️")
    st.image("hive.jpg")
    st.snow()

   
if no:
    st.write("You're missing out, bees are the bees knees")
    st.image("bees_knees.jpg")

#else:"Let's move on"
st.header("Data on Bee Colony Loss")
st.markdown("Below is a dataset from Bee Informed Partners examing bee colony losses from 2007-2019/n")
st.header('BIP Colony Loss Data')
bee_data=pd.read_csv("BIP_data.csv")
st.write(bee_data)




st.markdown("After skimming through the data let's exmaine it in an interactive chart!")

st.sidebar.header("Pick two variables for your barchart")
x_val=st.sidebar.selectbox("Pick your x axis", bee_data.columns.tolist())
y_val=st.sidebar.selectbox("Pick your y axis", bee_data.select_dtypes(include=np.number).columns.tolist())

st.sidebar.header("Year Filter")
#filtered_df=df_filter("Select the year to filter the data",bee_data)

st.sidebar.multiselect(
    "select the year:",
    options=bee_data["Year"].unique(),
    default=bee_data["Year"].unique(),
)
st.sidebar.header('State Filter')
st.sidebar.multiselect(
    "select the State:",
    options=bee_data["State"].unique(),
    default=bee_data["State"].unique(),
)
st.sidebar.header('Region Filter')
st.sidebar.multiselect(
    "select the Region:",
    options=bee_data["Region"].unique(),
    default=bee_data["Region"].unique(),
)

#color_scale = alt.Scale(
    #domain=domains,
    #range=['rgb(5,0,200)', 'rgb(14,181,164)', 'rgb(3,9,193)', 'rgb(191,31,49)']

bar = alt.Chart(bee_data, title=f"{x_val} and {y_val}").mark_bar().encode(
    alt.X(x_val,title=f"{x_val}"),
    alt.Y(y_val,title=f"{y_val}"),
    tooltip=(x_val,y_val),
   # color='rgb(5,0,200)'
    #alt.Shape('animal:N', legend=None, scale=shape_scale),
   # alt.Color('animal:N', legend=None, scale=color_scale),
)
st.altair_chart(bar, use_container_width=True)
#st.plotly_chart(bar)


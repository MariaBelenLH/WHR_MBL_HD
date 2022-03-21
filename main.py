import streamlit as st


header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

with header:
	st.title("World Happiness Report")
	st.text("blah blah")


with dataset:
	st.header("World Happiness Report Dataset")


with features:
	st.header("Features")

with model_training:
	st.header("Training the model")
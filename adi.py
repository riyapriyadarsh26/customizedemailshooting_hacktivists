import streamlit as st

# Title
st.title("Simple Streamlit UI")

# Header
st.header("This is a header")

# Subheader
st.subheader("This is a subheader")

# Text
st.write("This is some text.")

# Markdown
st.markdown("You can use **Markdown** for formatting.")

# Display an image
st.image("your_image.png", caption="This is an image")

# Display a video
st.video("your_video.mp4")

# Sidebar
st.sidebar.header("Sidebar Header")
st.sidebar.write("This is the sidebar content")

# Adding a slider
slider_value = st.slider("Select a value", 0, 100, 50)

# Adding a button
if st.button("Click me"):
    st.success("Button clicked!")

# Adding a checkbox
if st.checkbox("Check this box"):
    st.write("Checkbox is checked")

# Adding a selectbox
option = st.selectbox("Choose an option", ["Option 1", "Option 2", "Option 3"])
st.write("You selected:", option)

# Adding a radio button
radio_option = st.radio("Choose one option", ["Radio 1", "Radio 2", "Radio 3"])
st.write("You selected:", radio_option)

# Text input
text_input = st.text_input("Enter some text:")
st.write("You entered:", text_input)

# Number input
number_input = st.number_input("Enter a number:")
st.write("You entered:", number_input)

# Text area
text_area = st.text_area("Enter a long text:")
st.write("You entered:", text_area)

# Date input
date_input = st.date_input("Select a date")
st.write("You selected:", date_input)

# Time input
time_input = st.time_input("Select a time")
st.write("You selected:", time_input)

# File uploader
uploaded_file = st.file_uploader("Upload a file", type=["csv", "txt"])
if uploaded_file is not None:
    st.write("File uploaded:", uploaded_file)

# Progress bar
import time
with st.spinner("In progress..."):
    time.sleep(5)
    st.success("Done!")

# Display data in a table
import pandas as pd
data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 22]
})
st.write("Data in a table:")
st.write(data)

# Plotting
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 10, 100)
y = x**2
st.pyplot(plt.plot(x, y))

# Map
st.map(data)

# Latex
st.latex(r'\alpha^2 + \beta^2 = \gamma^2')

# Display raw code
st.code("print('Hello, Streamlit!')")

# Display JSON
st.json({"name": "John", "age": 30})

# Show a progress bar
import time
progress_bar = st.progress(0)
for i in range(100):
    progress_bar.progress(i + 1)
    time.sleep(0.01)

# Expander
with st.beta_expander("Click to expand"):
    st.write("This is hidden by default")

# Display an HTML component
st.write("You can also use HTML:")
st.markdown("<a href='https://www.streamlit.io/'>Streamlit Official Website</a>", unsafe_allow_html=True)

# Adding a footer
st.text("This is the footer")

# Add a link to the official Streamlit documentation
st.markdown("[Streamlit Documentation](https://docs.streamlit.io/0.88.0/)")

import streamlit as st

st.title('Text App')
st.header('Arbeiten mit Text')
st.subheader('Wir schreiben heute etwas')

# Displaying Text
st.write('With this method we can write simple texts in Streamlit')
st.write('Wir können viele Zeilen an Text schreiben...')

zitat = "Cogito ergo sum"
# Write fixed-width and preformatted text.
st.text('Ein Zitat für heute: "{}"'.format(zitat))

# Write arguments to the app
# "This is the Swiss Army knife of Streamlit commands" 
#  st.write() also accepts other data formats, such as numbers, data frames, styled data frames, and assorted objects:
st.write('Ein Zitat für heute: "{}"'.format(zitat))
# It is not only for text
st.write(10*11)
import streamlit as st
import pandas as pd

# Define a function to create the first page
def page1():
    # Create a Pandas dataframe with 5 rows of data
    data = {'Name': ['John', 'Mary', 'David', 'Samantha', 'Michael'],
            'Age': [28, 23, 31, 25, 29],
            'Salary': [50000, 60000, 70000, 55000, 65000]}
    df = pd.DataFrame(data)

    # Show the dataframe
    st.header('Page 1 - Simple Pandas Dashboard')
    st.markdown("""<style>.stTable td {padding: 10px;}</style>""", unsafe_allow_html=True)
    st.dataframe(df)

    # Show summary statistics
    st.header('Summary Statistics')
    st.markdown("""<style>.stMarkdown {padding: 10px; margin-top: 20px; margin-bottom: 20px;}</style>""", unsafe_allow_html=True)
    st.write(df.describe())

# Define a function to create the second page
def page2():
    # Create a simple chart
    chart_data = pd.DataFrame(
        [['John', 28], ['Mary', 23], ['David', 31], ['Samantha', 25], ['Michael', 29]],
        columns=['Name', 'Age'])
    st.header('Page 2 - Simple Chart')
    st.bar_chart(chart_data.set_index('Name'))

# Define the main function to run the app
def main():
    # Set the page configuration
    st.set_page_config(page_title='Simple Streamlit Dashboard',
                       page_icon=':bar_chart:',
                       layout='wide',
                       initial_sidebar_state='auto')

    # Create a dictionary of page names and their corresponding functions
    pages = {
        'Page 1': page1,
        'Page 2': page2
    }

    # Create a Streamlit app with a sidebar to select the page
    st.sidebar.title('Select a page')
    selection = st.sidebar.radio('', list(pages.keys()))

    # Run the selected page
    pages[selection]()

if __name__ == '__main__':
    main()



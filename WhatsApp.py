# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 09:58:08 2023

@author: Alex
"""

### ----- WHATSAPP CHAT APP -----

# Import libraries
import streamlit as st
import pandas as pd
from io import StringIO
#from PIL import Image

# Layout of application
st.set_page_config(layout="wide")

# Wrap everything into a function to avoid errors while waiting to select a file
try:
    # Header of app
    st.title('WhatsApp Parse Application')
        
    # Paragraph
    st.write("""
             Welcome to the WhatsApp message parse application. This application offers users
             the ability to clean their exported WhatsApp chat messages. 
                
             Embark on an interactive explortion of your WhatsApp chat messages with 
             Streamlit.
             
             From there, visualise your data in Python, Tableau, Power BI or other software
             technologies of your choice.
             """)

    # How to use App
    st.subheader('How to use this application?')

    # Paragraph
    st.write("""
             Inside your WhatsApp application, **press and hold** on a message exchange
             with one of your contact. Once the message is highlighted, navigate to
                 
             the top right and press the **three** button to bring up the next option. Download
             the chat message as a **text** file (.txt). 
                 
             You can choose to **include media messages or not** before exporting the file. 
                 
             Convert this .txt file into a csv.
             """)
             
    # File uploader widget
    upload_file = st.file_uploader("**Upload your csv file**", type=["csv"])

    df = pd.read_csv(upload_file, header=None, sep=',')
    #df = pd.read_csv(upload_file, header=None, error_bad_lines=False, sep=',')

    ### ----- DATA PREP -----
    
    # Remove the first row
    df = df.iloc[1:]
    
    # Rename columns
    #df.rename(columns = {'0':'Date1', '1':'Test', 
    #                     '2':'Text'}, inplace = True) 
    
    df.set_axis(['Date1', 'Test', 'Text'], axis='columns', inplace=True)
        
    # Create a new field and name the field 'Date'
    df[['Date', 'Time']] = df['Date1'].str.split(',', expand=True)
    
    # Drop columns
    df = df.drop(columns=['Date1', 'Time'])
    
    # Create a new field and name the field 'Date'
    df[['Time', 'User']] = df['Test'].str.split('-', expand=True)
    
    # Drop columns
    df = df.drop(columns=['Test', 'Time'])
    
    # Drop the rows where all data is empty ('na')
    df = df.dropna()

    # Rename the file values in the 'Content' column
    df.loc[df['Text'].str.contains('(file attached)'), 'Text'] = 'media file'
    
    
    #df[['Date']] = df[1].str.split('-', 1, expand=True)
    #df['Date'] = df[0]

    # Drop the previous Date field
    #df = df.drop(columns=0)

    # Create a new column called 'Time' and number 2 by splitting column 1 on the '-' object.
    #df[['Time', 2]] = df[1].str.split('-', 1, expand=True)

    # Drop the previous 1 field
    #df = df.drop(columns=1)

    # Create a new column called 'Name' and 'Content' by splitting column 2 on the ':' object.
    #df[['Name', 'Content']] = df[2].str.split(':', 1, expand=True)

    # Merge columns 3 and Content
    #df['Message'] = df['3'] + ' ' + df['Content']

    # Drop the previous 2 field
    #df = df.drop(columns=2)

    # Drop the rows where all data is empty ('na')
    #df = df.dropna()

    # Rename the file values in the 'Content' column
    #df.loc[df['Content'].str.contains('(file attached)'), 'Content'] = 'media file'

    # Show/Hide button
    #show_df = st.checkbox("Show Dataframe")

    # Display the Dataframe if checkbox is checked
    #if show_df:
    #        st.write(df)

    # Dataframe header
    st.subheader('Dataframe')

    # Paragraph
    st.write("""
             If media was included in the export, the value shown as **media file** was 
             standardised from all random names of the files exported.
             """)
             
    st.write(df)










   
# Read contents
#text_content_bytes= data_file.read()
    
# Decode the bytes to a string
#text_content_str = text_content_bytes.decode("utf-8")
    
# Convert text to CSV
#csv_content = StringIO(text_content_str)
#data = pd.read_csv(csv_content, delimiter='\t')
   
# Display original df
#st.write("Original df:")
    
# Add columns to file
#data.columns = ['Content']

### ----- DATA PREP -----
    
# Create a single Time column
#data[['Time', 'Details']] = data['Rest'].str.split('-', 1, expand=True)

# Create a user column
#data[['User', 'Contents']] = data['Details'].str.split(':', 1, expand=True)

# Drop columns
#data = data.drop(columns=['Content', 'Rest', 'Details'])

# Drop the rows where all data is empty ('na')
#data = data.dropna()

# Rename the file values in the 'Content' column
#data.loc[data['Contents'].str.contains('(file attached)'), 'Contents'] = 'media file'
      
# Save the Dataframe a CSV
#df = data.to_csv(index=False)

### ----- DATA PREP -----
    
    #st.write(df)
    
    # Display CSV content
    st.write("**Download CSV file**")
    #st.write(pd.read_csv(StringIO(df)))
        
    ### ----- DOWNLOAD CSV FILE -----
    
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button(
        "Press to Download",
        csv,
        "Clean_WhatsApp_file.csv",
        "text/csv",
        key='download-csv'
        )
        
except Exception:
    pass
    
    
    

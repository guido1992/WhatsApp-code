# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 09:58:08 2023

@author: Alex
"""

### ----- WHATSAPP CHAT APP -----

# Import libraries
import streamlit as st
import pandas as pd
#from PIL import Image

# Layout of application
st.set_page_config(layout="wide")

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

# Upload file to read data
st.subheader("Dataset")
data_file = st.file_uploader("Upload your text file below...", type=["txt"])

#uploaded_file = st.file_uploader("Upload your file here...", type=['txt'])

if data_file is not None:
    file_details = {"filename":data_file.name, "filetype":data_file.type,
                    "filesize":data_file.size}
    
df = pd.read_csv(data_file)
#df = pd.read_csv(data_file, header=None, error_bad_lines=False, sep=',')

### ----- DATA PREP -----

# Create a new field and name the field 'Date'
df['Date'] = df[0]

# Drop the previous Date field
df = df.drop(columns=0)

# Create a new column called 'Time' and number 2 by splitting column 1 on the '-' object.
df[['Time', 2]] = df[1].str.split('-', 1, expand=True)

# Drop the previous 1 field
df = df.drop(columns=1)

# Create a new column called 'Name' and 'Content' by splitting column 2 on the ':' object.
df[['Name', 'Content']] = df[2].str.split(':', 1, expand=True)

# Merge columns 3 and Content
#df['Message'] = df['3'] + ' ' + df['Content']

# Drop the previous 2 field
df = df.drop(columns=2)

# Drop the rows where all data is empty ('na')
df = df.dropna()

# Rename the file values in the 'Content' column
df.loc[df['Content'].str.contains('(file attached)'), 'Content'] = 'file'

# Show/Hide button
#show_df = st.checkbox("Show Dataframe")

# Display the Dataframe if checkbox is checked
#if show_df:
#    st.write(df)

# Dataframe header
st.subheader('Dataframe')

# Paragraph
st.write("""
         If media was included in the export, the value shown as **file** was standardised
         from all random names of the files exported.
         """)

# Show df
st.write(df)

### ----- DOWNLOAD CSV FILE -----

def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')

csv = convert_df(df)

# Paragraph
st.write('**Download CSV file**')

st.download_button(
   "Press to Download",
   csv,
   "Clean_WhatsApp_file.csv",
   "text/csv",
   key='download-csv'
)
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
    
#df = pd.read_csv(data_file, header=None, error_bad_lines=False, sep=',')
    
# Read contents
text_content_bytes= data_file.read()
    
# Decode the bytes to a string
text_content_str = text_content_bytes.decode("utf-8")
    
# Convert text to CSV
csv_content = StringIO(text_content_str)
data = pd.read_csv(csv_content, delimiter='\t')
   
# Display original df
#st.write("Original df:")
    
# Add columns to file
data.columns = ['Content']

### ----- DATA PREP -----
    
# Create a single Date column
#data[['Date', 'Rest']] = data['Content'].str.split(',', 1, expand=True)

# Create a single Time column
#data[['Time', 'Details']] = data['Rest'].str.split('-', 1, expand=True)

# Create a user column
#data[['User', 'Contents']] = data['Details'].str.split(':', 1, expand=True)

# Drop the 'Rest' column
#data = data.drop(columns=['Content', 'Rest', 'Details'])

# Drop the rows where all data is empty ('na')
#data = data.dropna()

# Rename the file values in the 'Content' column
#data.loc[data['Contents'].str.contains('(file attached)'), 'Contents'] = 'media file'
      
# Save the Dataframe a CSV
df = data.to_csv(index=False)

# Show/Hide button
#show_df = st.checkbox("Show Dataframe")

# Display the Dataframe if checkbox is checked
#if show_df:
#    st.write(df)

#st.write(data)
    
# Dataframe header
st.subheader('Dataframe')

# Paragraph
st.write("""
         If media was included in the export, the value shown as **media file** was 
         standardised from all random names of the files exported.
         """)

# Display CSV content
#st.write("Download CSV:")
st.write(pd.read_csv(StringIO(df)))

### ----- DOWNLOAD CSV FILE -----

csv = df.to_csv(index=False)
#csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    "Press to Download",
    csv,
    "Clean_WhatsApp_file.csv",
    "text/csv",
    key='download-csv'
)
    
    
    

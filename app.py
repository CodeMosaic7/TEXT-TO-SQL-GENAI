from dotenv import load_dotenv
import streamlit as st
import os
import sqlite3
import google.generativeai as genai

load_dotenv()

# Config Genai API key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Function to load Google Gemini Model and provide queries as response
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    # print(response)
    return response.text
# function to retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    # print("Executing SQL:", sql)
    rows=cur.fetchall()
    # print(rows)
    for row in rows:
        print("Row:", row)  # Debugging line
    # conn.commit()
    conn.close()
    return rows
    
    

# Most important step:Defining the prompt.
prompt=["""
You are an expert in converting English questions to SQL query!
The SQL database has the name STUDENT and has following columns- NAME, CLASS, SECTION \n\n For example 1-How many entries are present?
the SQL command will be like this SELECT COUNT(*) FROM STUDENT;
\n Example 2- Tell me the students studying in Data Science class?,
the SQL command will be something like this SELECT * FROM STUDENT WHERE CLASS='DATA SCIENCE';
also the sql code should not have ``` in the beginning or end and sql word in the output
"""]

# Streamlit App
st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Gemini App to Retrieve the SQL Data")

question=st.text_input('Input:',key='input')
submit=st.button("Ask the question")

# if submit is clicked
if submit and question:
    data=get_gemini_response(question,prompt)
    # print(data)
    response=read_sql_query(data,"C:\\Users\\hp\\OneDrive\\Desktop\\CODES\\PROJECTS\\TEXT-TO-SQL\\student.db")
    st.subheader("The response is:")
    # print(response)
    for row in response:
        st.write(row)
        # st.header(row)




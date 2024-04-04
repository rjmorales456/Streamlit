import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
import seaborn as sns
import holoviews as hv
import hvplot.pandas
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
warnings.filterwarnings('ignore')

with st.container():
    st.title("Latest Data Science Job Salaries 2020 - 2024")
    st.write("Credit by: SAURABH BADOL")
    st.write("EDA: Regolo Jerard L. Morales")
    st.write("Dataset Link: https://www.kaggle.com/datasets/saurabhbadole/latest-data-science-job-salaries-2024")
    st.write("Description: This dataset provides insights into data science job salaries from 2020 to 2024, including information on experience levels, employment types, job titles, and company characteristics. It serves as a valuable resource for understanding salary trends and factors influencing compensation in the data science field.")
    
job_salaries = pd.read_csv("Job_salaries/Latest Data Science Job Salaries 2020 - 2024/DataScience_salaries_2024.csv")

# Total Count Year
with st.container():
    
    st.header('Work Year Distribution',divider="gray")
    year_count = job_salaries['work_year'].value_counts()

    year_count_df = year_count.reset_index()
    year_count_df.columns = ['Work Year', 'count']
    
    st.bar_chart(year_count_df,x='Work Year', y='count',color='#AEC6CF',use_container_width=True)
    
    # fig1 = px.bar(year_count_df, x='work_year', y='count', color_discrete_sequence=['#AEC6CF'],title='Work Year Count', labels={'work_year': 'Work Year', 'count': 'Job Count Per Year'},)

    # # Show the plot
    # st.plotly_chart(fig1)
    
    st.write("""
             The Graph shows the work years for the past 5 years. And is showed that in 2023 has the highest count for the most works that are being distributed with the total of 8519.
             """)
    
# Total Salaries of Work Year
with st.container():
    st.header('Total Salary by Work Year',divider="gray")
    
    # Work Count By Salary

    year_salary = job_salaries.groupby('work_year')['salary'].sum().sort_values()

    year_salary_df = year_salary.reset_index()
    year_salary_df.columns = ["Work Year","Salary"];
    
    st.bar_chart(year_salary_df,x='Work Year', y='Salary',color='#AEC6CF',use_container_width=True)
    
    # Create a bar chart using Plotly Express (px.bar)
    # fig2 = px.bar(year_salary_df, x='work_year', y='salary', title='Total Salary Per Work Year',
    #             labels={'work_year': 'Work Year', 'salary': 'Total Salary'},color_discrete_sequence=['#AEC6CF'])
    # st.plotly_chart(fig2)
    st.write("""
             The Graph shows the total salary over the past 5 years of work. The graph shows that the year 2023 has the highest total among the 5 with the total of 1.36 Billion.
             """)
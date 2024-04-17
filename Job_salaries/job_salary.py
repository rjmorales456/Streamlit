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
    
    st.bar_chart(year_count_df,x='Work Year', y='count',color='#00435c',use_container_width=True)
    
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
    
    st.bar_chart(year_salary_df,x='Work Year', y='Salary',color='#00435c',use_container_width=True)
    
    st.write("""
             The Graph shows the total salary over the past 5 years of work. The graph shows that the year 2023 has the highest total among the 5 with the total of 1.36 Billion.
             """)
    
# Experience Level Distribution
with st.container():
    st.header('Experience Level Distribution',divider="gray")
    
    exp_level = job_salaries['experience_level'].value_counts()
    fig = px.pie(exp_level, values=exp_level.values, names=exp_level.index,
                color_discrete_sequence=['#00435c','#006971','#008c59','#81a51c','#ffa600'])

    # Show the plot
    st.plotly_chart(fig,use_container_width=True)

# Employment Type Distribution
with st.container():
    st.header('Employment Type Distribution',divider="gray")
    
    employment_type = job_salaries['employment_type'].value_counts()
    employment_type_df = employment_type.reset_index()
    employment_type_df.columns = ['Employment Type', 'Count']
    
    total_jobs = employment_type_df['Count'].sum()
    employment_type_df['Percentage'] = (employment_type_df['Count'] / total_jobs) * 100

    employment_type_df['Percentage'] = employment_type_df['Percentage'].map('{:.2f}%'.format)
    
    employment_type_df['Count'] = employment_type_df['Count'].map('{:,.0f}'.format)
    
    st.table(employment_type_df)
    
# Work Year and Experience
with st.container():
    st.header('Experience Level Distribution by Work Year',divider="gray")

    year_experience = job_salaries.groupby(['work_year','experience_level']).size().unstack()
    year_experience_df = year_experience.reset_index()

    fig = px.bar(year_experience_df,y='work_year',x=['EN', 'EX', 'MI', 'SE'],barmode='stack',orientation =  'h',color_discrete_sequence=['#00435c','#006971','#008c59','#81a51c','#ffa600'],labels={'work_year': 'Work Year', 'value': 'Count', 'variable': 'Experience Level'})

    st.plotly_chart(fig,use_container_width=True)

# Top Job TItles
with st.container():
    st.header('Most Sought out Job in Data Science',divider="gray")

    job_title = job_salaries.groupby(['job_title']).size().nlargest(10)
    job_title_df = job_title.reset_index()
    job_title_df.columns = ['Job Title', 'Count']
    
    job_title_df['Count'] = job_title_df['Count'].map('{:,.0f}'.format)
    st.table(job_title_df)
    
# Highest Paying Job Title
with st.container():
    # High Paying Job TItle
    
    st.header('Highest Salary for Data Science 2020 - 2024',divider="gray")
    
    selected_year = st.selectbox('Select Year', sorted(job_salaries['work_year'].unique()), index=len(job_salaries['work_year'].unique())-1)
    
    # Filter data based on selected year
    filtered_data = job_salaries[job_salaries['work_year'] == selected_year]
    
    highest_job_title = filtered_data.groupby(['job_title'])['salary'].sum().nlargest(10)
    highest_job_title_df = highest_job_title.reset_index()
    
    highest_job_title_df['salary'] = highest_job_title_df['salary'].map('{:,.0f}'.format)
    highest_job_title_df.columns = ['Job Title', 'Salary']
    
    st.table(highest_job_title_df)
    
# Work Title and Experience by Salary
with st.container():
    st.header('Job Title and Experience Levely by Salary 2020 - 2024',divider="gray")
    
    selected_year = st.selectbox('Select Year', sorted(job_salaries['work_year'].unique()), index=len(job_salaries['work_year'].unique())-1,key='title_experience')
    
    # Filter data based on selected year
    filtered_data = job_salaries[job_salaries['work_year'] == selected_year]
    
    # Work Title and Experience Level by Salary
    title_experience = filtered_data .groupby(['job_title','experience_level'])['salary'].sum().nlargest(10)
    top_title_experience_df = title_experience.reset_index()
    top_title_experience_df['salary'] = top_title_experience_df['salary'].map('{:,.0f}'.format)
    top_title_experience_df.columns = ['Job Title','Experience Level', 'Salary']
    
    st.table(top_title_experience_df)
    
# Company Size Distribution
with st.container():
    st.header('Company Size Distribution',divider="gray")
    
    company_size = job_salaries['company_size'].value_counts()
    fig = px.pie(company_size, values=company_size.values, names=company_size.index,
                title='Experience Level Distribution',color_discrete_sequence=['#00435c','#006971','#008c59','#81a51c','#ffa600'])
    
    st.plotly_chart(fig,use_container_width=True)
    
# Company Location
with st.container():
    st.header('Company Location Count',divider="gray")

    company_location = job_salaries['company_location'].value_counts().nlargest(10)

    company_location_df = company_location.reset_index()
    company_location_df.columns = ['Comapny Location', 'Count']
    
    company_location_df['Count'] = company_location_df['Count'].map('{:,.0f}'.format)
    st.table(company_location_df)

# Salary Currency
with st.container():
    st.header('Top Currency of the Salary being Denoted',divider="gray")
    
    salary_cuurrency = job_salaries['salary_currency'].value_counts().nlargest(10)

    salary_cuurrency_df = salary_cuurrency.reset_index()
    salary_cuurrency_df['salary_currency'] = salary_cuurrency_df['salary_currency'].map('{:,.0f}'.format)
    salary_cuurrency_df.columns = ['Salary Currency', 'Count']
    
    st.table(salary_cuurrency_df)
    
# Salary Converted to USD and Salary Currency
with st.container():
    st.header('Top Salary Currency converted in USD',divider="gray")
    
    salary_converted = job_salaries.groupby('salary_currency',)['salary_in_usd'].sum().nlargest(10)
    
    salary_converted_df = salary_converted.reset_index()
    salary_converted_df['salary_in_usd'] = salary_converted_df['salary_in_usd'].map('{:,.0f}'.format)
    salary_converted_df.columns = ['Salary Currency', 'Salary in USD']
    
    st.table(salary_converted_df)
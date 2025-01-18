import pandas as pd
import streamlit as st
import altair as alt

#_____AGE_HISTOGRAM___________________________________________________________
def age_histogram(df: pd.DataFrame):
    # Group the data by 'Age' and 'Attrition', counting occurrences
    pivot = df.groupby(['Age', 'Attrition']).size().reset_index(name='count')
    
    # Create the bar chart showing age distribution
    chart = (alt
             .Chart(data=pivot, mark=alt.MarkDef(type='bar', binSpacing=0))  # Bin spacing set to 0 for no space between bars
             .encode(x='Age:O', y='count:Q', color='Attrition')  # 'Age' as an ordinal axis and 'count' as quantitative
             .mark_bar()  # Create a bar chart
             .properties(title='Age Distribution')  # Set chart title
             .interactive()  # Allow interaction (e.g., tooltips, zoom)
            )

    # Display the chart in Streamlit with responsive container width
    return st.altair_chart(chart, use_container_width=True)


#_____EDUCATION_HISTOGRAM_____________________________________________________
def education_histogram(df: pd.DataFrame):
    # Group the data by 'Education' and 'Attrition', counting occurrences
    pivot = df.groupby(['Education', 'Attrition']).size().reset_index(name='count')
    
    # Create the bar chart showing education level distribution
    chart = (alt
             .Chart(data=pivot, mark=alt.MarkDef(type='bar', binSpacing=0))  # Bin spacing set to 0 for no space between bars
             .encode(x='Education:O', y='count:Q', color='Attrition')  # 'Education' as an ordinal axis and 'count' as quantitative
             .mark_bar()  # Create a bar chart
             .properties(title='Education Distribution')  # Set chart title
             .interactive()  # Allow interaction (e.g., tooltips, zoom)
            )

    # Display the chart in Streamlit with responsive container width
    return st.altair_chart(chart, use_container_width=True)


#_____EDUCATION_FIELD_HISTOGRAM_______________________________________________
def education_field_histogram(df: pd.DataFrame):
    # Group the data by 'EducationField' and 'Attrition', counting occurrences
    pivot = df.groupby(['EducationField', 'Attrition']).size().reset_index(name='count')
    
    # Create the bar chart showing education field distribution
    chart = (alt
             .Chart(data=pivot, mark=alt.MarkDef(type='bar', binSpacing=0))  # Bin spacing set to 0 for no space between bars
             .encode(y='EducationField:O', x='count:Q', color='Attrition')  # 'EducationField' as an ordinal axis and 'count' as quantitative
             .mark_bar()  # Create a bar chart
             .properties(title='Education Field Distribution')  # Set chart title
             .interactive()  # Allow interaction (e.g., tooltips, zoom)
            )

    # Display the chart in Streamlit with responsive container width
    return st.altair_chart(chart, use_container_width=True)


#_____SALARY_SLAB_HISTOGRAM___________________________________________________
def salary_slab_histogram(df: pd.DataFrame):
    # Group the data by 'SalarySlab' and 'Attrition', counting occurrences
    pivot = df.groupby(['SalarySlab', 'Attrition']).size().reset_index(name='count')
    
    # Define the order of salary slabs for correct visualization
    salary_order = ['Upto 5k', '5k-10k', '10k-15k', '15k+']

    # Create the bar chart showing salary slab distribution
    chart = (alt
             .Chart(data=pivot, mark=alt.MarkDef(type='bar', binSpacing=0))  # Bin spacing set to 0 for no space between bars
             .encode(
                 x=alt.X('SalarySlab:O', sort=salary_order),  # Sort 'SalarySlab' by the predefined order
                 y='count:Q',  # 'count' as quantitative on the y-axis
                 color='Attrition'  # Use 'Attrition' for color encoding
             )
             .mark_bar()  # Create a bar chart
             .properties(title='Salary Slab Distribution')  # Set chart title
             .interactive()  # Allow interaction (e.g., tooltips, zoom)
            )

    # Display the chart in Streamlit with responsive container width
    return st.altair_chart(chart, use_container_width=True)
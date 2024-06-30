import pandas as pd
import streamlit as st
import altair as alt
import plotly.express as px

# Read the data from Excel
data =pd.read_excel(r'Athlete_events.xlsx')

# Group members information
members_info = [
    {"name": "Tran Thi Thuy Trang", "student_id": "10323060", "email": "10323060@student.vgu.edu.vn", "major": "Finance & Accounting (BFA)"},
    {"name": "Tran Ngoc My Thao", "student_id": "10323059", "email": "10323059@student.vgu.edu.vn", "major": "Finance & Accounting (BFA)"},
    {"name": "Luong Nu Mai Nhung", "student_id": "10323056", "email": "10323056@student.vgu.edu.vn", "major": "Finance & Accounting (BFA)"},
    {"name": "Kim Duyen", "student_id": "10323044", "email": "10323044@student.vgu.edu.vn", "major": "Finance & Accounting (BFA)"}
]

# Set the page configuration
st.set_page_config(page_title="PYTHON 2 - BUSINESS IT 2", page_icon="🥰", layout="wide")

# HEADER SECTION
st.subheader("Hi everyone :wave: we're from group 7 class afternoon Business IT2")
st.title("What is there more to know about Olympic Athletes?")
st.write("Apart from their achievements, join us today on this app to get to know the athletes' Birth Countries and Average Age of Participation!")

# Display group members information
st.subheader("Group Members:")
for member in members_info:
    st.write(f"- **{member['name']}**: Student ID {member['student_id']}, {member['major']}, Contact email: {member['email']}")

# OUR DATASET
url = "https://www.kaggle.com/datasets/heesoo37/120-years-of-olympic-history-athletes-and-results"
st.write("---")
st.header("Our dataset :sparkles:")
st.markdown(f"[Click here to see the original dataset]({url})")
st.write("""
        Our refined data frame contains several main variables as follows:
        - *Name*: Name of the athlete
        - *Sport*: Sport they competed in
        - *Event*: Specific event they participated in
        - *Medal*: Type of medal they won (if any)
        - *NOC*: National Olympic Committee (country) they represented
        - *Age*: Age of the athlete at the time of the event
        - *Height*: Height of the athlete
        - *Weight*: Weight of the athlete
        """)

st.divider()
st.header("Top Birth Countries, Age Distribution, and Geographic Distribution Chart")
st.write("Discover these three graphs below with us")

# Add Sidebar
st.sidebar.write('**:bulb: Reporting to Dr. Tan Duc Do**')
st.sidebar.write('**:bulb: Members of Group 7 Business IT 2 :**')
for member in members_info:
    st.sidebar.write(member['name'])

# Initial 3 tabs for each interactive graph
tab1, tab2, tab3, tab4 = st.columns(4)

### TAB 1: BAR CHART
with tab1:
    st.subheader("Distribution of Medals Over Years")
    medal_counts = data.groupby(['Year', 'Medal']).size().reset_index(name='Count')
    fig1 = px.bar(medal_counts, x='Year', y='Count', color='Medal',
                  labels={'Year': 'Year', 'Count': 'Number of Medals', 'Medal': 'Medal Type'},
                  title='Distribution of Medals (Gold, Silver, Bronze) Over Years')
    st.plotly_chart(fig1, use_container_width=True)

### TAB 2: BAR CHART
with tab2:
    st.subheader("Top Countries by Number of Athletes")
    df_countries = data['NOC'].value_counts().reset_index(name='Number of Athletes').rename(columns={'index': 'NOC'})
    top_countries = st.slider("Select number of top countries", 1, 10, 5)
    top_countries_data = df_countries.head(top_countries)
    fig2 = px.bar(top_countries_data, x='NOC', y='Number of Athletes',
                  title=f'Top {top_countries} Countries by Number of Athletes')
    st.plotly_chart(fig2, use_container_width=True)

### TAB 3: BOXPLOT CHART
with tab3:
    st.subheader("Age Distribution in Summer and Winter Olympics")
    data_clean = data.dropna(subset=['Age'])
    fig3 = px.box(data_clean, x='Season', y='Age', color='Season', title='Age Distribution in Summer and Winter Olympics')
    st.plotly_chart(fig3, use_container_width=True)

### TAB 4: GEOGRAPHIC DISTRIBUTION
with tab4:
    st.subheader("Geographic Distribution of Athletes' Birth Countries")
    country_counts = data['NOC'].value_counts().reset_index(name='Count')
    country_counts.columns = ['NOC', 'Count']
    fig4 = px.scatter_geo(country_counts, locations="NOC", color="Count",
                          hover_name="NOC", size="Count",
                          projection="natural earth",
                          title="Geographic Distribution of Athletes' Birth Countries")
    st.plotly_chart(fig4, use_container_width=True)

st.header("Relationship between Height and Weight of Olympic Athletes")
data_filtered = data.dropna(subset=['Height', 'Weight'])
fig_scatter = px.scatter(data_filtered, x='Height', y='Weight', 
                         title='Relationship between Height and Weight of Olympic Athletes',
                         labels={'Height': 'Height (cm)', 'Weight': 'Weight (kg)'},
                         hover_name='Name', hover_data=['Sport', 'NOC'])
st.plotly_chart(fig_scatter, use_container_width=True)

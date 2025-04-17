import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from the CSV file
data = pd.read_csv('post2data.csv')

# Streamlit app
st.title('Football Teams Analysis')

# Sidebar for user inputs
st.sidebar.title('User Inputs')
selected_conference = st.sidebar.selectbox('Select a Conference', data['home_conference'].unique())
selected_team = st.sidebar.selectbox('Select a Team', data['home_team'].unique())
selected_week = st.sidebar.slider('Select Week', min_value=int(data['week'].min()), max_value=int(data['week'].max()), value=int(data['week'].min()))

# Tabs for different analyses
tab1, tab2, tab3 = st.tabs(["Conference Analysis", "Team Points Distribution", "Week Analysis"])

with tab1:
    st.write('Teams in the selected conference:')
    conf_df = data[data['home_conference'] == selected_conference]

    fig = plt.figure(figsize=(15, 8))
    sns.scatterplot(data=conf_df, x='home_points', y='home_team', label='Home Points vs Teams')

    plt.title(f'Teams in {selected_conference} Conference')
    plt.xlim(0, 100)
    plt.xlabel('Home Points')
    plt.ylabel('Team')
    plt.xticks(rotation=90)
    plt.legend()
    plt.tight_layout()

    st.pyplot(fig)

with tab2:
    st.write('Distribution of Home Points for All Teams')
    
    fig, ax = plt.subplots(figsize=(15, 8))
    sns.scatterplot(data=data, x='home_points', y=data.index, ax=ax)

    plt.title('Distribution of Home Points')
    plt.xlabel('Home Points')
    plt.ylabel('Frequency')
    plt.tight_layout()

    st.pyplot(fig)

with tab3:
    st.write(f'Analysis for Week {selected_week}')
    week_df = data[data['week'] == selected_week]

    fig = plt.figure(figsize=(15, 8))
    sns.scatterplot(data=week_df, x='home_points', y='home_team', label=f'Week {selected_week} Home Points vs Teams')

    plt.title(f'Teams in Week {selected_week}')
    plt.xlim(0, 100)
    plt.xlabel('Home Points')
    plt.ylabel('Team')
    plt.xticks(rotation=90)
    plt.legend()
    plt.tight_layout()

    st.pyplot(fig)

# Expander for detailed team analysis
with st.expander("Detailed Team Analysis"):
    team_df = data[data['home_team'] == selected_team]
    
    st.write(f'Detailed analysis for {selected_team}')
    
    fig = plt.figure(figsize=(15, 8))
    sns.scatterplot(data=team_df, x='week', y='home_points', label=f'{selected_team} Points per Week')

    plt.title(f'{selected_team} Points per Week')
    plt.xlabel('Week')
    plt.ylabel('Home Points')
    plt.xticks(rotation=90)
    plt.legend()
    plt.tight_layout()

    st.pyplot(fig)

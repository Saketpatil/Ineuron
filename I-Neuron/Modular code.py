import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import plotly.io as pio

# Set default plotly template
pio.templates.default = 'plotly_white'

# Data Reading
df = pd.read_csv('C:/Users/DELL/Desktop/Instagram/Instagram data.csv', encoding='latin-1')

# Displaying DataFrame
def display_data(df):
    print(df.head())

# Displaying DataFrame columns
def display_columns(df):
    print(df.columns)

# Displaying DataFrame information
def display_info(df):
    print(df.info())

# Getting row count
def get_row_count(df):
    row_count = len(df.index)
    print(row_count)

# Displaying descriptive statistics
def display_statistics(df):
    print(df.describe())

# Checking for missing values
def check_missing_values(df):
    print(df.isnull().sum())

# Histogram of Impressions
def plot_histogram(df):
    fig = px.histogram(df, x='Impressions', nbins=10, title='Impressions Distribution')
    fig.show()

# Line plot of Impressions over time
def plot_impressions_over_time(df):
    fig = px.line(df, x=df.index, y='Impressions', title='Impressions Over Time')
    fig.show()

# Histograms of all numerical columns
def plot_numerical_histograms(df):
    df.hist(figsize=(15, 15), color='blue', edgecolor='yellow')
    plt.gcf().set_facecolor('black')
    plt.show()

# Line plot of Likes, Saves, and Follows over time
def plot_metrics_over_time(df):
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df.index, y=df['Likes'], name='Likes'))
    fig.add_trace(go.Scatter(x=df.index, y=df['Saves'], name='Saves'))
    fig.add_trace(go.Scatter(x=df.index, y=df['Follows'], name='Follows'))

    fig.update_layout(title='Metrics Over Time', xaxis_title='Date', yaxis_title='Count')
    fig.show()

# Pie chart of traffic sources
def plot_traffic_sources(df):
    home = df['From Home'].sum()
    hashtags = df['From Hashtags'].sum()
    explore = df['From Explore'].sum()
    others = df['From Other'].sum()

    labels = ['From Home', 'From Hashtags', 'From Explore', 'From Other']
    values = [home, hashtags, explore, others]

    plt.figure()
    plt.pie(values, labels=labels, autopct='%.2f%%')
    plt.show()

# Scatter plot of Profile Visits vs Follows
def plot_profile_visits_vs_follows(df):
    fig = px.scatter(df, x='Profile Visits', y='Follows', trendline='ols', title='Profile Visits vs Follows')
    fig.show()

# Summary
def display_summary():
    summary_text = """
    SUMMARY:

    Exploratory data analysis involves delving into datasets to uncover hidden patterns and relationships, 
    providing invaluable insights that inform strategic decision-making and problem-solving in various domains. 
    It serves as a crucial precursor to data-driven initiatives, enabling informed actions based on a deeper 
    understanding of the underlying data landscape.
    """
    print(summary_text)


# Main function to run all analysis
def main():
    display_data(df)
    display_columns(df)
    display_info(df)
    get_row_count(df)
    display_statistics(df)
    check_missing_values(df)
    plot_histogram(df)
    plot_impressions_over_time(df)
    plot_numerical_histograms(df)
    plot_metrics_over_time(df)
    plot_traffic_sources(df)
    plot_profile_visits_vs_follows(df)
    display_summary()


if __name__ == "__main__":
    main()

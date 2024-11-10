import streamlit as st
import pandas as pd
import plotly.express as px

def load_data():
    return pd.read_csv('./data/processed_reddit_data.csv')

def main():
    st.title('Reddit Analytics Dashboard')
    
    df = load_data()
    
    # Time series of post metrics
    st.subheader('Post Metrics Over Time')
    
    # Create line chart for average scores
    fig_scores = px.bar(df, x='date', y='avg_score', 
                        title='Average Post Scores Over Time')
    st.plotly_chart(fig_scores)
    
    # Create line chart for average comments
    fig_comments = px.bar(df, x='date', y='avg_comments',
                          title='Average Comments Over Time')
    st.plotly_chart(fig_comments)
    
    # Create bar chart for post count
    fig_posts = px.bar(df, x='date', y='post_count',
                      title='Number of Posts per Day')
    st.plotly_chart(fig_posts)
    
    # Metrics summary
    st.subheader('Summary Statistics')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric('Avg Daily Posts', 
                 f"{df['post_count'].mean():.1f}")
    with col2:
        st.metric('Avg Score', 
                 f"{df['avg_score'].mean():.1f}")
    with col3:
        st.metric('Avg Comments', 
                 f"{df['avg_comments'].mean():.1f}")

if __name__ == '__main__':
    main()
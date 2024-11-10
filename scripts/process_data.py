from pyspark.sql import SparkSession
from pyspark.sql.functions import *

def process_reddit_data():
    # Initialize Spark session
    spark = SparkSession.builder \
        .appName("RedditDataProcessing") \
        .getOrCreate()

    # Read the CSV file
    df = spark.read.csv('./data/raw_reddit_data.csv', header=True)

    # Process the data
    processed_df = df.withColumn('date', to_date('created_utc')) \
        .groupBy('date') \
        .agg(
            avg('score').alias('avg_score'),
            avg('num_comments').alias('avg_comments'),
            avg('upvote_ratio').alias('avg_upvote_ratio'),
            count('*').alias('post_count')
        )

    # Save processed data
    processed_df.toPandas().to_csv('./data/processed_reddit_data.csv', index=False)
    spark.stop()
    return 'Data processed successfully'

if __name__ == '__main__':
    process_reddit_data()
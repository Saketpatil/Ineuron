# Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

# Load social media data
df = pd.read_csv('C:/Users/DELL/Desktop/Instagram/Instagram data.csv', encoding='latin-1')

# Convert text data to a matrix of TF-IDF features
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df)

# Define the number of clusters (categories of users)
num_clusters = 2

# Apply K-Means clustering
kmeans = KMeans(n_clusters=num_clusters)
kmeans.fit(X)

# Get the cluster labels for each data point
cluster_labels = kmeans.labels_

# Professional Output and Elaboration
print("Social Media Data Clustering Results:")
print("--------------------------------------")
print("The K-Means clustering algorithm has been applied to categorize users based on their social media activities.")
print("")

for i, label in enumerate(cluster_labels):
    print(f"Social media data point {i + 1} belongs to cluster {label + 1}.")
print("")

print("Elaboration:")
print("-------------")
print("In the context of the provided problem statement, the clustering process aims to categorize users into distinct groups based on their activities and interactions on social media platforms.")
print("By applying the K-Means algorithm, which is a popular technique in data mining, users are partitioned into clusters with similar characteristics.")
print("")

print("This clustering process enables the identification of user communities or groups who engage with specific types of content, such as posts related to the film industry or political discussions.")
print("The TF-IDF vectorization technique is employed to transform the text data from social media posts into numerical features, allowing for the application of the K-Means algorithm.")
print("")

print("The number of clusters is pre-defined based on the desired granularity of user categorization.")
print(f"In this case, {num_clusters} clusters have been specified.")
print("")

print("Each social media data point is assigned a cluster label, indicating the category to which the user belongs.")
print("These cluster labels can be further analyzed to gain insights into user behavior and preferences, aiding in user classification and community identification.")

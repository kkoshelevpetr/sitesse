import hdbscan

# Initialize HDBSCAN
cluster_model = hdbscan.HDBSCAN(min_cluster_size=5, metric='euclidean')

# Fit the model and get cluster labels
cluster_labels = cluster_model.fit_predict(reduced_embeddings)

import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.inspection import DecisionBoundaryDisplay

# Page Config
st.set_page_config(page_title="Voting Classifier Visualizer", layout="wide")
st.title("Voting Ensemble Decision Boundary Visualizer")

# Sidebar - Dataset Selection
st.sidebar.header("1. Dataset Settings")
dataset_type = st.sidebar.selectbox("Select Dataset", ["Moons", "Circles", "Linearly Separable"])
noise = st.sidebar.slider("Noise Level", 0.0, 0.5, 0.1)

# Sidebar - Classifier Selection
st.sidebar.header("2. Base Models")
use_lr = st.sidebar.checkbox("Logistic Regression", value=True)
use_svc = st.sidebar.checkbox("SVM (RBF)", value=True)
use_dt = st.sidebar.checkbox("Decision Tree", value=False)
use_knn = st.sidebar.checkbox("KNN", value=True)

# Sidebar - Voting Settings
st.sidebar.header("3. Ensemble Settings")
voting_type = st.sidebar.radio("Voting Type", ["hard", "soft"])

# Generate Data
if dataset_type == "Moons":
    X, y = make_moons(n_samples=200, noise=noise, random_state=42)
elif dataset_type == "Circles":
    X, y = make_circles(n_samples=200, noise=noise, factor=0.5, random_state=42)
else:
    X, y = make_classification(n_samples=200, n_features=2, n_redundant=0, n_informative=2, random_state=42, n_clusters_per_class=1)

# Initialize Estimators
estimators = []
if use_lr: estimators.append(('lr', LogisticRegression()))
if use_svc: estimators.append(('svc', SVC(probability=True))) # Probability=True needed for Soft Voting
if use_dt: estimators.append(('dt', DecisionTreeClassifier()))
if use_knn: estimators.append(('knn', KNeighborsClassifier()))

if len(estimators) < 2:
    st.warning("Please select at least two base models to see the Ensemble effect.")
else:
    # Create Voting Classifier
    vc = VotingClassifier(estimators=estimators, voting=voting_type)
    vc.fit(X, y)

    # Plotting
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Draw Decision Boundary
    DecisionBoundaryDisplay.from_estimator(
        vc, X, response_method="predict",
        grid_resolution=200, ax=ax, cmap=plt.cm.RdYlBu, alpha=0.8
    )
    
    # Plot Data Points
    ax.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', cmap=plt.cm.RdYlBu)
    ax.set_title(f"Voting Classifier ({voting_type.capitalize()} Voting)")
    
    st.pyplot(fig)

    # Show Accuracy
    accuracy = vc.score(X, y)
    st.write(f"### Model Accuracy: {accuracy:.2%}")
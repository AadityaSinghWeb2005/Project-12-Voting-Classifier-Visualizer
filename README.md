# Voting Classifier Visualizer 🗳️

An interactive web application built with **Streamlit** that visualizes how Voting Classifiers make decisions. This tool allows users to witness the Power of Hyperparameters in Machine Learning by combining multiple base models—such as Logistic Regression, SVM, and KNN—to create a robust ensemble.

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [How Voting Classifiers Work](#how-voting-classifiers-work)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project provides an interactive platform to understand and visualize the decision-making process of Voting Classifiers. By combining multiple base models, you can observe how ensemble methods improve prediction accuracy and robustness compared to individual classifiers.

## ✨ Features

- **Interactive Visualization**: Real-time visualization of decision boundaries and classifier decisions
- **Multiple Base Models**: Support for Logistic Regression, SVM (Support Vector Machine), and KNN (K-Nearest Neighbors)
- **Hyperparameter Tuning**: Dynamically adjust hyperparameters and observe their impact on model performance
- **Ensemble Learning**: Understand how voting mechanisms (hard and soft voting) combine predictions
- **Performance Metrics**: View accuracy, precision, recall, and F1-score for each model
- **Decision Boundaries**: Visual representation of how different models partition the feature space
- **Comparative Analysis**: Compare individual models vs. the voting classifier ensemble

## 📦 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Steps

1. Clone the repository:
```bash
git clone https://github.com/AadityaSinghWeb2005/Project-12-Voting-Classifier-Visualizer.git
cd Project-12-Voting-Classifier-Visualizer
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

Run the Streamlit application:

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

### How to Use the Application

1. **Select Dataset**: Choose between built-in datasets or upload your own
2. **Configure Base Models**: Adjust hyperparameters for each individual classifier
3. **Set Voting Strategy**: Choose between hard voting (majority vote) or soft voting (probability average)
4. **Visualize**: Observe the decision boundaries and predictions in real-time
5. **Analyze Results**: Review performance metrics and compare different configurations

## 📁 Project Structure

```
Project-12-Voting-Classifier-Visualizer/
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── models/
│   ├── __init__.py
│   ├── classifiers.py              # Base classifier implementations
│   └── voting_ensemble.py          # Voting Classifier logic
├── utils/
│   ├── __init__.py
│   ├── visualization.py            # Plotting and visualization functions
│   ├── data_loader.py              # Dataset loading utilities
│   └── metrics.py                  # Performance metrics calculation
├── data/
│   └── sample_datasets.csv         # Sample datasets for testing
└── README.md                       # Project documentation
```

## 🧠 How Voting Classifiers Work

A **Voting Classifier** is an ensemble method that combines predictions from multiple base estimators:

### Hard Voting
Each base classifier votes, and the class with the most votes is selected.

```
Model 1: Class A
Model 2: Class B
Model 3: Class A
─────────────────
Result: Class A (majority vote)
```

### Soft Voting
The predicted probabilities from each classifier are averaged, and the class with the highest average probability is selected.

```
Model 1: [0.2, 0.8] → Class B (80%)
Model 2: [0.6, 0.4] → Class A (60%)
Model 3: [0.3, 0.7] → Class B (70%)
─────────────────────────────────
Average: [0.37, 0.67] → Class B
```

### Advantages
- **Improved Accuracy**: Combining diverse models often yields better predictions
- **Robustness**: Less susceptible to overfitting than individual models
- **Stability**: Reduced variance through ensemble averaging
- **Flexibility**: Works with any classification model as a base estimator

## 🛠 Technologies Used

- **Python 3.x** - Programming language
- **Streamlit** - Web framework for interactive applications
- **scikit-learn** - Machine learning library for classifiers and metrics
- **NumPy** - Numerical computing
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Plotting and visualization
- **Seaborn** - Statistical data visualization

## 📋 Dependencies

See `requirements.txt` for a complete list of dependencies:

```
streamlit>=1.0
scikit-learn>=0.24
numpy>=1.20
pandas>=1.2
matplotlib>=3.3
seaborn>=0.11
```

## 💡 Learning Outcomes

By using this visualizer, you will understand:

- How different classification algorithms work
- The impact of hyperparameters on model behavior
- How ensemble methods combine multiple models
- The trade-offs between hard and soft voting
- Decision boundary visualization and interpretation
- Model performance evaluation and metrics

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙋 Support

If you have questions or need assistance:

- Open an issue on GitHub
- Check the documentation in the code comments
- Review scikit-learn documentation for classifier details

## 📚 Additional Resources

- [Scikit-learn Voting Classifier Documentation](https://scikit-learn.org/stable/modules/ensemble.html#voting-classifier)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Ensemble Methods in Machine Learning](https://towardsdatascience.com/ensemble-methods-in-machine-learning-what-are-they-and-why-use-them-68ec3886ff86)

---

**Author**: Aaditya Singh  
**Last Updated**: April 2026  
**Status**: Active Development ✅
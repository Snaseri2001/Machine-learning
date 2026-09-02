# Federated Learning on Tabular Data – Advanced Topics in Security & Privacy

**Topic:** Federated Learning on Tabular Data with Different ML Algorithms  
**Date:** July 2025  
**Institution:** TU Wien – Faculty of Informatics  


## 📌 Objective
The aim of this project is to explore **Federated Learning (FL)** — a decentralized machine learning approach where multiple clients collaboratively train a shared global model without centralizing their data.  
We investigate how the **number of participating clients** impacts the accuracy of the global model, comparing two algorithms:
- **Multi-Layer Perceptron (MLP)**
- **Gradient Boosting Decision Tree (GBDT)**

**Keywords:** Federated Learning, Tabular Data, MLP, Unbalanced Data

---

## ⚙️ Setup

### Datasets
- **Loan Dataset** (~9,500 entries, 7 classes: A–G)  
- **Breast Cancer Diagnostic Dataset (Wisconsin)** (569 entries, binary classification)  

### Algorithms
1. **Neural Network (MLP)** with 4 dense layers  
2. **Gradient Boosting Decision Tree**  

### Libraries & Environment
- Google Colab  
- TensorFlow Federated (TFF)  

---

## 🧠 Approaches

### 1. Neural Network (MLP) – Federated Learning Structure
1. **Model Creation:** MLP for classification  
2. **Model Packaging:** Wrap Keras model for TFF compatibility  
3. **Training:** FedAvg algorithm (clients train locally → models aggregated on server)

**Model Parameters:**
- Architecture:  
  - Dense(24, ReLU)  
  - Dense(8, Tanh)  
  - Dense(8, ReLU)  
  - Dense(8, ReLU)  
  - Dense(7, Softmax) for multiclass / Dense(1, Sigmoid) for binary
- Loss: SparseCategoricalCrossentropy (multiclass), BinaryCrossentropy (binary)
- Metric: SparseCategoricalAccuracy / BinaryAccuracy  
- Clients: Variable (1, 4, 7, 10, 40, 70, 100)  
- Batch size: 16, repeated 5 times (~5 epochs)  
- Early stopping: 10–20 rounds without improvement  

---

### 2. Gradient Boosting Decision Tree (GBDT)
- Clients: 1 to 100 (step 3)  
- Multiclass classification with Softmax and Log Loss  
- Learning rate: 0.3  
- Booster: 20 trees, max depth = 6  
- **Sequential update**: Clients update the global model one after another (no averaging)  

---

## 🔬 Experiments

### **Case Study 1:** Federated Class Imbalance
- Clients have only a subset of classes  
- Balanced sample distribution per client

### **Case Study 2:** Imbalanced Sample Distribution
- All classes present in every client  
- Uneven sample sizes across clients (one "big" client with most data)

---

## 📊 Results Summary

- **Neural Networks:**  
  - More sensitive to **class imbalance** than to sample imbalance.  
  - Class imbalance → noticeable accuracy drop.  
- **GBDT:**  
  - Better at handling class imbalance.  
  - Performance heavily affected by uneven sample sizes (dominant client bias).  

---

## 💡 Challenges
- **Non-IID data** caused:
  - Model bias toward dominant classes
  - Poor generalization for unseen classes
  - Divergent client updates (client drift)  
- **GBDT limitation in TFF** → Sequential updates instead of aggregation  

---

## 🚀 Possible Improvements
- Use advanced aggregation: **FedProx**, **FedNova**, **MOON**
- Apply personalization or cluster-based model updates
- Increase classes per client to reduce non-IID effects


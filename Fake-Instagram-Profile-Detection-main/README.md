# Fake-Instagram-Profile-Detection

# **Fake Instagram 🏆 Profile Detection Model - Accuracy Improvement**

## 📌 Overview  
In this repository, I aimed to **enhance the accuracy** of the **Fake Instagram Profile Detection Model** from **88% to 92%** using various **machine learning techniques and ensemble methods**.  

📌 **Original Project Link:**  
🔗 [Fake Instagram Profile Detection Model (Kaggle)](https://www.kaggle.com/code/durgeshrao9993/fake-instagram-profile-detection-model/notebook)  

---

##  Approach & Techniques  

### **1️⃣ Hyperparameter Tuning with Keras Tuner**  
- Used **Keras Tuner** to optimize the number of **layers** and **neurons**.  
- The **best model** found had **7 layers** with the following neurons:  
  **[25, 75, 50, 50, 50, 50, 2]**  
- **Results after tuning:**  

  | Class | Precision | Recall | F1-Score | Support |
  |-------|-----------|--------|----------|---------|
  | **0** | 0.93      | 0.87   | 0.90     | 60      |
  | **1** | 0.88      | 0.93   | 0.90     | 60      |
  | **Accuracy** | **90%** | - | - | 120 |

- **Early Stopping** was also tested, but the results remained the same.  

---

### **2️⃣ Ensemble Methods (Random Forest & XGBoost)**  
I experimented with **ensemble learning** to further boost accuracy.  

- **Random Forest (without PCA) improved accuracy to 92%** 🚀  
- **Results:**  

  | Class | Precision | Recall | F1-Score | Support |
  |-------|-----------|--------|----------|---------|
  | **0** | 0.90      | 0.93   | 0.92     | 60      |
  | **1** | 0.93      | 0.90   | 0.92     | 60      |
  | **Accuracy** | **92%** | - | - | 120 |

- I also tested **XGBoost**, but **Random Forest performed better**.  

---

### **3️⃣ Dimensionality Reduction (PCA) + Ensemble Methods**  
I applied **PCA (Principal Component Analysis)** to reduce data dimensions and then used **Random Forest & XGBoost**.  

- **However, PCA reduced the accuracy.**  
- This suggests that dimensionality reduction **removed useful information** in this dataset.  

---

## Final Conclusion  
✅ Best Model: **Random Forest without PCA** (92% accuracy)  and **Neural Network with 7 Layers** (90% accuracy)






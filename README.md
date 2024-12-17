# **Creastimate**

The **Creastimate** project integrates **machine learning (ML)** and **real-time communication** to predict creativity scores using crowdsourced data.

## **Project Overview**

Creastimate employs a combination of **crowdsourced user inputs** and **machine learning models** to estimate creativity levels in various contexts. It uses real-time interaction and predictive analytics to deliver insights to users.  

---

### **Key Features**

1. **Real-Time Data Collection and Interaction**
   - Uses **Socket.IO** for real-time communication.
   - Collects user inputs such as:
     - Number of unique words.
     - Number of difficult words.
     - Smart home experience.
     - Family size.
   - Processes inputs dynamically, providing immediate feedback to users.

2. **Machine Learning Integration**
   - Implements a **Support Vector Machine (SVM)** classifier to predict creativity scores.
   - Trains the ML model on a labeled dataset with features such as:
     - User experience.
     - Programming expertise.
     - Demographic details.
   - Categorical inputs (e.g., "Entertainment," "Home Security") are mapped into numeric values for effective processing.

3. **Scenarios and Feature Mapping**
   - Uses predefined categories like:
     - **Entertainment**
     - **Home Security**
     - **Health**
   - Key features for predictions:
     - Unique words (UW).
     - Difficult words (DW).
     - Total experience in months.
     - Family size.

4. **Performance Metrics**
   - Evaluates the ML model using:
     - **F1-score**
     - **Mean accuracy** on validation datasets.

5. **User Feedback Loop**
   - Creativity predictions are sent back to users in real-time using **Socket.IO**.
   - Fosters engagement and iterative improvement.

---

### **Technical Highlights**
- **Data Science Integration:** Combines real-world data processing with machine learning for innovative applications.
- **Interactive Feedback:** Provides users with immediate insights into creativity scores, promoting dynamic interaction.
- **Scalability:** The system is extensible to include additional predictors or categories for enhanced estimation.

---

### **How It Works**
1. **Input Collection:**
   - Users provide data via the live chat interface.
2. **Data Processing:**
   - Input features are processed and mapped to numeric values.
3. **Model Prediction:**
   - An SVM model trained on a crowdsourced dataset predicts the creativity score.
4. **Real-Time Feedback:**
   - Results are returned to the user in real time through the chat interface.

---

This project is a cutting-edge blend of real-time interactivity, crowdsourcing, and advanced ML techniques, aimed at fostering collaboration and creativity insights.

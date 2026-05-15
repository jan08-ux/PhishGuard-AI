# 🛡️ PhishGuard AI: Intelligent Phishing URL Detection

PhishGuard AI is a high-performance, machine learning-driven security tool designed to identify and block phishing attempts by analyzing URL patterns. Using advanced feature extraction and a calibrated Gradient Boosting model, it provides real-time analysis with explainable results.

---

## 🚀 Features

- **Explainable AI**: Not just a "Yes/No" answer—it tells you *why* a URL is suspicious.
- **Lightning Fast**: Analyzes URLs in milliseconds without the need for slow web scraping.
- **Rich GUI**: A clean, intuitive interface for non-technical users to verify links.
- **Deep Feature Extraction**: Analyzes 15+ indicators including entropy, WHOIS age, and character patterns.

---

## 🛠️ Project Structure

```bash
phishing_detection/
├── data/                  # Datasets (PhishTank & Majestic)
├── features.py            # Feature engineering logic
├── trainer.py             # ML Model training & calibration
├── gui_app.py             # Tkinter-based Graphical Interface
├── detector.py            # Command-line prediction tool
├── phishing_model.pkl     # Pre-trained ML model
└── README.md              # Documentation
```

---

## 📥 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/PhishGuard-AI.git
   cd PhishGuard-AI
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🖥️ Usage

### 1. Graphical Interface (Recommended)
Launch the interactive dashboard to scan URLs:
```bash
python gui_app.py
```

### 2. Command Line Detection
Quickly scan a single URL via terminal:
```bash
python detector.py
```

---

## 🧠 How it Works

1. **Feature Extraction**: The system breaks down the URL into lexical and statistical features (e.g., presence of `@`, number of dots, domain age).
2. **ML Classification**: A **Gradient Boosting** classifier (calibrated for high precision) evaluates the risk.
3. **Explanation Engine**: If a URL is flagged, PhishGuard lists the specific triggers (e.g., "Suspicious Keywords Found" or "High Entropy Hostname").

---

## 🤝 How to Upload to GitHub (Step-by-Step)

If you are setting up this repository for the first time, run these commands in your terminal:

1. **Initialize Git & Add Files:**
   ```powershell
   git init
   git add .
   git commit -m "Initial commit: PhishGuard AI release"
   ```

2. **Create Remote & Push:**
   *Create a repository named `PhishGuard-AI` on GitHub first.*
   ```powershell
   git remote add origin https://github.com/YOUR_USERNAME/PhishGuard-AI.git
   git branch -M main
   git push -u origin main
   ```

---

## 👤 Author

**Janjitha**  
*B.Tech ECE (Specialization in Cybersecurity)*  
Developed as part of a professional Cybersecurity Internship.

---

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.

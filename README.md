#  PhishGuard AI - Phishing URL Detection System

PhishGuard AI is a machine learning-based phishing URL detection system that analyzes suspicious URL patterns and predicts whether a link is legitimate or malicious . Using statistical feature extraction techniques and calibrated Gradient Boosting model, it provides real-time analysis with a simple graphical interface.

---

#  Features

- Detects phishing URLs using Machine Learning
- Fast URL-based prediction without webpage scraping
- Human-readable phishing indicators
- GUI application using Tkinter
- Feature extraction using URL patterns and entropy analysis
- Pre-trained ML model included (`phishing_model.pkl`)

---


#  Project Structure

```bash
phishing_detection/
│
├── features.py            
├── trainer.py             
├── detector.py            
├── gui_app.py             
├── phishing_model.pkl     
├── requirements.txt      
├── LICENSE                
└── README.md              
```

---

## Installation

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

##  Usage

### 1. Graphical Interface 
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

## License

Distributed under the MIT License. 

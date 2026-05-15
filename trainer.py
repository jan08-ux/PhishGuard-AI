
import pandas as pd
import joblib
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score, precision_recall_curve
from sklearn.calibration import CalibratedClassifierCV
from imblearn.over_sampling import SMOTE
from tqdm import tqdm
from features import extract_features

class PhishingModelTrainer:
    def __init__(self):
        self.model = None
        self.feature_columns = None
        self.threshold = 0.65
        
    def train(self, legit_path, phishing_path, model_path='phishing_model.pkl'):
        """Train and save model"""
        print("Loading data...")
        legit = pd.read_csv(legit_path)
        phishing = pd.read_csv(phishing_path)
        legit['label'] = 0
        phishing['label'] = 1
        df = pd.concat([legit, phishing]).sample(frac=1).reset_index(drop=True)
        
        print("Extracting features...")
        tqdm.pandas()
        df['features'] = df['url'].progress_apply(extract_features)
        X = pd.json_normalize(df['features'])
        y = df['label']
        self.feature_columns = list(X.columns)
        
        print("\nBalancing dataset...")
        X_res, y_res = SMOTE(random_state=42).fit_resample(X, y)
        X_train, X_test, y_train, y_test = train_test_split(
            X_res, y_res, 
            test_size=0.2, 
            random_state=42
        )
        
        print("\nTraining model...")
        base_model = GradientBoostingClassifier(
            n_estimators=150,
            learning_rate=0.1,
            max_depth=5,
            random_state=42,
            max_features='sqrt'
        )
        self.model = CalibratedClassifierCV(base_model, cv=3, method='isotonic')
        self.model.fit(X_train, y_train)
        
        # Find optimal threshold
        y_proba = self.model.predict_proba(X_test)[:,1]
        precision, recall, thresholds = precision_recall_curve(y_test, y_proba)
        f1_scores = 2 * (precision * recall) / (precision + recall + 1e-9)
        self.threshold = thresholds[np.argmax(f1_scores)]
        
        print("\n=== Model Evaluation ===")
        y_pred = (y_proba >= self.threshold).astype(int)
        print(classification_report(y_test, y_pred))
        print(f"Optimal Threshold: {self.threshold:.4f}")
        print(f"AUC-ROC: {roc_auc_score(y_test, y_proba):.4f}")
        
        self.save_model(model_path)
    
    def save_model(self, path):
        """Save model with metadata"""
        joblib.dump({
            'model': self.model,
            'features': self.feature_columns,
            'threshold': self.threshold
        }, path)
        print(f"Model saved to {path}")

if __name__ == "__main__":
    trainer = PhishingModelTrainer()
    trainer.train(
        legit_path="data/majestic_processed.csv",
        phishing_path="data/phishtank_processed.csv"
    )
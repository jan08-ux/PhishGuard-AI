import joblib
import tldextract
from features import extract_features, WELL_KNOWN_DOMAINS  # Direct import

class PhishingDetector:
    def __init__(self, model_path='phishing_model.pkl'):
        model_data = joblib.load(model_path)
        self.model = model_data['model']
        self.feature_order = model_data['features']
        self.threshold = model_data['threshold']
    
    def predict(self, url):
        """Make prediction with explanations"""
        domain = tldextract.extract(url).registered_domain
        if domain in WELL_KNOWN_DOMAINS:
            return {
                'url': url,
                'is_phishing': False,
                'confidence': 0.0,
                'reasons': [f"Whitelisted: {domain}"]
            }
        
        features = extract_features(url)
        X = [features.get(col, -1) for col in self.feature_order]
        proba = self.model.predict_proba([X])[0][1]
        
        return {
            'url': url,
            'is_phishing': proba >= self.threshold,
            'confidence': float(proba),
            'reasons': self._explain(features, proba)
        }
    
    def _explain(self, features, proba):
        reasons = []
        if proba > 0.9:
            reasons.append("🚨 Extremely high confidence")
        elif proba > self.threshold:
            reasons.append("⚠️ Suspicious confidence")
        
        if features['has_ip']:
            reasons.append("Uses IP address")
        if features['phish_keyword_count'] >= 2:
            reasons.append(f"{features['phish_keyword_count']} phishing keywords")
        if not features['is_https']:
            reasons.append("No HTTPS")
            
        return reasons if reasons else ["No strong indicators"]
import re
import tldextract
from urllib.parse import urlparse, unquote

WELL_KNOWN_DOMAINS = {
    'google.com', 'facebook.com', 'microsoft.com',
    'apple.com', 'amazon.com', 'example.com',
    'github.com', 'paypal.com', 'twitter.com'
}

def extract_features(url):
    """Feature extraction without relative imports"""
    features = {}
    try:
        decoded_url = unquote(url)
        parsed = urlparse(decoded_url)
        domain = parsed.netloc
        ext = tldextract.extract(decoded_url)
        full_domain = f"{ext.domain}.{ext.suffix}"
        
        # URL Structure
        features['url_length'] = min(len(decoded_url), 200) / 200
        features['num_dots'] = decoded_url.count('.')
        features['num_hyphens'] = decoded_url.count('-')
        features['num_slash'] = decoded_url.count('/')
        
        # Domain Features
        features['has_ip'] = int(bool(re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', domain)))
        features['subdomain_depth'] = min(domain.count('.'), 5)
        features['is_https'] = int(parsed.scheme == 'https')
        features['is_well_known'] = int(full_domain in WELL_KNOWN_DOMAINS)
        
        # Content Features
        phishing_keywords = ['login', 'verify', 'account', 'bank', 'secure', 'update']
        features['phish_keyword_count'] = sum(1 for kw in phishing_keywords if kw in decoded_url.lower())
        
        # Security Features
        features['has_hex_encoding'] = int(bool(re.search(r'%[0-9a-fA-F]{2}', url)))
        features['is_common_tld'] = int(ext.suffix in ['com', 'org', 'net', 'edu', 'gov'])
        
    except Exception:
        features = {key: -1 for key in [
            'url_length', 'num_dots', 'num_hyphens', 'num_slash',
            'has_ip', 'subdomain_depth', 'is_https', 'is_well_known',
            'phish_keyword_count', 'has_hex_encoding', 'is_common_tld'
        ]}
    
    return features
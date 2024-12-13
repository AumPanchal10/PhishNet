from urllib.parse import urlparse
from datetime import datetime

def is_suspicious_url(url):
    parsed_url = urlparse(url)
    print(f"Parsed URL: {parsed_url}")
    
    # Check for phishing patterns
    if len(url) > 75:
        print("URL is suspicious due to length.")
        return True
    if '@' in url:
        print("URL is suspicious due to '@' symbol.")
        return True
    if '//' in url[7:]:
        print("URL is suspicious due to '//' after protocol.")
        return True
    if url.count('-') > 2:
        print("URL is suspicious due to multiple hyphens.")
        return True
    return False

def count_dots_in_url(url):
    num_dots = url.count('.')
    print(f"Number of dots in URL: {num_dots}")
    return num_dots

def has_https(url):
    uses_https = url.startswith('https')
    print(f"URL uses HTTPS: {uses_https}")
    return uses_https

# Example combined analysis function
def analyze_url_features(url):
    features = {
        'length': len(url),
        'suspicious': is_suspicious_url(url),
        'num_dots': count_dots_in_url(url),
        'uses_https': has_https(url)
    }
    print(f"Analyzed URL features: {features}")
    return features

# Testing functions locally
if __name__ == "__main__":
    test_url = "https://google.com/"
    print(f"Is the URL suspicious? {'Yes' if is_suspicious_url(test_url) else 'No'}")
    
    # Example combined analysis
    analyze_url_features(test_url)

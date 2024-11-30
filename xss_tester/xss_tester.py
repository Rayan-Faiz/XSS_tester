import requests
from bs4 import BeautifulSoup
import sys

def load_payloads(file_path):
    """Load XSS payloads from a file."""
    try:
        with open(file_path, 'r') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: Payload file {file_path} not found.")
        sys.exit(1)

def find_forms(url):
    """Extract all forms from a URL."""
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.find_all('form')
    except requests.RequestException as e:
        print(f"Error: {e}")
        return []

def inject_payload(url, form, payload):
    """Inject a payload into a form and submit it."""
    action = form.get('action')
    method = form.get('method', 'get').lower()
    form_url = action if action.startswith('http') else f"{url}{action}"
    
    inputs = form.find_all('input')
    data = {inp.get('name', ''): payload for inp in inputs if inp.get('name')}

    try:
        if method == 'post':
            response = requests.post(form_url, data=data)
        else:
            response = requests.get(form_url, params=data)
        return payload in response.text
    except requests.RequestException as e:
        print(f"Error: {e}")
        return False

def test_xss(url, payloads):
    """Test a URL for XSS vulnerabilities."""
    forms = find_forms(url)
    if not forms:
        print("No forms found on the page.")
        return
    
    print(f"Found {len(forms)} forms. Testing for XSS vulnerabilities...")
    for form in forms:
        for payload in payloads:
            if inject_payload(url, form, payload):
                print(f"Vulnerability found with payload: {payload}")
                return
    print("No vulnerabilities found.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python xss_tester.py <url> <payload_file>")
        sys.exit(1)
    
    target_url = sys.argv[1]
    payload_file = sys.argv[2]
    xss_payloads = load_payloads(payload_file)
    
    test_xss(target_url, xss_payloads)

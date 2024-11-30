# XSS Vulnerability Tester

XSS Vulnerability Tester is a Python tool designed to test web applications for Cross-Site Scripting (XSS) vulnerabilities. It automates the injection of malicious payloads into web forms and URL parameters to detect potential vulnerabilities.

---

## Features

- Scans web pages for forms.
- Injects multiple XSS payloads into input fields.
- Detects reflected payloads in server responses.
- Easy-to-use command-line interface (CLI).
- Supports GET and POST methods.

---

## How it works

The tool:

1. Parses the target URL to extract all HTML forms.
2. Iteratively injects XSS payloads into input fields or query parameters.
3. Checks the server response to see if the payload is reflected in the output (indicating a potential XSS vulnerability).

---

## Requirements

- Python 3.7+
- Libraries:
-- requests
-- beautifulsoup4

Install dependencies using:
  ```bash
  pip install -r requirements.txt  
  ```

---

## Installation

1. Clone this repository:
  ```bash
  git clone https://github.com/Rayan-Faiz/xss-tester.git  
  cd xss-tester  
  ```

2. Install required dependencies:
  ```bash
  pip install -r requirements.txt 
  ``` 

---

## Usage

1. Prepare a list of XSS payloads in a file (e.g., payloads.txt). Example payloads are already included in this repository.

2. Run the tool with the following command:
  ```bash
  python xss_tester.py <target_url> payloads.txt
  ``` 

3. Review the output for any detected vulnerabilities.

---

## Example Output

  ```bash
  Found 2 forms. Testing for XSS vulnerabilities...  
  Vulnerability found with payload: <script>alert(1)</script>  
  ```

---

## Payloads

The payloads.txt file contains common XSS payloads. You can customize it by adding or removing payloads based on your testing needs.

Example payloads:
  ```bash
  <script>alert(1)</script>  
  "><script>alert('XSS')</script>  
  <svg/onload=alert(1)>  
  '"><img src=x onerror=alert(1)>  
  ```
## Future Enhancements

- Add support for cookies and authenticated sessions.
- Detect DOM-based XSS vulnerabilities.
- Save scan results to a report file (e.g., JSON or CSV).

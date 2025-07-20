# Selenium Editorial Link Demo

### 🔍 Simple Selenium test for [editorial.link](https://editorial.link/)

This is a basic example of using Selenium WebDriver and Pytest to test a real website.

---

## ✅ What this test does

- Opens [https://editorial.link/](https://editorial.link/)
- Waits for at least two `<a>` elements to load
- Clicks the second link
- Checks that the URL changes to contain `/case/`

---

## 🚀 How to run

1. Install Python (3.8+ recommended) and [ChromeDriver](https://chromedriver.chromium.org/).
2. Install dependencies:
	pip install -r requirements.txt
3. Run the test:
	pytest test_click_second_button.py


---

## 📂 Project structure

selenium-editorial-demo/
├── test_click_second_button.py
├── requirements.txt
├── .gitignore
└── README.md


---

## 💡 Notes

- Uses `WebDriverWait` instead of `time.sleep` for more reliable tests.
- Basic assertion for title and URL.
- Can be extended with Page Object Model for larger projects.


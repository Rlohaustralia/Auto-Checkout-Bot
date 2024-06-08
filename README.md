# Auto-Checkout-Bot (Selenium Web Automation Script)
This script is designed to automate the process of ordering a product from an online store using Selenium WebDriver.
It navigates through the website, selects a product, fills in the order form, and completes all necessary steps before the payment process.

# Demo
https://youtu.be/0WT81IIxJYc
<img width="911" alt="Thumb" src="https://github.com/Rlohaustralia/Auto-Checkout-Bot/assets/110233607/156591f2-64fe-4764-aa42-96e3fdcd7dc6">


# Prerequisites
Before running the script, ensure you have the following installed:
- Python 3.x
- Selenium WebDriver for Python
- Google Chrome browser
- ChromeDriver (compatible with your Chrome version)
You can install Selenium WebDriver for Python using pip:
pip install selenium

# Usage
1. Clone or download the repository to your local machine.
2. Navigate to the directory containing the script.
3. Run the script using the following command:
python main.py
4. Sit back and watch as the script automates the ordering process for you.

# Customization
Modify the XPATH expressions in the script to match the structure of the website you are automating.
You may need to inspect the elements of the website to find the correct XPATHs.
Adjust the time delays (time.sleep()) according to the speed of your internet connection and the responsiveness of the website.

# Notes
This script is provided as-is and may require customization to work with specific websites.
The script completes all steps up to the payment process.
You may need to manually review the order details and initiate the payment if required by the website.

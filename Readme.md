# LinkedIn Job Saver Bot

This Python script automates the process of saving job listings on LinkedIn using Selenium. It logs into a LinkedIn account, navigates to the job search page, and saves job listings based on specified search criteria.

## Output


https://github.com/sarvesh-2109/LinkedIn-Job-Saver-Bot/assets/113255836/f57d63f5-ec0f-4572-979c-4f21b3efe1a9



## Overview

The bot is designed to help users automate the tedious task of manually going through and saving relevant job listings on LinkedIn. It performs the following actions:

- Opens a Chrome browser and navigates to the LinkedIn job search page.
- Logs into LinkedIn using provided credentials.
- Iterates through the job listings on the search results page.
- Clicks on each job listing to open it and clicks the 'Save' button.

## Setup and Installation

### Prerequisites

- Python installed on your machine.
- Selenium WebDriver for Python.
- ChromeDriver installed and configured to match your Chrome browser's version.

### Steps to Run the Bot

1. **Install Selenium**: If you haven't already, install Selenium by running `pip install selenium` in your terminal or command prompt.

2. **Download ChromeDriver**: Ensure you have ChromeDriver downloaded and placed in a location accessible by your script. Adjust the path in the script if necessary.

3. **Configure the Script**: Update the `ACCOUNT_EMAIL` and `ACCOUNT_PASSWORD` variables with your LinkedIn credentials.

4. **Run the Script**: Execute the script by running `python linkedin_job_saver.py` (assuming `linkedin_job_saver.py` is the name of your script file).

## Usage Notes

- The script uses explicit time delays (`time.sleep`) to wait for page elements to load. Depending on your internet connection, you might need to adjust these delays.
- Ensure you're compliant with LinkedIn's terms of service when using this script. Automated actions can sometimes be against the terms of service of web platforms.
- The CSS selectors used in the script are based on the current LinkedIn website's structure and might need updates if LinkedIn updates its site.

## Disclaimer

This bot is intended for educational purposes only. Automated interaction with websites, including LinkedIn, can violate their terms of service. Use this script responsibly and ethically, and ensure you have permission to automate interactions with any website.

## Contributing

Contributions to improve the script or address issues are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.


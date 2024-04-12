import os
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from webdrivermanager import ChromeDriverManager

def check_driver_instance():
    try:
        # Specify the directory where the Chrome WebDriver executable is located
        chrome_driver_dir = "/usr/local/share/WebDriverManager/chrome/114.0.5735.90/chromedriver_linux64/chromedriver"


        # Add the directory to the PATH environment variable
        os.environ['PATH'] += os.pathsep + chrome_driver_dir

        # Create a WebDriver instance without specifying the executable path
        driver = webdriver.Chrome()

        # If the driver instance is created successfully, print a success message
        print("WebDriver instance created successfully.")

        # Close the WebDriver instance
        driver.quit()
    except Exception as e:
        # If an exception occurs during WebDriver creation, print an error message
        print("Error creating WebDriver instance:", e)

# Call the function to check WebDriver instance creation
check_driver_instance()

# Call the function to check WebDriver instance creation
check_driver_instance()

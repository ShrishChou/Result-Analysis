import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def scraping(url):

    # Specify the path to chromedriver.exe
    webdriver_path = "C:/Users/email/Documents/ResultTracker/bin/msedgedriver.exe"

# Create Chrome WebDriver instance
    options = webdriver.EdgeOptions()
    options.use_chromium = True  # Set this to True for the Chromium-based Edge browser
    options.add_argument("--headless")
    options.add_argument('--disable-extensions')
    options.add_argument('--blink-settings=imagesEnabled=false')
    options.add_argument('--disable-notifications')

    driver = webdriver.Edge(executable_path=webdriver_path, options=options)
    driver.get(url)
    wait_time = 10

    time.sleep(wait_time)
    element_xpath = '//*[@id="player-profile"]/section[2]/div[2]/div/div[2]/div[2]/div[2]/div[1]/div/h2'  

    element = driver.find_element("xpath", element_xpath)
    html_content = element.text
    html_content=html_content.split()

    
    driver.quit()

    return html_content  

def scrapingutr(url):
    login_url = 'https://app.utrsports.net/'
    html_content=""
    webdriver_path = "C:/Users/email/Documents/ResultTracker/bin/msedgedriver.exe"
    
    options = webdriver.EdgeOptions()
    options.use_chromium = True  # Set this to True for the Chromium-based Edge browser
    options.add_argument("--headless")
    options.add_argument('--disable-extensions')
    options.add_argument('--blink-settings=imagesEnabled=false')
    options.add_argument('--disable-notifications')

    driver = webdriver.Edge(executable_path=webdriver_path, options=options)
    driver.get(login_url)
    wait_time = 10
    time.sleep(wait_time)
    email_field = driver.find_element(By.ID, 'emailInput')  # Replace with the actual attribute
    password_field = driver.find_element(By.ID, 'passwordInput')  # Replace with the actual attribute
    email_field.send_keys('Pankaj1970@gmail.com')
    password_field.send_keys('Shrish@2005')
    submit_button = driver.find_element(By.XPATH, '//button[text()="SIGN IN"]')
    submit_button.click()

        
    
    wait_time = 10
    time.sleep(wait_time)
    profile_url = url
    driver.get(profile_url)

    time.sleep(wait_time)
    xpath_expression = '//*[@id="myutr-app-body"]/div/div[1]/div[1]/div/div/div/div[1]/div[2]/div/div/div[1]/div[2]'
    element = driver.find_element(By.XPATH, xpath_expression)
    html_content=float(element.text)
    
    driver.quit()

    return html_content  
    
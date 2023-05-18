from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from dotenv import load_dotenv
import pydub
import speech_recognition as sr
import tkinter as tk
import os
import time
import random
import string
import urllib.request


### Load From Env File If Exist ###
load_dotenv()

baseUrl = 'https://panel.gozargah.one/#'

### WebDriver Setting ###
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_argument("--incognito")
options.binary_location = os.environ['BROWSER_PATH']
driver = webdriver.Chrome(executable_path= os.environ['BROWSER_DRIVER'], chrome_options= options)
driver.maximize_window()


def websiteRegistration():
    print("[Info] - Signing Up...")
    
    #Opening Selected URL
    driver.get(baseUrl + '/register')
    time.sleep(random.randrange(5,10))

    emailField = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-container"]/div[2]/div/div/div/div[1]/div/div/div[2]/div[1]/input')))
    emailAddress = (''.join(random.choices(string.ascii_lowercase, k=16))+ '@gmail.com')
    emailField.send_keys(emailAddress)
    time.sleep(random.randrange(5,10))

    passwordField = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-container"]/div[2]/div/div/div/div[1]/div/div/div[2]/div[2]/input')))
    password = (''.join(random.choices(string.ascii_lowercase, k=16)))
    passwordField.send_keys(password)
    time.sleep(random.randrange(5,10))

    confirmPasswordField = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-container"]/div[2]/div/div/div/div[1]/div/div/div[2]/div[3]/input')))
    confirmPasswordField.send_keys(password)
    time.sleep(random.randrange(5,10))

    registerButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-container"]/div[2]/div/div/div/div[1]/div/div/div[2]/div[5]/button')))
    registerButton.click()
    time.sleep(random.randrange(5,10))

    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[title='reCAPTCHA']")))
    time.sleep(random.randrange(5,10))

    reCaptchaButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'recaptcha-checkbox-border')))
    reCaptchaButton.click()
    time.sleep(random.randrange(5,10))

    #Back To Default Web Page
    driver.switch_to.default_content()
    time.sleep(random.randrange(5,10))

    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[title='recaptcha challenge expires in two minutes']")))
    time.sleep(random.randrange(5,10))

    audioreCaptchaButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'recaptcha-audio-button')))
    audioreCaptchaButton.click()
    time.sleep(random.randrange(5,10))

    audioSource = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'audio-source'))).get_attribute('src')
    
    print('[INFO] - Audio Source: %s' %audioSource)
    urllib.request.urlretrieve(audioSource, os.getcwd() + '\\reCAPTCHA.mp3')

    print('[INFO] - Bypassing reCAPTCHA')
    sound = pydub.AudioSegment.from_mp3(os.getcwd() + '\\reCAPTCHA.mp3')
    sound.export(os.getcwd() + '\\reCAPTCHA.wav', format='wav')

    #Convert Audio To Text 
    sampleAudio = sr.AudioFile(os.getcwd() + '\\reCAPTCHA.wav')
    r = sr.Recognizer()
    with sampleAudio as source:
        audio = r.record(source)

    key = r.recognize_google(audio)
    print('[INFO] - reCAPTCHA Passcode: %s' %key)

    audioResponse = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'audio-response')))
    audioResponse.send_keys(key)
    time.sleep(random.randrange(5,10))

    verifyButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'recaptcha-verify-button')))
    verifyButton.click()
    time.sleep(random.randrange(5,10))

    return emailAddress, password

def websiteLogIn(emailAddress, password):
    print("[Info] - Logging In...")

    #Opening Selected URL
    driver.get(baseUrl + '/login')
    time.sleep(random.randrange(5,10))

    emailField  = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-container"]/div[2]/div/div/div/div[1]/div/div/div[2]/input')))
    emailField.send_keys(emailAddress)
    time.sleep(random.randrange(5,10))

    passwordField = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-container"]/div[2]/div/div/div/div[1]/div/div/div[3]/input')))
    passwordField.send_keys(password)
    time.sleep(random.randrange(5,10))

    loginButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="main-container"]/div[2]/div/div/div/div[1]/div/div/div[4]/button')))
    loginButton.click()
    time.sleep(random.randrange(5,10))

    subscriptionButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'v2board-shortcuts-item')))
    subscriptionButton.click()
    time.sleep(random.randrange(5,10))

    subscriptionUrl = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'oneClickSubscribe___2t9Xg')))
    subscriptionUrl.click()
    time.sleep(random.randrange(5,10))

    print("[Info] - Subscription Token Created!")

    #Get Clipboard content
    root = tk.Tk()
    root.withdraw()  # to hide the window
    token = root.clipboard_get()

    # All windows related to driver instance will quit
    driver.quit()

    return token


emailAddress, password = websiteRegistration()
subscriptionToken = websiteLogIn(emailAddress, password)

print(f'[Info] - This {subscriptionToken} Token Is Dedicated To This {emailAddress} Email Address')

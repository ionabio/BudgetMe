import pandas as pd
import numpy as np
from selenium import webdriver

def read_data(file_path):
    """
    Function to read data from a file
    """
    data = pd.read_csv(file_path)
    return data

def process_data(data):
    """
    Function to process data
    """
    processed_data = data.dropna()
    return processed_data

def format_data(data):
    """
    Function to format data
    """
    formatted_data = data.round(2)
    return formatted_data

def connect_spendee():
    """
    Function to connect to Spendee using Selenium
    """
    driver = webdriver.Firefox()
    driver.get("https://www.spendee.com/")
    return driver
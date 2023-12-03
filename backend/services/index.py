import requests
import pandas as pd
from selenium import webdriver

class SpendeeService:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def login(self):
        self.driver.get("https://www.spendee.com/login")
        self.driver.find_element_by_name("email").send_keys(self.username)
        self.driver.find_element_by_name("password").send_keys(self.password)
        self.driver.find_element_by_class_name("submit").click()

    def fetch_transactions(self):
        self.driver.get("https://www.spendee.com/transactions")
        transactions = self.driver.find_elements_by_class_name("transaction")
        transactions_list = []
        for transaction in transactions:
            transactions_list.append({
                'date': transaction.find_element_by_class_name("date").text,
                'amount': transaction.find_element_by_class_name("amount").text,
                'category': transaction.find_element_by_class_name("category").text
            })
        return transactions_list

    def close(self):
        self.driver.quit()

class BudgetService:
    def __init__(self, transactions):
        self.transactions = transactions

    def analyze_spending(self):
        df = pd.DataFrame(self.transactions)
        spending_by_category = df.groupby('category').sum()
        return spending_by_category.to_dict()

    def create_budget(self, budget):
        df = pd.DataFrame(self.transactions)
        spending_by_category = df.groupby('category').sum()
        budget_dict = {}
        for category, amount in budget.items():
            budget_dict[category] = {
                'budget': amount,
                'spent': spending_by_category.get(category, 0),
                'remaining': amount - spending_by_category.get(category, 0)
            }
        return budget_dict
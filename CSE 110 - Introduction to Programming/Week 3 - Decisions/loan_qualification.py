"""
This program is to know if a user is qualify for a loan 
based on some questions answered
"""
print("You are to rate the following question from 1-10")
loan = int(input("How large is the loan? "))
credit_history = int(input("How good is your credit history? "))
income = int(input("How high is your income? "))
down_payment = int(input("How large is your down payment? "))
if loan >= 5:
    if credit_history >= 7 and income >= 7:
        print(f"Loan: {loan}, credit history: {credit_history}, income: {income}, down payment: {down_payment}, Descision: Yes")
    elif (credit_history >= 7 or income >= 7) and down_payment >= 5:
        print(f"Loan: {loan}, credit history: {credit_history}, income: {income}, down payment: {down_payment}, Descision: Yes")
    else:
        print(f"Loan: {loan}, credit history: {credit_history}, income: {income}, down payment: {down_payment}, Descision: No")
else:
    if credit_history < 4:
        print(f"Loan: {loan}, credit history: {credit_history}, income: {income}, down payment: {down_payment}, Descision: No")
    elif income >= 7 or down_payment >= 7:
        print(f"Loan: {loan}, credit history: {credit_history}, income: {income}, down payment: {down_payment}, Descision: Yes")
    elif income >= 4 and down_payment >= 4:
        print(f"Loan: {loan}, credit history: {credit_history}, income: {income}, down payment: {down_payment}, Descision: Yes")
    else:
        print(f"Loan: {loan}, credit history: {credit_history}, income: {income}, down payment: {down_payment}, Descision: No")
        
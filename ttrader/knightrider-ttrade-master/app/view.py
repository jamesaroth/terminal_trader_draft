import time

def welcome():
    print("Welcome to KnightRider Trader!\n\nPlease select from the following options\n")

def login_menu():
    answer = input("1. Create an Account\n2. Login\n3. Quit\n\nYou select: ")
    return answer

def username_inpt():
    inpt = input("Enter your username: ")
    return inpt

def password_inpt():
    inpt = input("Enter your password: ")
    return inpt

def set_password_inpt():
    inpt = input("Create your secure password: ")
    return inpt

def invalid_info():
    print("Invalid account number or Password. Try again.\n")

def choose_valid():
    print("Please choose a valid option. Try again.\n")

def enter_digit():
    print("Enter a single numerical digit only.\n")
 
def program_end():
    print("Thank You for trading with us! Come back soon!\n")

def saving_change():
    print("Changes have been saved.\n\n")

def acc_created(username):
    print("A new account for the username: {} has been created\n".format(username))

def ask_ticker():
    ticker = input("Please enter the stock's ticker symbol:\n")
    return ticker

def show_ticker_price(ticker, price):
    print("The current share price of {0}: ${1:.2f}".format(ticker.upper(), price))

def main_menu(username):
    print('Hello '+ username + "!\nPlease choose from the following options:\n")
    inpt = input("1. View Account Balance\n2. Look up current trading price of a stock\n3. Deposit Funds\n4. Buy a stock\n5. Sell a stock\n6. View stock holding details\n7. View detailed trade history\n8. Reset password\n9. Logout and return to main menu\n\nYou select: ")
    return inpt

def deposit_inpt():
    inpt = int(input("How much would you like to deposit into your account? "))
    return inpt

def deposit_outp(amount):
    print("You deposited ${0:.2f} to your account. Changes have been saved\n".format(amount))
    
def balance_statement(amount):
    print("Your account cash balance is: {0:.2f} dollars\n".format(amount))

def newbalance_statement(amount):
    print("Your new account cash balance is: {0:.2f} dollars\n".format(amount))

def not_funds(amount):
    print("You don't have enough funds to withdraw ${0:.2f}".format(amount))

def ask_num_shares():
    inpt = int(input("Please enter the number of shares:\n"))
    return inpt

def bal_and_pos(cash):
    print("\nYour current cash balance: ${0:.2f}".format(cash))

def stockbal(shares, ticker, amount):
    if shares < 0:
        print("You are short {0} shares of {1} currently valued at ${2:.2f}\n".format(abs(shares), ticker, amount))
    else:
        print("You are long {0} shares of {1} currently valued at ${2:.2f}\n".format(shares, ticker.upper(), amount))

def totbal(amount):
    print("The total value of your stock portfolio: ${0:.2f}\n".format(amount))

def totport(amount):
    print("The total value of your portfolio including cash and stock: is ${0:.2f}\n".format(amount))

def no_positions():
    print("You currently have no active stock positions.\n")

def trade_detail(volume, ticker, price, total, date):
    if volume <0:
        print("\nTrade Date & Time: {0}\nYou sold {1} shares of {2} at ${3:.2f}/share for a total of ${4:.2f}".format(time.asctime(time.localtime(date)), -1 * volume, ticker, price, -1 * total))
    else:
        print("\nTrade Date & Time: {0}\nYou bought {1} shares of {2} at ${3:.2f}/share for a total of ${4:.2f}".format(time.asctime(time.localtime(date)), volume, ticker, price, total))

def total_trades(total):
    print("You've executed a total of {} trades".format(total))

def confirm_order(buy_sell, ticker, shares, total):
    inpt = input("To confirm: You would like to {0} {1} shares of {2} for a total of {3:.2f}\n\nType 'Y' to confirm.".format(buy_sell, shares, ticker, total))
    return inpt

def insuf_funds():
    print("You do not have enough funds available to complete this trade.  Please enter a smaller number of shares to complete this trade.\n")

def no_position_stock():
    print("You do not own a sufficient number of shares of this stock.  Please select another stock ticker.")
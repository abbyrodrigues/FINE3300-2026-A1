# ExchangeRates.py
# This is an exchange rate converter using Bank of Canada data given in the CSV file
# Reads the latest USD/CAD rate from the CSV file

class ExchangeRates:
    def __init__(self, filename):
        # open the file and read all lines
        file = open(filename, "r")
        lines = file.readlines()
        file.close()

        # the last line has the newest rates
        last_line = lines[-1].strip()
        parts = last_line.split(",")

        # FXAUSDCAD is the 26th column (index 25)
        # this is how many Canadian dollars equal 1 US dollar
        self.usd_to_cad = float(parts[25])

    def convert(self, amount, from_currency, to_currency):
        # convert the amount from one currency to the other
        if from_currency == "USD" and to_currency == "CAD":
            result = amount * self.usd_to_cad
        elif from_currency == "CAD" and to_currency == "USD":
            result = amount / self.usd_to_cad
        else:
            # same currency, just return the amount
            result = amount
        return result


# main program starts here

# create the object and load the rates
rates = ExchangeRates("BankOfCanadaExchangeRate.2026.csv")

# ask the user for the three pieces of information
amount = float(input("Enter the amount: "))
from_curr = input("Enter the from currency (USD or CAD): ").upper()
to_curr = input("Enter the to currency (USD or CAD): ").upper()

# do the conversion
converted = rates.convert(amount, from_curr, to_curr)

# print the result rounded to the nearest penny with $ and currency
print(f"${converted:,.2f} {to_curr}")
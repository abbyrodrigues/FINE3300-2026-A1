# ExchangeRatesAI.py
# This was generated with the help of a Grok LLM for comparison purposes

import csv
# Import the csv module the exchange rate file is easily readable

class ExchangeRates:
    def __init__(self, filename):
        with open(filename, mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)
            # last data row contains the most recent rates
            latest = rows[-1]
            # USD/CAD rate is in column index 26
            self.rate = float(latest[26])
            # Store the latest USD/CAD rate (how many CAD equal 1 USD)

    def convert(self, amount, from_currency, to_currency):
        from_currency = from_currency.upper()
        to_currency = to_currency.upper()
        # Convert the amount based on the direction the user requested
        if from_currency == "USD" and to_currency == "CAD":
            return amount * self.rate
        elif from_currency == "CAD" and to_currency == "USD":
            return amount / self.rate
        else:
            return amount


if __name__ == "__main__":
    converter = ExchangeRates("BankOfCanadaExchangeRate.2026.csv")
    amount = float(input("Enter amount: "))
    from_curr = input("From currency (USD/CAD): ")
    to_curr = input("To currency (USD/CAD): ")
    result = converter.convert(amount, from_curr, to_curr)
    print(f"${result:,.2f} {to_curr.upper()}")
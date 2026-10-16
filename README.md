# FINE3300-2026-A1

Exchange Rate Calculator – FINE 3300 Assignment #1

## Description

This project converts amounts between Canadian Dollars (CAD) and US Dollars (USD) using the latest exchange rate published by the Bank of Canada in the provided CSV file.

The program reads the file BankOfCanadaExchangeRate.2026.csv and uses the most recent USD/CAD rate.

## How to Run

1. Make sure the CSV file is in the same folder.
2. Run either:
   - python ExchangeRates.py   (this one is my own code)
   - python ExchangeRatesAI.py (AI-generated version)

Python will prompt you and should be asked for the amount and the two currencies. For example (from my own code, not the AI code): "Enter the amount:" or "Enter the from/to currency (USD or CAD):"

## Files

- ExchangeRates.py – my original solution
- ExchangeRatesAI.py – version written with the help of the Grok LLM
- BankOfCanadaExchangeRate.2026.csv – source data from Bank of Canada

## Sample Output

$100,000 USD to CAD → $139,780.00 CAD  
$100,000 CAD to USD → $71,540.99 USD
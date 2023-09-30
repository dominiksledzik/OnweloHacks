# generate a pdf file with a title, then some description and a table with some data

# import the necessary libraries
from fpdf import FPDF
import requests
import datetime
import json


#globals
report_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#load the data from the json file
with open('example_report.json') as f:
    report = json.load(f)

# print(report)

#create a pdf object
pdf = FPDF()

# add a page
pdf.add_page()

def generate_title(title):
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt=title, ln=1, align="C")

def generate_description(description):
    pdf.set_font("Arial", '', 12)
    pdf.cell(200, 10, txt=description, ln=1, align="L")

def generate_portfolio_table(report):
    pdf.set_font("Arial", '', 10)

    pdf.cell(30, 10, txt="Waluta", border=1, align="C")
    pdf.cell(30, 10, txt="Ilosc", border=1, align="C")
    pdf.cell(30, 10, txt="Kurs w PLN", border=1, align="C")
    pdf.cell(30, 10, txt="Cena w PLN", border=1, align="C")
    pdf.ln()

    total_portfolio_pln = 0.0

    for coin in report['cryptocurrencies']:
        # get coin data
        coin_name = coin['name']
        coin_volume = coin['volume']
        
        coin_exchange_pln = 0.0

        for exchange in coin['exchanges']:
            if "pln" in exchange:
                coin_exchange_pln += exchange['pln']
            elif "usd" in exchange:
                coin_exchange_pln += (exchange['usd'] * report['nbp_usd_pln'])
            else:
                pass

        coin_exchange_pln /= 3
        coin_price_pln = coin_volume * coin_exchange_pln
        
        total_portfolio_pln += coin_price_pln

        # add data to table
        pdf.cell(30, 10, txt=coin_name, border=1, align="C")
        pdf.cell(30, 10, txt="{:.2f}".format(coin_volume), border=1, align="C")
        pdf.cell(30, 10, txt="{:.2f}".format(coin_exchange_pln), border=1, align="C")
        pdf.cell(30, 10, txt="{:.2f}".format(coin_price_pln), border=1, align="C")
        # pdf.cell(30, 10, txt=coin_last_updated, border=1, align="C")
        pdf.ln()

    # add total value of the portfolio
    pdf.ln()
    pdf.cell(30, 10, txt="Suma w PLN", border=1, align="C")
    pdf.cell(30, 10, txt="{:.2f}".format(total_portfolio_pln), border=1, align="C")
    pdf.ln()


def generate_currency_table(report):
    for currency in report['cryptocurrencies']:
        generate_title(currency['name'])
        pdf.ln()

        pdf.set_font("Arial", '', 10)
        pdf.cell(30, 10, txt="Nazwa gieldy", border=1, align="C")
        pdf.cell(30, 10, txt="Kurs w USD", border=1, align="C")
        pdf.cell(30, 10, txt="Kurs w PLN", border=1, align="C")
        pdf.cell(40, 10, txt="Data aktualizacji", border=1, align="C")
        pdf.ln()

        for exchange in currency['exchanges']:
            exchange_name = exchange['name']
            if "pln" in exchange:
                exchange_price_usd = "-"
                exchange_price_pln = "{:.2f}".format(exchange['pln'])
            elif "usd" in exchange:
                exchange_price_usd = "{:.2f}".format(exchange['usd'])
                exchange_price_pln = "{:.2f}".format(exchange['usd'] * report['nbp_usd_pln'])
            
            pdf.cell(30, 10, txt=exchange_name, border=1, align="C")
            pdf.cell(30, 10, txt=exchange_price_usd, border=1, align="C")
            pdf.cell(30, 10, txt=exchange_price_pln, border=1, align="C")
            pdf.cell(40, 10, txt=report_date, border=1, align="C")
            pdf.ln()

        pdf.ln()


# Title section of the PDF
generate_title("Crypto Price Data")

# Description section of the PDF
generate_description("This is a pdf file with some crypto price data")


'''
First part of the PDF - general data about the portfolio
'''

# General table report
generate_portfolio_table(report)


'''
Second part of the PDF - average price of the coins on different exchanges
'''

generate_currency_table(report)


pdf.output("crypto_price_data.pdf")
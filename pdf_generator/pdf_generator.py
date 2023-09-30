# generate a pdf file with a title, then some description and a table with some data

# import the necessary libraries
from fpdf import FPDF
import datetime
import requests

#create a pdf object
pdf = FPDF()

# add a page
pdf.add_page()

# set style and size of font

# font style
# 'B' = 'Bold'
# 'U' = 'Underline'
# 'I' = 'Italic'
# '' = 'Regular'

# font size
# 16 = 16pt
# 32 = 32pt
# 64 = 64pt


# Title section of the PDF
pdf.set_font("Arial", 'B', 16)

pdf.cell(200, 10, txt="Crypto Price Data", ln=1, align="C")

# Description section of the PDF
pdf.set_font("Arial", '', 12)

pdf.cell(200, 10, txt="This is a pdf file with some crypto price data", ln=1, align="L")

# Table section of the PDF
pdf.set_font("Arial", '', 10)

pdf.cell(30, 10, txt="Waluta", border=1, align="C")
pdf.cell(30, 10, txt="Ilosc", border=1, align="C")
pdf.cell(30, 10, txt="Kurs w USD", border=1, align="C")
pdf.cell(30, 10, txt="Cena w USD", border=1, align="C")
pdf.cell(30, 10, txt="Kurs w PLN", border=1, align="C")
pdf.cell(30, 10, txt="Cena w PLN", border=1, align="C")
pdf.ln()

# get data from coinmarketcap
url = "https://api.coinmarketcap.com/data-api/v3/cryptocurrency/listing?start=1&limit=10&sortBy=market_cap&sortType=desc&convert=USD&cryptoType=all&tagType=all&audited=false"
response = requests.get(url)
data = response.json()
coin_data = data['data']['cryptoCurrencyList']
usd_pln_rate = 4.38

sum_in_pln = 0.0

# loop through the data
for coin in coin_data:
    # get coin data
    coin_name = coin['name']
    coin_volume = 500.0
    coin_exchange_usd = coin['quotes'][0]['price']
    coin_price_usd = coin_volume * coin_exchange_usd
    coin_exchange_pln = coin_exchange_usd * usd_pln_rate
    coin_price_pln = coin_volume * coin_exchange_pln
    
    #Adding up the total value of the portfolio
    sum_in_pln += coin_price_pln

    # convert timestamp to date
    # coin_last_updated = datetime.datetime.fromtimestamp(coin_last_updated/1000).strftime("%Y-%m-%d %H:%M:%S")
    
    # add data to table
    pdf.cell(30, 10, txt=coin_name, border=1, align="C")
    pdf.cell(30, 10, txt="{:.2f}".format(coin_volume), border=1, align="C")
    pdf.cell(30, 10, txt="{:.2f}".format(coin_exchange_usd), border=1, align="C")
    pdf.cell(30, 10, txt="{:.2f}".format(coin_price_usd), border=1, align="C")
    pdf.cell(30, 10, txt="{:.2f}".format(coin_exchange_pln), border=1, align="C")
    pdf.cell(30, 10, txt="{:.2f}".format(coin_price_pln), border=1, align="C")
    # pdf.cell(30, 10, txt=coin_last_updated, border=1, align="C")
    pdf.ln()

# add total value of the portfolio
pdf.ln()
pdf.cell(30, 10, txt="Suma w PLN", border=1, align="C")
pdf.cell(30, 10, txt="{:.2f}".format(sum_in_pln), border=1, align="C")
# save the pdf with name .pdf
pdf.output("crypto_price_data.pdf")
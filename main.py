from backend import backend
from pdf_generator import pdf_generator

currencies = {"BTC": 0.005, "ETH": 12, "CITY": 2000}

output = backend.get_data(currencies)
pdf_generator.generate_pdf(output)
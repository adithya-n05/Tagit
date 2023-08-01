import app_store_scraper
import fpdf
from datetime import datetime

AppCountry = "us"
AppName = "zenith-bank-eazymoney"
AppID = 732850254

def Scraper(AppCountry, AppName, AppID):

    pdf = fpdf.FPDF(format='letter')
    pdf.add_page()
    pdf.set_font("Arial", "",  size=10)

    axis_bank = app_store_scraper.AppStore(country=AppCountry, app_name=AppName, app_id=AppID)   # Axis Mobile

    axis_bank.review(how_many=100000)    # 20000 reviews

    print(axis_bank.reviews)

    for i in range(len(axis_bank.reviews)):
        text = "User Name - " + str(axis_bank.reviews[i]['userName']) + ":"
        review = text.encode('latin-1', 'replace').decode('latin-1')
        pdf.write(12, review) 
        pdf.ln()
        text = "Date and time - " + datetime.strftime(axis_bank.reviews[i]['date'], "%d/%m/%Y %H:%M:%S") + ":"
        review = text.encode('latin-1', 'replace').decode('latin-1')
        pdf.write(12, review) 
        pdf.ln()
        text = "Review - " + str(axis_bank.reviews[i]['review']) + ":"
        review = text.encode('latin-1', 'replace').decode('latin-1')
        pdf.write(12, review)
        pdf.ln()

    pdf.output("Comments-" + AppName + ".pdf")

Scraper(AppCountry, AppName, AppID)
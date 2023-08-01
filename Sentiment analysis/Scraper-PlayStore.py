import google_play_scraper
import fpdf
from datetime import datetime
import pandas as pd

AppCountry = "US"
AppName = "com.zenithBank.eazymoney"

def Scraper(AppCountry, AppName):

    pdf = fpdf.FPDF(format='letter')
    pdf.add_page()
    pdf.set_font("Arial", "",  size=10)

    axis_bank = google_play_scraper.reviews_all(AppName, country=AppCountry, lang="en", sleep_milliseconds=0)

    print(axis_bank)

    dataframepd = pd.json_normalize(axis_bank)

    print(dataframepd)

    for i in range(len(dataframepd[dataframepd.columns[0]].values.tolist())):
        text = str(dataframepd[dataframepd.columns[1]].values.tolist()[i]) + ":"
        review = text.encode('latin-1', 'replace').decode('latin-1')
        pdf.write(12, review) 
        pdf.ln()
        text = "Score - " + str(dataframepd[dataframepd.columns[4]].values.tolist()[i]) + ":"
        review = text.encode('latin-1', 'replace').decode('latin-1')
        pdf.write(12, review) 
        pdf.ln()
        text = "Date and time - " + str(dataframepd[dataframepd.columns[7]].values.tolist()[i]) + ":"
        review = text.encode('latin-1', 'replace').decode('latin-1')
        pdf.write(12, review) 
        pdf.ln()
        text = str(dataframepd[dataframepd.columns[3]].values.tolist()[i]) + ":"
        review = text.encode('latin-1', 'replace').decode('latin-1')
        pdf.write(12, review)
        pdf.ln()


    pdf.output("Comments-" + "PlayStore-" + AppName + ".pdf")

Scraper(AppCountry, AppName)
from dotenv import load_dotenv
from excel_parser import get_inventory
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import os


def get_age_text(years):
    if int(str(years)[-1:]) == 1 and int(str(years)[-2:]) != 11:
        age_text = "год"
    elif int(str(years)[-1:]) in range(2, 5) and (years < 10 or int(str(years)[-2:-1]) != 1):
        age_text = "года"
    else:
        age_text = "лет"

    return age_text


def main():
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    load_dotenv()

    spreadsheet = os.getenv("SPREADSHEET_PATH", default="wine.xlsx")
    inventory = get_inventory(spreadsheet)

    founding_date = datetime.date(year=1920, month=1, day=1)
    company_age = datetime.date.today() - founding_date
    company_years = company_age.days//365

    age_text = get_age_text(company_years)

    rendered_page = template.render(
        company_years=f"Уже {company_years} {age_text} с вами",
        inventory=inventory
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()

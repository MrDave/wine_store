from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape
import datetime
import pandas
from excel_parser import get_inventory

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')
inventory = get_inventory("wine2.xlsx")
founding_date = datetime.date(year=1920, month=1, day=1)
company_age = datetime.date.today()-founding_date
company_years = company_age.days//365
if company_years % 10 == 1 and company_years != 11 and company_years % 100 != 11:
    age_text = "год"
elif company_years % 10 in range(2, 5) and company_years not in range(12, 15):
    age_text = "года"
else:
    age_text = "лет"

wines = pandas.read_excel("wine.xlsx").to_dict(orient="records")

rendered_page = template.render(
    company_years=f"Уже {company_years} {age_text} с вами",
    inventory=inventory
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()

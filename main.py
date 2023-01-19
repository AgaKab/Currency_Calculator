import requests
from datetime import datetime

waluta = input("Sprawdź dzisiejszy kurs dla waluty: ").upper()
# data = input("Którego dnia kurs chcesz sprawdzi? Podaj datę w formacie (YYYY-MM-DD): ")
today = datetime.now()
x=today.strftime("%Y-%m-%d")
# print(x)

URL=f"http://api.nbp.pl/api/exchangerates/rates/a/{waluta}/{x}/?format=json"


response = requests.get(URL)
results = response.json()["rates"][0]["mid"]
print(results)
score = f"1 {waluta} = {results} PLN"
print(score)


# dane = {
#     "table":"A",
#     "currency":"dolar amerykański",
#     "code":"USD",
#     "rates":[
#         {"no":"064/A/NBP/2016",
#          "effectiveDate":"2016-04-04",
#          "mid":3.7254}
#     ]}
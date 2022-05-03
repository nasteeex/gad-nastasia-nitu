from bs4 import BeautifulSoup
import requests
import pandas as pd

r = requests.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-20-ianuarie-ora-13-00/")
link = BeautifulSoup(r.text, "html.parser")

title = link.find_all("div", attrs={"class": "entry-content"})

header = []
dataset = []
index = 0
for i in title:
    for table_index in i.find_all("table"):
        for tbody_index in table_index.find_all("tbody"):
            index += 1
            if index > 1:
                break
            for tr_index in tbody_index.find_all("tr"):
                if tr_index.find_all("td"):
                    for td_index in tr_index.find_all("td"):
                        td_list = []
                        header.append(td_index.get_text())
                for index, td_value in enumerate(tr_index.find_all("td")):
                    td_list.append(td_value.get_text())
                dataset.append(td_list)
            else:
                break

header = header[0:5]
dataset = dataset[1:]

df = pd.DataFrame(dataset, columns=header)
df.set_index(header[0], inplace=True)
df.to_csv("covid_eu.csv", header=header[1:5])
df.to_csv("covid_eu.xls", header=header[1:5])

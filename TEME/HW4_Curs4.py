from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://ro.wikipedia.org/wiki/Jude%C8%9Bele_Rom%C3%A2niei")

table = browser.find_element(by=By.XPATH, value='//*[@id="mw-content-text"]/div[1]/table[3]')
# print(table.text)
lista = table.text.split("\n")
# print(lista)

header_len = browser.find_element(by=By.XPATH, value='//*[@id="mw-content-text"]/div[1]/table[3]/thead/tr')
header = header_len.text.split("\n")

dictionar = {i: [] for i in header}
for j in range(0, len(header)):
    for i in range(len(header) + int(j), len(lista), len(header)):
        # print(lista[i])        dictionar[header[int(j)]].append(lista[i])
# print(dictionar)

df = pd.DataFrame(dictionar)
df.to_csv("HW4_Wikipedia.csv")
df.to_csv("HW4_Wikipedia.xls")
browser.close()

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
browser = webdriver.Chrome(ChromeDriverManager().install())
dictionary = {}
for i in range(20, 28):
    browser.get(f"https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-{i}-ianuarie-ora-13-00/")
    table = browser.find_element(by=By.XPATH, value='//table')
    list = table.text.split('\n')[1:43]
    list2 = []
    for j in list:
        tmp = j.split(' ')
        list2.append([tmp[0]] + [''.join(tmp[1:len(tmp) - 3])] + tmp[-3:])
    list = list2
    header = []
    for j in range(5):
        header.append(browser.find_element(by=By.XPATH, value=f'//table//td[{j + 1}]').text)
    if len(dictionary) == 0:
        dictionary = {i: [] for i in header}
    for it in list2:
        for j in range(len(header)):
            dictionary[header[j]].append(it[j])
print(dictionary)
df = pd.DataFrame(dictionary)
df.to_csv('covid_grupa5.xls')
browser.close()
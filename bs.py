from bs4 import BeautifulSoup
import requests
import pandas as pd

r = requests.get("https://bnr.ro/Cursul-de-schimb--7372.aspx")
# prin(r.text)
link = BeautifulSoup(r.text, "html.parser")
# print(link)

title = link.find_all("div", attrs = {"class": "contentDiv"})
# print(title)

header = []
dataset = []
for i in title:
    # print(i)
    for tr_index in i.find_all("table"):
        # print(tr_index)
        for td_index in tr_index.find_all("tr"):
            # print(td_index)
            td_list = []
            if td_index.find_all("th"):
                # # print(td_index.find_all("th"))
                # for th_index in td_index.find_all("th"):
                #     # print(th_index.get_text())
                #     # header.append(th_index.get_text())
                header = [th_index.get_text() for th_index in td_index.find_all("th")]
            for index, td_value in enumerate(td_index.find_all("td")):
                print(index, td_value)
                if index == 0:
                    td_list.append(td_value.get_text())
                else:
                    td_list.append(float(td_value.get_text().replace(",", ".")))
            dataset.append(td_list)
print(dataset)

df = pd.DataFrame(dataset, columns = header)
# print(df)
df.to_csv("CursBNR.csv", header = header)
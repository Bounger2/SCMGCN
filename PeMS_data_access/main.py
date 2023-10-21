import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
data = {"redirect": "", "username": "xxxxxxxx",
        "password": "xxxxxxxx", "login": "Login"}

data_id=pd.read_excel("data/pems03.xlsx",header=0,index_col=None).values
datas=[]
for id in data_id:
    url="https://pems.dot.ca.gov/?station_id="+str(id[0])+"&dnode=VDS&content=sta_cfg"


    # 发送HTTP请求获取HTML内容
    # url = "https://pems.dot.ca.gov/?station_id=317814&dnode=VDS&content=sta_cfg"  # 将YOUR_URL替换为包含表格的网页URL


    session = requests.session()
    response = session.post(url, headers=headers, data=data)
    response = session.get(url)

    html_content = response.content

    # 使用BeautifulSoup解析HTML内容
    soup = BeautifulSoup(html_content, 'html.parser')

    # 查找包含数据的表格行（tr）
    table_rows = soup.find_all('tr')

    lon=[]
    lat=[]
    # 循环遍历表格行，提取所需的数据
    for row in table_rows:
        # 查找包含数据的单元格（td）
        cells = row.find_all('td')

        # 提取所需的两个值
        if len(cells) >= 9:
            value1 = cells[7].text.strip()  # 第8个单元格的值
            value2 = cells[8].text.strip()  # 第9个单元格的值
            lat.append(value1)
            lon.append(value2)
            # # 打印提取的值
            # print("Value 1:", value1)
            # print("Value 2:", value2)
    print(id[0],lon[0],lat[0])

    datas.append([id[0],lon[0],lat[0]])
    datasf=pd.DataFrame(datas)
    datasf.to_csv("data/pems03_lonlat.csv")
    time.sleep(15)




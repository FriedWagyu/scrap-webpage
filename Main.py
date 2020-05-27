import requests
from bs4 import BeautifulSoup
import openpyxl

htmlFile = requests.get("http://www.pgh.cuhk.edu.hk/announcements/2020/SuccessList.php").text
soup = BeautifulSoup(htmlFile, "html.parser")
table = soup.find("table", attrs = {"border": 1})
tds = table.findAll("td")
studentInfo = []

for td in tds:
    studentInfo.append(td.text.strip())

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "Admitted"

countRow = 1
countCol = 1

for info in studentInfo:
    if countCol == 4:
        countRow = countRow + 1
        countCol = 1
    sheet.cell(row = countRow, column = countCol).value = info
    countCol = countCol + 1

wb.save("data.xlsx")
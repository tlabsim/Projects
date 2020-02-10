import requests
import time
import bs4
import xlwt
import xlutils
import xlrd
from xlutils.copy import copy
from xlwt import Workbook
wb=Workbook()
sheet1 = wb.add_sheet('Sheet 1') 
conter=0
def get_single_item_data(item_url):
    global count1,count2,conter
    count1=w_sheet.nrows+conter
    count2=w_sheet.nrows+conter
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = bs4.BeautifulSoup(plain_text)
    for item_name in soup.findAll('h1', {'class': 'title mb10'}):
        for i in range(w_sheet.nrows):
          str=w_sheet.cell_value(i,0)  
          if(item_name.text==str):
              return
        
        print(item_name.text)
        cpy_sheet.write(count1, 0, item_name.text)
        count1=count1+1
        #conter=conter+1
    for item_name in soup.findAll('div', {'itemprop': 'articleBody'}):
        #print(item_name.text)
        cpy_sheet.write(count2, 1, item_name.text)
        #count2=count2+1     
    


tt=0
#p=w_sheet.nrows
#print(p)
#print(w_sheet.nrows) 
while True:
    url = 'https://www.prothomalo.com/' 
    source_code = requests.get(url)
    plain_text = source_code.text
    soup2 = bs4.BeautifulSoup(plain_text)
    for link in soup2.findAll('a',{'class':'link_overlay'}):
        rb=xlrd.open_workbook('Prothom_Alo.xls')
        wb=copy(rb)
        cpy_sheet=wb.get_sheet(0)
        w_sheet = rb.sheet_by_index(0) 
        count1=w_sheet.nrows
        count2=w_sheet.nrows
        href = "https://www.prothomalo.com"+link.get('href')
        get_single_item_data(href)
        wb.save('Prothom_Alo.xls') 
    tt=tt+1
    print(tt)
    clk=0
    while clk<120:
        time.sleep(1)
        clk=clk+1
    

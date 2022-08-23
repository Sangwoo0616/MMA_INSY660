# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 10:05:59 2022

@author: User
"""

import pandas as pd
import requests
from bs4 import BeautifulSoup



#------------------------------------------------------
#Qu2 : Create the for loop to get the review information from the 1st to 10th page.
#------------------------------------------------------
url_list=[]
page1_to_10 = ''
for i in range (1, 11):
    url_page = soup.fin_all(class_='https://www.bankbazaar.com/reviews.html?reviewPageNumber='+ str(i))
    url_list.append(url_page)
    page = requests.get(url_page)
    page_text = page.text
    page1_to_10 += page_text
    
#------------------------------------------------------
#Correction
#------------------------------------------------------
def url_page(page_num):
    url_base='https://www.bankbazaar.com/reviews.html?reviewPageNumber='
    url=url_base+str(page_num)
    return url

url_list=[]

for page_num in range (1,11):
    url_list.append(url_page(page_num))

page_text = ""
for url in url_list:
    page = requests.get(url)
    page_text += page.text



#------------------------------------------------------
#Qu3 : Collecte Review Rate Data
#------------------------------------------------------

review_elem=soup.find_all(class_='rating-section review-user-score')

review_score=[]
for item in review_elem :
   review_score.append(item.find('input').get('value'))
   
#add the key to the dictionnary
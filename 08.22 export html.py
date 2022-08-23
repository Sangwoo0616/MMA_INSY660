# -*- coding: utf-8 -*-
"""
Created on Mon Aug 22 09:33:02 2022

@author: User
"""

#----------------------------
#Step 0 : import module
#----------------------------

import pandas as pd
import requests
from bs4 import BeautifulSoup


#----------------------------
#Step 1 : send Request
#----------------------------

#1) URL
url = 'https://www.bankbazaar.com/reviews.html'
url_2 = 'https://www.bankbazaar.com/reviews.html?reviewPageNumber=2'
#2) requests.get()
page = requests.get(url)
page_text = page.text
page_2 = requests.get(url_2)
page_text_2=page_2.text


#----------------------------
#Step 2 : Parsing Data
#----------------------------

#page 1
soup = BeautifulSoup(page_text, 'html.parser')

#1) read review text
review_text_elem = soup.find_all(class_='text_here review-desc-more')
review_text=[]
for item in review_text_elem:
    #review_text.append(item.text)
    review_text.append(item.text.lstrip())
    #remove all the spaces

user_name_elem = soup.find_all(class_='js-author-name')

user_name=[]
for item in user_name_elem:
    user_name.append(item.text)

bank_name_elem = soup.find_all(class_='review-bank-title')

bank_name=[]
for item in bank_name_elem:
    bank_name.append(item.text)    


#----------------------------
#Step 3 create dataframe
#----------------------------

final_dict = {'User_Name' : user_name,
              'Bank_Name' : bank_name,
              'Review_Text' : review_text,
              #'Review_Rate' : review_score,
              }

df = pd.DataFrame(final_dict)


#----------------------------
#save df to csv file
#----------------------------

df.to_csv('bank_review.csv', index=False)


#----------------------------
#save df to excel file
#----------------------------

df.to_excel('scrapping_bank.xlsx', index = False)






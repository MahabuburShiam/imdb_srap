import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
url = 'https://www.imdb.com/chart/top/'
options = Options()
options.headless = True
driver = webdriver.Chrome(options=options)
try:
    driver.get(url)
    #driver.raise_for_status()
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    movies = soup.find('ul',class_='ipc-metadata-list ipc-metadata-list--dividers-between sc-e22973a9-0 khSCXM compact-list-view ipc-metadata-list--base').find_all('li',class_='ipc-metadata-list-summary-item')
    #print(len(movies))
    
    for movie in movies:
       # print(movie)
        title=movie.find('div',class_="ipc-title ipc-title--base ipc-title--title ipc-title--title--reduced ipc-title-link-no-icon ipc-title--on-textPrimary sc-d145e74b-2 kJNxDo cli-title with-margin")
        title=title.a.text #getting content in tag a --> 1.Shaswank Redemption
        title=title.split('.')
        
        rank=title[0]
        movie_name=title[1]
        
        rating=movie.find('span',class_='ipc-rating-star--rating').text
        
        #year_runtime=movie.find_all('span',class_='sc-dc48a950-8 gikOtO cli-title-metadata-item')
        #year=movie.find('span',class_='sc-dc48a950-8 gikOtO cli-title-metadata-item').text
        
        test=movie.find_all('span',class_='sc-dc48a950-8 gikOtO cli-title-metadata-item')
        year=test[0].text
        run_time=test[1].text
        
        vote_count=movie.find('span',class_='ipc-rating-star--voteCount').text
        
        #print(rank,movie_name,rating,year,run_time)
        vote_count=vote_count.strip('()')
        for i in vote_count:
            if i!='(' and i!=')':
                print(i,end="")
        break
        
        
    
    driver.quit()
    
    
except Exception as e:
    print(e)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

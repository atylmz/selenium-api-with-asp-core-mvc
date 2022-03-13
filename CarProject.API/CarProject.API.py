
import json
import time
from selenium import webdriver
from flask import Flask

app = Flask(__name__)

wsgi_app = app.wsgi_app
browser = webdriver.Chrome("C:\\Users\\ahmet\\Desktop\\chromedriver")


@app.route('/cars')
def call_cars():
    browser.get("https://www.cars.com/shopping/results/")
    i = 6
    time.sleep(1)
    item = [] 
  
    while i < 10 :
           i = i+1
           if i != 5 and i != 11 and i != 16 and i != 21 :
                clickthis = browser.find_element_by_xpath("/html/body/section/div[2]/div[6]/div/div[1]/div[{}]/div/div[1]".format(i))
                clickthis.click()
                time.sleep(3)
                title = browser.find_element_by_xpath("/html/body/section/div[5]/section/header/div[1]/h1")
                thistitle = title.text
                price = browser.find_element_by_xpath("/html/body/section/div[5]/section/header/div[2]/span[1]")
                thisprice = price.text
                carURL = browser.find_element_by_id("swipe-index-0").get_attribute("src")
                thiscarURL = carURL
                splitted = title.text.split(" ",1)
                brand = splitted[1]
                year = splitted[0]
                color = browser.find_element_by_xpath("/html/body/section/div[5]/div[2]/section[1]/dl/dd[1]")
                thiscolor = color.text
                transmission = browser.find_element_by_xpath("/html/body/section/div[5]/div[2]/section[1]/dl/dd[6]")
                thistransmission = transmission.text
                car_dict = {         
                "title": thistitle,
                "price" : thisprice,
                "carURL" : thiscarURL,
                "brand" : brand,
                "year" : year,
                "color" : thiscolor,
                "transmission" : thistransmission
                } 
                time.sleep(1)
                browser.execute_script("window.history.go(-1)")
                time.sleep(1)
                i = i + 1
                item.append(car_dict) 
    return json.dumps(item)         
       

@app.route('/filter/<string:color>/<string:brand>/<string:tran>')
def filter(color,brand,tran):
     color_param = color
     make_param = brand
     trans_param = tran
     browser = webdriver.Chrome("C:\\Users\\ahmet\\Desktop\\chromedriver")
     item =[]
     browser.get("https://www.cars.com/shopping/results/?dealer_id=&/exterior_color_slugs[]={}&makes[]={}&transmission_slugs[]={}".format(color_param, make_param, trans_param))
     time.sleep(3)
     i = 6
     while i < 10 :
           i = i+1
           if i != 5 and i != 11 and i != 16 and i != 21 :
                clickthis = browser.find_element_by_xpath("/html/body/section/div[2]/div[6]/div/div[1]/div[{}]/div/div[1]".format(i))
                clickthis.click()
                time.sleep(3)
                title = browser.find_element_by_xpath("/html/body/section/div[5]/section/header/div[1]/h1")
                thistitle = title.text
                price = browser.find_element_by_xpath("/html/body/section/div[5]/section/header/div[2]/span[1]")
                thisprice = price.text
                carURL = browser.find_element_by_id("swipe-index-0").get_attribute("src")
                thiscarURL = carURL
                splitted = title.text.split(" ",1)
                brand = splitted[1]
                year = splitted[0]
                color = browser.find_element_by_xpath("/html/body/section/div[5]/div[2]/section[1]/dl/dd[1]")
                thiscolor = color.text
                transmission = browser.find_element_by_xpath("/html/body/section/div[5]/div[2]/section[1]/dl/dd[6]")
                thistransmission = transmission.text
                car_dict = {         
                "title": thistitle,
                "price" : thisprice,
                "carURL" : thiscarURL,
                "brand" : brand,
                "year" : year,
                "color" : thiscolor,
                "transmission" : thistransmission
                } 
                time.sleep(1)
                browser.execute_script("window.history.go(-1)")
                time.sleep(1)
                i = i + 1
                item.append(car_dict) 
     return json.dumps(item)         



if __name__ == '__main__':
    app.run(port=62154)















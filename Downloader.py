from selenium import webdriver
import urllib.request
driver = webdriver.Chrome("C:\\Users\\USERP\\Downloads\\chromedriver.exe")
driver.get("link of the site here");

#change this with url

list = ["list of the image to be downloaded"]

a = 0

for i in list:
    driver.get(i)
    image_name = "image" + str(a) + ".jpg"
    image = driver.find_element_by_xpath('//*[@id="hamaraphotos-photo"]')
    src = image.get_attribute('src')
    urllib.request.urlretrieve(src,image_name)
    a = a + 1

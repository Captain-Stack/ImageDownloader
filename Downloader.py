from selenium import webdriver
import urllib.request
driver = webdriver.Chrome("C:\\Users\\USERP\\Downloads\\chromedriver.exe")
driver.get("https://hamaraphotos.com/thumbnails.php?search=shreya+ghoshal&album=search&type=full")

#change this with url

list = ["https://hamaraphotos.com/bollywood_photos_search_results_-_shreya_ghoshal_search_0_0.html",
"https://hamaraphotos.com/bollywood_photos_search_results_-_shreya_ghoshal_search_0_1.html",
"https://hamaraphotos.com/bollywood_photos_search_results_-_shreya_ghoshal_search_0_2.html"]

a = 0

for i in list:
    driver.get(i)
    image_name = "image" + str(a) + ".jpg"
    image = driver.find_element_by_xpath('//*[@id="hamaraphotos-photo"]')
    src = image.get_attribute('src')
    urllib.request.urlretrieve(src,image_name)
    a = a + 1

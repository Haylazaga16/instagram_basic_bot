from selenium import webdriver
import time
#import pyautogui


browser = webdriver.Firefox()
browser.get("https://www.instagram.com")
time.sleep(2)

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")
username.send_keys("udemyicin")
password.send_keys("selenium")
time.sleep(2)
try:
    login = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]")
    login.click()
    time.sleep(2)
except:
    login = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div")
    login.click()
    time.sleep(2)
    try:
        login = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div")
        login.click()
        time.sleep(2)
    except:
        print("Giris yapa tiklayamadik \n")
time.sleep(2)

browser.get("https://www.instagram.com/p/CBitlZLgbMZ/")
time.sleep(2)

login2 = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[2]/div/div/a")
login2.click()
time.sleep(2)

"""
Eski Scroll
pyautogui.moveTo(1047, 776)
pyautogui.click()
pyautogui.click()
pyautogui.click()
pyautogui.click()
pyautogui.click()
time.sleep(4)
"""

#xpath tam olarak küçük ekranın scroll yazan html kodunun xpath kopyasıdır.
fBody  = browser.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/div")

scroll = 0
while scroll < 4: # 10 sefer scroll yapar, istenirse sonsuz döngüye alınabilir
    browser.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
    time.sleep(2)
    scroll += 1

    followersList = []
    #aşağıda seçilen sınıf diğer sınıflarla aynı olsun diye baktım. 3 farklı nokta vardı birbirleri ile karşılaştırdım.
    followers = browser.find_elements_by_css_selector(".FPmhX.notranslate.MBL3Z")

    for follower in followers:
        followersList.append(follower.text)

    with open("file/photo_likes.txt", "a", encoding="UTF-8") as file: #Dosya acma islemlerine iyi bak
        for follower in followersList:
            file.write(follower + "\n")

print("Daha fazla Scroll edilemiyor.")
time.sleep(5)
browser.close()

import time
from selenium import webdriver
from getpass import getpass
from selenium.webdriver.support.ui import Select
from datetime import datetime, timedelta
from tqdm import tqdm

tkbid = input("enter ID: ")
password = getpass("enter password(it won't show): ")
print("線代(1)")
print("離散(2)")
print("資結(3)")
print("OS(4)")
print("ALGO(5)")
class_num = input("enter class: ")
date_num = input("enter date(the latest is 7, today is 1): ")
location = "新竹數位學堂"
class_time = input("input time(ex. 1 2 4 or just 1): ")
class_time = class_time.split(" ")
dhm = input("input dhm: ")
dhm = dhm.split(" ")
[d, h, m] = dhm


def login(tkbid, password):
    id_input = driver.find_element_by_id("id")
    pwd_input = driver.find_element_by_id("pwd")
    submit_btn = driver.find_element_by_link_text("送出")
    id_input.send_keys(tkbid)
    pwd_input.send_keys(password)
    submit_btn.click()
    time.sleep(5)


driver = webdriver.Chrome()
driver.get("https://www.tkblearning.com.tw/index")
reserve_page = driver.find_element_by_link_text("預約上課")
print(reserve_page)
reserve_page.click()
# login(tkbid,password)
time.sleep(2)
url = driver.current_url
while (
    url == "https://bookseat.tkblearning.com.tw/book-seat/student/login/login"
    or url == "https://bookseat.tkblearning.com.tw/book-seat/student/bookSeat/index"
):
    try:
        login(tkbid, password)
        time.sleep(1)

    except:
        pass
    try:
        url = driver.current_url
    except:
        pass

url = driver.current_url
while url == "https://bookseat.tkblearning.com.tw/book-seat/student/login/loginRecord":
    try:
        driver.switch_to_alert().accept()
        driver.switch_to_alert().dismiss()
        time.sleep(1)
    except:
        pass
    try:
        url = driver.current_url
    except:
        pass
print("!!!")
url = driver.current_url
print(url)
# try:
x = datetime.today()
y = x.replace(
    day=x.day + int(d), hour=int(h), minute=int(m), second=0, microsecond=0
)  # + timedelta(days=1)
delta_t = y - x
secs = delta_t.total_seconds()
print(secs)
# time.sleep(secs)
if secs<0:
    secs=0
for i in tqdm(range(int(secs))):
    time.sleep(1)
    pass
time.sleep(secs - int(secs))
driver.refresh()
flag = 0
while flag == 0:
    try:
        select_class = Select(driver.find_element_by_id("class_selector"))
        select_class.select_by_index(class_num)
        flag = 1
    except:
        pass

flag = 0
while flag == 0:
    try:
        select_date = Select(driver.find_element_by_id("date_selector"))
        select_date.select_by_index(date_num)
        flag = 1
    except:
        pass

flag = 0
while flag == 0:
    try:
        select_location = Select(driver.find_element_by_id("branch_selector"))
        select_location.select_by_visible_text(location)
        flag = 1
    except:
        pass
    
flag = 0
while flag == 0:
    try:
        for i in class_time:
            cb = driver.find_element_by_xpath("//input[@value={}]".format(str(i)))
            cb.click()
        flag = 1
    except:
        pass
submit_btn = driver.find_element_by_link_text("送出")
submit_btn.click()

flag = 0
while flag == 0:
    try:
        driver.switch_to_alert().accept()
        flag = 1
    except:
        pass

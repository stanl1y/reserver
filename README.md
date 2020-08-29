# TKB-reserver
This is a TKB reserver for CS student.  

Requirement:  
-------
python3  
python package:  
* selenium  
* getpass
* datetime
* tqdm

download the selenium chrome driver for your version of chrome, then unzip it. and add the path of your chrome driver to the environment variable, then reopen your computer.
https://chromedriver.chromium.org/downloads  
ex.  
![image](https://github.com/stanl1y/TKB-reserver/blob/master/folder.png)
![image](https://github.com/stanl1y/TKB-reserver/blob/master/env_var.png) 

Execution:  
-------  
`python reserv.py`

Input:
-------
`enter id: (身分證字號)`  
`enter password: (密碼)`  
`enter classes: (依照提示輸入數字)`  
`enter date: (1是今天，2是明天，...，7是過00:00以後會釋出的那天)`  
`input time: (輸入要哪一節，如果要好幾節的話可以中間加空格 例如"1 3")`  
`input dhm: (輸入要什麼時間點預約，例如要在00:00預約剛釋出的，就要輸入"1 0 0"，第一個數字代表今天+幾天，所以1就代表明天，第二個數字代表幾點，所以0代表0點，第三個數字代表幾分，所以0代表0分，如果是現在就要預約，可以直接打"0 0 0")`  

理論上接下來會彈出一個chrome視窗，然後接下來就讓它自東操作就好了，有一點要注意的是，如果你要預約那場已經滿了，那他就不會繼續幫你預約了，接下來你可以手動介入。

import requests
from time import time
req_header ={
    'Host': '45.56.82.176',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.5,zh;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://45.56.82.176/plugin.php?H_name-tasks.html',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}
url_task = 'http://45.56.82.176/plugin.php'
req_day={
        'H_name':'tasks',
        'action':'ajax',
        'actions':'job',
        'cid':'14',
        'nowtime':'1483113052575',
        'verify':'8bb01727',
        }

user = {
        'cktime':'31536000',
        'jumpurl':'http://45.56.82.176/index.php?',
        'lgt':'0',
        'pwpwd':'',
        'pwuser':'',
        'step':'2',
        }
req_week = req_day.copy()
get_day = req_day.copy()
req_week['cid'] = '15'
get_day['actions'] = 'job2'
get_week = req_week.copy()
get_week['actions'] = 'job2'
req_day['nowtime'] = str(int(time()))
req_week['nowtime'] = str(int(time()))
get_day['nowtime'] = str(int(time()))
get_week['nowtime'] = str(int(time()))


url = 'http://45.56.82.176/login.php'

s = requests.session()
res = s.post(url,data = user,params = req_header )
#  with open('test.html','w') as f:
#      f.write(res.content)
res = s.get(url_task, params= req_day)
res = s.get(url_task, params= req_week)
res = s.get(url_task, params= get_day)
res = s.get(url_task, params= get_week)

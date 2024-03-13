import requests

url = "https://img-s-msn-com.akamaized.net/tenant/amp/entityid/BB1jiheu.img?w=628&h=372&q=90&m=6&f=jpg&u=t"
r = requests.get(url)
with open('Alternative power.png', mode='wb')as mf:
    mf.write(r.content)
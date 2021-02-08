import requests
from requests_ntlm import HttpNtlmAuth

uname = "ZAMBEEF\moondem"
pword ="S@muel9judah"
res=requests.get("https://portal.zambeef.co.zm:4433/sites/intranet",auth=HttpNtlmAuth(uname,pword))
print(res)
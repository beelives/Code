import requests

s = requests.post(i+'/j_security_check',data =data,timeout=5)
if s.content.count('Home Page') !=0 or s.content.count('WebLogic Server Console') !=0 or s.content.count('console.portal') !=0:
    print i,'Success!!!!!' 

# requests自带countent.count('XX')可以查找返回中指定字符串

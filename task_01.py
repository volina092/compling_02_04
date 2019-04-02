import urllib.request 
import json
req = urllib.request.Request('https://api.vk.com/method/wall.get?owner_id=308903303&count=2&v=5.92&access_token=2d222a29abf1f629f91269ff8f07fdcfdf13912d535717d2b05f5b1fb03844ca94ab9707047e41e60214d') 
req = urllib.request.Request('https://api.vk.com/method/account.getProfileInfo?owner_id=308903303&v=5.92&access_token=2d222a29abf1f629f91269ff8f07fdcfdf13912d535717d2b05f5b1fb03844ca94ab9707047e41e60214d') 
response = urllib.request.urlopen(req) 
result = response.read().decode('utf-8')
data = json.loads(result) 

#(data)
print('МОИ...')
print('имя: ' + data['response']['first_name'])
print('фамилия: ' + data['response']['last_name'])
print('дата рождения: ' + data['response']['bdate'])
print('статус: ' + data['response']['status'])
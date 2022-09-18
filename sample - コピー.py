import requests

response = requests.get("https://www.python.jp")
response.encoding = response.apparent_encoding  # 文字化け対策 この行を追加
print(response.text)
print(1+3)
text = input('?')
print(text)



data= -100
print(data.__abs__())

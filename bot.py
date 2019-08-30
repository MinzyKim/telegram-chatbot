import requests
import random
from decouple import config

# 0. 로또 번호 추출

numbers = range(1,46) ## 반복문
text = sorted(random.sample(numbers,6))
#print(lotto)

# 1. 토큰 값 설정
token = config('TELEGRAM_TOKEN')
# 2. url 설정
# chat_id, text 요청변수 설정
# string interpolation - 문자열 내에 변수 값 삽입(f-string)
base_url = f'https://api.telegram.org/bot{token}'
chat_id=712426337
# text='안녕'
url = f'{base_url}/sendMessage?chat_id={chat_id}&text={text}'


# 3. 메시지 보내기
requests.get(url)

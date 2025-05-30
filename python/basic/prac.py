print("Hello World")

print("Mary's cosmetics")

print('신씨가 소리질렀다. "도둑이야".')

print("C:\\Windows")

print("오늘은", "일요일") # 오늘은 일요일

print("naver","kakao","sk","samsung", sep=";")

print("naver", "kakao", "sk", "samsung", sep="/")

print("first", end="");print("second")

print(5/3)

삼성전자 = 50000
총평가금액 = 삼성전자 * 10
print(총평가금액)

시가총액 = 298
현재가 = 50000
PER = 15.79
print(시가총액, type(시가총액))
print(현재가, type(현재가))
print(PER, type(PER))

s = "hello"
t = "python"
print(f"{s}! {t}")

a = "132"
print(type(a)) # <class 'str'>

num_str = "720"
num_str = int(num_str)
print(type(num_str)) # <class 'int'>

f = "15.79"
f = float(f)
print(type(f)) # <class 'float'>

year = "2020"
print(int(year)- 3)
print(int(year)- 2)
print(int(year)- 1)

air_conditioner = 48584
installment = 36
print(air_conditioner * installment)

letters = 'python'
print(letters[0], letters[2])

license_plate = "24가 2210"
print(license_plate[-4:])

string = "홀짝홀짝홀짝"
print(string[0::2])

string2 = "PYTHON"
print(string2[::-1])

phone_number = "010-1111-2222"
print(phone_number.replace("-"," "))
print(phone_number.replace("-",""))

url = "http://sharebook.kr"
url_split = url.split('.') # .을 기준으로 split
print(url_split[1]) 

# lang = 'python'
# lang[0] = 'P' # 문자열은 수정 불가
# print(lang)

string = 'abcdfe2a354a32a'
string = string.replace('a', 'A')
print(string)

print("Hi" * 3)
print("-"*80)

t1 = 'python'
t2 = 'java'
print((t1 + " " +  t2 + " ") * 4)

name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print(f"이름: {name1} 나이: {age1}\n이름: {name2} 나이: {age2}")
print("이름: %s 나이: %d" %(name1, age1))
print("이름: %s 나이: %d" %(name2, age2))
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))

상장주식수 = "5,969,782,550"
상장주식수 = int(상장주식수.replace(",", ""))
print(상장주식수)

분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

data = "   삼성전자    "
print(data.replace(" ", ""))
print(data.strip())

ticker = "btc_krw"
print(ticker.upper())

ticker = "BTC_KRW"
print(ticker.lower())

a = "hello"
print(a.capitalize()) # Hello --> 첫번째만 대문자, 나머지는 소문자
b = "HEllO"
print(b.capitalize()) # 똑같이 첫번째만 대문자 --> Hello

file_name = '보고서.xlsx'
print(file_name.endswith('xlsx'))
print(file_name.endswith(('xlsx', 'xls')))

file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))

a = "hello world"
print(a.split(" ")) # 뭘 기준으로 split할 것인지?

ticker = "btc_krw"
print(ticker.split("_"))

date = "2020-05-01"
print(date.split("-"))

data = "039490     "
print(data.rstrip()) # rstrip: 오른쪽 공백 제거

movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rank)
movie_rank.append("배트맨") # append는 마지막에만 추가 가능
print(movie_rank)
movie_rank.insert(1, "슈퍼맨") # insert(인덱스, 원소) 특정 위치 끼어넣기 가능능
print(movie_rank)

movie_rank.remove("럭키") # 특정 요소 삭제 가능
print(movie_rank)

del movie_rank[1] # 인덱스로 삭제 가능
print(movie_rank)

movie_rank2 = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
# movie_rank2.remove("스플릿")
# movie_rank2.remove("배트맨")
del movie_rank2[2]
del movie_rank2[-1]
print(movie_rank2)

lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]

langs = lang1 + lang2
print(langs)

nums = [1, 2, 3, 4, 5, 6, 7]
print(f"max: {max(nums)}\nmin: {min(nums)}")

nums = [1, 2, 3, 4, 5]
print(sum(nums))

cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

nums = [1, 2, 3, 4, 5]
print(sum(nums) / len(nums))

price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[0::2])
print(nums[1::2])
nums.reverse()
print(nums)

interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))
print("/".join(interest))
print("\n".join(interest))

string = "삼성전자/LG전자/Naver"
print(string.split("/"))

data = [2, 4, 3, 1, 5, 10, 9]
data.sort() # 오름차순
print(data)
data.reverse() # 내림차순
print(data)

my_variable = ()
print(type(my_variable)) # <class 'tuple'>
print(my_variable)

movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
print(movie_rank)

num = (1)
print(num)

my_tuple = (1,)
print(my_tuple)

# t = (1, 2, 3)
# t[0] = 'a' # TypeError: 'tuple' object does not support item assignment, Tuple의 원소(element)의 값 변경 불가능

t = 1, 2, 3, 4
print(type(t)) # <class 'tuple'>

t = ('a', 'b', 'c') 
t = ("A", 'b', 'c') # 튜플의 값 변경은 불가능하지만, 동일한 변수에다가 새로운 튜플 생성하면 가능
print(t)

interest = ('삼성전자', 'LG전자', 'SK Hynix')
data = list(interest) # 리스트로 변환시 list 사용
print(data)

tuples = tuple(data)
print(tuples)

temp = ('apple', 'banana', 'cake')
a, b, c = temp # 튜플의 각 요소를 하나씩 변수에 저장하는 과정
print(a, b, c)

# for i in range(100):
#   if i % 2 == 0:
#     print(tuple(i,))
    
data = tuple(range(2, 100, 2))
print(data)

# 다음과 같이 10개의 값이 저장된 scores 리스트가 있을 때, start expression을 사용하여 좌측 8개의 값을 valid_score 변수에 바인딩하여라.
scores = [8.8, 8.9, 8.7, 9.2, 9.3, 9.7, 9.9, 9.5, 7.8, 9.4]
*valid_score, _, _ = scores # *valid_score, _, _ 에서 _를 한 이유는 두 개의 값을 저장하지만,  아무런 값을 할당하지 않기 위함
print(valid_score)
a, b, *valid_score = scores
print(valid_score)

a, *valid_score, b = scores
print(valid_score)

temp = { }
print(temp)

ice_cream = {"메로나": 1000, "폴라포":12000, "빵빠레":1800}
print(ice_cream)
ice_cream["죠스바"] = 1200
ice_cream["월드콘"] = 1500
print(ice_cream)
print(f"메로나 가격: {ice_cream['메로나']}")
ice_cream["메로나"] = 1300
print(ice_cream)
del ice_cream["메로나"]
print(ice_cream)

inventory = {"메로나": [300, 20], "비비빅": [400, 3], "죠스바": [250, 100]}
print(inventory)
print(inventory["죠스바"][0], "원")
print(inventory["메로나"][1], "개")

inventory.update({"월드콘": [500, 7]})
print(inventory)

inventory["쿠앤크"] = [300, 7]
print(inventory)

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
print(list(icecream.keys()))
print(list(icecream.values()))
print(sum(icecream.values()))

icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000}
icecream.update(new_product)
print(icecream)

keys = ("apple", "pear", "peach")
vals = (300, 250, 400)
result = dict(zip(keys, vals))
print(result)

date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table)
str = input()
print(str.swapcase())

# upper()
a = "Python is easy to learn"
print(a.upper()) # PYTHON IS EASY TO LEARN
print(a.lower()) # python is easy to learn

a = "PythonMaster"
a.swapcase()
print(a) # PythonMaster --> 원본 출력
print(a.swapcase()) #pYTHONmASTER" --> swapcase()는 대문자를 소문자로, 소문자를 대문자로 바꿔줌
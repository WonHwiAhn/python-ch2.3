from collections import namedtuple

# global, local 심볼 테이블 내용 확인

def f():
    l_a = 2
    l_b = '마이콜'
    print(locals())

class MyClass:
    def f1(self):
        haha = 2
        print(haha)
    x = 10
    y = 20

MyClass.f1(MyClass)

# integer class의 인스턴스 객체
g_a = 1
g_b = '둘리'

print(globals())
f()

# 1. 정의된 함수 객체
f.k = 'hello'
print(f.__dict__)

# 2. 클래스 객체
print(MyClass.__dict__)     # 사용자 정의 클래스 객체
print(int.__dict__)         # 내장 정의 클래스 객체

# int.k = 10    # syboltable에 값을 넣지 못해서 error

# 3. 인스턴스 객체
o = MyClass()
o.x = 100
print(o.__dict__)

# 내장 함수 (얘도 sysboltable에 값 추가 못함.)
# print(print.__dict__)

# 내장 클래스의 인스턴스 객체에 대한 namespace가 있는지 확인
# 없음! (얘도 확장 불가)
# print(g_a.__dict__)


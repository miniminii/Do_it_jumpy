#!/usr/bin/env python
# coding: utf-8

# # ch5. 파이썬 날개 달기
# 
# 1. 클래스
# 2. 모듈
# 3. 패키지
# 4. 예외처리
# 5. 내장 함수
# 6. 라이브러리
# 

# ## 1. 클래스
# 
# - 별개의 계산기 cal1, cal2가 각각의 역할을 수행한다.
# - 다른 계산기의 결괏값과 상관없이 독립적인 값을 유지한다.
# 

# In[1]:


class Calculator :
      def __init__(self):
        self.result = 0
     
      def add(self, num) :
        self.result += num
        return self.result

cal1 = Calculator()
cal2 = Calculator()


# ### 클래스와 객체

# In[2]:


class Cookie : 
     pass


# In[3]:


a = Cookie()
b = Cookie()

# cookie가 클래스 / a,b가 객체이다


# ### 사칙연산 클래스 만들기

# In[5]:


class FourCal : 
      pass


# In[6]:


a = FourCal()
type(a)  #객체a의 타입은 클래스다.


# - 클래스 안에 setdata함수를 만든다. 
# - 클래스 안에 구현된 함수는 메서드 method라고 부른다.
# - setdata 메서드는 매개변수로 self, first, second 3개 입력값을 받는다.

# In[8]:


class FourCal :
    def setdata(self, first, second) :
        self.first = first
        self.second = second


# - 하지만, 첫번째 매개변수 self에는 객체a가 자동전달되어서 따로 지정해주지 않아도 된다.

# In[10]:


a = FourCal()
a.setdata(4,2)
print(a.first)
print(a.second)


# - 더하기 기능 만들기

# In[11]:


class FourCal :
    def setdata(self, first, second) :
        self.first = first
        self.second = second

    def add(self) :
        result = self.first + self.second
        return result


# In[12]:


a = FourCal()
a.setdata(4,2)
a.add()


# ### 생성자(construnction)

# - setdata보다 생성자로 객체에 초깃값을 주는게 안전한 방법이다.

# In[13]:


class FourCal :
        def __init__(self, first,second) :
            self.first = first
            self.second = second

        def setdata(self, first, second) :
            self.first = first
            self.second = second
        def add(self) :
            result = self.first + self.second
            return result


# ## 2. 모듈

# - from 모듈이름 import 모듈함수

# In[ ]:


#mod1.py
def add(a,b) :
    return a + b

def sub(a,b) :
    return a - b


# In[ ]:


import mod1
print(mod1.add(3,4))


# #### if__name__ == "__main__"

# - 파일을 실행했을 때는 if__name__ == "main"이 참이 되어 if문 다음 문장이 수행된다.

# In[ ]:


#mod1.py
def add(a,b) :
    return a + b

def sub(a,b) :
    return a - b

if__name__ == "__main__" : 
    print(add(1,4))
    print(sun(4,2))


# ## 3. 패키지

# In[ ]:


#echo.py
def echo_test() :
    print("echo")


# In[ ]:


#render.py
def render_test() :
    print("render")


# - 패키지 안의 함수를 실행하는 방법으로 세가지가 있다.

# In[ ]:


import game.sound.echo
game.sound.echo.echo_test()


# In[ ]:


from game.sound import echo
echo.echo_test()


# In[ ]:


from game.sound.echo import echo_test
echo_test()


# - __init__.py 의 용도 : 
# - 패키지에서 모든것(*)을 import할 때 조심
# - 특정 디렉터리의 모듈을 *를 사용하여 import할 때에는 다음과 같이 해당 디렉터리의 __init__.py파일에 __all__변수를 설정하고 import할 수 있는 모듈을 정의해주어야한다.

# ## 4. 예외처리
# - 오류 예외 처리하는 기법

# In[ ]:


#### try, except문


# In[ ]:


# 1. try, except만 쓰는 방법
try : 
    ...
except : 
    ...


# In[ ]:


# 2. 발생오류만 포함한 except문
try : 
    ...
except 발생오류 :
    ...


# In[ ]:


# 3. 발생오류와 오류메세지 변수까지 포함한 except문
try : 
    ...
except 발생 오류 as 오류 메세지 변수


# In[14]:


try : 
    4/0
except ZeroDivisionError as e :
    print(e)


# #### try ... finally

# In[ ]:


# 여러개의 오류 처리하기
try : 
    ...
except 발생오류1 :
    ...
except 발생오류2 :
    ...


# - 오류 회피하려면 except ~ : pass 해주면 된다.

# ## 5. 내장함수

# #### abs

# In[16]:


# abs
print(abs(2))
print(abs(-2))
print(abs(-1.2))


# #### all : 반복가능한 자료형 x를 입력변수로 받아서 참이면 true

# In[18]:


# all
print(all([1,2,3]))
print(all([1,2,3,0]))


# #### any : x중 하나라도 참이면 true 

# In[19]:


# any 
print(any([1,2,3,0]))
print(any([0,""]))


# #### chr - 아스키ascii코드

# In[20]:


# chr - 아스키ascii코드
print(chr(97))


# #### dir : 객체가 가지고 있는 변수나 함수

# In[ ]:


#dir : 객체가 가지고 있는 변수나 함수


# #### divmod : a를 b로 나눈 몫과 나머지
# 

# In[21]:


# divmod : a를 b로 나눈 몫과 나머지
divmod(7,3)


# #### enumerate : 자료형을 입력으로 받아 인덱스값을 포함하는 객체를 돌려준다.
# 

# In[22]:


# enumerate : 자료형을 입력으로 받아 인덱스값을 포함하는 객체를 돌려준다.
enumerate(['body', 'foo', 'bar'])


# In[23]:


for i, name in enumerate(['body', 'foo', 'bar']) :
     print(i, name)


# #### eval - 문자열을 입력으로 받아 문자열을 실행한 겨로가값
# 

# In[24]:


# eval - 문자열을 입력으로 받아 문자열을 실행한 겨로가값
eval('1+2')


# #### filter함수는 첫번째 인수로 함수이름을, 두번째 인수로 그 함수에 차례로 들어갈 반복가능한 자료형을 받는다
# 

# In[25]:


#filter : filter함수는 첫번째 인수로 함수이름을, 두번째 인수로 그 함수에 차례로 들어갈 반복가능한 자료형을 받는다

def positive(X) :
    return X > 0

print(list(filter(positive, [1,-3,2,0,-5,6])))


# #### hex : 정수값을 입력받아 16진수로 변환
# 

# In[26]:


#hex : 정수값을 입력받아 16진수로 변환
hex(234)


# #### id : 객체를 입력받아 객체의 고유주소값을 돌려준다
# 

# In[27]:


#id : 객체를 입력받아 객체의 고유주소값을 돌려준다
id(3)


# #### input() :사용자 입력을 받는 함수

# In[ ]:


#input()
a = input()


# #### 그외
# - len 
# - list
# - map : 함수와 반복 가능한 자료형을 입력으로 받는다. map은 입력받은 자료형의 각 요소를 함수가 수행한 결과를 묶어서 돌려준다.
# - max
# - min
# - oct : 8진수로 만듦
# - open : 파일 읽기
# - pow : x의 y제곱한 결과값
# - range
# - round
# - sorted
# - str
# - sum
# - tuple
# - type
# - zip

# In[30]:


#### map
def twotimes(x) : 
    return x*2

list(map(twotimes, [1,2,3,4]))


# ## 6. 라이브러리
# 
# - sys 모듈은 파이썬 인터프리터가 제공하는 변수와 함수를 직접 제어할 수 있게 해주는 모듈
# - pickle - 객체를 그대로 유지하면서 불러올 수 있음
# - shutil : 파일을 복사해주는 모듈
# - glob
# - tempfile
# - time

# In[ ]:





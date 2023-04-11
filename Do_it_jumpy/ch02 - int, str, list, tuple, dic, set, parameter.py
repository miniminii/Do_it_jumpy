#!/usr/bin/env python
# coding: utf-8

# # 파이썬 프로그래밍의 기초, 자료형 
# 
# 1. 숫자형
# 2. 문자열 자료형
# 3. 리스트 자료형
# 4. 튜플 자료형
# 5. 딕셔너리 자료형
# 6. 집합 자료형
# 7. 불 자료형
# 8. 자료형 값 저장하는 공간, 변수

# ## 1. 숫자형

# - 제곱을 나타내는 연산자 : **
# - 나머지를 반환하는 연한사 %
# - 몫을 반환하는 연산자 //
# 

# ## 2. 문자열 자료형
# #### 문자열 인덱싱 : 파이썬은 0부터 숫자를 센다

# In[7]:


a = '20010301raniny'
date = a[:8]
weather = a[8:]
print(date)
print(weather)


# #### f문자열 포매팅 : 문자열 앞에 f접두사를 붙이자

# In[8]:


name = '김유민'
age = 24
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'


# ####  소수점, % 표시하기

# In[9]:


y = 3.142244
print(f'{y:0.4f}')


# In[10]:


import math
pi=math.pi
print(pi)
print(f"파이: {pi:.3f}")


# In[11]:


percent=0.9522
print(f"퍼센트: {percent:.2%}")


# #### 아니면 함수 만들어서 사용하기

# In[ ]:


def to_percentage(x) : 
    return str(round(x,2)) + '%'

df['변수명'] = df['변수명'].apply(to_percentage)


# ### 문자열 관련 함수

# In[14]:


",".join('abcd') #abcd문자열 사이에 , 삽입


# In[15]:


'hi'.upper()


# In[17]:


'HI'.lower()


# In[18]:


" hi".lstrip()  #왼쪽 공백 제거


# In[19]:


" hi ".strip() #양쪽 공백 제거


# In[20]:


a = 'life is too short'
a.replace('life', 'your leg') # replace


# In[21]:


a = 'life is too short'
a.split()


# In[23]:


b = 'life: is: too: short'
b.split(':') #괄호안에 나눌 부호 넣기


# ## 3. 리스트 자료형

# #### 리스트 인덱싱

# In[31]:


a = [1,3,5,6,7]
print(a[0:1])


# - 리스트 더하기 + 
# - 리스트 반복하기 *
# - 길이구하기 : len

# In[32]:


a = [1,2,3]
del a[1] #두번째 값 삭제
a


# #### 리스트 관련 함수

# In[33]:


a = [1,2,3]
a.append(4)
a


# In[35]:


a = [1,4,6,33,2]
a.sort()
a


# In[40]:


a = [1,2,3]
a.insert(0,4) #첫번째 자리에 4 삽입
a


# In[42]:


a = [1,2,3]
a.remove(3) #3제거
a


# In[54]:


a = [1,2,3]
a.pop() # 마지막부터 나오기


# ## 4. 튜플 자료형
# - 리스트는 []으로 둘러싸지만 튜플은 ()로 둘러싼다

# ## 5. 딕셔너리 자료형

# - key와 value로 이루어져있음

# In[49]:


grade = {'pey' : 10, 'juliet' : 99}
print(grade['pey'])  #key로 value반환
print(grade.get('pey')) # get함수


# In[45]:


grade.keys()


# In[46]:


list(grade.keys())


# In[48]:


grade.values()


# ## 6. 집합형
# - set()의 괄호 안에 리스트를 입력하여 만든다

# In[51]:


s1 = set([1,2,3])
s1


# - 교집합 : &
# - 합집합 : |
# - 차집합 : -

# ## 7. T/F 자료형

# - 참 거짓 나타내면 됨

# ## 8. 자료형 변수를 저장하는 공간, 변수

# - =기호를 써서 넣는다.
# - copy()를 써서 그대로 넣는다.

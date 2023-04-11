#!/usr/bin/env python
# coding: utf-8

# # ch04. 프로그램의 입력과 출력은 어떻게 해야할까?
# 
# 1. 함수
# 2. 사용자 입력과 출력
# 3. 파일 읽고 쓰기
# 

# ## 1. 함수
# 
# #### 함수의 구조
# - 함수 이름 -> 괄호 안에 입력값 변수 넣어주기

# In[1]:


# 함수 만들기

def add(a,b) : 
    return a + b

add(3,4)


# In[2]:


# 일반적인 함수

def add(a,b) : 
    result = a + b
    return result

add(3,4)


# - 입력값이 몇 개가 될지 모를 때는 ?
# - 여러개의 입력값을 받는 함수 만들기

# In[4]:


def add(*args) :  # *기호 넣어주기
    result = 0
    for i in args :
        result = result + i
    return result

add(1,2,3,4)


# - 매개변수들을 많이 설정할수도

# In[6]:


def add_or_mul(choice, *args) :
    if choice == 'add' :
        result = 0
        for i in args :
            result = result + i
    elif choice == 'mul' :
        reult = 1
        for i in args :
            result = result * i
    return result

add_or_mul('add', 3,4,5)


# In[8]:


a = 1

def vartest(x) :
    x = x + 1
    return(x)

vartest(1)


# #### lambda
# - lambda로 만든 함수는 return명령어가 없어도 결과값을 보여준다

# In[9]:


add = lambda a,b : a+b

add(3,4)


# ## 2. 사용자 입력과 출력

# - input 문

# In[ ]:


number = input('숫자를 입력하세요 : ')


# - print문

# ## 3. 파일 읽고 쓰기

# - read, readline

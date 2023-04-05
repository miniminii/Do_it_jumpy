#!/usr/bin/env python
# coding: utf-8

# # 프로그램의 구조를 쌓는다 ! 제어문
# 
# 1. if문
# 2. while문
# 3. for문

# ## 1. if 문

# In[1]:


money = True
if money : 
    print('택시를 타고 가라')
else :
    print('걸어가라')  #true로 받음


# In[3]:


money = 2000
if money > 3000 : 
    print('택시 타라')
else :
    print('걸어가라')


# - x in s, x not in s

# In[4]:


1 in [1,2,3]


# In[5]:


1 not in [1,2,3]


# In[6]:


pocket = ['paper', 'cellphone', 'money']

if 'money' in pocket : 
    print('택시 타라')
else : 
    print('걸어가라')


# #### 조건문 표현식

# In[9]:


score = 80

message = 'success' if score>=60 else 'fail'
message


# ## 2. while문

# In[11]:


treehit = 0
while treehit < 10 :
    treehit = treehit + 1
    print('나무를 %d번 찍었습니다.' % treehit)
    if treehit == 10 :
        print('나무넘어갑니다')


# In[ ]:


coffee = 10

while True : 
    money = int(input())
    if money == 300 :
        print('커피를 줍니다')
        coffee = coffee -1
    elif money > 300 :
        print('거스름돈 {money - 300}를 줍니다')
        coffee = coffee -1
    else : 
        print('돈을 다시 돌려주고 커피를 주지 않습니다')
        print('남은 커피의 개수는 {coffee}입니다')
    if coffee == 0 :
        print('커피가 다 떨어졌습니다')
        break


# In[26]:


a= 0
while a < 10 :
    a = a + 1
    if a % 2==0 : continue # 맨 처음으로 돌아가기
    print(a)


# ## 3. for문

# #### 전형적인 for 문

# In[28]:


test_list = ['one', 'two', 'three']
for i in test_list : 
      print(i)


# In[35]:


marks = [90, 25, 57, 45, 80]
number = 0

for i in marks :
    number = number + 1
    if i >= 60 : 
        print('%d번학생은 합격입니다' % number)
    else : 
        print('%d번학생은 불합격입니다' % number)


# In[36]:


marks = [90, 25, 57, 45, 80]
number = 0

for i in marks :
    number = number + 1
    if i >= 60 : 
        print(number,'번학생은 합격입니다' )
    else : 
        print(number,'번학생은 불합격입니다' )


# In[38]:


marks = [90, 25, 57, 45, 80]

for i in range(len(marks)) :
    if marks[i] < 60 : continue 
    print(i, '번 학생 축하합니다. 합격입니다')


# In[39]:


a = [1,2,3,4]

result = [num * 3 for num in a if num % 2 == 0]
result #짝수만 3곱하기


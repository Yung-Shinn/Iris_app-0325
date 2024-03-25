# streamlit run APP\test.py (在終端機裡面執行)

import streamlit as st
import numpy as np 
import pandas as pd 

st.title("abc")
st.write("abc")     #跟print()的效果比較像
st.header("abc")    #文章開頭用的
st.text("abc")      #顯示內文用的

st.write("# abc")   # '#'加上去就跟tital一樣大了，最多可以加6個，'#'越多字體就越小
st.write("## abc")

a = np.array([10, 20, 30])
st.write(a)

b = np.array([[10, 20, 30],[100, 200, 300]])
st.write(b)
st.table(b)         #table()，就會有index了

c = pd.DataFrame([[10, 20, 30],[100, 200, 300]])
st.write(c)
st.table(c)  

name = "Leo"
st.write(name, b[0], c[0])  #注意! 這邊在取c[0]的時候，它取值的邏輯和python的邏輯不一樣，是用網頁的邏輯。
st.info(name)

# 核取方塊
st.write("### 核取方塊----------------")
re1 = st.checkbox("美食")
if re1:
    st.info("喜歡美食")     #這邊用write()取代info()也是可以的。
else:
    st.info("不喜歡美食")

re2 = st.checkbox("運動")
if re2:
    st.info("喜歡運動")
else:
    st.info("不喜歡運動")

# 核取方塊2
st.write("### 核取方塊2----------------")    
res = st.columns(3)
with res[0]:
    c1 = st.checkbox("A")
    if c1:
        st.info("a")
with res[1]:
    c2 = st.checkbox("B")
    if c2:
        st.info("b")
with res[2]:
    c3 = st.checkbox("C")
    if c3:
        st.info("c")

# 選項按鈕
st.write("### 選項按鈕----------------")
re3 = st.radio("性別:", ("男","女","三性"), index=1) #將index設為1的話，初始的選項就會停留在"女"
st.write(re3)

re4 = st.radio("性別:", ("男","女","三性"), index=1, key=1) #如過這裡不設key的話，radio元件會認為key重複然後無法運行
st.write(re4)

# 選項按鈕2
st.write("### 選項按鈕2----------------")
col1, col2 = st.columns(2)
with col1:
    num1 = st.number_input("請輸入數字")
with col2:
    num2 = st.number_input("請輸入任一整數", key="num2")

re5 = st.radio("計算:", ("＋","－","＊","／"), key=2)   #很奇怪，這邊的標點符號必須要用全形才有辦法在網頁上顯示。 (shift+空白鍵)*1就可以切換成全形
if re5 == "＋":
    st.write("{}+{}={}".format(num1,num2, num1+num2))  
elif re5 == "－":
    st.write("{}-{}={}".format(num1,num2, num1-num2))
elif re5 == "＊":
    st.write("{}*{}={}".format(num1,num2, num1*num2))
elif re5 == "／":
    st.write("{}/{}={}".format(num1,num2, num1/num2))

# 滑桿
st.write("### 滑桿---------------")
re6 = st.slider("數量:", 1.0, 20.0, step=0.5)
st.info(re6)

# 下拉選單
st.write("### 下拉選單---------------")
re7 = st.selectbox("請選擇分類器", ("KNN","CART","RF","SVC"))
st.info(re7)

import streamlit as st
import joblib 

# 頁面標題
st.title("IRIS 品種預測")

# 載入模型
svc = joblib.load("app\svc.joblib")
knn = joblib.load("app\knn.joblib")
lr = joblib.load("app\LogisticRegressin.joblib")
rf = joblib.load("app\RF.joblib")

# 左側: 選單欄
name = st.sidebar.selectbox("### 請選擇分類器:", ("KNN",
                                                  "Logistic Regression",
                                                  "SVC",
                                                  "Random Forest"))

if name == "KNN":
    model = knn
elif name == "Logistic Regression":
    model = lr
elif name == "SVC":
    model = svc
elif name == "Random Forest":
    model = rf

# 右側: 接收資料並預測
s1 = st.slider("花萼長度", 3.5, 8.5, 4.0)   #範圍要比最小值還小，比最大值還大
s2 = st.slider("花萼寬度", 1.5, 5.5, 3.0)
s3 = st.slider("花瓣長度", 0.6, 7.5, 4.0)
s4 = st.slider("花瓣寬度", 0.05, 3.5, 2.0)
 
labels = ['setosa', 'versicolor', 'virginica']
re = st.button("進行預測")
if re:
    X = [[s1, s2, s3, s4]]
    y_hat = model.predict(X)
    st.write("### 預測結果", y_hat[0])      #如果沒有寫[0]的話，會直接列出list(這樣不好看)
    st.write("### 品種名稱", labels[y_hat[0]])

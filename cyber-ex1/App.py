import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split

from sklearn.ensemble import IsolationForest



keys=0



button_sent_1 = st.button("Detect")

final_list=[]
                           
   

title1 = st.text_input('unique_id',keys)
keys=keys+1


title2 = st.text_input('duration_',keys)
keys=keys+1


title3 = st.text_input('src_bytes',keys)
keys=keys+1


title4 = st.text_input('dst_bytes',keys)
keys=keys+1


keys=keys+1


list=[]
list=[title1,title2,title3,title4]
final_list.append(list)

dat =  pd.DataFrame(columns=["record ID","duration_","src_bytes","dst_bytes"])

dat.loc[0] = [final_list[0][0],final_list[0][1],final_list[0][2],final_list[0][3]] 


dat.to_csv('out.csv', mode='a', index=False, header=False)



if button_sent_1:
        
        dat = pd.read_csv('./out.csv'
,names=["record ID","duration_", "src_bytes","dst_bytes"], header=None)
    
dat = dat.dropna()
dat=dat.drop([0])
dat.reset_index()
dat=dat.drop_duplicates("record ID",keep='last')
dat.reset_index(drop=True,inplace=True)



dat_with_unique_Id=dat.copy()

dat1=dat.drop("record ID",axis=1)

try:
    model=IsolationForest(n_estimators=1, max_samples='auto', contamination=float(0.1))
    model.fit(dat1)
    m1=model.predict(dat1)
    dat_with_unique_Id['anomaly']=m1

except ValueError:
      pass


from sklearn import svm
from sklearn import preprocessing
try:
    x_train, x_test, y_train, y_test = train_test_split(
        dat1, m1, test_size=0.2, random_state=0)

    dat_with_unique_Id.drop("duration_",axis=1)
    dat_with_unique_Id.drop("src_bytes",axis=1)
    dat_with_unique_Id.drop("dst_bytes",axis=1)
#standardScaler normalization
    scaler = preprocessing.StandardScaler().fit(x_train)
    x_train_transformed = scaler.transform(x_train)
    clf = svm.SVC(C=1).fit(x_train_transformed, y_train)
    x_test_transformed = scaler.transform(x_test)
      
    st.write('Detection DataFrame:', dat_with_unique_Id)
    
except Exception:
      pass
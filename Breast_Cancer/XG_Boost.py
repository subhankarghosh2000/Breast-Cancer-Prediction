import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
from matplotlib import pyplot as plt 

data=pd.read_csv('Breast_Cancer/normalized_dataset.csv')

Y=data['diagnosis']
Y=np.array(Y)

X = data.drop('diagnosis',axis=1)
X=np.array(X)



def input_fetch(data_list):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y,test_size = 0.2)

    xgb = XGBClassifier(learning_rate=0.4,max_depth=7)
    xgb.fit(X_train,Y_train)

    Y_test_predicted=xgb.predict(X_test)  
    Y_train_predicted=xgb.predict(X_train)

    acc_train_tree = accuracy_score(Y_train,Y_train_predicted)
    acc_test_tree = accuracy_score(Y_test,Y_test_predicted)

    print("XG BOOST : Accuracy on training Data: {:.3f}".format(acc_train_tree))
    print("XG BOOST : Accuracy on test Data: {:.3f}".format(acc_test_tree))
    
    input_vector=[data_list]
    input_vector_np=np.array(input_vector)
    Y_output_predict=xgb.predict(input_vector_np)
    return Y_output_predict,"{:.3f}".format(acc_test_tree*100)
  



# X=[]
# for i in range(len(X_test)):
#     X.append(i)

# plt.figure(figsize=(50,15))
# plt.plot(X,Y_test_predicted,color="red",label="Predicted Value")
# plt.plot(X,Y_test,color="blue",label="Actual Value")
# plt.title("XG Boost Classifier",fontsize=30)
# plt.xlabel("Cases",fontsize=25)
# plt.ylabel("Prediction",fontsize=25)
# leg = plt.legend(fontsize=25,loc=1)

# plt.show()




    
    
    
    
    
    
    
    
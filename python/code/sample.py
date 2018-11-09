from svmutil import *
# Read data in LIBSVM format

kfold =10

#accuracy = []
for i in range(kfold):
	print(i)
	y_train, x_train = svm_read_problem('C:/Users/user/Desktop/python/data/d2_t5_libsvm/train'+str(i)+'.LIBSVM')
	m = svm_train(y_train, x_train)

	y_test,x_test = svm_read_problem('C:/Users/user/Desktop/python/data/d2_t5_libsvm/test'+str(i)+'.LIBSVM')
	p_label, p_acc, p_val = svm_predict(y_test, x_test, m)
	#print(p_label,p_acc,p_val)
	ACC, MSE, SCC = evaluations(y_test, p_label)
	
	#print(ACC,MSE,SCC)
	print("accuracy",ACC)
	
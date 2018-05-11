import numpy as np
import time
import matplotlib.pyplot as plt
import numpy as np

from sklearn.datasets import fetch_mldata
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.utils import check_random_state
from sklearn.utils.extmath import safe_sparse_dot, squared_norm
from scipy.misc import comb, logsumexp 
from sklearn.linear_model.logistic import _multinomial_loss_grad
from sklearn.linear_model.logistic import _multinomial_grad_hess
from sklearn.linear_model import SGDClassifier

import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import random
from scipy.optimize import minimize


#Get Data (Takes a long time)
mnist = fetch_mldata('MNIST original')
#mnist is a dict with ['COL_NAMES', 'DESCR', 'data', 'target']
#2 'COL_NAMES': 'label' and 'data'
#34 'DESCR': the string "'mldata.org dataset: mnist-original'"
#70000 'data': Each has shape 784 with values 0 to 255
#70000 'target' ranges from 0 to 9 with average 4.45
X = mnist.data.astype('float64')
y = mnist.target


#Split Data into training and test datasets
train_samples = 30000

random_state = check_random_state(0)#0 indicates a static seed based off 0

permutation = random_state.permutation(X.shape[0]) #check_random_state is a numpy object so it accepts numpy commands like permutation
#randomly permutates a sequence

#sort data based on permutation
X = X[permutation]
y = y[permutation]
X = X.reshape((X.shape[0], -1))#reshapes array to 70000 by 784??? step not necessary...

#Split arays into random training and testing subsets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=train_samples, test_size=10000, random_state=1)
#X_train is 30000 by 784
#X_test is 10000 by 784
#y_train is 30000
#y_test is 10000


#Normalize Data
scaler = StandardScaler()#create standard scaler object

X_train = scaler.fit_transform(X_train)#normalize training data by finding mean and std
X_test = scaler.transform(X_test)#apply training set normalization to test dataset

#Initialize all Y_trian and T_test to 1
Y_train = np.zeros((len(y_train), 10))
for i,j in enumerate(y_train):
    Y_train[i, int(j)] = 1# of Form ind, rounded y value
Y_test = np.zeros((len(y_test), 10))
for i,j in enumerate(y_test):
    Y_test[i, int(j)] = 1# of Form ind, rounded y value



#clf = LogisticRegression(C=50. / train_samples, multi_class='multinomial', \
#                       penalty='l1', solver='saga', tol=0.1)
#clf.fit(X_train, Y_train)





# #Defining a loss function
# def loss_function(X,Y, w, alpha=0):
#     n_classes = Y.shape[1]
#     n_features = X.shape[1]
#     w = w.reshape(n_classes, -1)
#     fit_intercept = w.size == (n_classes * (n_features + 1))
#     old_w = w.copy()
#     if fit_intercept:
#         intercept = w[:, -1]
#         w = w[:, :-1]
#     else:
#         intercept = 0
#     p = safe_sparse_dot(X, w.T)
#     p += intercept
#     p -= logsumexp(p, axis=1)[:, np.newaxis]
#     loss = -(Y * p).sum()
#     loss += 0.5 * alpha * squared_norm(w)
#     p = np.exp(p, p)
#     return loss, p, w


# def grad_loss(X, Y, w, alpha=0):
#     """
#     """
#     loss, grad, p = _multinomial_loss_grad(w, X, Y, alpha)
#     return loss, grad, p
#     #pass


# def hessian_loss(X, Y, w, alpha=0):
#     """
#     """
#     grad, hessp = _multinomial_grad_hess(w, X, Y, alpha)
#     return grad, hessp
#     #pass


# fit_intercept = True




# def flam_erf(sT_lam):
#     """error function we want to minimize
#     sT_lam = input learning rate and momentum = [mu[T], momentum[T]]
#     st has dimensions t,[mu,momentum]
#     eta = st[t][1]
#     """
#     lam_lr = 0.01 #I am making the learning rate for the lambda parameters constant
#     lam_eta = 0.9 #I am making the momentum for the lambda parameters constant
#     v[maxepoch] = lam_lr*v[maxepoch-1] + grad_J(w[maxepoch - 1])
#     w[maxepoch] = w[maxepoch - 1] - lam_eta*(lam_lr*v[maxepoch - 1] - grad_J(w[maxepoch - 1]))


#     #USE ALL VALUES TO COMPUTE ACCURACY
#     mean_accuracy = clf[epoch+1].score(X_train, Y_train)
#     print(mean_accuracy)
#     error = 1-mean_accuracy#I assume mean_accuracy is between 0 and 1
#     return error




def sgd(X_train, Y_train, momentum=0.9, lr=0.01, batch_size=1001, alpha=0.1, maxepoch=50, eps=1e-8):
    """
    Real-time forward-mode algorithm using stochastic gradient descent with constant learning 
    rate. Observe that you should only find the optimal learning rate (lr), and 
    penalty parameter (alpha). 
    
    We use the SGD with momentum, which is defined here: 
    http://ufldl.stanford.edu/tutorial/supervised/OptimizationStochasticGradientDescent/
    """
    #divide data into batches
    shuffleInds = np.arange(X_train.shape[0])
    np.random.shuffle(shuffleInds)#randomly shuffle list of inds
    nBatches = int(X_train.shape[0]/batch_size)#number of batches
    startInds = np.arange(nBatches)*batch_size#batch start ind
    stopInds = (np.arange(nBatches)+1)*batch_size+1#batch end ind

    mu = list()
    eta = list()
    w = list()
    #eta = np.zeros(maxepoch)

    mu.append(lr) # initial learning rate
    eta.append(momentum) # initial momentum
    deltaLam = list()

    # res = minimize(flam_erf, x0,  args=(), method=None, jac=None, hess=None, hessp=None, bounds=None, constraints=(), tol=None, callback=None, options=None)
    # res.x # solution array
    # res.success # flag indicating optimizer exited successfully
    # res.message # cause of termination

    #Run initial classification to get first values for everything
    epoch = 0
    inds = shuffleInds[startInds[epoch]:stopInds[epoch]]#inds from original X_train data to use
    #used learning rate = mu[epoch] = 0.01
    clf = list()
    clf.append(SGDClassifier(learning_rate='constant', eta0=mu[epoch], alpha=eta[epoch], epsilon=eps, loss="log", penalty="l2"))#This creates the untrained SGDClassifier
    clf[epoch].fit(X_train[inds], Y_train[inds]) #Generate Phi_0
    w.append(clf[epoch].coef_)#I think w is s. This is (10,784)
    mean_accuracy = list()
    mean_accuracy.append(clf[epoch].score(X_train[inds], Y_train[inds]))


    for epoch in np.arange(nBatches):# epochNum < maxepoch:#Each epoch is an analysis of a single batch
        #Indices of the batch
        inds = shuffleInds[startInds[epoch]:stopInds[epoch]]#inds from original X_train data to use

        #Create SGDClassifier http://scikit-learn.org/stable/modules/sgd.html, http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.SGDClassifier.html
        #Here we calculate s_t = Phi(s_t,lam_t)
        clf.append(SGDClassifier(learning_rate='optimal', eta0=mu[epoch], alpha=eta[epoch], epsilon=eps, loss="log", penalty="l2"))#This creates the untrained SGDClassifier
        #Run SGDClassifier
        clf[epoch+1].fit(X_train[inds], Y_train[inds])#Calculates Phi
        #hmmm lets try using score for deltaphi
        deltaPhi = clf[epoch+1].score(X_train[inds], Y_train[inds]) - clf[epoch].score(X_train[inds], Y_train[inds])#okay this doesn't  technically work, but this step needs to be done here

        w.append(clf[epoch+1].coef_)#weights of the features
        deltaW = w[epoch+1] - w[epoch]#deltaS


        #HOW DO I CALCULATE eta[epoch] and mu[epoch]
        params = clf[epoch+1].get_params(deep=True) #this gets the eta0 and alpha used for epoch+1
        print clf[epoch+1].get_params(deep=True)['alpha']
        print clf[epoch+1].get_params(deep=True)['eta0']
        mu.append(params['eta0'])
        eta.append(params['alpha'])
        deltaLam.append([mu[epoch+1] - mu[epoch], eta[epoch + 1] - eta[epoch]])#this is the delta in hyperparameters

        mean_accuracy.append(clf[epoch+1].score(X_train[inds], Y_train[inds]))
        print(mean_accuracy[epoch+1])
        error = 1-mean_accuracy[epoch]#I assume mean_accuracy is between 0 and 1

        #must update mu[epoch+1] and eta[epoch+1] somewhere


        # #mu = lr
        # #eta = momentum
        # v[epoch+1] = mu[epoch]*v[epoch] + grad_J(w[epoch+1], w[epoch])
        # w[epoch+1] = w[epoch] - eta[epoch]*(mu[epoch]*v[epoch] - grad_J(w[epoch+1], w[epoch]))

    return mu, eta, w, clf, mean_accuracy


out = sgd(X_train, y_train)#, momentum=0.9, lr=0.01, batch_size=1001, alpha=0.1, maxepoch=50, eps=1e-8):

# def J_obj(w):
#     """The objective function (the classification error for the given weight vector w)
#     Args:
#         w: weight vector
#     Returns:
#     """

#     error = 1-mean_accuracy
#     return error

# def grad_J(w_new, w_old, ):
#     """Technically this is Jhat
#     Args:
#         w_new: most recent vector of weights
#         w_old: last vector of weights
#     Returns:
#         vector of partials of J w.r.t. each w
#     """
#     w_diff = w_new-w_old
#     J_diff = J_obj(w_new) - J_obj(w_old)
#     return J_diff/w_diff



#     # v_t = lr*v_t[n-1] + grad_loss(w_t[n-1])
#     # w_t= w_t[n-1] - momentum*(lr*v_t[n-1] - grad_loss(w_t[n-1]))


#     # return v_t, w_t

# #Could Try logistic regression if SGD doesn't work out
# #http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
# logReg = LogisticRegression()
# #SGD
# #x[k+1] = x[k] - lam[k]*grad_fhat(x[k])
# x[k] = x[k-1] - lam[k - 1]*grad_fhat(x[k - 1])

# pass


# clf.fit(X_train, y_train)






# # From Class Lecture Notes on 4/16/2018 and 4/18/2018
# def grad_fhat(x_k,l):
#     """
#     x_k: The kth value of x
#     l: batch size
#     """
#     mySum = 0
#     for i in range(l):
#         mySum += grad_h(x_k,i)#NOTES SAY THIS IS idot... 
#     mySum = 1/l*mySum
#     return mySum

# def h(x_k,l):
#     mySum1 = 0
#     for j in range(m):
#         mySum1 += (x_l*beta[j])*(y_l[j])

#     mySum2 = sum(x_l*beta_l)
#     return -mySum1 + mySum2

# def sgd(momentum=0.9, lr=0.01, batch_size=1001, alpha=0.1, maxepoch=50, eps=1e-8):
#     """
#     l: batch_size
#     """
#     l = batch_size
#     x[k] = x[k - 1]*lam[k - 1]*grad_fhat(x[k - 1], l)




# #From Franceschi 2017 paper
# def forwardHG(lam, s0):
#     """
#     s0 = [v_0, w_0]
#     """


#     s = np.zeros((T,2))
#     s[0] = s0
#     Z[0] = 0
#     for t in np.arange(0,T)+1:
#         s[t] = PHI(s[t-1],lam)
#         Z[t] = A[t]*Z[t-1]+B[t]
#     grad_E
#     Z_T = Z[T]
#     return grad_E*Z_T
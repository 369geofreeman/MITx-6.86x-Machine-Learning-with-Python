# Pegasos algorithm



class SVMPegasos(LinearClassifier):
    """Implementation of SVM with SGD with PEGASOS Algorithm"""

    def __init__(self, n_iter=10, lambda1=1):
       self.n_iter = n_iter
       self.lambda1 = lambda1

    def fit(self, X, Y):
       Y = list(Y)
       self.find_classes(Y)
       # convert all output values to +1 or -1
       Yn = [sign(y, self.positive_class) for y in Y]
       X = X.toarray()
       m, n_features = X.shape[0], X.shape[1]
       self.w = numpy.zeros( n_features )
       for i in range(self.n_iter):
           eta = 1. / (self.lambda1*(i+1))
           j = numpy.random.choice(m, 1)[0]
           x, y = X[j], Yn[j]
           score = self.w.dot(x)
           if y*score < 1:
              self.w = (1 - eta*self.lambda1)*self.w + eta*y*x
           else:
              self.w = (1 - eta*self.lambda1)*self.w

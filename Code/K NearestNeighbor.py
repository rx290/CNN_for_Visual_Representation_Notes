import numpy as np

class NearestNeighbor:
    # Constructor
    def __init__(self):
        pass

    def train(self,row,dimension):
        self.row_trainset = row
        self.dimension_trainset = dimension

    def predict(self,row):
        num_test = row.shape[0]

        # finding the item which resembles the input

        prediction = np.zeros(num_test,dtype= self.dimension_trainset.dtype)

        # iterate through the test rows:
        for n in range(num_test):
            # L1 / Manhattan Distance
            distances = np.sum(np.abs(self.row_trainset - row[n,:]), axis = 1)
            min_index = np.argmin(distances)
            prediction = self.dimension_trainset[min_index]

        return prediction
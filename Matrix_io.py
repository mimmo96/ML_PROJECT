import numpy as np

class Matrix_io:
    
    def __init__(self, matrix, len_output):
        self.matrix = matrix
        self.len_output = len_output
    
    def input(self):
        return  self.matrix[:, 0:self.matrix.shape[1] - self.len_output]
    
    def output(self):
        return self.matrix[:, self.matrix.shape[1] - self.len_output: self.matrix.shape[1]]
    
    def get_len_output(self):
        return self.len_output        
    

    def set(self, new_matrix):
        if self.matrix.shape == new_matrix.shape:
            self.matrix = new_matrix
        else:
            raise ("self.matrix_input.shape != new_matrix_input.shape")
    
    def create_batch(self, batch_size):
        #array di matrici contenente blocchi di dimensione batch_size
        np.random.shuffle(self.matrix)
        mini_batches = []
        #definisce numero di batch
        no_of_batches = self.matrix.shape[0] // batch_size
        for i in range(no_of_batches):
            mini_batch = Matrix_io(self.matrix[i*batch_size:(i+1)*batch_size], self.len_output)
            mini_batches.append(mini_batch)
        if self.matrix.shape[0] / batch_size != 0:
            #matrice con le restanti righe di self.matrix
            mini_batch = Matrix_io(self.matrix[(i+1)*batch_size:], self.len_output)
            if mini_batch.matrix.shape[0] < batch_size:
                mini_batch.matrix = np.append(mini_batch.matrix, self.matrix[0:batch_size-mini_batch.matrix.shape[0]], axis = 0)
            mini_batches.append(mini_batch)
        return mini_batches
        
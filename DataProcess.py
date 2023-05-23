import numpy as np
class DataProcess:
    def __init__(self, filepath):
        self.filepath =filepath
    def Process(self):
        data = np.loadtxt(self.filepath)
        for i in range(len(data[:])):
            for j in range(3):
                if(j == 0):
                    data[i][j] = data[i][j]/1000
                elif(j == 1):
                    data[i][j] = data[i][j]*1000
                elif(j == 2):
                    data[i][j] = (1/data[i][j])*304800
        return data



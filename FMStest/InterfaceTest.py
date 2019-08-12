import pandas as pd

class analyseExcel():
    def __init__(self):

        pass

    def readExcel(self):
        self.excel = pd.read_excel('./FMS接口.xlsx')







if __name__ == '__main__':
    a = analyseExcel()
    a.readExcel()
    print(a.excel)
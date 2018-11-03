# -*- coding: utf-8 -*-

import sys, os
from time import time
from PyQt5.QtWidgets import QApplication, QMainWindow
from Main_framework import Ui_Form
from Vivo_x23_data import Vivo_x23_data_main
from Vivo_x23_data_analysis import Vivo_x23_data_analysis_main
from Huawei_p20_data import Huawei_p20_data_main
from Huawei_p20_data_analysis import Huawei_p20_data_analysis_main
from Oppo_r17_data import Oppo_r17_data_main
from Oppo_r17_data_analysis import Oppo_r17_data_analysis_main
from Iphone_xs_max_data import Iphone_xs_max_data_main
from Iphone_xs_max_data_analysis import Iphone_xs_max_data_analysis_main

class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
    #数据采集
    def data(self):
        Name = self.mobileComboBox.currentText()
        file1 = os.path.exists(str(Name) + '.txt')
        file2 = os.path.exists(str(Name) + '_clean.txt')
        if not file1 and not file2:
            self.resultText.append('{}数据开始采集'.format(Name))
            begin = time()
            self.data_spider(Name)
            end = time()
            self.resultText.append('{}数据采集清洗完毕,用时{}s'.format(Name,(end - begin)))
        else:
            self.resultText.append('请先清空文件')

    #数据分析
    def data_analysis(self):
        Name = self.mobileComboBox.currentText()
        file = os.path.exists(str(Name)+'_clean.txt')
        if file:
            self.resultText.append('{}数据开始分析'.format(Name))
            self.data_analysis_spider(Name)
            self.resultText.append('{}数据分析完成'.format(Name))
        else:
            self.resultText.append('请先开始数据采集')
    #手机分析型号判断

    def data_analysis_spider(self,Name):
        if Name == 'Vivo_x23':
            Vivo_x23_data_analysis_main()
        elif Name == 'Huawei_p20':
            Huawei_p20_data_analysis_main()
        elif Name == 'Oppo_r17':
            Oppo_r17_data_analysis_main()
        elif Name == 'Iphone_xs_max':
            Iphone_xs_max_data_analysis_main()
        else:
            pass
    #手机采集型号判断

    def data_spider(self, Name):
        if Name == 'Vivo_x23':
            Vivo_x23_data_main()
        elif Name == 'Huawei_p20':
            Huawei_p20_data_main()
        elif Name == 'Oppo_r17':
            Oppo_r17_data_main()
        elif Name == 'Iphone_xs_max':
            Iphone_xs_max_data_main()
        else:
            pass

    #清空文本

    def clearResult(self):
        self.resultText.clear()
    #清空文件

    def clearFile(self):
        Name = self.mobileComboBox.currentText()
        file1 = os.path.exists(str(Name)+'.txt')
        file2 = os.path.exists(str(Name)+'_clean.txt')
        file3 = os.path.exists(str(Name) + '_sentiments.csv')
        if file1:
            os.remove(str(Name)+'.txt')
        if file2:
            os.remove(str(Name)+'_clean.txt')
        if file3:
            os.remove(str(Name)+'_sentiments.csv')
        self.resultText.append('文件清空完毕')

if __name__=="__main__":  
    app = QApplication(sys.argv)  
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())  

#第一种导入方法的方式
#import printingFunctions
#printingFunctions.showName()
#第二种方式 导入特定的函数 from 文件 导入 showName方法
#from  printingFunctions import showName
#showName();
#第三种方式 使用 as给导入的函数指定别名
#from printingFunctions import showName as show
#show()
#第四种方式，导入模块中的所有函数
from printingFunctions import *
showName()
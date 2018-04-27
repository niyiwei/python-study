#导入测试模块
import unittest
#导入要测试的函数
from nameFunction import getFormattedName

#编写测试类 类名随意，最好包含Test，必须继承unittest.TestCase
class NamesTestCase(unittest.TestCase):
	"""测试nameFunction.py"""

	def test_first_last_name(self):
		"""能够正确的处理像Janis Joplin这样的姓名吗？"""
		formattedName = getFormattedName('janis', 'joplin')
		#使用断言方法
		self.assertEqual(formattedName, 'Janis Joplin')

unittest.main()
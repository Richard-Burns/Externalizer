"""
Extension for saving all py_* ops and all module_* ops
"""

import os

from TDStoreTools import StorageManager
TDF = op.TDModules.mod.TDFunctions

class Main:

	def __init__(self, ownerComp):
		self.ownerComp = ownerComp
		self.libPath = 'lib/'
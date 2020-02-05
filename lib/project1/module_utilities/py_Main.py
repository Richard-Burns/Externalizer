"""
Extension for saving all py_* ops and all module_* ops
"""

import os

from TDStoreTools import StorageManager
TDF = op.TDModules.mod.TDFunctions

class Main:

	def __init__(self, ownerComp):
		self.ownerComp = ownerComp
		self.libPath = 'lib'
		
	def ExternalizePython(self, opPath):
		o = op(opPath)
		os.makedirs(self.libPath+o.path, exist_ok=True)
		filepath = self.libPath + opPath + '.py'
		o.par.file = self.libPath + opPath + '.py'
		o.par.loadonstart = True
		o.save(filepath)
		
		
	def ExternalizeTox(self, opPath):
		o = op(opPath)
		os.makedirs(self.libPath+o.path, exist_ok=True)
		
		if o.par.enablecloning and o.par.clone != "":
			toxPath = self.libPath + opPath + '.tox'
			o.par.externaltox = toxPath
			o.save(toxPath)
		
		
	def SaveAll(self):
		o = op('select_ops')
		
		for r in o.rows():
			type = r[0].val.split('_')[0]
			opName = r[0]
			path = r[2]
			
			# handle python
			if type == "py":
				self.ExternalizePython(path)
				
			# handle toxs
			if type == "module" or type == "base":
				self.ExternalizeTox(path)
				
	def SaveParent(self):
		
		# get our network editor panes and find parent comp
		for p in ui.panes:
			if p.type == PaneType.NETWORKEDITOR:
				self.ExternalizeTox(p.owner.path)
						
				pythonOps = p.owner.findChildren(name='py_*', maxDepth=1)
					
					
				for o in pythonOps:
					self.ExternalizePython(o.path)
					
	
	def SaveParentAndChildren(self):
		
		# get our network editor panes and find parent comp
		for p in ui.panes:
			if p.type == PaneType.NETWORKEDITOR:
				pa = p.owner
				self.ExternalizeTox(pa.path)
				
					
				subModules = pa.findChildren(name='module_* base_*')
					
				for module in subModules:
					self.ExternalizeTox(module.path)
						
				
				pythonOps = pa.findChildren(name='py_*')
					
				for o in pythonOps:
					self.ExternalizePython(o.path)
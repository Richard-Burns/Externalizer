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
		
	def ExternalizePython(self, opParentPath, opName):

		opPath = opParentPath + '/' + opName

		o = parent.Project.op(opPath)
		filepath = self.libPath + opPath + '.py'
		o.par.file = self.libPath + opPath + '.py'
		o.par.loadonstart = True
		o.save(filepath)
		
		
	def ExternalizeTox(self, opParentPath, opName):
		opPath = opParentPath + opName
		o = parent.Project.op(opPath)
		toxPath = self.libPath + opPath + '.tox'
		o.par.externaltox = toxPath
		o.save(toxPath)
		
		
	def SaveAll(self):
		o = op('select_ops')
		
		for r in o.rows():
			type = r[0].val.split('_')[0]
			opName = r[0]
			parentPath = r[3]
			
			#fix empty parent paths and add trailing slash
			if not parentPath:
				parentPath = ''
			else:
				parentPath = parentPath+"/"
			
			
			# if directories dont exist make them
			os.makedirs(self.libPath+r[3], exist_ok=True)
			
			# handle python
			if type == "py":
				self.ExternalizePython(r[3], opName)
				
			# handle toxs
			
			if type == "module":
				self.ExternalizeTox(parentPath, opName)
				
	def SaveParent(self):
		
		# get our network editor panes and find parent comp
		for p in ui.panes:
			if p.type == PaneType.NETWORKEDITOR:
				pa = p.owner
				folderpath = pa.par.externaltox.val
				folderpath = folderpath[:-4]
				os.makedirs(folderpath, exist_ok=True)
				
				pa.save(pa.par.externaltox)
					
				pythonOps = pa.findChildren(name='py_*', maxDepth=1)
				
				for o in pythonOps:
					filepath = o.par.file.val
					folderPath = filepath.split('.')
					folderPath = folderPath[0]
					os.makedirs(folderpath, exist_ok=True)
					o.save(filepath)
					
	
	def SaveParentAndChildren(self):
		
		# get our network editor panes and find parent comp
		for p in ui.panes:
			if p.type == PaneType.NETWORKEDITOR:
				pa = p.owner
				print(pa.path)
				
				folderpath = pa.par.externaltox.val
				folderpath = folderpath[:-4]
				os.makedirs(folderpath, exist_ok=True)
				
				pa.save(pa.par.externaltox)
				
				subModules = pa.findChildren(name='module_*')
				
				for module in subModules:
					folderpath = module.par.externaltox.val
					folderpath = folderpath[:-4]
					os.makedirs(folderpath, exist_ok=True)
				
					module.save(module.par.externaltox)
					
				pythonOps = pa.findChildren(name='py_*')
				
				for o in pythonOps:
					filepath = o.par.file.val
					folderPath = filepath.split('.')
					folderPath = folderPath[0]
					os.makedirs(folderpath, exist_ok=True)
					o.save(filepath)
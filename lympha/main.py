#!/usr/bin/python3
# -*- coding: ascii -*-
import sys

#for the graph function:
import os

prefilecom = ""
filecom = ""
argvlen = len(sys.argv)
filename = ""

starts = list()
steps = 0
modegraph = False
modestate = False
filecheck = False
modeexe = False
modeshow = False
modemap = False
exe_list = list()
show_list = list()
map_list = list()
series = list()
substates = list()
nextstates = list()
specs = list()
tipoint = None
operator = None

object_list = list()
exe_objects = list()

'''
class Factor:
	def __init__(self, name, tipoint, operator, next_list, spec_list, cont_list):
        		
		#list of next nodes:
		#next_list = next_list
		self.next_list = []
		
		#list of specifications:
		#spec_list = spec_list
		self.spec_list = []

		#list of contents:
		#cont_list = cont_list
		self.cont_list = []

		#name
		self.name = name
		
		#tipping point
		self.tipoint = tippoint
		
		#relational operator
		self.operator = operator

class Event:
	def __init__(self, name, next_list, spec_list, cont_list):
        		
		#list of next nodes:
		#next_list = next_list
		self.next_list = []
		
		#list of specifications:
		#spec_list = spec_list
		self.spec_list = []

		#list of contents:
		#cont_list = cont_list
		self.cont_list = []

		#name
		self.name = name
'''

class Statement:
	def __init__(self, name, tipoint, operator, next_list, cont_list, spec_list):
        
		self.flow = False
        		
		#list of next nodes:
		#next_list = next_list
		self.next_list = list(next_list)
		
		#list of specifications:
		#spec_list = spec_list
		self.spec_list = list()

		#list of contents:
		#cont_list = cont_list
		self.cont_list = list(cont_list)

		#name
		self.name = name
		
		#tipping point
		self.tipoint = tipoint
		
		#relational operator
		self.operator = operator

#object_list.append(Event(i))
#object_list.append(Factor(i))

def exefunc() :
# Add objects.name to show_list.
	global object_list
	global starts
	global show_list
	global steps
	nextstates = list()
	for step in range(0,steps) :
		for start in starts :
			for obj in object_list :
				if ("%s" % obj.name) == ("%s" % start) :
					print ("step %s: %s" % (step, start))
					
					for next_object in obj.next_list:
						obj.next_list
						nextstates.append(next_object)
		starts = list()			
		seen2 = {}
		nextstates = [seen2.setdefault(x, x) for x in nextstates if x not in seen2]
		starts = list(nextstates)
		nextstates = list()

def showfunc():
# Add objects.name to show_list.
	global object_list
	global starts
	global show_list
	global steps
	if modegraph == True:
		graphstr = 'digraph lympha {\n'	
	print ("step 1: %s" % (starts[0]))
	if modegraph == True:
		graphstr += ('%s [label="step 1: %s"] \n' % (starts[0],starts[0]))
	for step in range(1,steps):
		nextstates = list()
		###critical:
		#print("starts:%s" % starts)
		for start in starts:
			
			for obj in object_list:
				
				if ("%s" % obj.name) == ("%s" % start) :
					#print ("\n\nobj%s\n\n"%obj.next_list)
					#print ("step %s: %s" % (step, start))
					for next_object in obj.next_list :
						if obj.name != next_object :
							print ("step %s: %s" % (step+1, next_object))
							if modegraph == True and start != next_object :
								graphstr += ('%s->%s \n' % (start,next_object))
								graphstr += ('%s [label="step %s: %s"] \n' % (next_object,step+1,next_object))
							nextstates.append(next_object)
		seen2 = {}
		nextstates = [seen2.setdefault(x, x) for x in nextstates if x not in seen2]
		del starts[:]
		starts = list(nextstates)
		del nextstates[:]
	graphstr += '}'
	open('lympha.dot', 'w').close()
	outputfile = open("lympha.dot", "w")
	outputfile.write(graphstr)
	outputfile.close()
	cmd = 'dot lympha.dot -Tps -o lympha.pdf'
	os.system(cmd)

def mapfunc():
# Add objects.name to show_list.
	global object_list
	global starts
	global show_list
	global steps
	nextstates = list()
	for step in range(0,steps):
		for start in starts:
			print("start: %s\n" % start)
			for obj in object_list:
				print("start: %s\n" % start)
				if ("%s" % obj.name) == ("%s" % start):
					print("start: %s\n" % start)
					print ("step %s: %s" % (step, start))
					for next_object in obj.next_list:
						nextstates.append(next_object)
		start = list()				
		starts = list(nextstates)
		nextstates = list()

def statefunc():
	global object_list
	for obj in object_list:
		print("%s" % obj.name)	



def new(name, tipoint, operator, next_list, cont_list, spec_list):
	global object_list
	nameused = False
	for obj in object_list:
		if obj.name == name:
			nameused = True
	if nameused == False:
		name = name.replace(' ', '')
		statement = Statement(name, tipoint, operator, next_list, cont_list, spec_list)
		#statement = Statement(name, tipoint, operator, list(next_list), cont_list, spec_list)
		#if next_list != [] :
		#	statement.next_list = list(next_list)
		#if cont_list != [] :
		#	pass
		object_list.append(statement)

def assasement(eqobjs):
	#0 = operator
	#1 = tipping point
	#2 = content
	try:
		scale = eqobjs.split('==')
		scale.insert(0, "equiv")
		return eqobjs
		#break
	except:
		pass
	try:
		scale = eqobjs.split('>=')
		scale.insert(0, "geq")
		return eqobjs
		#break
	except:
		pass
	try:
		scale = eqobjs.split('<=')
		scale.insert(0, "leq")
		return eqobjs
		#break
	except:
		pass
	try:
		scale = eqobjs.split('!=')
		scale.insert(0, "no")
		return eqobjs
		#break
	except:
		pass
	try:
		scale = eqobjs.split('>')
		scale.insert(0, "g")
		return eqobjs
		#break
	except:
		pass
	try:
		scale = eqobjs.split('<')
		scale.insert(0, "l")
		return eqobjs
		#break
	except:
		pass


def run():
#loop problem in the same serie
	global object_list
	nexts = list()
	conts = list()
	for serie in series:
		arrowobjs = serie.split('->')
		count = 0
		nexts = list()
		conts = list()
		specs = list()
		tipoint = int()
		operator = str()
		# many nexts vs one
		scale = list()
		for anobj in arrowobjs:
			try:
				eqobjs = arrowobjs.split('=')
				scale = assasement(eqobjs)
				tipoint = scale[1]
				# delete first two and last two characters in scale[1] by [2:-2]:
				conts = split.scale[2][2:-2]
				
				if scale[0] == "equiv":
					thesum = subs.count(True)
					operator = scale[0]
					tipoint = scale[1]
					pass
				if scale[0] == "geq":
					thesum = subs.count(True)
					operator = scale[0]
					tipoint = scale[1]
					pass
					
				if scale[0] == "leq":
					thesum = subs.count(True)
					operator = scale[0]
					tipoint = scale[1]
					pass
					
				if scale[0] == "g":
					thesum = subs.count(True)
					operator = scale[0]
					tipoint = scale[1]
					pass
					
				if scale[0] == "l":
					thesum = subs.count(True)
					operator = scale[0]
					tipoint = scale[1]
					pass
					
				if scale[0] == "no":
					thesum = subs.count(True)
					operator = scale[0]
					tipoint = scale[1]
					pass
					
			except:
				pass
			anobj.replace(" ","")
			new(anobj,tipoint, operator,nexts,conts, specs)			
	seen = {}
	object_list = [seen.setdefault(x.name, x) for x in object_list if x.name not in seen]
	for serie in series:
		arrowobj = serie.split('->')
		count = 0
		nexts = list()
		conts = list()
		# many nexts vs one
		for anobj in arrowobj:
			anobj.replace(" ","")
			if not anobj == "":
				for bnobj in object_list:
					#critical:
					if (" %s " % bnobj.name) == ("%s" % anobj):
						nexting = ""
						try:
							newcount=count+1
							nexting = arrowobj[newcount].replace(" ","")
							if not nexting == "":
								#nexts.append(nexting)
								#bnobj.next_list += nexts
								bnobj.next_list.append(nexting)
								#print( "obj.next_list:%s" % bnobj.next_list )
								#nexts = []
								#nexting = ""
						except:
							pass
					seen3 = {}
					bnobj.next_list = [seen3.setdefault(x, x) for x in bnobj.next_list if x not in seen3]
				
				count += 1
			count = 0
	#seen = {}
	#object_list = [seen.setdefault(x.name, x) for x in object_list if x.name not in seen]			

	if modeexe == True:
		exefunc()	
	if modeexe == True:
		showfunc()
	if modeshow == True:
		showfunc()
	if modemap == True:
		mapfunc()
	if modestate == True:
		statefunc()	
if __name__=='__main__':
	for x in range(0, argvlen):
		if sys.argv[x] == "-f":
			prefilecom = sys.argv[x]
			filecom = sys.argv[x+1]
			filename = filecom
			textfile = open(filename, 'r')
			filetext = textfile.read()
			filetext = filetext.replace('\n', ' ')
			filetext = filetext.replace('  ', ' ')
			series = filetext.split(';')
			filecheck = True
		if sys.argv[x] == "-h":
			print ("-h for help\n-f file")
		if sys.argv[x] == "-exe":
			modeexe = True
		if sys.argv[x] == "-show":
			modeshow = True
		if sys.argv[x] == "-map":
			modemap = True		
		if sys.argv[x] == "-graph":
			modegraph = True					
		if sys.argv[x] == "-statements":
			modestate = True	
		if sys.argv[x] == "-steps":
			steps = int(sys.argv[x+1])
		if sys.argv[x] == "-start":
			starts.append(sys.argv[x+1])
# Execute functions that are connected to the arguments:
	if filecheck == True:
		run()

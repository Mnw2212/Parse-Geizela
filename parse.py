import types

def type_determine(x):
	NumberTypes = (types.IntType, types.LongType, types.FloatType)
	return isinstance(x,NumberTypes)


def mapping(x):
	# horizontal mapping
	# allows easily mapping of input strings and table
	horiz={'&':0,"'":1,'(':2,')':3,',':4,'-':5,':':6,'>':7,'@':8,\
	'a':9,'b':10,'{':11,'}':12,'$':13,'A':14,'B':15,'P':16,'Q':17,\
	'R':18,'S':19}
	#NTmap={'P':"P'",'a':'P',"'A":'P','P','&'}
	return horiz[x]

def parse(new):
	'''
	Tested, works with int, add float support
	'''
	words=list(new)
	'''						# Split into character list
	for i in range(len(words)):			# Changes every int,float etc into a
		if type_determine(int(words[i]))==True :

			print "variable found"
			words[i]='a'						# reason : Easy to parse 
	'''											# and check datatype according to grammar
	print words
	return words


def shift_state(s):
	# s will contain [ ids, next_state,state ]
	'''
	1. initial state=0,identity =id
	2. push id then push next state
	out[0] = state     			
		out[1] = val				# initial character
		out[2] = action[0] 			# will give the reduce or shift
		out[3] = int(action[1:]) 	# gives the next state number
	'''
	ids = s[1]
	next_state = s[3]
	stack.append(ids)
	stack.append(next_state)

	s[0] = stack[-1:]				# next state becomes current state
	s[1] = 
	# update out / s
	print stack
	return s


def reduce_state(r):
	'''
	1. pop |B| items 				--done
	out[0] = state     			
		out[1] = val				# initial character
		out[2] = action[0] 			# will give the reduce or shift
		out[3] = int(action[1:]) 	# gives the next state number
	'''
	# r will contain [ pops,ids, next_state ]
	red_map={1:1,2:2,3:2,4:2,5:3,6:1,7:4,8:6,9:0,10:5\
			,11:0,12:8,13:3,14:3,15:3,16:0}
	for i in range(red_map[r[0]]):
		stack.pop()

	print "pop done"
	print "reduce it"

					#stack is full now !!	
def sr(x):
	'''
	x => [state,val]
	initial state 0 before parsing, value is in_str[0]
	'''
	out=[0,0,0,0]
	state = x[0]					# x[0] gives current state
	val = x[1]						# x[1] gives character
	tab_map = mapping(val)
	action = table[state][tab_map]
	if(action == 0):
		print "String is invalid"
	else:
		out[0] = state     			
		out[1] = val				# initial character
		out[2] = action[0] 			# will give the reduce or shift
		out[3] = int(action[1:]) 	# gives the next state number


	print out
	return out


def get_string():
	string=raw_input("Enter the string : ")	#Get input string
	return parse(string)					# split string by char by char
	


if __name__=="__main__":

	table=[['s1','s2','s3',0,0,0,0,0,'s4','s6',0,0,0,0,0,0,5,0,0,0],
			[0,0,0,'r11',0,'r11',0,0,0,0,'s8','r11','r11','r11',0,0,0,0,0,0],
			[0,0,'s9',0,0,0,0,0,0,0,0,'s11',0,0,10,0,0,0,0,0],
			['s1','s2','s12',0,0,0,0,0,'s4','s6',0,0,0,0,0,0,13,14,0,0],
		  ]

	stack=[0]
	
	in_str = get_string()			#input string split well
	first = in_str[0]				#first character in input

	select=[0,first]

	act = sr(select)
	if act[0]=='s':
		shift_state(act)
	elif act[0]=='r':
		reduce_state(act)

	'''
	[0, str[0]] => s1 or r1 ...
	and 
	[id,state] => r1  comparison
	'''





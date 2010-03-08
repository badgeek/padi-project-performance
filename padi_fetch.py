# WEB DATA -> PD
# 2010 iyok@deadmediafm.org

print "\n\n--- PADI PY EXTERNAL"
print "--- by iyok@deadmediafm.org"

try:
	import urllib
	import pyext
except:
	print "ERROR!! FCK!"


class padiclass(pyext._class):

	#
	#	INLET 1 TIPE BANG, GET PADI DATA OUTPUT VARIABEL padi_data  ----> OUTLET 2 UKURAN ARRAY
	#	INLET 2 TIPE DATA INT, OUTPUT LIST USER DARI WEB P.A.D.I	----> OUTLET 1 LIST DATA
	#	

	_inlets  = 2
	_outlets = 2
	
	padi_data = [(1,1,1,1,1,1)]

	def readPadi(self):
		print "--DOWNLOADING DATA"
		try:
			file = urllib.urlopen('http://padi.natural-fiber.com/index.php/main/getdata').read()
			test = file.split('\n')
			
			test.pop()
			#test = test.remove(len(test) - 1)

			for user in test:
				#print user + "ok!\n"
				#individual_1 = user.split("|")
				#individual_2 = [int(i) for i in individual_1]
				T1 = user.split('|')
				print T1
				#T1.remove(-1)
				T1 = map(int, user.split('|'))
				self.padi_data.append(T1)
				
				

			#ARRAY SIZE
			self._outlet(2,len(self.padi_data))
			print "--DATA DOWNLOADED...OK"
		except:
			##self._outlet(2,len(self.padi_data))
			print "--ERROR CANNOT DOWNLOAD DATA"

	def bang_1(self):
		self.readPadi()
		print len(self.padi_data)
		##self._outlet(1,)
		
	def int_2(self,f):
	#	try:
			if (f < len(self.padi_data)) and (f >= 0):
				self._outlet(1,self.padi_data[f])
				##print self.padi_data[f]
	#	except:
	#		print "--ERROR OUT OF RANGE"
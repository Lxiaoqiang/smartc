__author__ = 'damao'

from ctypes import *
import time
import base64
import random

lib=CDLL("C:\Python27\Lib\site-packages\ccks_interface_lib\softkey.dll")

func=lib.testfunc
func.argtypes = (c_int,c_int)
func.restype = c_int

ming2mi=lib.changmingtomi
ming2mi.argtypes = (c_char_p,c_char_p,c_int)
ming2mi.restype = c_int

ccks_en=lib.ccks_en
ccks_en.argtypes=(c_char_p,c_char_p,c_char_p,c_uint,c_char_p,POINTER(c_uint))
ccks_en.restype = c_int

ccks_de=lib.ccks_de
ccks_de.argtypes=(c_char_p,c_char_p,c_uint,c_char_p,POINTER(c_uint))
ccks_de.restype = c_int

sha256=lib.SHA256_Data_Zgz
sha256.argtypes=(c_char_p,c_uint,c_char_p)
sha256.restype = c_char_p

ccks_sign=lib.ccks_sign_add
ccks_sign.argtypes=(c_char_p,c_char_p,c_uint,c_char_p,POINTER(c_uint))
ccks_sign.restype = c_int

en_data=(c_char*1024)()
en_data_len = c_uint(0)

de_data=(c_char*1024)()
de_data_len = c_uint(0)

shadata=(c_char*1024)()
shadata_len=c_uint(0)

sign_data=(c_char*1024)()
sign_data_len=c_uint(0)

class ccks_interface_encryption(object):

	ROBOT_LIBRARY_SCOPE = 'GLOBAL'

	def __init__(self):
		pass

	def concatenate(self,var1,var2):
		buf=b'\x31\x18\xe3\x77\x35\x09\x27\x29\xbd\x93\x3d\x70\xba\xe7\x6a\x55\x2a\x97\xf4\xd4\x21\x48\xcf\x1f\x35\x6a\xb8\x78\xf8\x02\x00\x50\xb3\xe5\x6a\x69\x68\x31\x4f\xeb\xad\x8e\xd0\x6c\xc0\x7b\x6d\x60\xb5\x4a\x8b\xcc\x10\x8a\xad\x1b\x00\x8e\x7c\xe7\xa4\x63\x5d\xcf\xb6\x1a\xbf\x7d\xd8\xb5\x27\xec\x93\xc7\x27\x49\xa2\x02\x54\xa7\x67\x2d\xf8\x5d\x82\xf5\xdf\x74\x73\x4f\xaf\xa6\x79\x15\x21';
		#buf=b'\x31\x18\xe3\x77\x35\x09\x27\x29\xbd\x93\x3d\x70\xfe\xeb\x9d\xa9\x54\xaa\x5f\xd3\x50\x85\x23\x3c\x7c\xd5\xaa\xe1\xe3\xe0\x0b\xe0\x05\x0b\x3e\x56\xa6\x96\x83\x14\xfe\xba\xd8\xed\x06\xfb\x30\x1e\xdb\x58\x2d\x52\xa2\xf3\x04\x22\xab\x46\xc0\x23\x9f\x39\xe9\x18\xd7\x73\xed\x86\xaf\xdf\x76\x2d\x49\xfb\x24\xf1\xc9\xd2\x68\x80\x95\x29\xd9\xcb\x7e\x17\x60\xbd\x77\xdd\x1c\xd3\xeb\xe9\x9f\xf9\x15\x21'
		buf_len=len(buf)
		print(buf_len,buf)
		res = ccks_de("tsm_bjtbiz.pack",buf, buf_len ,de_data,byref((de_data_len)))
		if (res==0):
			str = de_data[0:de_data_len.value]
			return str
		else:
			print("res", res)
			return res


	def jiami(self,var1,var2):
		print (func(int(var1),int(var2)))
		print (var1,var2)
		print (len(var1))
		print (ming2mi(bytes(var1),bytes(var2),len(var1)))
		print (var1,var2)

	#var1 mingdata  var2 midata   var3 midatalen
	def ccksen(self,var1):
		data=var1.encode('utf-8')
		data_len = len(data)
		print ("ccksen",data,data_len)

		#"tsm_bjtbiz.pack","tsm.csc.so"
		#"rms_bjtbiz.pack","rms.csc.so"
		res = ccks_en("tsm_bjtbiz.pack","tsm.csc.so" ,data, data_len ,en_data,byref((en_data_len)))
		#retdict = {'res':res,'en_data':en_data[0:en_data_len.value],'en_data_len':en_data_len.value}
		print (en_data,en_data_len.value)
		print ("res",res)
		if (res==0):
			#str = unicode(en_data[0:en_data_len.value], errors='ignore')
			str = en_data[0:en_data_len.value]
			print (str,len(str))
			#os.mknod("test.txt")
			#fp = open("test.dat","wb")
			#fp.write(str)
			#fp.close()
			return base64.urlsafe_b64encode(str)
		else:
			return res
		#return retdict
		#return (res,en_data,en_data_len)

	#var1 midata  var2 mingdata   var3 mingdatalen

	def ccksde(self,var1):
		data=var1
		print ("data", data)
		lens = len(var1)
		loopnum=3-lens%3
		if loopnum>0 :
			for i in range (0,loopnum):
				data=data+"="
		else:
			data=var1
		print ("data", data)
		#data = base64.b64decode(data[:lenx])
		#print "data", data
		#data_len=len(data)
		#print "var1",var1

		data = base64.urlsafe_b64decode(data)
		data_len=len(data)
		print ("ccksde:",data,data_len)

		#"tsm_bjtbiz.pack","tsm.csc.so"
		#"rms_bjtbiz.pack","rms.csc.so"
		res = ccks_de("tsm_bjtbiz.pack",data, data_len ,de_data,byref((de_data_len)))
		#retdict = {'res':res,'de_data':de_data[],'de_data_len':de_data_len.value}
		print ("de_data:",de_data,de_data_len.value)
		#return retdict
		if (res==0):
			#str = unicode(de_data[0:de_data_len.value], errors='ignore')
			str = de_data[0:de_data_len.value].decode('utf-8')
			return str
		else:
			print("res", res)
			return res

	def hashfunc(self,var1):
		data=var1
		data_len=len(var1)
		print ("hashfunc",data,data_len)
		res=sha256(data,data_len,shadata)
		return shadata[0:64	]

	def getts(self,var1):
		return int(time.time()+var1)

	def getps(self):
		return int(time.time())

	def wait_time(self,num):
		time.sleep(int(num))
		return num

	def append_list(self,i):
		list =[]
		list.append(i)
		return list

	def sum_list(self,list):
		sum_list = sum(list)
		return sum_list

	def add(self,v1,v2):
		v1 = v1+v2
		return v1

	def cckssign(self,var1):
		data=var1
		data_len=len(var1)
		print ("cckssign",data,data_len)
		res=ccks_sign("tsm_bjtbiz.pack",data,data_len,sign_data,byref((sign_data_len)))
		return base64.b64encode(sign_data[0:sign_data_len.value])


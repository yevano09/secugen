#pswebcam.py
import subprocess

def gettakePicture(name):
	print(" entering getTakePicture")
	print( name )
	fname= name+'.jpg'
	result = subprocess.Popen(['fswebcam','-S', '8',  fname ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = result.communicate()
	print( out ) 
	return


def getface(name):
	print(" Entering face recognition" )
	retVal = False;
	fname=name+'.jpg'
	result = subprocess.Popen(['face_recognition', 'knownfaces/', fname ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = result.communicate() 
	res =(out.rsplit(',', 1)[1]).strip()
	if( name.lower() == res.lower() ):
		print( name +" Image matches with DB ")
		retVal = True
	else:
		print( name + " Image does not match with DB")
	return retVal



if __name__ == "__main__":
	getface("Jawahar")

#psfingerprintcheck.py

import subprocess

def checkFingerImage(name):
	print( "name is : "+name)
	retVal = False
	name=name+'1.raw'
	result = subprocess.Popen(['./../bin/pi/match_fdu05', './../bin/pi/'+name ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = result.communicate()
	print( out )
	if( "NO" not in out):
		print( " no not in out ")
		retVal = True
	return retVal


if __name__ == "__main__":
		checkFingerImage("jawahar")

#psfingerprintcheck.py

import subprocess

def checkFingerImage(name):
	name=name+'1.raw'
	result = subprocess.Popen(['./../bin/pi/match_fdu05', name ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = result.communicate()
	print( out) 


if __name__ == "__main__":
	checkFingerImage("jawahar")

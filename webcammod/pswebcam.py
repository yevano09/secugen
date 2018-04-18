#pswebcam.py
import subprocess


def getface(name):
	result = subprocess.Popen(['face_recognition', 'knownfaces/', name ], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	out, err = result.communicate()
	print( out.rsplit(',', 1)[1]) 


if __name__ == "__main__":
	getface("unknown.jpg")

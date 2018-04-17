#register.py 
# intention is to register the person by taking the image and finger print
import sys, getopt
import subprocess


def main(argv):
   nametoregister = ''
   print "inmain :", argv

   try:
      opts, args = getopt.getopt(argv,"hr:","regname=")
   except getopt.GetoptError:
      print 'register.py -r <name>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
	 print 'register.py -r <name>'
         sys.exit()
      elif opt in ("-r", "--regname"):
         nametoregister="./imageload_fdu05"
	 subprocess.call( [nametoregister,  arg ])


	


if __name__ == "__main__":
   main(sys.argv[1:])
	





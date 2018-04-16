import subprocess

p = subprocess.Popen( [ "./match_fdu05", "jawahar"], stdout=subprocess.PIPE,shell=True)

(output, err) = p.communicate()

p_status = p.wait()

print "command output :", output
print "command exit/status :", p_status

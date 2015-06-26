#!/usr/bin/python3
import subprocess, os

print('hello world')

os.system('echo hello system')


########### CALL ########### 

subprocess.call(['echo', 'hello subprocess'])
subprocess.call(['echo', '\n\tSoftware file content :\n'])
subprocess.call('echo $HOME', shell=True)

p = subprocess.Popen(["ls", "-l", "/home/anaisb/software/"], stdout=
subprocess.PIPE)
output, err = p.communicate()
print "*** Running ls -l command ***\n", output

#subprocess.check_call(['false'])

output = subprocess.check_output(['ls', '-1', '/home/anaisb/software'])
print 'Have %d bytes in output' %len(output)
print output


########### PIPE ########### 

p = subprocess.Popen("date", stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
print "\n\tToday is ", output

print '\nread:'
proc = subprocess.Popen(['echo', 'to stdout'], stdout=subprocess.PIPE)
stdout_value = proc.communicate()[0]
print '\tstdout:', repr(stdout_value)

print '\nwrite:'
proc = subprocess.Popen(['cat', '-'],stdin=subprocess.PIPE,)
proc.communicate('\tstdin : to stdin\n')

print '\npopen2:' 
proc = subprocess.Popen(['cat', '-'], stdin=
subprocess.PIPE, stdout=subprocess.PIPE,) 
stdout_value = proc.communicate('through stdin to stdout')[0] 
print '\tpass through:', 
repr(stdout_value)

print '\npopen3:'
proc = subprocess.Popen('cat -; echo "to stderr" 1>&2',shell=True,
stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,)
stdout_value, stderr_value = proc.communicate('through stdin to stdout')
print '\tpass through:', repr(stdout_value)
print '\tstderr      :', repr(stderr_value)

print '\npopen4:'
proc = subprocess.Popen('cat -; echo "to stderr" 1>&2', shell=True, 
stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.
STDOUT, )
stdout_value, stderr_value = proc.communicate('through stdin to stdout\n')
print '\tcombined output:', repr(stdout_value)
print '\tstderr value   :', repr(stderr_value)



cat = subprocess.Popen(['cat', 'test1.py'], stdout=subprocess.PIPE, )
grep = subprocess.Popen(['grep', '.. include::'], stdin=cat.stdout, 
stdout=subprocess.PIPE, )
cut = subprocess.Popen(['cut', '-f', '3', '-d:'], stdin=grep.stdout, 
stdout=subprocess.PIPE, )
end_of_pipe = cut.stdout
print 'Included files:'
for line in end_of_pipe:
    print '\t', line.strip()


print '\n\nOne line at a time:'
proc = subprocess.Popen('python repeater.py', 
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        )
for i in range(10):
    proc.stdin.write('%d\n' % i)
    output = proc.stdout.readline()
    print output.rstrip()
remainder = proc.communicate()[0]
print remainder

print
print 'All output at once:'
proc = subprocess.Popen('python repeater.py', 
                        shell=True,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        )
for i in range(10):
    proc.stdin.write('%d\n' % i)

output = proc.communicate()[0]
print output

#~ ######################################################################
#~ output=`mycmd myarg`
#~ # becomes
#~ output = check_output(["mycmd", "myarg"])
#~ 
#~ output=`dmesg | grep hda`
#~ # becomes
#~ p1 = Popen(["dmesg"], stdout=PIPE)
#~ p2 = Popen(["grep", "hda"], stdin=p1.stdout, stdout=PIPE)
#~ p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
#~ output = p2.communicate()[0]
#~ OR
#~ output=check_output("dmesg | grep hda", shell=True)
#~ 
#~ status = os.system("mycmd" + " myarg")
#~ # becomes
#~ status = subprocess.call("mycmd" + " myarg", shell=True)
#~ 
#~ pipe = os.popen("cmd", 'r', bufsize)
#~ ==>
#~ pipe = Popen("cmd", shell=True, bufsize=bufsize, stdout=PIPE).stdout
#~ 
#~ pipe = os.popen("cmd", 'w', bufsize)
#~ ==>
#~ pipe = Popen("cmd", shell=True, bufsize=bufsize, stdin=PIPE).stdin
#~ 
#~ (child_stdin, child_stdout) = os.popen2("cmd", mode, bufsize)
#~ ==>
#~ p = Popen("cmd", shell=True, bufsize=bufsize,
          #~ stdin=PIPE, stdout=PIPE, close_fds=True)
#~ (child_stdin, child_stdout) = (p.stdin, p.stdout)
#~ 
#~ (child_stdin,
 #~ child_stdout,
 #~ child_stderr) = os.popen3("cmd", mode, bufsize)
#~ ==>
#~ p = Popen("cmd", shell=True, bufsize=bufsize,
          #~ stdin=PIPE, stdout=PIPE, stderr=PIPE, close_fds=True)
#~ (child_stdin,
 #~ child_stdout,
 #~ child_stderr) = (p.stdin, p.stdout, p.stderr)
#~ 
#~ (child_stdin, child_stdout_and_stderr) = os.popen4("cmd", mode,
                                                   #~ bufsize)
#~ ==>
#~ p = Popen("cmd", shell=True, bufsize=bufsize,
          #~ stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
#~ (child_stdin, child_stdout_and_stderr) = (p.stdin, p.stdout)
#~ 

#~ pipe = os.popen("cmd", 'w')
#~ ...
#~ rc = pipe.close()
#~ if rc is not None and rc >> 8:
    #~ print "There were some errors"
#~ ==>
#~ process = Popen("cmd", 'w', shell=True, stdin=PIPE)
#~ ...
#~ process.stdin.close()
#~ if process.wait() != 0:
    #~ print "There were some errors"
    
    
   #~ import re
   #~ def arping(ipaddress="10.0.1.1"):
     #~ """Arping function takes IP Address or Network, returns nested mac/ip list"""
   #~ 
     #~ #Assuming use of arping on Red Hat Linux
     #~ p = subprocess.Popen("/usr/sbin/arping -c 2 %s" % ipaddress, shell=True,
                           #~ stdout=subprocess.PIPE)
     #~ out = p.stdout.read()
     #~ result = out.split()
     #~ pattern = re.compile(":")
     #~ for item in result:
       #~ if re.search(pattern, item):
         #~ print item
   #~ arping()

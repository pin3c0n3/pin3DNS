import os
clear = lambda: os.system('clear')
clear()
print ('\033[1;47m  Version 0.5  \033[1;m', '\n', '\033[1;46m  Created by Philip Kohn | @pin3c0n3  \033[1;m', '\n')
domain = input("Enter domain: ")
sub = ['aut1odiscover', 'email', 'ftp', 'imap', 'mail', 'pop', 'pop3', 'remote', 'secure', 'sftp', 'sip', 'smtp', 'vpn', 'www']
#file = open('targets.txt', 'w')
targetsName = ('target_' + domain + '.txt')
resultsName = ('results_' + domain + '.txt')
cmd = ("dig -f ./target/" + targetsName + " +noall +answer > ./results/" + resultsName)
file = open("./target/" + targetsName, 'w')
file.write (domain + '\n')
for i in range(len(sub)):
   file.write (sub[i] + "." + domain + '\n')

file.close()

#os.system( 'dig -f fileName +noall +answer > results.txt' )
#os.system( 'cat results.txt' )
os.system(cmd)
cmd = ("cat ./results/" + resultsName)
os.system(cmd)

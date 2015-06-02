import os
clear = lambda: os.system('clear')
clear()
print ('\033[1;47m  Version 0.6.5  \033[1;m', '\n', '\033[1;46m  Created by Philip Kohn | @pin3c0n3  \033[1;m', '\n')
domain = input("Enter domain: ")
sub = ['admin', 'aut1odiscover', 'dev', 'download', 'drop', 'email', 'files', 'ftp', 'imap', 'm', 'mail', 'media', 'mobile', 'pop', 'pop3', 'qa', 'remote', 'secure', 'sftp', 'sip', 'smtp', 'test', 'tst', 'video', 'videos', 'vpn', 'www', 'wwwqa']
if not os.path.exists("./targets"):
    os.makedirs("./targets")
if not os.path.exists("./results"):
    os.makedirs("./results")
targetsName = ('./targets/target_' + domain + '.txt')
resultsName = ('./results/results_' + domain + '.txt')
cmd = ("dig -f " + targetsName + " +noall +answer > " + resultsName)
file = open(targetsName, 'w')
file.write (domain + '\n')
for i in range(len(sub)):
   file.write (sub[i] + "." + domain + '\n')

file.close()

os.system(cmd)
cmd = ("cat " + resultsName)
os.system(cmd)

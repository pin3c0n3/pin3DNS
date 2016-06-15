import os
clear = lambda: os.system('clear')
clear()
print ('\033[1;47m  Version 0.7.6 \033[1;m', '\n', '\033[1;46m  Created by Philip Kohn | https://www.philipkohn.com | @pin3c0n3  \033[1;m', '\n')
domain = input("Enter domain: ")
sub = ['admin', 'aut1odiscover', 'dev', 'download', 'drop', 'email', 'files', 'firewall', 'ftp', 'imap', 'm', 'mail', 'media', 'mobile', 'mx', 'ns1', 'ns2', 'ns3', 'ns4', 'owa', 'pop', 'pop3', 'proxy', 'qa', 'remote', 'router', 'secure', 'sftp', 'siem', 'sip', 'smtp', 'syslog', 'test', 'tst', 'video', 'videos', 'vpn', 'webmail', 'www', 'www2', 'wwwqa']
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

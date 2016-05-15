from ftplib import FTP

host = raw_input('host to connect to >> ')
usr = raw_input('user name >> ')
pwd = raw_input('password >> ')

host = str(host)
usr = str(usr)
pwd = str(pwd)

ftp = FTP(host)
ftp.login(usr, pwd)
ftp.retrlines('LIST')
ftp.quit()
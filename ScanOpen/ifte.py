import socket
import time

socket.setdefaulttimeout(0.5)
sk=socket.socket(socket.AF_INET, socket.SOCK_STREAM)   #TCP连接
sk.gettimeout()
ip = input('>>>请输入IP:')
port =  int(input('>>>请输入端口:'))
error = sk.connect_ex((ip,port))
conA = '连接失败'
conB = '连接成功'
conC = '错误代码：'





while (error >= 0):
 if error > 0:
     print(conA, conC, error)
     sk.close()
     time.sleep(0.5)
     sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     error = sk.connect_ex((ip, port))
 elif error == 0:
     print(conB, ip,':',port)
     sk.close()
     time.sleep(1)
     sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     error = sk.connect_ex((ip, port))

sk.close()



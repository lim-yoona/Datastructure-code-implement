# try:
#     list1=[1,2,3,4,5,6]
#     print(list1['a'])
#     print('Hello')
# except BaseException:
#     print(BaseException.__context__)
# finally:
#     print('End!')


# class Person:
#     i=3
#     def prin(self,j):
#         print('%d  %d'%(self.i,j))
#         print(__doc__)
# class student:
#     __name=''
#     __age=-1
#     def prin(self,j):
#         print('Helloworld!')
# if __name__ == '__main__':
#     t=Person()
#     t.prin(9)
#     print(t.__dict__)
#     s=student()
#     s=t
#     s.prin(4)


# import re
# str1='Hello world! I am jack. I am from Americ'
# pattern='wor'
# i=re.search(pattern,str1)
# print(i)


# import  socket
#
# s=socket.socket()
# r=socket.socket()
# host=socket.gethostname()
# port=12345
# s.bind((host,port))
# s.listen(5)
# while True:
#     c,addr=s.accept()
#     print('address:',addr)
#     str_send=input()
#     c.send(str.encode(str_send))
#     host1=addr[0]
#     port1=addr[1]
#     r.connect((host1,port1))
#     print(s.recv(1024))
#     c.close()
#     r.close()

import collections
#python实现栈
def stack():
    list1 = []
    list1.append(3)
    list1.append(89)
    print(list1)
    list1.pop()
    print(list1)

#python实现队列
def queue():
    q=collections.deque()
    q.append(7)
    q.append(8)
    print(q)
    q.popleft()
    print(q)

def linkList():
    class Node:
        a=-1
        b=-1
    head=Node()
    head.a=0
    head.b=-1;
    p=Node()
    p.a=1
    p.b=-1
    head.b=p
    p=Node()
    p.a=2
    p.b=-1
    head.b.b=p
    p=head
    while p!=-1:
        print(p.a)
        print(p.b)
        p=p.b


if __name__ == '__main__':
    linkList()
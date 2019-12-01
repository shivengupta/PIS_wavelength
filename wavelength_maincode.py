

from time import sleep
import threading
import playsound
from winsound import PlaySound, SND_FILENAME, SND_LOOP, SND_ASYNC

import serial




s1=serial.Serial('COM4',9600)


def back_beat(n):
    while True:
        playsound.playsound(n)
        sleep(0.001)


set1=list(range(1,5))
set2=list(range(5,9))
set3=list(range(9,13))
set4=list(range(13,17))
set5=list(range(17,21))
set6=list(range(21,25))
set7=list(range(25,29))
set8=list(range(29,33))
set9=list(range(33,37))
set10=list(range(37,41))
set11=list(range(41,45))
set12=list(range(45,49))
set13=list(range(49,53))
set14=list(range(53,57))
set15=list(range(57,61))
def myset1(n):
    
    for i in range(len(listme1)):
        listme1[i]=n+listme1[i]

def myset2(n):
    
    for i in range(len(listme2)):
        listme2[i]=n+listme2[i]

def myset3(n):
    
    for i in range(len(listme3)):
        listme3[i]=n+listme3[i]

def myset4(n):
    
    for i in range(len(listme4)):
        listme4[i]=n+listme4[i]




listme4=['beatc2.wav','beatd2.wav','beate2.wav','beatg2.wav','beata2.wav','beatc3.wav','beatd3.wav','beate3.wav','beatg3.wav','beata3.wav','beatc4.wav','beatd4.wav','beate4.wav','beatg4.wav','beata4.wav']
myset4('d')

listme3=['beatc2.wav','beatd2.wav','beate2.wav','beatg2.wav','beata2.wav','beatc3.wav','beatd3.wav','beate3.wav','beatg3.wav','beata3.wav','beatc4.wav','beatd4.wav','beate4.wav','beatg4.wav','beata4.wav']
myset3('j')

listme2=['beatc2.wav','beatd2.wav','beate2.wav','beatg2.wav','beata2.wav','beatc3.wav','beatd3.wav','beate3.wav','beatg3.wav','beata3.wav','beatc4.wav','beatd4.wav','beate4.wav','beatg4.wav','beata4.wav']
myset2('j')

listme1=['beatc2.wav','beatd2.wav','beate2.wav','beatg2.wav','beata2.wav','beatc3.wav','beatd3.wav','beate3.wav','beatg3.wav','beata3.wav','beatc4.wav','beatd4.wav','beate4.wav','beatg4.wav','beata4.wav']
myset1('d')


def foreground():
    aprev=[1000]
    bprev=[1000]
    cprev=[1000]
    dprev=[1000]
    while True:
        read=s1.readline().decode()
        read=read.split()
        a=int(read[0])
        b=int(read[1])
        c=int(read[2])
        d=int(read[3])
        if a in aprev:
            continue
        if a in set1:
            PlaySound(listme1[0],SND_FILENAME|SND_ASYNC)
            aprev=set1
            continue
        elif a in set2:
            PlaySound(listme1[1],SND_FILENAME|SND_ASYNC)
            aprev=set2
            continue
        elif a in set3:
            PlaySound(listme1[2],SND_FILENAME|SND_ASYNC)
            aprev=set3
            continue
        elif a in set4:
            PlaySound(listme1[3],SND_FILENAME|SND_ASYNC)
            aprev=set4
            continue
        elif a in set5:
            PlaySound(listme1[4],SND_FILENAME|SND_ASYNC)
            aprev=set5
            continue
        elif a in set6:
            PlaySound(listme1[5],SND_FILENAME|SND_ASYNC)
            aprev=set6
            continue
        elif a in set7:
            PlaySound(listme1[6],SND_FILENAME|SND_ASYNC)
            aprev=set7
            continue
        elif a in set8:
            PlaySound(listme1[7],SND_FILENAME|SND_ASYNC)
            aprev=set8
            continue
        elif a in set9:
            PlaySound(listme1[8],SND_FILENAME|SND_ASYNC)
            aprev=set9
            continue
        elif a in set10:
            PlaySound(listme1[9],SND_FILENAME|SND_ASYNC)
            aprev=set10
            continue
        elif a in set11:
            PlaySound(listme1[10],SND_FILENAME|SND_ASYNC)
            aprev=set11
            continue
        elif a in set12:
            PlaySound(listme1[11],SND_FILENAME|SND_ASYNC)
            aprev=set12
            continue
        elif a in set13:
            PlaySound(listme1[12],SND_FILENAME|SND_ASYNC)
            aprev=set13
            continue
        elif a in set14:
            PlaySound(listme1[13],SND_FILENAME|SND_ASYNC)
            aprev=set14
            continue
        elif a in set15:
            PlaySound(listme1[14],SND_FILENAME|SND_ASYNC)
            aprev=set15
            continue
        elif b in bprev:
            continue
        elif b in set1:
            PlaySound(listme2[0],SND_FILENAME|SND_ASYNC)
            bprev=set1
            continue
        elif b in set2:
            PlaySound(listme2[1],SND_FILENAME|SND_ASYNC)
            bprev=set2
            continue
        elif b in set3:
            PlaySound(listme2[2],SND_FILENAME|SND_ASYNC)
            bprev=set3
            continue
        elif b in set4:
            PlaySound(listme2[3],SND_FILENAME|SND_ASYNC)
            bprev=set4
            continue
        elif b in set5:
            PlaySound(listme2[4],SND_FILENAME|SND_ASYNC)
            bprev=set5
            continue
        elif b in set6:
            PlaySound(listme2[5],SND_FILENAME|SND_ASYNC)
            bprev=set6
            continue
        elif b in set7:
            PlaySound(listme2[6],SND_FILENAME|SND_ASYNC)
            bprev=set7
            continue
        elif b in set8:
            PlaySound(listme2[7],SND_FILENAME|SND_ASYNC)
            bprev=set8
            continue
        elif b in set9:
            PlaySound(listme2[8],SND_FILENAME|SND_ASYNC)
            bprev=set9
            continue
        elif b in set10:
            PlaySound(listme2[9],SND_FILENAME|SND_ASYNC)
            bprev=set10
            continue
        elif b in set11:
            PlaySound(listme2[10],SND_FILENAME|SND_ASYNC)
            bprev=set11
            continue
        elif b in set12:
            PlaySound(listme2[11],SND_FILENAME|SND_ASYNC)
            bprev=set12
            continue
        elif b in set13:
            PlaySound(listme2[12],SND_FILENAME|SND_ASYNC)
            bprev=set13
            continue
        elif b in set14:
            PlaySound(listme2[13],SND_FILENAME|SND_ASYNC)
            bprev=set14
            continue
        elif b in set15:
            PlaySound(listme2[14],SND_FILENAME|SND_ASYNC)
            bprev=set15
            continue
        elif c in cprev:
            continue
        elif c in set1:
            PlaySound(listme3[0],SND_FILENAME|SND_ASYNC)
            cprev=set1
            continue
        elif c in set2:
            PlaySound(listme3[1],SND_FILENAME|SND_ASYNC)
            cprev=set2
            continue
        elif c in set3:
            PlaySound(listme3[2],SND_FILENAME|SND_ASYNC)
            cprev=set3
            continue
        elif c in set4:
            PlaySound(listme3[3],SND_FILENAME|SND_ASYNC)
            cprev=set4
            continue
        elif c in set5:
            PlaySound(listme3[4],SND_FILENAME|SND_ASYNC)
            cprev=set5
            continue
        elif c in set6:
            PlaySound(listme3[5],SND_FILENAME|SND_ASYNC)
            cprev=set6
            continue
        elif c in set7:
            PlaySound(listme3[6],SND_FILENAME|SND_ASYNC)
            cprev=set7
            continue
        elif c in set8:
            PlaySound(listme3[7],SND_FILENAME|SND_ASYNC)
            cprev=set8
            continue
        elif c in set9:
            PlaySound(listme3[8],SND_FILENAME|SND_ASYNC)
            cprev=set9
            continue
        elif c in set10:
            PlaySound(listme3[9],SND_FILENAME|SND_ASYNC)
            cprev=set10
            continue
        elif c in set11:
            PlaySound(listme3[10],SND_FILENAME|SND_ASYNC)
            cprev=set11
            continue
        elif c in set12:
            PlaySound(listme3[11],SND_FILENAME|SND_ASYNC)
            cprev=set12
            continue
        elif c in set13:
            PlaySound(listme3[12],SND_FILENAME|SND_ASYNC)
            cprev=set13
            continue
        elif c in set14:
            PlaySound(listme3[13],SND_FILENAME|SND_ASYNC)
            cprev=set14
            continue
        elif c in set15:
            PlaySound(listme3[14],SND_FILENAME|SND_ASYNC)
            cprev=set15
            continue
        elif d in dprev:
            continue
        elif d in set1:
            PlaySound(listme4[0],SND_FILENAME|SND_ASYNC)
            dprev=set1
            continue
        elif d in set2:
            PlaySound(listme4[1],SND_FILENAME|SND_ASYNC)
            dprev=set2
            continue
        elif d in set3:
            PlaySound(listme4[2],SND_FILENAME|SND_ASYNC)
            dprev=set3
            continue
        elif d in set4:
            PlaySound(listme4[3],SND_FILENAME|SND_ASYNC)
            dprev=set4
            continue
        elif d in set5:
            PlaySound(listme4[4],SND_FILENAME|SND_ASYNC)
            dprev=set5
            continue
        elif d in set6:
            PlaySound(listme4[5],SND_FILENAME|SND_ASYNC)
            dprev=set6
            continue
        elif d in set7:
            PlaySound(listme4[6],SND_FILENAME|SND_ASYNC)
            dprev=set7
            continue
        elif d in set8:
            PlaySound(listme4[7],SND_FILENAME|SND_ASYNC)
            dprev=set8
            continue
        elif d in set9:
            PlaySound(listme4[8],SND_FILENAME|SND_ASYNC)
            dprev=set9
            continue
        elif d in set10:
            PlaySound(listme4[9],SND_FILENAME|SND_ASYNC)
            dprev=set10
            continue
        elif d in set11:
            PlaySound(listme4[10],SND_FILENAME|SND_ASYNC)
            dprev=set11
            continue
        elif d in set12:
            PlaySound(listme4[11],SND_FILENAME|SND_ASYNC)
            dprev=set12
            continue
        elif d in set13:
            PlaySound(listme4[12],SND_FILENAME|SND_ASYNC)
            dprev=set13
            continue
        elif d in set14:
            PlaySound(listme4[13],SND_FILENAME|SND_ASYNC)
            dprev=set14
            continue
        elif d in set15:
            PlaySound(listme4[14],SND_FILENAME|SND_ASYNC)
            dprev=set15
            continue
        else:
            PlaySound(None,SND_FILENAME|SND_ASYNC)
        
        
        
            

                


        
t1=threading.Thread(target=back_beat,args=('kick-082.wav',))
t2=threading.Thread(target=foreground)



t1.start()
t2.start()

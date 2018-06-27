def teststorage():
 import json,time,os
 m=''
 a=[]
 b=[0,1,2,3,4,5,6,7,8,9,10]
 
 if not os.path.exists('fair.txt'):
   with open('fair.txt','w') as zzil:
     json.dump(a,zzil)

 
 for i in b:
   time.sleep(5)
   if i !=10:
     if os.path.exists('fair.txt'):
       with open('fair.txt','r') as fil:
         a=json.load(fil)
         print(a)

   #else:
    # try:
      # with open('fair.txt','w') as bil:
      #   json.dump(None,bil)
    # except TypeError:
     #  print('no')




if __name__ == "__main__":
    tp=teststorage()

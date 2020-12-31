import Mycode as k 
#importing the main file("code" is the name of the file I have used) as a library 


k.create("sastra",25)
#to create a key with key_name,value given and with no time-to-live property


k.create("src",70,3600) 
#to create a key with key_name,value given and with time-to-live property value given(number of seconds)


k.read("sastra")
#it returns the value of the respective key in Jasonobject format 'key_name:value'


k.read("src")
#it returns the value of the respective key in Jasonobject format if the TIME-TO-LIVE IS NOT EXPIRED else it returns an ERROR


k.create("sastra",50)



k.modify("sastra",55)


 
k.delete("sastra")

t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t2.start()
t2.sleep()

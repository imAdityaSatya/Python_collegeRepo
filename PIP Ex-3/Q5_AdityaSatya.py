'''
Aditya Satya
Ques 5
Write a python program that takes the x – y coordinates of a point in the Cartesian plane and
prints a message telling either an axis on which the point lies or the quadrant in which it is found.
'''

x,y= input("Enter x and y: ").split()
x,y= float(x), float(y)

if(x>0 and y>0):
    print("(",x,",", y,") is in quadrant I")

elif(x<0 and y>0):
    print("(",x,",", y,") is in quadrant II")
		
elif(x<0 and y<0):
    print("(",x,",", y,") is in quadrant III")

elif(x>0 and y<0):
    print("(",x,",", y,") is in quadrant IV")

elif(x==0):
    print ("(",x,",", y,") is on y-axis")

elif(y==0):
    print ("(",x,",", y,") is on x-axis")

else:
    print ("(",x,",", y,") is origin")



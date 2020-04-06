from matplotlib import pyplot as plt

x = [1,2,3,4]
y = [3,3,3,3]

plt.plot(x,y)

plt.title('Light Intensity vs. Kinetic Energy ')
plt.ylabel('Kinetic Energy')
plt.xlabel('Light Intensity')

plt.show()
print("plancks constant =6.6^10-34")
h =6.624*10**-34
c=3*10**8
print("enter frequency ")
f=float(input())
#print("enter kinetic energy")
#k=float(input())
#print("enter wavelength in nm")
#l=float(input())
print("enter mass of body")
m=int(input())
print("enter velocity of paerticle")
v=int(input())
w=-(h*f-0.5*m*v*v)
#w=-((h*c)/(l*10**-9)-k)
print("work function =",w,"ev")
tf=(w*1.6*10**-19)/h
print("threshold frequency=",tf,"Hz")


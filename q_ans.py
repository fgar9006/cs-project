import random

#need to check if the numbers work in the equation
def gen_qa(mode):
    check=True
    while check:
        s=round(random.uniform(-100,-1),2)#-100,100 since it could be positive or negative
        u=round(random.uniform(1,20),2)
        v=round(random.uniform(-20,-1),2)
        a=-9.80
        t=round(random.uniform(1,10),2)

        if s==(u*t)+(0.5*a*t**2):
            if mode.lower()=='s':
                q='The particle is thrown up with initial velocity',u,'ms-1 and travels a displacement of s after',t,'secs. Calculate the displacement.'
                ans=s
                check=False
            if mode.lower()=='u':
                q='The particle is thrown up and travels a displacement of',s,'m after',t,'secs. Calculate the intial velocity.'
                ans=u
                check=False
            if mode.lower()=='t':
                q='The particle is thrown up with initial velocity',u,'ms-1 and travels a displacement of',s,'m. Calculate the time taken.'
                ans=t
                check=False
        elif (v**2)==(u**2)+(2*a*s):
            if mode.lower()=='s':
                q='The particle is thrown up with initial velocity',u,'ms-1 and after a while reaches a velocity of',v,'ms-1. Calculate the displacement.'
                ans=s
                check=False
            if mode.lower()=='u':
                q='The particle is thrown up and travels a displacement of',s,'m where it reaches',v,'ms-1 at that point. Calculate the intial velocity.'
                ans=u
                check=False
            if mode.lower()=='v':
                q='The particle is thrown up with initial velocity',u,'ms-1 and travels a displacement of',s,'m. Calculate the final velocity.'
                ans=v
                check=False
        elif s==((u+v)/2)*t:
            if mode.lower()=='s':
                q='The particle is thrown up with initial velocity',u,'ms-1 and reaches',v,'ms-1 after',t,'secs. Calculate the displacement.'
                ans=s
                check=False
            if mode.lower()=='u':
                q='The particle is thrown up and travels a displacement of',s,'m and has velocity',v,'after',t,'secs. Calculate the intial velocity.'
                ans=u
                check=False
            if mode.lower()=='v':
                q='The particle is thrown up with initial velocity',u,'ms-1 and after',t,'secs has a displacement of',s,'m. Calculate the final velocity.'
                ans=v
                check=False    
            if mode.lower()=='t':
                q='The particle is thrown up with initial velocity',u,'ms-1 and travels a displacement of',s,'m. Calculate the time taken.'
                ans=t
                check=False
    result=" ".join(map(str,q)) #this is to remove the commas and brackets in the question
    return result,ans

def time(start_time,duration_time , day=None):
    t , ampm =start_time.split()
    h1,m1=t.split(":")
    h2,m2=duration_time.split(":")
    hour=int(h1)+int(h2)
    minute=int(m1)+int(m2)
    n=0
    old_dayno=0
    new_dayno=0
    
#12hour clock --> 24hour clock 
    if ampm=="PM":
        hour+=12

#minutes-->hour if minutes>=60
    if minute>=60:
        minute-=60
        hour+=1
        
#counting no. of after days
    if hour>24:
        while hour>=24 :
            n=n+1
            hour-=24
    
    if n==1:
        afterday="(next day)"
    elif n>1:
        afterday="("+str(n)+" days later)"
            
#deciding AM or PM
    if hour>=12 :
        ampm="PM"
    else:
        ampm="AM"
        
#24hour clock --> 12hour clock
    if hour>12:
        hour-=12     
    if hour==0:
        hour=12
    if minute<10:
        s="0"+str(minute)
        minute=s
        
#deciding day of week
    week={1:"Monday", 2:"Tuesday" , 3:"Wednesday" , 4:"Thursday" ,5:"Friday",6:"Saturday",7:"Sunday"}
    for i in week:
        if day.capitalize()==week[i]:
            old_dayno=i
            break
    new_dayno= (old_dayno+n)-7 if (old_dayno+n)>7 else old_dayno+n
    
#output statement
    a=str(hour)+":"+minute+" "+ampm
    answer=a+" "+afterday
    if day!=None:
        answer=a+" ,"+week[new_dayno]+" "+afterday
        
    return answer

print(time("6:03 PM", "205:02" ,"Tuesday" ))
    

#Recovery Triangle

session = True
work = True
family = True
x = "You are in right way"

if session and work and family:
    print(f"Congratulations: {x}")
elif not session:
    print("You are in danger") 
elif session or family:
    print(f"Dont wory just find a job: {x}")    
else:
    print("come back to 12 steps")    
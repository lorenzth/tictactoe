# tic tac toe game

# without design, print x and o.
a1 = "_"
a2 = "_"
a3 = "_"
b1 = "_"
b2 = "_"
b3 = "_"
c1 = "_"
c2 = "_"
c3 = "_"
def grid():
    
    print("   1  2  3")
    print(f"A  {a1}  {a2}  {a3}")
    print(f"B  {b1}  {b2}  {b3}")
    print(f"C  {c1}  {c2}  {c3}")
def find_loc_user():
    loc = input("Choose the location of your X : ")
    loc.lower()
    loc = str(loc)
    if loc == "a1":
        a1 = "X"
    if loc == "a2":
        a2 = "X"
    if loc == "a3":
        a3 = "X"
    if loc == "b1":
        b1 = "X"
    if loc == "b2":
        b2 = "X"
    if loc == "b3":
        b3 = "X"
    if loc == "c1":
        c1 = "X"
    if loc == "c2":
        c2 = "X"
    if loc == "c3":
        c3 = "X"
    print("At the end of the find_loc_user function, a1 is equal to" , a1)
    

ready = input("Are you ready to play Tic Tac Toe with me ? (say yes): ")
ready.lower()
if ready == "yes":
    print("Here is the grid")
    grid()
    while True:   
        find_loc_user()
        print("After the find_loc_user (outside of it) , a1 is equal to", a1)
        grid()

# when I print the grid after having chosen a1, a1 is again equal to _ not X like it was just before
        
        
        

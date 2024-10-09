L1=list(map(int,input("enter the 1stlist of integers(space_sepaatd):").split()))
L2=list(map(int,input("enter the 2ndlist of integers(space_sepaatd):").split()))
if len(L1)==len(L2):
    print("the two lists are same length")
else:
    print("the two lists are not same length")
if sum(L1)==sum(L2):
    print("the two lists sum to the same value")
else:
    print("the two lit sum is not same value")
common_values=set(L1).intersection(set(L2))
if common_values:
    print(f"common values b/w the lists:{common_values}")
else:
    print("no common value b/w the lits")

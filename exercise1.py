def distance_from_zero(value):

     if isinstance(value,int) or isinstance(value,float):
        return abs(value)
     else:
        return("Nope")


print(distance_from_zero(32))
print(distance_from_zero("hi"))

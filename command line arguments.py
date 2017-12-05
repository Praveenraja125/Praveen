def function(a,*b,**c):
    print('a=',a)
    print('type=',type(a))
    print('type=',type(b))
    print('type=',type(c))
    for i in b:
        print('The tuple assignment are=',b)
    for i in c:
        print('The keyword arguments are= ',c)
function(10,"hi,how","are,you",x='xyz',s='string')

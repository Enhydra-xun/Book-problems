def foo(*args,**kwargs):
    print 'args=',kwargs
    print'-------------------------------------'

if __name__ == '_main_':
    foo(1,2,3,4)
    foo(a=1,b=2,c=3)
    foo(1,2,3,4,a=1,b=2,c=3)
    foo('a', 1, None, a=1, b='2', c=3)

        

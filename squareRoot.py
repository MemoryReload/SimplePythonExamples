#coding: utf-8
def sqrt(x,epsilon):
    """
    caculate the square root of x
    :param x:
    :param epsilon:
    :return:
    """
    assert x>=0, "x should be no less than 0"
    if x==0:
        return 0
    assumption= float(x)/2
    counts=0
    while abs(assumption**2-x)>epsilon :
        assumption=(assumption+x/assumption)/2
        counts+=1
    print counts," times search to find the square root."
    return assumption


# input=raw_input("please input a number:")
# result=sqrt(float(input),0.0000001)
# print "the square root of ",input," is ",result

for i in range(0,130,2) :
    result=sqrt(i,0.0000001);
    print "the square root of ",i," is ",result
print "测试中文支持！"


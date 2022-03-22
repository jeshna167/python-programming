import datetime
#print(datetime.date.today())
#print(datetime.datetime.now())
#print(datetime.datetime.now().strftime('%X'))
time=datetime.datetime.now().strftime('%X')
print(time)
def covert12(t1):
    if int(t1[0:2]) == 00 :
        return str(int(t1[0:2])+12)+t1[2:8]+" AM"
    elif int(t1[0:2]) == 12:
        return t1[:]+" PM"
    elif int(t1[0:2]) > 12:
        return str(int(t1 [0:2])-12)+t1[2:8]+' PM'
    else:
        return t1[:]+" AM"
#    print(str(int(t1[0:2])+12)+t1[2:8]+" AM")
 #   print(type (str(int(t1[0:2])+12)+":00:40"))
 #   print(type(int(t1[0:2])+12)+":00:40")
#n=covert12("01:34:50")
n=covert12(time)
print(n)
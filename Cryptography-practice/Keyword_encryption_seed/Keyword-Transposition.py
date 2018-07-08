n = int(input("Please give the number of seeds"))
if n==10:
    n =1
while (n!=0):
    w = input("seed")

    result = []
    for c in w:
        if c not in result:
            result.append(c)
    l = len(result)
    m = l
    a = 65
    while (m!=26):
        while chr(a) in result:
            a+=1
        result.append(chr(a))
        m+=1
    rim = int((26 - 26%l)/l)
    if 26%l == 0:
        kam = rim
    else:
        kam = rim + 1
        for i in range(l - 26%l):
            result.append(" ")
    #print(rim)
    #for i in range(l - 26%l):
        #result.append(" ")
    def swap(i,j):
        #print("i: "+str(i)+" j: "+str(j))
        tmp = result[j]
        result[j]=result[i]
        result[i]=tmp
        
    for i in range(l):
        for j in range(i):
            #print("Result : ",result[0:6])
            #print("Result 2 : ",result[6:12])
            if ord(result[j])>ord(result[i]):
                #print("Kam : ",kam)
                for k in range(kam):
                    swap(i+k*l,j+k*l)
    #print (result)
    otp = []
    e=0
    #print("result=",result)
    while (e!=l):
        #print("rim ",rim)
        for i in range(kam):
            #print(str(i*l+e)+" e = "+str(e))
            otp.append(result[i*l+e])
        e+=1
    otp = [x for x in otp if x != ' ']
    d = {}
    for i in range(26):
        d[otp[i]]=chr(65+i)
    msg = input("Veuillez Taper le message à envoyer(Please type the message to send):")
    res = []
    for i in range(len(msg)):
        if msg[i]!=" ":
            res.append(d[msg[i]])
        else:
            res.append(" ")
    print ("Encrypted case:"+"".join(res))
    n -= 1

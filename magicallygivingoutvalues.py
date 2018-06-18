def parseme(message):
    mess=message.split('\n')
    attrib=[]
    value=[]
    try:
        get,file,http=mess[0].split()
        file=file.strip('/')
    except:
        get="GET"
        file=""
    attrib.append(get)
    value.append(file)
    for i in mess[1:len(mess)-2]:
        splitval=i.split(": ")
        attrib.append(splitval[0])
        value.append(splitval[1].strip('\r'))

    valuesdict=dict(zip(attrib,value))
    return valuesdict

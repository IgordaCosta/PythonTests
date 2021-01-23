def ValueToBytes(ListofValues):

    ListofChars=[ord(x) for x in list(ListofValues)]

    return ListofChars


print(ValueToBytes("body"))

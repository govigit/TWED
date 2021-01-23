def do_decryption(number1, number2):
    alphabet="ab~cdef`gh\ij@k lm#no|pq$rs}tu%vw{xy^z12]3&45[67*890A(BC;DE)FG:HI_JK>LM-NO.PQ+RS<TUV=WX,YZ"
    key=number2
    decrypt=""
    for i in number1:
        position=alphabet.find(i)
        newposition=(position-key)%90
        decrypt+=alphabet[newposition]
    return decrypt
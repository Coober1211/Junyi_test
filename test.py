##test


def inverse_matrix(input_m):
    output_m=[]
    if(type(input_m)==type([1])):
        for i in range(len(input_m)-1,-1,-1):
            if type(input_m[i])!=type([1]):
                output_m.append(input_m[i])
            else:
                sub_m=inverse_matrix(input_m[i])
                output_m.append(sub_m)

        return output_m


def Q_2(number):
    answer=[]
    out=[]
    for i in range(1,number+1):
        if(i % 15==0):
            answer.append(i)
        elif(i % 3==0):
            out.append(i)
        elif(i % 5==0):
            out.append(i)
        else:
            answer.append(i)

    print "out:"+str(out)
    print "left:"+str(answer)
    print len(answer)








if __name__ == '__main__':
    input_m=[1,[12,3,[4,[5,16]]]]  
    output_m=inverse_matrix(input_m)
    print input_m
    print output_m
    input_m=[1,[2,3],[4,[5,6]],7]
    output_m=inverse_matrix(input_m)
    print input_m
    print output_m

    Q_2(15)
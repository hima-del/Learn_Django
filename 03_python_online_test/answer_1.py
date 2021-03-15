def server_cost(d1,m1,y1,d2,m2,y2):
    if d1==d2 and m1==m2 and y1==y2:
        cost = 20
    elif m1==m2:
        cost = 30*(d2-d1)
    elif y1==y2:
        cost = 1000*(m2-m1)
    else:
        cost = 20000
    return cost                 

if __name__=="__main__":
    created_date = str(input("enter the created date"))
    d1m1y1 = created_date.split()
    d1 = int(d1m1y1[0])
    m1 = int(d1m1y1[1])
    y1 = int(d1m1y1[2])

    deleted_date = str(input("enter the deleted date"))
    d2m2y2 = deleted_date.split()
    d2 = int(d2m2y2[0])
    m2 = int(d2m2y2[1])
    y2 = int(d2m2y2[2])

    result = server_cost(d1,m1,y1,d2,m2,y2)
    print(str(result))        
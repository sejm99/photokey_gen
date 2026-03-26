import gdstk

def main(input,layer_no,scale_x,scale_y,thin):
    # 알파벳 & Number Define
    x=float(scale_x)
    y=float(scale_y)
    size=float(thin)
    size_n = float(size/2) #FlexPath 사용을 위함

    if input == "A":
        points = [(size_n,size_n),(size_n,(1*y-size_n)),((1*x-size_n),(1*y-size_n)),((1*x-size_n),size_n)]
        rect1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        points = [(size_n,(0.6*y-size_n)),((1*x-size_n),(0.6*y-size_n))]
        rect2 = gdstk.FlexPath(points,size,joins=["miter"],ends=["flush"])
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "B":
        points = [(size_n,size_n),(size_n,(1*y-size_n)),((0.9*x-size_n),(1*y-size_n)),((1*x-size_n),(0.9*y-size_n)),((1*x-size_n),(0.6*y-size_n)),((0.9*x-size_n),1*y/2),
                  ((1*x-size_n),(0.4*y+size_n)),((1*x-size_n),(0.15*y-size_n)),((0.85*x+size_n),size_n),(size_n,size_n)]
        rect1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        points = [(size_n,(1*y/2)),(0.9*x-size_n,(1*y/2))]
        rect2 = gdstk.FlexPath(points,size,joins=["natural"],ends=["flush"])
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "C":
        points = [(1*x-size_n,size_n),(0.2*x-size_n,size_n),(size_n,0.2*y-size_n),(size_n,0.8*y+size_n),((0.2*x-size_n),(1*y-size_n)),(1*x-size_n,1*y-size_n)]
        step1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["round"],layer=int(layer_no))
        return step1
    elif input == "D":
        points = [(size_n,size_n),(size_n,1*y-size_n),((0.85*x-size_n),(1*y-size_n)),(1*x-size_n,(0.85*y-size_n)),(1*x-size_n,(0.15*y+size_n)),(0.85*x-size_n,size_n),(size_n,size_n)]
        step1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"],layer=int(layer_no))
        return step1
    elif input == "E":
        points = [(1*x-size_n,size_n),(size_n,size_n),(size_n,1*y-size_n),(1*x-size_n,1*y-size_n)]
        rect1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        points = [(size_n,size_n),(size_n,(1*y/2)),(1*x-size_n,(1*y/2))]
        rect2 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "F":
        points = [(size_n,size_n),(size_n,1*y-size_n),(1*x-size_n,1*y-size_n)]
        rect1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        points = [(size_n,size_n),(size_n,(1*y/2)),(1*x-size_n,(1*y/2))]
        rect2 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "G":
        points = [(1*x-size_n,size_n),(0.2*x-size_n,size_n),(size_n,0.2*y-size_n),(size_n,(0.8*y+size_n)),((0.2*x-size_n),(1*y-size_n)),(1*x-size_n,1*y-size_n)]
        rect1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        points = [(1*x/2,1*y/2),(1*x-size_n,(1*y/2)),(1*x-size_n,size_n)]
        rect2 = gdstk.FlexPath(points,size,joins=["natural"],ends=["round"])
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "H":
        points = [(size_n,size_n),(size_n,1*y-size_n)]
        rect1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        points = [(1*x-size_n,1*y-size_n),(1*x-size_n,size_n)]
        rect2 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        points = [(size_n,(1*y/2)),(1*x-size_n,(1*y/2))]
        rect3 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        step2 = gdstk.boolean(rect3,step1,"or",layer=int(layer_no))
        return step2
    elif input == "I":
        points = [(size_n,size_n),(1*x-size_n,size_n)]
        rect1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        points = [(size_n,1*y-size_n),(1*x-size_n,1*y-size_n)]
        rect2 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        points = [((1*x/2),size_n),((1*x/2),1*y-size_n)]
        rect3 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        step2 = gdstk.boolean(rect3,step1,"or",layer=int(layer_no))
        return step2
    elif input == "J":
        points = [(size_n,1*y-size_n),(1*x-size_n,1*y-size_n)]
        rect1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        points = [(size_n,size_n),(0.5*x-size_n,size_n),((0.7*x-size_n),(0.2*y+size_n)),((1*x*0.7-size_n),1*y-size_n)]
        rect2 = gdstk.FlexPath(points,size,joins=["natural"],ends=["flush"])
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "K":
        points = [(size_n,1*y-size_n),(size_n,size_n)] 
        rect1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        points = [(size_n,(1*y/2)),((1*x/2),(1*y/2)),((1*x-size_n),(1*y-size_n))]
        rect2 = gdstk.FlexPath(points,size,joins=["natural"],ends=["flush"])                   
        points = [(size_n,(1*y/2)),((1*x/2),(1*y/2)),((1*x-size_n),size_n)]
        rect3 = gdstk.FlexPath(points,size,joins=["natural"],ends=["flush"])
        step1 = gdstk.boolean(rect2,rect3,"or",layer=int(layer_no))
        step2 = gdstk.boolean(rect1,step1,"or",layer=int(layer_no))
        return step2
    elif input == "L":
        points = [(size_n,1*y-size_n),(size_n,size_n),(1*x-size_n,size_n)]
        step1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"],layer=int(layer_no))
        return step1
    elif input == "M":
        points = [(size_n,size_n),(size_n,(1*y-size_n)),((0.2*x-size_n),(1*y-size_n)),((1*x/2),(0.7*y-size_n)),
                  ((0.8*x+size_n),(1*y-size_n)),((1*x-size_n),(1*y-size_n)),((1*x-size_n),size_n)] 
        step1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"],layer=int(layer_no))
        return step1
    elif input == "N":
        points = [(size_n,size_n),(size_n,(1*y-size_n)),((0.1*x-size_n),(1*y-size_n)),((0.9*x+size_n),size_n),((1*x-size_n),size_n),((1*x-size_n),(1*y-size_n))]
        step1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"],layer=int(layer_no))
        return step1
    elif input == "O":
        points = [(size_n,size_n),(size_n,1*y-size_n),(1*x-size_n,1*y-size_n),(1*x-size_n,size_n),(size_n,size_n)]
        step1 = gdstk.FlexPath(points,size,joins=["round"],ends=["round"],layer=int(layer_no))
        return step1
    elif input == "P":
        points = [(size_n,size_n),(size_n,1*y-size_n),(1*x-size_n,1*y-size_n),((1*x-size_n),(1*y/2)),(size_n,(1*y/2))]
        step1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"],layer=int(layer_no))
        return step1
    elif input == "Q":
        points = [(size_n,(0.2*y-size_n)),(size_n,(0.8*y+size_n)),((0.2*x-size_n),(1*y-size_n)),((0.8*x+size_n),(1*y-size_n)),
                  ((1*x-size_n),(0.8*y+size_n)),((1*x-size_n),(0.2*y-size_n)),((0.8*x+size_n),size_n),((0.2*x-size_n),size_n),(size_n,(0.2*y-size_n))]
        rect1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["round"])
        points = [((1*x-size_n),size_n),((0.7*x-size_n),(0.3*y+size_n))]
        rect2 = gdstk.FlexPath(points,size,joins=["natural"],ends=["round"])
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "R":
        points = [(size_n,size_n),(size_n,(1*y-size_n)),((0.9*x-size_n),(1*y-size_n)),((1*x-size_n),(0.9*y-size_n)),((1*x-size_n),(0.6*y-size_n)),((0.9*x-size_n),1*y/2),
                  ((1*x-size_n),(0.4*y+size_n)),((1*x-size_n),size_n)]
        rect1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        points = [(size_n,(1*y/2)),(0.9*x-size_n,(1*y/2))]
        rect2 = gdstk.FlexPath(points,size,joins=["natural"],ends=["flush"])
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "S":
        points = [((1*x-size_n),(0.7*y+size_n)),((1*x-size_n),(0.9*y-size_n)),((0.9*x-size_n),(1*y-size_n)),((0.1*x+size_n),(1*y-size_n)),(size_n,(0.9*y-size_n)),(size_n,(0.6*y-size_n)),
                  ((0.1*x+size_n),(1*y/2)),((0.9*x-size_n),(1*y/2)),((1*x-size_n),(0.4*y+size_n)),((1*x-size_n),(0.1*y+size_n)),((0.9*x-size_n),size_n),((0.1*x+size_n),size_n),
                  (size_n,(0.1*y+size_n)),(size_n,(0.3*y-size_n))]
        step1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["flush"],layer=int(layer_no))
        return step1
    elif input == "T":
        points = [(size_n,(1*y-size_n)),((1*x-size_n),(1*y-size_n))]
        rect1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        points = [((1*x/2),size_n),((1*x/2),1*y-size_n)]
        rect2 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "U":
        points = [(size_n,(1*y-size_n)),(size_n,(0.1*y-size_n)),((0.1*x-size_n),size_n),((0.9*x+size_n),size_n),((1*x-size_n),(0.1*y-size_n)),((1*x-size_n),(1*y-size_n))]
        step1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"],layer=int(layer_no))
        return step1
    elif input == "V":
        points = [(size_n,(1*y-size_n)),(size_n,(1*y/2-size_n)),((1*x/2-size_n),size_n),((1*x/2+size_n),size_n),((1*x-size_n),(1*y/2-size_n)),((1*x-size_n),(1*y-size_n))]
        step1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"],layer=int(layer_no))
        return step1
    elif input == "W":
        points = [(size_n,(1*y-size_n)),(size_n,(0.3*y-size_n)),((0.3*x-size_n),size_n),((1*x/2),(0.4*y+size_n)),((0.7*x+size_n),size_n),((1*x-size_n),(0.3*y-size_n)),((1*x-size_n),(1*y-size_n))]
        step1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"],layer=int(layer_no))
        return step1
    elif input == "X":
        points = [(size_n,(1*y-size_n)),((1*x-size_n),(size_n))]
        rect1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        points = [((1*x-size_n),(1*y-size_n)),(size_n,size_n)]
        rect2 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "Y":
        points = [(size_n,(1*y-size_n)),((0.1*x-size_n),(1*y-size_n)),(1*x/2,(0.7*y-size_n)),(1*x/2,size_n)]
        rect1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        points = [((1*x-size_n),(1*y-size_n)),((0.9*x+size_n),(1*y-size_n)),(1*x/2,(0.7*y-size_n)),(1*x/2,size_n)]
        rect2 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "Z":
        points = [(size_n,(1*y-size_n)),((1*x-size_n),(1*y-size_n)),((1*x-size_n),(0.9*y-size_n)),(size_n,(0.1*y+size_n)),(size_n,size_n),((1*x-size_n),size_n)]
        step1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"],layer=int(layer_no))
        return step1
    elif input == "0":
        points = [(size_n,(0.2*y-size_n)),(size_n,(0.8*y+size_n)),((0.2*x-size_n),(1*y-size_n)),((0.8*x+size_n),(1*y-size_n)),
                  ((1*x-size_n),(0.8*y+size_n)),((1*x-size_n),(0.2*y-size_n)),((0.8*x+size_n),size_n),((0.2*x-size_n),size_n),(size_n,(0.2*y-size_n))]
        step1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["round"],layer=int(layer_no))
        return step1
    elif input == "1":
        points = [(size_n,(1*y-size_n)),((0.6*x-size_n),(1*y-size_n)),((0.6*x-size_n),size_n)]
        rect1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        points = [(size_n,size_n),(1*x-size_n,size_n)]
        rect2 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "2":
        points = [(size_n,(1*y-size_n)),((1*x-size_n),(1*y-size_n)),((1*x-size_n),(1*y/2)),(size_n,(1*y/2))]
        rect1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        points = [(size_n,(1*y/2)),(size_n,size_n),((1*x-size_n),size_n)]
        rect2 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "3":
        points = [(size_n,(1*y-size_n)),((1*x-size_n),(1*y-size_n)),((1*x-size_n),(size_n)),(size_n,size_n)]
        rect1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        points = [(size_n,(1*y/2)),((1*x-size_n),(1*y/2))]
        rect2 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "4":
        points = [(size_n,(1*y-size_n)),(size_n,(0.3*y-size_n)),((1*x-size_n),(0.3*y-size_n))]
        rect1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        points = [((1*x-size_n),(1*y-size_n)),((1*x-size_n),size_n)]
        rect2 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "5":
        points = [((1*x-size_n),(1*y-size_n)),(size_n,(1*y-size_n)),(size_n,(1*y/2)),((1*x-size_n),(1*y/2))]
        rect1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        points = [((1*x-size_n),(1*y/2)),((1*x-size_n),size_n),(size_n,size_n)]
        rect2 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "6":
        points = [((1*x-size_n),(1*y-size_n)),(size_n,(1*y-size_n)),(size_n,size_n),((1*x-size_n),size_n),((1*x-size_n),(1*y/2)),(size_n,(1*y/2))]
        step1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"],layer=int(layer_no))
        return step1
    elif input == "7":
        points = [(size_n,(1*y-size_n)),((1*x-size_n),(1*y-size_n)),((1*x-size_n),size_n)]
        step1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"],layer=int(layer_no))
        return step1
    elif input == "8":
        points = [(size_n,(1*y-size_n)),(size_n,size_n),((1*x-size_n),size_n),((1*x-size_n),(1*y-size_n)),(size_n,(1*y-size_n))]
        rect1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        points = [(size_n,(1*y/2)),((1*x-size_n),(1*y/2))]
        rect2 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "9":
        points = [(size_n,(1*y/2)),(size_n,(1*y-size_n)),((1*x-size_n),(1*y-size_n)),((1*x-size_n),size_n),(size_n,size_n)]
        rect1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        points = [(size_n,(1*y/2)),((1*x-size_n),(1*y/2))]
        rect2 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1

if __name__ == "__main__":
    main()
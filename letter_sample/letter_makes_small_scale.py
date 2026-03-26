import gdstk

def Make_thin_letter(input,layer_no,scale_x,scale_y,thin):
    # 알파벳 & Number Define
    x=float(scale_x)
    y=float(scale_y)
    size=float(thin)
    size_n = float(size/2) #path 사용을 위해 n/2 설정!!

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
        points = [(1*x-size_n,size_n),(0.2*x-size_n,size_n),(size_n,0.2*y-size_n),(size_n,0.8*y-size_n),((0.2*x-size_n),(1*y-size_n)),(1*x-size_n,1*y-size_n)]
        step1 = gdstk.FlexPath(points,size,joins=["bevel"],ends=["round"],layer=int(layer_no))
        return step1
    elif input == "D":
        points = [(size_n,size_n),(size_n,1*y-size_n),((0.85*x-size_n),(1*y-size_n)),(1*x-size_n,(0.85*y-size_n)),(1*x-size_n,(0.15*y-size_n)),(0.85*x-size_n,size_n),(size_n,size_n)]
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
        points = [(1*x-size_n,size_n),(0.2*x-size_n,size_n),(size_n,0.2*y-size_n),(size_n,(0.8*y-size_n)),((0.2*x-size_n),(1*y-size_n)),(1*x-size_n,1*y-size_n)]
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
        points = [(size_n,size_n),(0.5*x-size_n,size_n),((0.7*x-size_n),(0.2*y-size_n)),((1*x*0.7-size_n),1*y-size_n)]
        rect2 = gdstk.FlexPath(points,size,joins=["natural"],ends=["flush"])
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "K":
        points = [(size_n,size_n),(size_n,1*y-size_n)] 
        rect1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["flush"])
        points = [(size_n,(1*y/2-size_n)),((0.5*x-size_n),(1*y/2-size_n)),((1*x-size_n),(1*y-size_n))]
        rect2 = gdstk.FlexPath(points,size,joins=["natural"],ends=["flush"])                   
        points = [(size_n,(1*y/2-size_n)),((0.5*x-size_n),(1*y/2-size_n)),((1*x-size_n),size_n)]
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
        points = [(size_n,size_n),(size_n,(1*y-size_n)),((0.1*x-size_n),(1*y-size_n)),((1*x-size_n),size_n),((1*x-size_n),(1*y-size_n))]
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
        points = [((0.2*x-size_n),size_n),(size_n,(0.8*y-size_n)),((0.2*x-size_n),(1*y-size_n)),((0.8*x-size_n),(1*y-size_n)),
                  ((1*x-size_n),(0.8*y-size_n)),((1*x-size_n),(0.2*y-size_n)),((0.8*x-size_n),size_n),((0.2*x-size_n),size_n)]
        rect1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["flush"])
        points = [((0.2*x-size_n),size_n),(size_n,(0.8*y-size_n)),((0.2*x-size_n),(1*y-size_n))] 
        rect2 = gdstk.FlexPath(points,size,joins=["natural"],ends=["flush"])   
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
        points = [(size_n,(0.3*y-size_n)),(size_n,(0.1*y+size_n)),((0.1*x+size_n),size_n),((0.9*x-size_n),size_n),((1*x-size_n),(0.1*y+size_n)),((1*x-size_n),(1*y/2)),((0.9*x-size_n),(1*y/2)),(size_n,(1*y/2))]
        rect1 = gdstk.FlexPath(points,size,joins=["bevel"],ends=["flush"])
        points = [((1*x-size_n),(1*y/2)),((0.1*x+size_n),(1*y/2)),(size_n,(1*y/2)),(size_n,(0.9*y-size_n)),((0.1*x+size_n),(1*y-size_n)),((0.9*x-size_n),(1*y-size_n)),((1*x-size_n),(0.9*y-size_n)),((1*x-size_n),(0.7*y+size_n))]
        rect2 = gdstk.FlexPath(points,size,joins=["bevel"],ends=["flush"])
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1 
    elif input == "T":
        points = [(size_n,(1*y-size_n)),((1*x-size_n),(1*y-size_n))]
        rect1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        points = [((1*x/2),size_n),((1*x/2),1*y-size_n)]
        rect2 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"])
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "U":
        points = [(size_n,(1*y-size_n)),(size_n,size_n),((1*x-size_n),size_n),((1*x-size_n),(1*y-size_n))]
        step1 = gdstk.FlexPath(points,size,joins=["bevel"],ends=["extended"],layer=int(layer_no))
        return step1
    elif input == "V":
        points = [(size_n,(1*y-size_n)),(size_n,(0.4*y+size_n)),((0.4*x-size_n),size_n),((0.6*x+size_n),size_n),((1*x-size_n),(0.4*y+size_n)),((1*x-size_n),(1*y-size_n))]
        step1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["extended"],layer=int(layer_no))
        return step1
    elif input == "W":
        points = [(size_n,(1*y-size_n)),(size_n,(0.2*y+size_n)),((0.2*x-size_n),size_n),((1*x/2),(0.3*y-size_n)),((0.8*x+size_n),size_n),((1*x-size_n),(0.2*y+size_n)),((1*x-size_n),(1*y-size_n))]
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

def main():
    lib = gdstk.Library()
    result = gdstk.Cell("TEST")
    let_1 = gdstk.Cell("let_1_text")
    let_2 = gdstk.Cell("let_2_text")
    pre_result = gdstk.Cell("cell_name")
    # Letter Input Information
    Layer_name = "89"
    layer_no = "3"
    boundary = "10"
    etch_type = "T"
    # Make_letter(글자1,layer_no,size_x,size_y,thin_size)
    polygons = Make_thin_letter(Layer_name[0],int(layer_no),7,7,0.5)
    try:
        let_1.add(*polygons)
    except:
        let_1.add(polygons)
    # 글자1 대한 배치
    pre_result.add(gdstk.Reference(let_1,(0,0)))

    #Make_letter(글자2,layer_no,size_x,size_y,thin_size)
    polygons = Make_thin_letter(Layer_name[1],int(layer_no),7,7,0.5)
    try:
        let_2.add(*polygons)
    except:
        let_2.add(polygons)
    # 글자2 대한 배치 : 글자1 + 여백2 만큼 공백
    pre_result.add(gdstk.Reference(let_2,(int(boundary)+2,0)))
    # 임의 overlay textbox boundary
    rect = gdstk.rectangle((0,0),(20,10))
    if etch_type == "M":
        text_1 = gdstk.boolean(rect,gdstk.Reference(pre_result),"not",layer=int(layer_no))
    else:
        text_1 = gdstk.boolean(rect,gdstk.Reference(pre_result),"and",layer=int(layer_no))
    try:
        result.add(*text_1)
    except:
        result.add(text_1)

    lib.add(result)
    lib.write_gds("./letter7.gds")

if __name__ == "__main__":
    main()
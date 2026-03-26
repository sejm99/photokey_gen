import gdstk

def Make_letter(input,layer_no,scale_x,scale_y):
    #알파벳 만들기
    x=float(scale_x)
    y=float(scale_y)
    if input == "A":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.3*x,0.6*y),(0.7*x,0.8*y))
        rect3 = gdstk.rectangle((0.3*x,0),(0.7*x,0.4*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "B":
        points = [(0,0),(0,1*y),(0.9*x,1*y),(1*x,0.9*y),(1*x,0.6*y),(0.9*x,0.5*y),(1*x,0.4*y),(1*x,0.1*y),(0.9*x,0),(0,0)]
        rect1 = gdstk.Polygon(points)
        rect2 = gdstk.rectangle((0.2*x,0.2*y),(0.8*x,0.4*y))
        rect3 = gdstk.rectangle((0.2*x,0.6*y),(0.8*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "C":
        points = [(0,0.2*y),(0,0.8*y),(0.2*x,1*y),(0.9*x,1*y),(1*x,0.9*y),(1*x,0.8*y),(0.9*x,0.7*y),(0.4*x,0.7*y),(0.3*x,0.6*y),(0.3*x,0.4*y),(0.4*x,0.3*y),(0.9*x,0.3*y),(1*x,0.2*y),(1*x,0.1*y),(0.9*x,0),(0.2*x,0),(0,0.2*y)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "D":
        points = [(0,0),(0,1*y),(0.8*x,1*y),(1*x,0.8*y),(1*x,0.2*y),(0.8*x,0),(0,0)]
        rect1 = gdstk.Polygon(points)
        points = [(0.2*x,0.2*y),(0.2*x,0.8*y),(0.7*x,0.8*y),(0.8*x,0.7*y),(0.8*x,0.3*y),(0.7*x,0.2*y),(0.2*x,0.2*y)]
        rect2 = gdstk.Polygon(points)
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "E":
        points = [(0,0),(0,1*y),(1*x,1*y),(1*x,0.8*y),(0.3*x,0.8*y),(0.3*x,0.6*y),(1*x,0.6*y),(1*x,0.4*y),(0.3*x,0.4*y),(0.3*x,0.2*y),(1*x,0.2*y),(1*x,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "F":
        points = [(0,0),(0,1*y),(1*x,1*y),(1*x,0.8*y),(0.3*x,0.8*y),(0.3*x,0.6*y),(1*x,0.6*y),(1*x,0.4*y),(0.3*x,0.4*y),(0.3*x,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "G":
        points = [(0,0),(0,1*y),(1*x,1*y),(1*x,0.8*y),(0.3*x,0.8*y),(0.3*x,0.2*y),(0.8*x,0.2*y),(0.8*x,0.4*y),(0.5*x,0.4*y),(0.5*x,0.6*y),(1*x,0.6*y),(1*x,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "H":
        points = [(0,0),(0,1*y),(0.3*x,1*y),(0.3*x,6.5),(0.7*x,6.5),(0.7*x,1*y),(1*x,1*y),(1*x,0),(0.7*x,0),(0.7*x,3.5),(0.3*x,3.5),(0.3*x,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "I":
        points = [(0,0),(0,0.2*y),(3.5,0.2*y),(3.5,0.8*y),(0,0.8*y),(0,1*y),(1*x,1*y),(1*x,0.8*y),(6.5,0.8*y),(6.5,0.2*y),(1*x,0.2*y),(1*x,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "J":
        points = [(0,0.8*y),(0,1*y),(1*x,1*y),(1*x,0.8*y),(0.9*x,0.8*y),(0.9*x,0.1*y),(0.8*x,0),(0.2*x,0),(0.1*x,0.1*y),(0.1*x,0.5*y),(0.3*x,0.5*y),(0.3*x,0.2*y),(0.7*x,0.2*y),(0.7*x,0.8*y),(0,0.8*y)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "K":
        points = [(0,0),(0,1*y),(0.3*x,1*y),(0.3*x,0.6*y),(0.7*x,1*y),(1*x,1*y),(0.9*x,0.9*y),(0.5*x,0.5*y),(0.9*x,0.1*y),(1*x,0),(0.7*x,0),(0.3*x,0.4*y),(0.3*x,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "L":
        points = [(0,0),(0,1*y),(0.3*x,1*y),(0.3*x,0.3*y),(1*x,0.3*y),(1*x,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "M":
        points = [(0,0),(0,1*y),(0.2*x,1*y),(0.45*x,0.65*y),(0.55*x,0.65*y),(0.8*x,1*y),(1*x,1*y),(1*x,0),(0.8*x,0),(0.8*x,0.7*y),(0.55*x,0.4*y),(0.45*x,0.4*y),(0.2*x,0.7*y),(0.2*x,0.2*y),(0.2*x,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "N":
        points = [(0,0),(0,1*y),(0.2*x,1*y),(0.8*x,0.3*y),(0.8*x,1*y),(1*x,1*y),(1*x,0),(0.8*x,0),(0.2*x,0.7*y),(0.2*x,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "O":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.2*x,0.2*y),(0.8*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "P":
        points = [(0,0),(0,1*y),(1*x,1*y),(1*x,0.4*y),(0.2*x,0.4*y),(0.2*x,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        rect2 = gdstk.rectangle((0.2*x,0.6*y),(0.8*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "Q":
        rect1 = gdstk.rectangle((0,0.1*y),(0.9*x,1*y))
        rect2 = gdstk.rectangle((0.2*x,0.3*y),(0.7*x,0.8*y))
        points = [(0.4*x,0.6*y),(0.6*x,0.6*y),(1*x,0.1*y),(1*x,0),(0.9*x,0),(0.4*x,0.6*y)]
        rect3 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"or",layer=int(layer_no))
        return step2
    elif input == "R":
        points = [(0,0),(0,1*y),(1*x,1*y),(1*x,0.4*y),(0.2*x,0.4*y),(0.2*x,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        rect2 = gdstk.rectangle((0.2*x,0.6*y),(0.8*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        points = [(0.8*x,0),(0.3*x,0.4*y),(0.6*x,0.4*y),(1*x,0.1*y),(1*x,0),(0.8*x,0)]
        rect3 = gdstk.Polygon(points,layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"or",layer=int(layer_no))
        return step2
    elif input == "S":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0,0.2*y),(0.8*x,0.4*y))
        rect3 = gdstk.rectangle((0.2*x,0.6*y),(1*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "T":
        rect1 = gdstk.rectangle((0,0.7*y),(1*x,1*y))
        rect2 = gdstk.rectangle((3.5,0),(6.5,1*y))
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "U":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.3*x,0.3*y),(0.7*x,1*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "V":
        points = [(0.4*x,0),(0,0.3*y),(0,1*y),(1*x,1*y),(1*x,0.3*y),(0.6*x,0),(0.4*x,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        rect2 = gdstk.rectangle((0.3*x,0.4*y),(0.7*x,1*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "W":
        points = [(0,1*y),(0.2*x,1*y),(0.3*x,0.3*y),(0.4*x,1*y),(0.6*x,1*y),(0.7*x,0.3*y),(0.8*x,1*y),(1*x,1*y),(0.8*x,0),(0.6*x,0),(0.5*x,0.7*y),(0.4*x,0),(0.2*x,0),(0,1*y)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "X":
        points = [(0,1*y),(0.3*x,1*y),(1*x,0),(0.7*x,0),(0,1*y)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        points = [(0,0),(0.7*x,1*y),(1*x,1*y),(0.3*x,0),(0,0)]
        rect2 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "Y":
        points = [(0,1*y),(0.3*x,1*y),(0.5*x,0.6*y),(0.7*x,1*y),(1*x,1*y),(0.65*x,0.4*y),(0.65*x,0),(0.35*x,0),(0.35*x,0.4*y),(0,1*y)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "Z":
        points = [(0,1*y),(1*x,1*y),(1*x,0.8*y),(0.3*x,0.2*y),(1*x,0.2*y),(1*x,0),(0,0),(0,0.2*y),(0.7*x,0.8*y),(0,0.8*y),(0,1*y)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "0":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.2*x,0.2*y),(0.8*x,0.8*y))
        points = [(0.1*x,0),(0,0),(0,0.1*y),(0.9*x,1*y),(1*x,1*y),(1*x,0.9*y),(0.1*x,0)]
        rect3 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"or",layer=int(layer_no))
        return step2
    elif input == "1":
        points = [(0.1*x,0),(0.1*x,0.2*y),(0.4*x,0.2*y),(0.4*x,0.7*y),(0.2*x,0.7*y),(0.2*x,0.9*y),(0.4*x,0.9*y),(0.4*x,1*y),(0.7*x,1*y),(0.7*x,0.2*y),(0.9*x,0.2*y),(0.9*x,0),(0.1*x,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "2":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0,0.6*y),(0.8*x,0.8*y))
        rect3 = gdstk.rectangle((0.2*x,0.2*y),(1*x,0.4*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "3":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0,0.6*y),(0.8*x,0.8*y))
        rect3 = gdstk.rectangle((0,0.2*y),(0.8*x,0.4*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "4":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0,0),(0.7*x,0.3*y))
        rect3 = gdstk.rectangle((0.3*x,0.6*y),(0.7*x,1*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "5":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0,0.2*y),(0.8*x,0.4*y))
        rect3 = gdstk.rectangle((0.2*x,0.6*y),(1*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "6":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.2*x,0.2*y),(0.8*x,0.4*y))
        rect3 = gdstk.rectangle((0.2*x,0.6*y),(1*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "7":
        points = [(0,0.6*y),(0,1*y),(1*x,1*y),(1*x,0),(0.8*x,0),(0.8*x,0.8*y),(0.2*x,0.8*y),(0.2*x,0.6*y),(0,0.6*y)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "8":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.2*x,0.2*y),(0.8*x,0.4*y))
        rect3 = gdstk.rectangle((0.2*x,0.6*y),(0.8*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "9":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0,0),(0.8*x,0.4*y))
        rect3 = gdstk.rectangle((0.2*x,0.6*y),(0.8*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2

def main():
    lib = gdstk.Library()
    result = gdstk.Cell("TEST")
    let_1 = gdstk.Cell("let_1_text")
    let_2 = gdstk.Cell("let_2_text")
    pre_result = gdstk.Cell("cell_name")
    # input
    Layer_name = "GJ"
    layer_no = "3"
    boundary = "10"
    etch_type = "T"
    # Make_letter(글씨,layer_no,size_x,size_y)
    polygons = Make_letter(Layer_name[0],int(layer_no),7,7)
    try:
        let_1.add(*polygons)
    except:
        let_1.add(polygons)
    pre_result.add(gdstk.Reference(let_1,(0,0)))
    polygons = Make_letter(Layer_name[1],int(layer_no),7,7)
    try:
        let_2.add(*polygons)
    except:
        let_2.add(polygons)
    # 입력한 boundary +2 만큼 간격 두고 글씨2 작성
    pre_result.add(gdstk.Reference(let_2,(int(boundary)+2,0)))
    # 임의로 잡은 boundary
    rect = gdstk.rectangle((-5, -5),(25,15))
    if etch_type == "M":
        text_1 = gdstk.boolean(rect,gdstk.Reference(pre_result),"not",layer=int(layer_no))
    else:
        text_1 = gdstk.boolean(rect,gdstk.Reference(pre_result),"and",layer=int(layer_no))
    try:
        result.add(*text_1)
    except:
        result.add(text_1)

    lib.add(result)
    lib.write_gds("./letter_test.gds")

if __name__ == "__main__":
    main()
    
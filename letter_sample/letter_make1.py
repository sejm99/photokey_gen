import gdstk

def Make_letter(input,layer_no):
    #알파벳 만들기
    if input == "A":
        rect1 = gdstk.rectangle((0,0),(7,7))
        rect2 = gdstk.rectangle((2.1,4.2),(4.9,5.6))
        rect3 = gdstk.rectangle((2.1,0),(4.9,2.8))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "B":
        points = [(0,0),(0,7),(5.6,7),(7,5.6),(7,4.2),(6.3,3.5),(7.0,2.8),(7.0,1.4),(5.6,0),(0,0)]
        rect1 = gdstk.Polygon(points)
        rect2 = gdstk.rectangle((2.1,1.4),(4.9,2.8))
        rect3 = gdstk.rectangle((2.1,4.1),(4.9,5.6))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "C":
        points = [(0,2),(0,8),(2,10),(9,10),(10,9),(10,8),(9,7),(4,7),(3,6),(3,4),(4,3),(9,3),(10,2),(10,1),(9,0),(2,0),(0,2)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "D":
        points = [(0,0),(0,7),(5.6,7),(7,5.6),(7,1.4),(5.6,0),(0,0)]
        rect1 = gdstk.Polygon(points)
        rect2 = gdstk.rectangle((2.1,1.4),(4.9,5.6))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "E":
        points = [(0,0),(0,10),(10,10),(10,8),(3,8),(3,6),(10,6),(10,4),(3,4),(3,2),(10,2),(10,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "F":
        points = [(0,0),(0,10),(10,10),(10,8),(3,8),(3,6),(10,6),(10,4),(3,4),(3,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "G":
        points = [(0,0),(0,10),(10,10),(10,8),(3,8),(3,2),(8,2),(8,4),(5,4),(5,6),(10,6),(10,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "H":
        points = [(0,0),(0,10),(3,10),(3,6.5),(7,6.5),(7,10),(10,10),(10,0),(7,0),(7,3.5),(3,3.5),(3,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "I":
        points = [(0,0),(0,2),(3.5,2),(3.5,8),(0,8),(0,10),(10,10),(10,8),(6.5,8),(6.5,2),(10,2),(10,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "J":
        points = [(0,8),(0,10),(10,10),(10,8),(9,8),(9,1),(8,0),(2,0),(1,1),(1,5),(3,5),(3,2),(7,2),(7,8),(0,8)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "K":
        points = [(0,0),(0,7),(2.1,7),(2.1,4.2),(3.15,4.2),(5.95,7),(7,7),(7,5.6),(4.9,3.5),(4.9,3.15),(7,1.05),(7,0),(5.6,0),(3.15,2.45),(2.1,2.45),(2.1,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "L":
        points = [(0,0),(0,10),(3,10),(3,3),(10,3),(10,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "M":
        points = [(0,0),(0,10),(2,10),(4.5,6.5),(5.5,6.5),(8,10),(10,10),(10,0),(8,0),(8,7),(5.5,4),(4.5,4),(2,7),(2,2),(2,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "N":
        points = [(0,0),(0,10),(2,10),(8,3),(8,10),(10,10),(10,0),(8,0),(2,7),(2,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "O":
        rect1 = gdstk.rectangle((0,0),(10,10))
        rect2 = gdstk.rectangle((2,2),(8,8))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "P":
        points = [(0,0),(0,10),(10,10),(10,4),(2,4),(2,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        rect2 = gdstk.rectangle((2,6),(8,8))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "Q":
        rect1 = gdstk.rectangle((0,1),(9,10))
        rect2 = gdstk.rectangle((2,3),(7,8))
        points = [(4,6),(6,6),(10,1),(10,0),(9,0),(4,6)]
        rect3 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"or",layer=int(layer_no))
        return step2
    elif input == "R":
        points = [(0,0),(0,10),(10,10),(10,4),(2,4),(2,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        rect2 = gdstk.rectangle((2,6),(8,8))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        points = [(8,0),(3,4),(6,4),(10,1),(10,0),(8,0)]
        rect3 = gdstk.Polygon(points,layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"or",layer=int(layer_no))
        return step2
    elif input == "S":
        points = [(1.4,0),(5.6,0),(7,1.4),(7,2.8),(4.9,2.8),(4.9,1.4),(2.1,1.4),(2.1,2.1),(0,2.1),(0,1.4),(1.4,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        points = [(7,2.8),(5.6,4.2),(2.1,4.2),(2.1,5.6),(4.9,5.6),(4.9,4.9),(7,4.9),(7,5.6),(5.6,7),(1.4,7),(0,5.6),(0,4.2),(1.4,2.8),(4.9,2.8),(7,2.8)]
        rect2 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "T":
        rect1 = gdstk.rectangle((0,5.18),(7,7))
        rect2 = gdstk.rectangle((2.45,0),(4.55,5.18))
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "U":
        rect1 = gdstk.rectangle((0,0),(10,10))
        rect2 = gdstk.rectangle((3,3),(7,10))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "V":
        points = [(0,7),(2.1,7),(2.1,3.08),(3.08,2.1),(3.92,2.1),(4.9,3.08),(4.9,7),(7,7),(7,2.24),(4.76,0),(2.24,0),(0,2.24),(0,7)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "W":
        points = [(0,7),(2.1,7),(2.1,3.36),(2.52,3.36),(3.29,4.13),(3.71,4.13),(4.48,3.36),(4.9,3.36),(4.9,7),(7,7),(7,1.4),(5.6,0),(5.25,0),(3.71,1.54),(3.29,1.54),(1.75,0),(1.4,0),(0,1.4),(0,7)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "X":
        points = [(0,10),(3,10),(10,0),(7,0),(0,10)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        points = [(0,0),(7,10),(10,10),(3,0),(0,0)]
        rect2 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "Y":
        points = [(0,10),(3,10),(5,6),(7,10),(10,10),(6.5,4),(6.5,0),(3.5,0),(3.5,4),(0,10)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "Z":
        points = [(0,10),(10,10),(10,8),(3,2),(10,2),(10,0),(0,0),(0,2),(7,8),(0,8),(0,10)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "0":
        rect1 = gdstk.rectangle((0,0),(10,10))
        rect2 = gdstk.rectangle((2,2),(8,8))
        points = [(1,0),(0,0),(0,1),(9,10),(10,10),(10,9),(1,0)]
        rect3 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"or",layer=int(layer_no))
        return step2
    elif input == "1":
        points = [(1,0),(1,2),(4,2),(4,7),(2,7),(2,9),(4,9),(4,10),(7,10),(7,2),(9,2),(9,0),(1,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "2":
        rect1 = gdstk.rectangle((0,0),(10,10))
        rect2 = gdstk.rectangle((0,6),(8,8))
        rect3 = gdstk.rectangle((2,2),(10,4))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "3":
        rect1 = gdstk.rectangle((0,0),(10,10))
        rect2 = gdstk.rectangle((0,6),(8,8))
        rect3 = gdstk.rectangle((0,2),(8,4))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "4":
        rect1 = gdstk.rectangle((0,0),(10,10))
        rect2 = gdstk.rectangle((0,0),(7,3))
        rect3 = gdstk.rectangle((3,6),(7,10))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "5":
        rect1 = gdstk.rectangle((0,0),(10,10))
        rect2 = gdstk.rectangle((0,2),(8,4))
        rect3 = gdstk.rectangle((2,6),(10,8))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "6":
        rect1 = gdstk.rectangle((0,0),(10,10))
        rect2 = gdstk.rectangle((2,2),(8,4))
        rect3 = gdstk.rectangle((2,6),(10,8))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "7":
        points = [(0,6),(0,10),(10,10),(10,0),(8,0),(8,8),(2,8),(2,6),(0,6)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "8":
        rect1 = gdstk.rectangle((0,0),(10,10))
        rect2 = gdstk.rectangle((2,2),(8,4))
        rect3 = gdstk.rectangle((2,6),(8,8))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "9":
        rect1 = gdstk.rectangle((0,0),(10,10))
        rect2 = gdstk.rectangle((0,0),(8,4))
        rect3 = gdstk.rectangle((2,6),(8,8))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2

def main():
    lib = gdstk.Library()
    result = gdstk.Cell("TEST")
    let_1 = gdstk.Cell("let_1_text")
    let_2 = gdstk.Cell("let_2_text")
    pre_result = gdstk.Cell("cell_name")
    Layer_name = "ST"
    layer_no = "3"
    txtbound = "7"
    etch_type = "T"
    boundary = "63"
    polygons = Make_letter(Layer_name[0],int(layer_no))
    try:
        let_1.add(*polygons)
    except:
        let_1.add(polygons)
    pre_result.add(gdstk.Reference(let_1,(5.8,1.5)))
    polygons = Make_letter(Layer_name[1],int(layer_no))
    try:
        let_2.add(*polygons)
    except:
        let_2.add(polygons)
    pre_result.add(gdstk.Reference(let_2,(5.8+int(txtbound)+1.4,1.5)))
    rect = gdstk.rectangle((0,0),(27,10))
    if etch_type == "M":
        text_1 = gdstk.boolean(rect,gdstk.Reference(pre_result),"not",layer=int(layer_no))
        bound = gdstk.rectangle((0, 0),(27,10), layer=int(boundary))
        result.add(*text_1)
        result.add(bound)
    else:
        text_1 = gdstk.boolean(rect,gdstk.Reference(pre_result),"and",layer=int(layer_no))
        bound = gdstk.rectangle((0, 0),(27,10), layer=int(boundary))
        result.add(*text_1)
        result.add(bound)

    lib.add(result)
    lib.write_gds("./letter_test.gds")

if __name__ == "__main__":
    main()
    
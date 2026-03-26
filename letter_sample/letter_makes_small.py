import gdstk

def Make_letter(input,layer_no,scale_x,scale_y):
    x=float(scale_x)
    y=float(scale_y)
    if input == "A":
        rect1 = gdstk.rectangle((0,0),(6,6))
        rect2 = gdstk.rectangle((0.5,0),(5.5,3))
        rect3 = gdstk.rectangle((0.5,3.5),(5.5,5.5))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "B":
        points = [(0,0),(0,6),(5.7,6),(6,5.7),(6,3.2),(5.8,3),(6,2.8),(6,0.3),(5.7,0),(0,0)]
        rect1 = gdstk.Polygon(points)
        rect2 = gdstk.rectangle((0.5,0.5),(5.5,2.74))
        rect3 = gdstk.rectangle((0.5,3.24),(5.5,5.5))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "C":
        points = [(1.3,0),(0,1.3),(0,4.7),(1.3,6),(6,6),(6,0),(1.3,0)]
        rect1 = gdstk.Polygon(points)
        points = [(1.51,0.5),(0.5,1.51),(0.5,4.49),(1.51,5.5),(6,5.5),(6,0.5),(1.51,0.5)]
        rect2 = gdstk.Polygon(points)
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "D":
        points = [(0,0),(0,6),(5.7,6),(6,5.7),(6,0.3),(5.7,0),(0,0)]
        rect1 = gdstk.Polygon(points)
        rect2 = gdstk.rectangle((0.5,0.5),(5.5,5.5))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "E":
        rect1 = gdstk.rectangle((0,0),(6,6))
        rect2 = gdstk.rectangle((0.5,0.5),(6,2.75))
        rect3 = gdstk.rectangle((5.5,2.75),(6,3.25))
        rect4 = gdstk.rectangle((0.5,3.25),(6,5.5))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(rect1,rect3,"not",layer=int(layer_no))
        step3 = gdstk.boolean(step1,rect4,"not",layer=int(layer_no))
        return step3
    elif input == "F":
        rect1 = gdstk.rectangle((0,0),(6,6))
        rect2 = gdstk.rectangle((0.5,0),(6,2.75))
        rect3 = gdstk.rectangle((5.5,2.75),(6,3.25))
        rect4 = gdstk.rectangle((0.5,3.25),(6,5.5))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        step3 = gdstk.boolean(step1,rect4,"not",layer=int(layer_no))
        return step3
    elif input == "G":
        rect1 = gdstk.rectangle((0,0),(6,6))
        rect2 = gdstk.rectangle((0.5,0.5),(5.5,3.1))
        rect3 = gdstk.rectangle((0.5,3.1),(3,3.6))
        rect4 = gdstk.rectangle((0.5,3.6),(6,5.5))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        step3 = gdstk.boolean(step2,rect4,"not",layer=int(layer_no))
        return step3
    elif input == "H":
        rect1 = gdstk.rectangle((0,0),(6,6))
        rect2 = gdstk.rectangle((0.5,0),(5.5,2.75))
        rect3 = gdstk.rectangle((3.25,0.5),(5.5,6))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "I":
        rect1 = gdstk.rectangle((0,0),(6,6))
        rect2 = gdstk.rectangle((0,0.5),(2.75,5.5))
        rect3 = gdstk.rectangle((3.25,0.5),(6,5.5))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "J":
        points = [(0,0),(0,0.5),(3.28,0.5),(3.5,0.72),(3.5,5.5),(4,5.5),(4,0.5),(3.5,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        rect2 = gdstk.rectangle((0,5.5),(6,6))
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "K":
        rect1 = gdstk.rectangle((0,0),(0.5,6))
        rect2 = gdstk.rectangle((0.5,2.75),(2.75,3.25))
        points = [(2.75,3.25),(5.5,6),(6,6),(6,5.5),(5.75,5.5),(3.25,3),(5.75,0.5),(6,0.5),(6,0),(5.5,0),(2.75,2.75),(2.75,3.25)]
        rect3 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"or",layer=int(layer_no))
        return step2
    elif input == "L":
        rect1 = gdstk.rectangle((0,0),(6,6))
        rect2 = gdstk.rectangle((0.5,0.5),(6,6))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "M":
        points = [(0,0),(0,6),(0.5,6),(3,3.5),(5.5,6),(6,6),(6,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        points = [(0.5,0),(0.5,5.25),(3,2.75),(5.5,5.25),(5.5,0),(0.5,0)]
        rect2 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "N":
        rect1 = gdstk.rectangle((0,0),(6,6))
        points = [(0.5,0),(0.5,5),(0.6,5),(5.6,0),(0.5,0)]
        rect2 = gdstk.Polygon(points,layer=int(layer_no))
        points = [(0.4,6),(5.4,1),(5.5,1),(5.5,6),(0.35,6)]
        rect3 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "O":
        rect1 = gdstk.rectangle((0,0),(6,6))
        rect2 = gdstk.rectangle((0.5,0.5),(5.5,5.5))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "P":
        rect1 = gdstk.rectangle((0,0),(6,6))
        rect2 = gdstk.rectangle((0.5,0),(6,3.5))
        rect3 = gdstk.rectangle((0.5,4),(5.5,5.5))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "Q":
        points = [(0,0.28),(0,5.72),(0.28,6),(5.72,6),(6,5.5),(6,0.57),(5.84,0.41),(6,0.25),(5.75,0),(5.59,0.16),(5.43,0),(0.28,0),(0,0.28)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        rect2 = gdstk.rectangle((0.5,0.5),(5.5,5.5))
        points = [(5.25,0.5),(5.14,0.61),(5.39,0.86),(5.5,0.75),(5.25,0.5)]
        rect3 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"or",layer=int(layer_no))
        return step2
    elif input == "R":
        points = [(0,0),(0,6),(0.28,6),(5.72,6),(6,5.48),(6,3.24),(5.8,3),(6,2.74),(6,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        rect2 = gdstk.rectangle((0.5,0),(5.5,2.74))
        rect3 = gdstk.rectangle((0.5,3.24),(5.5,5.5))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "S":
        points = [(0.5,0),(0,0.5),(0,1.62),(0.5,1.62),(0.5,0.72),(0.72,0.5),(5.28,0.5),(5.5,0.72),(5.5,2.53),(5.29,2.74),(5.5,3.25),(6,2.75),(6,0.5),(5.5,0),(0.5,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        points = [(0.5,2.74),(0,3.24),(0,5.49),(0.51,6),(5.49,6),(6,5.49),(6,4.37),(5.5,4.37),(5.5,5.27),(5.28,5.49),(0.73,5.49),(0.51,5.27),(0.51,3.45),(0.71,3.25),(5.5,3.25),(5.15,2.74),(0.5,2.74)]
        rect2 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "T":
        rect1 = gdstk.rectangle((2.7,0),(3.2,5.5))
        rect2 = gdstk.rectangle((0,5.5),(6,6))
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "U":
        points = [(0,0.5),(0,6),(6,6),(6,0.5),(5.5,0),(0.5,0),(0,0.5)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        points = [(0.75,0.5),(0.5,0.75),(0.5,6),(3,6),(3,0.5),(0.75,0.5)]
        rect2 = gdstk.Polygon(points,layer=int(layer_no))
        points = [(3,0.5),(3,6),(5.5,6),(5.5,0.75),(5.25,0.5),(3,0.5)]
        rect3 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "V":
        points = [(2.75,0),(0,2.75),(0,6),(6,6),(6,2.75),(3.25,0),(2.75,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        points = [(3,0.5),(0.5,3),(0.5,6),(5.5,6),(5.5,3),(3,0.5)]
        rect2 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "W":
        points = [(0,0.2*y),(0,1*y),(1*x,1*y),(1*x,0.2*y),(0.8*x,0),(0.5*x,0.3*y),(0.2*x,0),(0,0.2*y)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        points = [(0.3*x,1*y),(0.3*x,0.4*y),(0.5*x,0.6*y),(0.7*x,0.4*y),(0.7*x,1*y),(0.3*x,1*y)]
        rect2 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "X":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        points = [(0.2*x,0),(0.5*x,0.3*y),(0.8*x,0),(0.2*x,0)]
        rect2 = gdstk.Polygon(points,layer=int(layer_no))
        points = [(0,0.2*y),(0.3*x,0.5*y),(0,0.8*y),(0,0.2*y)]
        rect3 = gdstk.Polygon(points,layer=int(layer_no))
        points = [(0.2*x,1*y),(0.5*x,0.7*y),(0.8*x,1*y),(0.2*x,1*y)]
        rect4 = gdstk.Polygon(points,layer=int(layer_no))
        points = [(1*x,0.8*y),(0.7*x,0.5*y),(1*x,0.2*y),(1*x,0.8*y)]
        rect5 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect2,rect3,"or",layer=int(layer_no))
        step2 = gdstk.boolean(rect4,rect5,"or",layer=int(layer_no))
        step3 = gdstk.boolean(step1,step2,"or",layer=int(layer_no))
        step4 = gdstk.boolean(rect1,step3,"not",layer=int(layer_no))
        return step4
    elif input == "Y":
        rect1 = gdstk.rectangle((0.35*x,0),(0.65*x,0.45*y))
        points = [(0.35*x,0.45*y),(0,0.8*y),(0,1*y),(0.2*x,1*y),(0.5*x,0.7*y),(0.8*x,1*y),(1*x,1*y),(1*x,0.8*y),(0.65*x,0.45*y),(0.35*x,0.45*y)]
        rect2 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "Z":
        points = [(0,0),(0,0.2*y),(0.55*x,0.75*y),(0,0.75*y),(0,1*y),(1*x,1*y),(1*x,0.8*y),(0.45*x,0.25*y),(1*x,0.25*y),(1*x,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        return rect1
    elif input == "0":
        points = [(0,0.15*y),(0,0.85*y),(0.15*x,1*y),(0.85*x,1*y),(1*x,0.85*y),(1*x,0.15*y),(0.85*x,0),(0.15*x,0),(0,0.15*y)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        rect2 = gdstk.rectangle((0.25*x,0.25*y),(0.75*x,0.75*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "1":
        rect1 = gdstk.rectangle((0,0),(1*x,0.2*y))
        rect2 = gdstk.rectangle((0,0.8*y),(0.65*x,1*y))
        rect3 = gdstk.rectangle((0.35*x,0.2*y),(0.65*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"or",layer=int(layer_no))
        return step2
    elif input == "2":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.3*x,0.2*y),(1*x,0.4*y))
        rect3 = gdstk.rectangle((0,0.6*y),(0.7*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "3":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0,0.2*y),(0.7*x,0.4*y))
        rect3 = gdstk.rectangle((0,0.6*y),(0.7*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "4":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0,0),(0.7*x,0.3*y))
        rect3 = gdstk.rectangle((0.3*x,0.5*y),(0.7*x,1*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "5":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0,0.2*y),(0.7*x,0.4*y))
        rect3 = gdstk.rectangle((0.3*x,0.6*y),(1*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "6":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.3*x,0.2*y),(0.7*x,0.4*y))
        rect3 = gdstk.rectangle((0.3*x,0.6*y),(1*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "7":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0,0),(0.7*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "8":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.3*x,0.2*y),(0.7*x,0.4*y))
        rect3 = gdstk.rectangle((0.3*x,0.6*y),(0.7*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "9":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0,0.2*y),(0.7*x,0.4*y))
        rect3 = gdstk.rectangle((0.3*x,0.6*y),(0.7*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2

def main():
    lib = gdstk.Library()
    result = gdstk.Cell("TEST")
    let_1 = gdstk.Cell("let_1_text")
    let_2 = gdstk.Cell("let_2_text")
    pre_result = gdstk.Cell("cell_name")
    Layer_name = "AB"
    layer_no = "3"
    txtbound = "6"
    etch_type = "T"
    boundary = "63"
    polygons = Make_letter(Layer_name[0],int(layer_no),6,6)
    try:
        let_1.add(*polygons)
    except:
        let_1.add(polygons)
    pre_result.add(gdstk.Reference(let_1,(5.5,1.5)))
    polygons = Make_letter(Layer_name[1],int(layer_no),6,6)
    try:
        let_2.add(*polygons)
    except:
        let_2.add(polygons)
    pre_result.add(gdstk.Reference(let_2,(5.5+float(txtbound)+2,1.5)))
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
    lib.write_gds("./letter_test_6.gds")

if __name__ == "__main__":
    main()
    
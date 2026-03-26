import gdstk

def main(input,layer_no,scale_x,scale_y):
    x=float(scale_x)
    y=float(scale_y)
    if input == "A":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.3*x,0),(0.7*x,0.4*y))
        rect3 = gdstk.rectangle((0.3*x,0.6*y),(0.7*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "B":
        points = [(0,0),(0,1*y),(0.85*x,1*y),(1*x,0.85*y),(1*x,0.6*y),(0.9*x,0.5*y),(1*x,0.4*y),(1*x,0.15*y),(0.85*x,0),(0,0)]
        rect1 = gdstk.Polygon(points)
        rect2 = gdstk.rectangle((0.3*x,0.2*y),(0.7*x,0.4*y))
        rect3 = gdstk.rectangle((0.3*x,0.6*y),(0.7*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "C":
        points = [(0.2*x,0),(0,0.2*y),(0,0.3*y),(0.9*x,0.3*y),(1*x,0.2*y),(1*x,0.1*y),(0.9*x,0),(0.2*x,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        rect2 = gdstk.rectangle((0,0.3*y),(0.3*x,0.7*y))
        points = [(0,0.7*y),(0,0.8*y),(0.2*x,1*y),(0.9*x,1*y),(1*x,0.9*y),(1*x,0.8*y),(0.9*x,0.7*y),(0,0.7*y)]
        rect3 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"or",layer=int(layer_no))
        return step2
    elif input == "D":
        points = [(0,0),(0,1*y),(0.85*x,1*y),(1*x,0.85*y),(1*x,0.15*y),(0.85*x,0),(0,0)]
        rect1 = gdstk.Polygon(points)
        rect2 = gdstk.rectangle((0.3*x,0.2*y),(0.7*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "E":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.3*x,0.2*y),(1*x,0.4*y))
        rect3 = gdstk.rectangle((0.3*x,0.6*y),(1*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "F":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.3*x,0),(1*x,0.4*y))
        rect3 = gdstk.rectangle((0.3*x,0.6*y),(1*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "G":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.3*x,0.2*y),(0.7*x,0.4*y))
        rect3 = gdstk.rectangle((0.3*x,0.4*y),(0.5*x,0.6*y))
        rect4 = gdstk.rectangle((0.3*x,0.6*y),(1*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        step3 = gdstk.boolean(step2,rect4,"not",layer=int(layer_no))
        return step3
    elif input == "H":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.3*x,0),(0.7*x,0.4*y))
        rect3 = gdstk.rectangle((0.3*x,0.6*y),(0.7*x,1*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "I":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0,0.2*y),(0.35*x,0.8*y))
        rect3 = gdstk.rectangle((0.65*x,0.2*y),(1*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "J":
        points = [(0,0),(0,0.2*y),(0.35*x,0.2*y),(0.45*x,0.3*y),(0.45*x,0.8*y),(0.7*x,0.8*y),(0.7*x,0.2*y),(0.5*x,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        rect2 = gdstk.rectangle((0,0.8*y),(1*x,1*y))
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "K":
        rect1 = gdstk.rectangle((0,0),(0.3*x,1*y))
        points = [(0.3*x,0.35*y),(0.45*x,0.35*y),(0.8*x,0),(1*x,0),(1*x,0.2*y),(0.7*x,0.5*y),(1*x,0.8*y),(1*x,1*y),(0.8*x,1*y),(0.45*x,0.6*y),(0.3*x,0.6*y),
                  (0.3*x,0.4*y),(0.3*x,0.35*y)]
        rect2 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "L":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.3*x,0.3*y),(1*x,1*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "M":
        points = [(0,0),(0,1*y),(1*x,1*y),(1*x,0),(0.75*x,0),(0.75*x,0.6*y),(0.5*x,0.35*y),(0.25*x,0.6*y),(0.25*x,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        points = [(0.2*x,1*y),(0.5*x,0.7*y),(0.8*x,1*y),(0.2*x,1*y)]
        rect2 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "N":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        points = [(0.3*x,0),(0.3*x,0.5*y),(0.8*x,0),(0.3*x,0)]
        rect2 = gdstk.Polygon(points,layer=int(layer_no))
        points = [(0.2*x,1*y),(0.7*x,0.5*y),(0.7*x,1*y),(0.2*x,1*y)]
        rect3 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "O":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.3*x,0.2*y),(0.7*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        return step1
    elif input == "P":
        rect1 = gdstk.rectangle((0,0),(1*x,1*y))
        rect2 = gdstk.rectangle((0.3*x,0),(1*x,0.4*y))
        rect3 = gdstk.rectangle((0.3*x,0.6*y),(0.7*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "Q":
        points = [(0,0.2*y),(0,0.8*y),(0.2*x,1*y),(0.8*x,1*y),(1*x,0.8*y),(1*x,0.2*y),(0.8*x,0),(0.2*x,0),(0,0.2*y)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        rect2 = gdstk.rectangle((0.3*x,0.2*y),(0.7*x,0.8*y))
        points = [(0.8*x,0),(0.9*x,-0.1*y),(1*x,0),(0.9*x,0.1*y),(0.8*x,0)]
        rect3 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"or",layer=int(layer_no))
        return step2
    elif input == "R":
        points = [(0,0),(0,1*y),(0.8*x,1*y),(1*x,0.8*y),(1*x,0.6*y),(0.9*x,0.5*y),(1*x,0.4*y),(1*x,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        rect2 = gdstk.rectangle((0.3*x,0),(0.7*x,0.4*y))
        rect3 = gdstk.rectangle((0.3*x,0.6*y),(0.7*x,0.8*y))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "S":
        points = [(0.2*x,0),(0,0.2*y),(0,0.3*y),(0.3*x,0.3*y),(0.3*x,0.2*y),(0.7*x,0.2*y),(0.7*x,0.4*y),(1*x,0.4*y),(1*x,0.2*y),(0.8*x,0),(0.2*x,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        points = [(0.7*x,0.4*y),(0.2*x,0.4*y),(0,0.6*y),(0,0.8*y),(0.2*x,1*y),(0.8*x,1*y),(1*x,0.8*y),(1*x,0.7*y),(0.7*x,0.7*y),(0.7*x,0.8*y),(0.3*x,0.8*y),
                  (0.3*x,0.6*y),(0.8*x,0.6*y),(1*x,0.4*y),(0.7*x,0.4*y)]
        rect2 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "T":
        rect1 = gdstk.rectangle((0,0.7*y),(1*x,1*y))
        rect2 = gdstk.rectangle((0.35*x,0),(0.65*x,0.7*y))
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "U":
        points = [(0,0),(0,1*y),(0.3*x,1*y),(0.3*x,0.35*y),(0.35*x,0.3*y),(0.65*x,0.3*y),(0.7*x,0.35*y),(0.7*x,1*y),(1*x,1*y),(1*x,0),(0,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        points = [(0,0),(0,0.2*y),(0.2*x,0),(0,0)]
        rect2 = gdstk.Polygon(points,layer=int(layer_no))
        points = [(0.8*x,0),(1*x,0.2*y),(1*x,0),(0.8*x,0)]
        rect3 = gdstk.Polygon(points,layer=int(layer_no))
        step1 = gdstk.boolean(rect1,rect2,"not",layer=int(layer_no))
        step2 = gdstk.boolean(step1,rect3,"not",layer=int(layer_no))
        return step2
    elif input == "V":
        points = [(0.32*x,0),(0,0.32*y),(0,1*y),(1*x,1*y),(1*x,0.32*y),(0.68*x,0),(0.32*x,0)]
        rect1 = gdstk.Polygon(points,layer=int(layer_no))
        points = [(0.3*x,1*y),(0.3*x,0.44*y),(0.5*x,0.24*y),(0.7*x,0.44*y),(0.7*x,1*y),(0.3*x,1*y)]
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

if __name__ == "__main__":
    main()
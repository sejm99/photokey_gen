import gdstk,numpy

def Make_letter(input,layer_no,scale_x,scale_y,thin):
    #알파벳 만들기
    x=float(scale_x)
    y=float(scale_y)
    size=float(thin)
    if input == "A":
        points = [(0,0),(0,1*x),(1*x,1*y),(1*y,0)]
        rect1 = gdstk.FlexPath(points,size,joins=["natural"],ends=["flush"])
        points = [(0,0),(0,0.6*y),(1*x,0.6*y),(1*y,0)]
        rect2 = gdstk.FlexPath(points,size,joins=["natural"],ends=["flush"])
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "B":
        points = [(0,0),(0,1*y),(1*x,1*y),(1*x,0),(0,0)]
        rect1 = gdstk.FlexPath(points,size,joins=["bevel"],ends=["extended"])
        points = [(0,0),(0,(1*y/2)),(1*x,(1*y/2)),(1*y,0),(0,0)]
        rect2 = gdstk.FlexPath(points,size,joins=["bevel"],ends=["extended"])
        step1 = gdstk.boolean(rect1,rect2,"or",layer=int(layer_no))
        return step1
    elif input == "C":
        points = [(1*x,0),(0.2*x,0),(0,0.2*y),(0,0.8*y),(0.2*x,1*y),(1*x,1*y)]
        step1 = gdstk.FlexPath(points,size,joins=["bevel"],ends=["round"],layer=int(layer_no))
        return step1

def main():
    lib = gdstk.Library()
    result = gdstk.Cell("TEST")
    let_1 = gdstk.Cell("let_1_text")
    let_2 = gdstk.Cell("let_2_text")
    pre_result = gdstk.Cell("cell_name")
    # input
    Layer_name = "BC"
    layer_no = "3"
    boundary = "10"
    etch_type = "T"
    # Make_letter(글씨,layer_no,size_x,size_y)
    polygons = Make_letter(Layer_name[0],int(layer_no),7,7,0.5)
    try:
        let_1.add(*polygons)
    except:
        let_1.add(polygons)
    pre_result.add(gdstk.Reference(let_1,(0,0)))
    polygons = Make_letter(Layer_name[1],int(layer_no),7,7,0.5)
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
    lib.write_gds("./letter_test_1.gds")

if __name__ == "__main__":
    main()
    
"""
lib =  gdstk.Library()
cell1 = lib.new_cell("test_top1")
cell2 = lib.new_cell("test_top2")
cell3 = lib.new_cell("test_top3")

points = [(0,0),(0,7),(7,7),(7,0)]
path_1 = gdstk.FlexPath(points,0.5, joins=["natural"], ends=["flush"],
    layer=[0])
cell1.add(path_1)
points = [(0,0),(0,4),(7,4),(7,0)]
path_2 = gdstk.FlexPath(points,0.5, joins=["natural"], ends=["flush"],
    layer=[0])
cell1.add(path_2)
lib.write_gds("./test_A.gds")

points = [(0, 8), (0, 0), (8, 0), (18, 13), (18, -8)]
path_1 = gdstk.FlexPath(points , 1, datatype=1)
path_2 = gdstk.FlexPath(points , 1, bend_radius=3)

#joins=["natural", "bevel", "miter", "round"], 
#ends=["flush", "extended", (0.4, 0.8), "round"],

#cell2.add(path_1)
#cell2.add(path_2)
#lib.write_gds("./test2.gds")

def custom_broken_join(p0, v0, p1, v1, center, width):
    p0 = numpy.array(p0)
    v0 = numpy.array(v0)
    p1 = numpy.array(p1)
    v1 = numpy.array(v1)
    center = numpy.array(center)
    # Calculate intersection point p between lines defined by
    # p0 + u0 * v0 (for all u0) and p1 + u1 * v1 (for all u1)
    den = v1[1] * v0[0] - v1[0] * v0[1]
    lim = 1e-12 * ((v0[0] ** 2 + v0[1] ** 2) *
                   (v1[0] ** 2 + v1[1] ** 2))
    if den ** 2 < lim:
        # Lines are parallel: use mid-point
        u0 = u1 = 0
        p = 0.5 * (p0 + p1)
    else:
        dx = p1[0] - p0[0]
        dy = p1[1] - p0[1]
        u0 = (v1[1] * dx - v1[0] * dy) / den
        u1 = (v0[1] * dx - v0[0] * dy) / den
        p = 0.5 * (p0 + v0 * u0 + p1 + v1 * u1)
    if u0 <= 0 and u1 >= 0:
        # Inner corner
        return [p]
    # Outer corner
    return [p0, center, p1]
def custom_pointy_end(p0, v0, p1, v1):
    p0 = numpy.array(p0)
    v0 = numpy.array(v0)
    p1 = numpy.array(p1)
    v1 = numpy.array(v1)
    r = 0.5 * numpy.sqrt(numpy.sum((p0 - p1) ** 2))
    v0 /= numpy.sqrt(numpy.sum(v0 ** 2))
    v1 /= numpy.sqrt(numpy.sum(v1 ** 2))
    return [p0, 0.5 * (p0 + p1) + 0.5 * (v0 - v1) * r, p1]
path3 = gdstk.FlexPath(
    [(1, 6), (1, 1), (6, 1), (6, 6), (5, 6), (4, 3), (3, 6), (2, 6)],0.5,
    joins=custom_broken_join,
    ends=custom_pointy_end,
)
#cell3.add(path3)
#lib.write_gds("./test4.gds")

    #[(0, 5), (0, 0), (5, 0), (15, 10), (15, -5)],
    #3,
    #joins=custom_broken_join,
    #ends=custom_pointy_end,"""

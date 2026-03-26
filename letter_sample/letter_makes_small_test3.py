import gdstk,tkinter

def create_text_cells(library):
    cell_size = 0.5
    layer = 0
    text_list = [chr(i) for i in range(65, 91)] + [str(i) for i in range(10)]
    num_rows = 7
    num_cols = 7
    spacing = 2

    for i in range(num_rows):
        for j in range(num_cols):
            text = text_list[i * num_cols + j]
            position = ((cell_size + spacing) * j, (cell_size + spacing) * i)
            cell = gdstk.Cell(f"{text}_cell")
            #cell.add(gdstk.text((text),(cell_size),(position),(layer)))
            cell.add(gdstk.text((text),(cell_size),(position),(layer)))
            library.add(cell)

def main():
    library = gdstk.Library()
    create_text_cells(library)
    library.write_gds("text_cells.gds")

if __name__ == "__main__":
    main()






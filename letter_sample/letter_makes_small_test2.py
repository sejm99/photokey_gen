import gdstk

lib = gdstk.Library()

# Define a function to create a cell for each character
def create_char_cell(char):
    cell = gdstk.Cell(f"{char}")
    #poly = gdstk.Polygon([(0,0), (0,7), (7,7), (7,0)], 0.5, 0.5)
    poly = gdstk.Polygon([(0,0), (0,7), (7,7), (7,0)], 0.5, 0.5)
    #poly = gdstk.Polygon(gdstk.rectangle(0, 0, 7, 7),0.5,datatype=0)
    #size = 7  # Size of the character cell
    #thickness = 0.5  # Thickness of the character
    #x0, y0 = 0, 0  # Starting position
    #x1, y1 = x0 + size, y0 + size  # Ending position
    #poly = gdstk.Polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], thickness)
    cell.add(poly)
    return cell

# Create cells for each character
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
for char in characters:
    cell = create_char_cell(char)
    lib.add(cell)

# Save the library to a GDSII file
lib.write_gds("characters.gds")

print("Characters created and saved as 'characters.gds'")







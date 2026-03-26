import gdstk

# Create a new library
library = gdstk.Library()

# Define cell size and grid parameters
cell_size = 0.5
grid_size = 7
grid_spacing = 1.0
char ="A"
position = (0,0)
# Create a new cell
cell = gdstk.Cell("CELL")

# Define function to add text to cell
def add_text(char, position):
    text = gdstk.Text(char, cell_size, position, layer=0, texttype=0)
    cell.add(text)

# Define function to add rectangle to cell
def add_rectangle(position):
    rectangle = gdstk.rectangle(position, position + (int(cell_size), int(cell_size)), layer=1)
    cell.add(rectangle)

# Iterate over the grid and add characters and rectangles
for i in range(grid_size):
    for j in range(grid_size):
        position = (i * grid_spacing, j * grid_spacing)
        add_rectangle(position)
        add_text(chr(65 + i*grid_size + j), position)  # Add A-Z characters
        add_text(str(i*grid_size + j), position)      # Add 0-9 characters

# Add the cell to the library
library.add(cell)

# Write the GDSII file
library.write_gds("output.gds")


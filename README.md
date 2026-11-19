# Conway's Game of Life
Simple simulation of "The Game of Life" imagined by John Horton Conway.

**Gosper Glider Gun :**

https://github.com/user-attachments/assets/e940b5ef-9a43-4ad3-a1c0-25f61f1ce8b4

## How it works
The program reads a binary grid from a text file whose path is specified in the **GRID_FILE_PATH** constant located in **main.py**.

Each cell in the grid is represented by a binary value:

- 1 represents an initially **alive** cell.
- 0 represents an initially **dead** cell.

The window dimensions are automatically determined based on the number of rows and columns found in the input file, eliminating the need for manual configuration.

Once the grid is loaded, the simulation runs continuously, computing and displaying successive generations according to Conway's Game of Life rules.

### Creating Custom Patterns
To create your own Game of Life pattern, simply define a binary grid in a **.txt** file using 0s and 1s, then update the GRID_FILE_PATH constant to point to your file. The program will automatically load the pattern and adapt the simulation window to its dimensions.

### Controls
**Space:** Pause or resume the simulation
**G:** Enable or disable the next-generation preview
**Up Arrow:** Increase the simulation speed (FPS)
**Down Arrow:** Decrease the simulation speed (FPS)


## Tech Stack
### Requirements
- Python 3.10+
- Pygame

## Running the Simulation
```
python src/main.py
```

## Project structure

```
/Snake_game
  ├── src/
  │   ├── main.py
  │   └── methods.py     
  ├── Gosper_Glider_Gun.txt
  ├── grid.txt
  └── README.md
```

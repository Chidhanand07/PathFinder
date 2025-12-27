# A* Pathfinding Visualizer

An interactive pathfinding visualization tool built with Python and Pygame that demonstrates the A* algorithm in real-time. Click anywhere on the map to see the optimal path calculated from a fixed starting point.

## Features

- **Real-time Pathfinding**: Click on any walkable tile to instantly see the shortest path
- **A* Algorithm**: Uses the efficient A* pathfinding algorithm with diagonal movement
- **Visual Feedback**: 
  - Highlighted cell under mouse cursor
  - Red line showing the calculated path
  - Custom map overlay
- **Interactive Interface**: Simple click-to-navigate interface
- **60 FPS Smooth Animation**: Butter-smooth visualization

## Requirements

- Python 3.x
- Pygame
- pathfinding library

## Installation

1. Install Python from [python.org](https://www.python.org/)

2. Install required packages:
```bash
pip install pygame
pip install pathfinding
```

3. Prepare your assets:
   - Place your `map.png` file in the project directory
   - Place your `selection.png` file (for cell highlighting) in the project directory

## Project Structure

```
pathfinder/
│
├── main.py              # Main pathfinding application
├── map.png              # Background map image (1280x736)
├── selection.png        # Cell selection overlay image (32x32)
└── README.md            # This file
```

## How to Run

```bash
python main.py
```

## Usage

1. **Launch the Application**: Run the script to open the pathfinding visualizer
2. **Click to Navigate**: Click on any white (walkable) area to create a path
3. **Watch the Path**: A red line will draw from the starting point (1,1) to your clicked location
4. **Click Again**: Click different locations to recalculate paths in real-time

## Map Matrix

The pathfinding uses a grid-based matrix where:
- `0` = Obstacle (walls, barriers - not walkable)
- `1` = Walkable path (open areas)

The current map is a 23x40 grid with 32-pixel tiles (total resolution: 1280x736).

## Starting Point

The default starting position is set at coordinates `(1, 1)`. You can modify this in the code:

```python
start_x, start_y = [1, 1]  # Change these values
```

## Customization

### Change Map Size
Modify the matrix dimensions and screen size:
```python
screen = p.display.set_mode((your_width, your_height))
```

### Edit the Map
Update the `mat` array to create your own custom obstacles and paths.

### Adjust Tile Size
If you want different tile sizes, modify the division factor (currently 32):
```python
row, col = mouse_pos[1] // 32, mouse_pos[0] // 32  # Change 32 to your tile size
```

### Diagonal Movement
The pathfinder uses diagonal movement by default. To disable it:
```python
finder = AStarFinder(diagonal_movement=DiagonalMovement.never)
```

## How It Works

1. **Grid Initialization**: The map matrix is converted to a pathfinding grid
2. **Mouse Click Detection**: When you click, the coordinates are converted to grid position
3. **A* Algorithm**: Calculates the shortest path from start to clicked position
4. **Path Drawing**: Converts grid coordinates back to pixel coordinates and draws a line
5. **Visual Update**: The path is displayed as a red line connecting all waypoints

## Features Explanation

### Active Cell Highlighting
- Hover over any walkable tile to see a selection overlay
- Only highlights tiles where pathfinding is possible (value = 1)

### Path Visualization
- Red line connects all waypoints in the calculated path
- 7-pixel width line for clear visibility
- Updates instantly when clicking new destinations

## Technical Details

- **Algorithm**: A* (A-star) pathfinding
- **Movement**: Diagonal movement enabled
- **Grid Size**: 23 rows × 40 columns
- **Tile Size**: 32×32 pixels
- **Frame Rate**: 60 FPS
- **Resolution**: 1280×736 pixels

## Troubleshooting

### "File not found" error
Make sure `map.png` and `selection.png` are in the same directory as your script, or update the file paths in the code.

### Path not appearing
- Ensure you're clicking on a walkable tile (white areas, value = 1 in matrix)
- Check that the starting position (1,1) is also walkable
- Verify there's a valid path between start and clicked position

### Selection not showing
- Check that `selection.png` exists and has transparency (alpha channel)
- Ensure the image is 32×32 pixels to match tile size

## Future Enhancements

- Draggable start and end points
- Multiple pathfinding algorithms (Dijkstra, BFS, etc.)
- Real-time obstacle editing
- Path cost visualization
- Algorithm speed comparison


## License

This project is open source and available for educational purposes.
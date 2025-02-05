# Soccer Match Analysis System
A comprehensive system for analyzing and visualizing soccer match events, player statistics, and match dynamics using Python.

## Overview
This system processes and analyzes soccer match data from Excel files, providing detailed analysis of match events, player statistics, team formations, and real-time visualization of match movements. The project consists of three main components:

1. Constant Analysis Module (`constant_analysis.py`)
2. GUI Visualization Tool (`gui.py`)
3. Data Structure Analysis (`row_name_analysis.py`)

## Features

### Data Analysis Components
- Team and player identification
- Event tracking and classification
- Goal analysis
- Goalkeeper performance tracking
- Match event visualization
- Team formation analysis
- Player position tracking
- Real-time match replay capabilities

### Visualization Features
- Interactive match playback
- Event path visualization
- Timeline-based navigation
- Start and end point marking
- Color-coded event representation
  - Blue: Starting positions
  - Green: Ending positions
  - Red: Movement paths

## Technical Implementation

### Data Processing (`constant_analysis.py`)

#### Key Functions:

1. `load_excel(file_path)`
   - Loads match data from Excel files
   - Uses pandas with openpyxl engine
   - Handles large datasets efficiently

2. `extract_first_row_columns(excel_data, columns_to_extract)`
   - Extracts critical match metadata
   - Processes core match information including:
     - Match ID and labels
     - Competition details
     - Season information
     - Match period data

3. `get_unique_teams(excel_data)`
   - Identifies unique team entries
   - Processes team formations
   - Maintains team identification consistency

4. `get_unique_players(excel_data)`
   - Catalogs all players
   - Groups players by teams
   - Excludes placeholder entries (player_id = 0)

5. `get_unique_goalkeepers(excel_data)`
   - Specialized goalkeeper tracking
   - Handles team association
   - Implements team name reversal for opposing teams

6. `get_unique_event_types_with_counts_and_teams(excel_data)`
   - Comprehensive event classification
   - Statistical analysis of event frequencies
   - Team-specific event distribution

### Visualization System (`gui.py`)

#### Core Components:

1. **GUI Framework**
   - Built using tkinter
   - Canvas-based visualization
   - Real-time update capabilities

2. **Event Visualization**
   - Dynamic line drawing
   - Point plotting
   - Color-coded event representation

3. **Navigation Controls**
   - Forward and backward navigation
   - Timeline tracking
   - State management

4. **Data Scaling**
   - Coordinate system scaling (x10 for x-axis, x6 for y-axis)
   - Maintains aspect ratio
   - Pixel-perfect positioning

### Data Structure (`row_name_analysis.py`)
Handles 85+ data columns including:
- Match metadata
- Event timestamps
- Player statistics
- Team information
- Event classifications
- Spatial coordinates
- Performance metrics
- Possession statistics

## Technical Requirements

### Dependencies
- Python 3.x
- pandas
- tkinter
- PIL (Python Imaging Library)
- openpyxl

### File Structure Requirements
```
project_root/
│
├── constant_analysis.py
├── gui.py
├── row_name_analysis.py
└── data/
    ├── AL_Ein_Match_event.xlsx
    └── GT.jpg
```

## Data Schema

### Core Event Data Fields
- Event identification
- Temporal information
- Spatial coordinates
- Player/team associations
- Event classifications
- Performance metrics

### Match Metadata
- Competition details
- Season information
- Team formations
- Player rosters
- Match periods

## Usage Instructions

### Running Analysis
```python
# Load and analyze match data
python constant_analysis.py

# Launch visualization tool
python gui.py

# Analyze data structure
python row_name_analysis.py
```

### Visualization Controls
- **Next Button**: Advance to next event
- **Back Button**: Return to previous event
- **Timeline**: Shows match timestamp
- **Visual Indicators**:
  - Blue dots: Event start positions
  - Green dots: Event end positions
  - Red lines: Movement paths

## Performance Considerations

### Data Processing
- Efficient pandas operations
- Optimized data structures
- Memory management for large datasets

### Visualization
- Canvas redraws optimized
- Event caching
- Efficient state management

## Future Enhancements
1. Additional statistical analysis
2. Enhanced visualization features
3. Real-time data processing
4. Export capabilities
5. Advanced filtering options

## Notes
- Coordinate system uses custom scaling
- Team names are automatically reversed for goalkeeper analysis
- Events are tracked chronologically
- Multiple event types per action are supported

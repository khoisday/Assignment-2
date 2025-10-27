# DTW_UR_SA2 GeoJSON Raw Data Access

This repository contains tools to extract and work with raw JSON data from the `DTW_UR_SA2.geojson` file.

## File Information

- **File**: `data/DTW_UR_SA2.geojson`
- **Size**: ~76MB
- **Type**: GeoJSON FeatureCollection
- **Features**: 2,292 geographical regions (SA2 areas)
- **Data Fields**: Geography codes, labels, statistical measures, and polygon coordinates

## Raw JSON Data Access

### Method 1: Using the Python Extractor (Recommended)

```python
from json_extractor import DTWJsonExtractor

# Initialize the extractor
extractor = DTWJsonExtractor()

# Get complete raw JSON data as Python dictionary
raw_data = extractor.get_raw_json()

# Get formatted JSON string
formatted_json = extractor.get_formatted_json()

# Get compact JSON string
compact_json = extractor.get_compact_json()

# Save to file
extractor.save_raw_json('output.json', formatted=True)
```

### Method 2: Using the Command Line Script

```bash
# Get file information
python3 extract_raw_json.py info

# Get raw JSON (compact format)
python3 extract_raw_json.py raw

# Get pretty-formatted JSON
python3 extract_raw_json.py pretty

# Get help
python3 extract_raw_json.py help
```

### Method 3: Direct File Access

```python
import json

# Load the raw JSON data directly
with open('data/DTW_UR_SA2.geojson', 'r') as file:
    raw_data = json.load(file)
```

## Data Structure

The raw JSON data follows the GeoJSON format:

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "id": 1,
      "type": "Feature",
      "properties": {
        "primaryindex": 1,
        "Geography_Code": "101021007",
        "Geography_Label": "Braidwood",
        "Count": 1511,
        "Average": 37.95,
        "Median": 19.52,
        "Interquartile_Range": 71.43,
        "Std_Dev": 41.46
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [...]
      }
    }
  ]
}
```

## Usage Examples

### Get Specific Feature Data

```python
from json_extractor import DTWJsonExtractor

extractor = DTWJsonExtractor()

# Get feature by index
first_feature = extractor.get_feature_by_index(0)

# Get feature by geography code
braidwood = extractor.get_feature_by_geography_code("101021007")

# Get all geography codes
all_codes = extractor.get_all_geography_codes()
```

### Export Data

```python
# Save formatted JSON to file
extractor.save_raw_json('dtw_formatted.json', formatted=True)

# Save compact JSON to file
extractor.save_raw_json('dtw_compact.json', formatted=False)
```

## Output Raw JSON Data

To get the complete raw JSON data, run:

```bash
python3 extract_raw_json.py raw > dtw_raw_data.json
```

This will output the entire raw JSON content to a file.

## Requirements

- Python 3.x
- No external dependencies (uses only built-in `json` module)

## Files

- `data/DTW_UR_SA2.geojson` - Original GeoJSON data file
- `extract_raw_json.py` - Command-line tool for JSON extraction
- `json_extractor.py` - Python class for programmatic access
- `README.md` - This documentation file
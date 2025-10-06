#!/usr/bin/env python3
"""
Script to extract and display raw JSON data from DTW_UR_SA2.geojson file.
This script provides access to the raw JSON content of the GeoJSON file.
"""

import json
import sys
import os

def extract_raw_json(file_path, output_format='pretty'):
    """
    Extract raw JSON data from GeoJSON file.
    
    Args:
        file_path (str): Path to the GeoJSON file
        output_format (str): 'pretty' for formatted JSON, 'raw' for compact JSON
    
    Returns:
        dict: The raw JSON data
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            raw_data = json.load(file)
        
        if output_format == 'pretty':
            print(json.dumps(raw_data, indent=2, ensure_ascii=False))
        elif output_format == 'raw':
            print(json.dumps(raw_data, ensure_ascii=False))
        elif output_format == 'return':
            return raw_data
            
        return raw_data
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Invalid JSON in file '{file_path}': {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

def get_file_info(file_path):
    """Get basic information about the GeoJSON file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        print("=== DTW_UR_SA2.geojson File Information ===")
        print(f"Type: {data.get('type', 'Unknown')}")
        
        if 'features' in data:
            print(f"Number of features: {len(data['features'])}")
            
            if data['features']:
                # Show first feature as example
                first_feature = data['features'][0]
                print(f"First feature ID: {first_feature.get('id', 'No ID')}")
                print(f"Feature type: {first_feature.get('type', 'Unknown')}")
                
                if 'properties' in first_feature:
                    print("Properties in first feature:")
                    for key, value in first_feature['properties'].items():
                        print(f"  - {key}: {value}")
                
                if 'geometry' in first_feature:
                    geometry = first_feature['geometry']
                    print(f"Geometry type: {geometry.get('type', 'Unknown')}")
        
        print("=" * 45)
        
    except Exception as e:
        print(f"Error getting file info: {e}")

def main():
    """Main function to handle command line arguments and execute extraction."""
    file_path = os.path.join(os.path.dirname(__file__), 'data', 'DTW_UR_SA2.geojson')
    
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == 'info':
            get_file_info(file_path)
        elif command == 'raw':
            extract_raw_json(file_path, 'raw')
        elif command == 'pretty':
            extract_raw_json(file_path, 'pretty')
        elif command == 'help':
            print("Usage:")
            print("  python extract_raw_json.py info     - Show file information")
            print("  python extract_raw_json.py raw      - Output raw JSON (compact)")
            print("  python extract_raw_json.py pretty   - Output formatted JSON")
            print("  python extract_raw_json.py help     - Show this help message")
        else:
            print(f"Unknown command: {command}")
            print("Use 'python extract_raw_json.py help' for usage information")
    else:
        # Default: show file info
        get_file_info(file_path)

if __name__ == "__main__":
    main()
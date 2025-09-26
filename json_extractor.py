#!/usr/bin/env python3
"""
JSON Extractor for DTW_UR_SA2.geojson
Simple tool to extract and work with the raw JSON data from the GeoJSON file.
"""

import json
import os

class DTWJsonExtractor:
    """Class to handle extraction and manipulation of DTW_UR_SA2.geojson data."""
    
    def __init__(self, file_path=None):
        """Initialize the extractor with the GeoJSON file path."""
        if file_path is None:
            file_path = os.path.join(os.path.dirname(__file__), 'data', 'DTW_UR_SA2.geojson')
        
        self.file_path = file_path
        self._data = None
    
    def load_data(self):
        """Load the JSON data from file."""
        if self._data is None:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                self._data = json.load(file)
        return self._data
    
    def get_raw_json(self):
        """Get the complete raw JSON data."""
        return self.load_data()
    
    def get_formatted_json(self, indent=2):
        """Get the JSON data formatted as a string."""
        data = self.load_data()
        return json.dumps(data, indent=indent, ensure_ascii=False)
    
    def get_compact_json(self):
        """Get the JSON data in compact format."""
        data = self.load_data()
        return json.dumps(data, ensure_ascii=False, separators=(',', ':'))
    
    def get_feature_count(self):
        """Get the number of features in the collection."""
        data = self.load_data()
        return len(data.get('features', []))
    
    def get_feature_by_index(self, index):
        """Get a specific feature by index."""
        data = self.load_data()
        features = data.get('features', [])
        if 0 <= index < len(features):
            return features[index]
        return None
    
    def get_feature_by_geography_code(self, code):
        """Get a feature by Geography_Code."""
        data = self.load_data()
        features = data.get('features', [])
        for feature in features:
            if feature.get('properties', {}).get('Geography_Code') == code:
                return feature
        return None
    
    def get_all_geography_codes(self):
        """Get all Geography_Code values."""
        data = self.load_data()
        features = data.get('features', [])
        return [feature.get('properties', {}).get('Geography_Code') 
                for feature in features 
                if feature.get('properties', {}).get('Geography_Code')]
    
    def save_raw_json(self, output_path, formatted=True):
        """Save the raw JSON data to a file."""
        data = self.load_data()
        with open(output_path, 'w', encoding='utf-8') as file:
            if formatted:
                json.dump(data, file, indent=2, ensure_ascii=False)
            else:
                json.dump(data, file, ensure_ascii=False, separators=(',', ':'))

def main():
    """Main function to demonstrate usage."""
    extractor = DTWJsonExtractor()
    
    print("=== DTW_UR_SA2.geojson Raw JSON Data Extractor ===")
    print(f"File: {extractor.file_path}")
    print(f"Feature count: {extractor.get_feature_count()}")
    
    print("\n=== Available Geography Codes (first 10) ===")
    codes = extractor.get_all_geography_codes()[:10]
    for i, code in enumerate(codes, 1):
        print(f"{i:2d}. {code}")
    
    print(f"\n... and {extractor.get_feature_count() - 10} more features")
    
    print("\n=== Sample Feature (first feature) ===")
    first_feature = extractor.get_feature_by_index(0)
    if first_feature:
        print(json.dumps(first_feature, indent=2)[:1000] + "...")
    
    print("\n=== Raw JSON Data Access Methods ===")
    print("1. extractor.get_raw_json() - Returns complete JSON as Python dict")
    print("2. extractor.get_formatted_json() - Returns formatted JSON string")
    print("3. extractor.get_compact_json() - Returns compact JSON string")
    print("4. extractor.save_raw_json(path) - Saves JSON to file")

if __name__ == "__main__":
    main()
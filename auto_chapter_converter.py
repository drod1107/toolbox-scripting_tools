import os
import json

project_dir = '/path/to/project'

# Find the project.osp file and load the JSON data
project_file = os.path.join(project_dir, 'project.osp')
with open(project_file) as f:
    project_data = json.load(f)

# Extract the markers list from the project data
markers = project_data.get('markers', [])

# Initialize an empty list to hold the formatted markers
formatted_markers = []

# Loop through the marker data and format it  
for marker in markers:
    timestamp = marker.get('position', '')
    label = marker.get('title', 'Unnamed Marker')
    
    # Format the timestamp and label for YouTube
    youtube_timestamp = f"{int(timestamp // 3600):02d}:{int((timestamp % 3600) // 60):02d}:{int(timestamp % 60):02d}"
    youtube_label = f"{youtube_timestamp} - {label}"
    
    formatted_markers.append(youtube_label)

# Save the formatted markers to a text file for YouTube description
with open('youtube_markers.txt', 'w') as f:
    f.write('\n'.join(formatted_markers))

print("Formatted markers extracted from project and saved to 'youtube_markers.txt'")
import csv
import os
from datetime import datetime

from .utils import check_website
from .utils import format_date

def store_outfits(outfits, url, style_type, page):
    # Define the field names for the CSV file
    fieldnames = ['id', 'title', 'sex', 'style', 'date', 'views', 'model', 'comment', 'link', 'imagelink']
    
    # Define the output file path relative to the script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    website = check_website(url)
    try :
        website = check_website(url)
        if website is None:
            raise ValueError("Website not recognized")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)  # Exit the program with a non-zero exit code indicating an error

    output_directory = os.path.join(script_dir, '..', 'data', website)
    os.makedirs(output_directory, exist_ok=True)  # Create the directory if it doesn't exist
    
    output_file = os.path.join(output_directory, f'{style_type}{page}-outfits.csv')

    url = url[:-5] + "views/"
    # Open the CSV file in write mode
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        # Create a CSV writer object
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header row
        writer.writeheader()

        # Write the outfits to the CSV file
        for outfit in outfits:
            outfit['link'] = url + outfit['id']
            outfit['style'] = style_type
            outfit['date'] = format_date(outfit['date'])
            writer.writerow(outfit)
import os
import csv
import hashlib
import requests

def download_image(url, product_number, output_directory):
    try:
        # Prepend 'http:' or 'https:' to the URL if missing
        if url.startswith('//'):
            url = 'http:' + url  # You may want to change this to 'https:' depending on your needs

        # Send a GET request to the image URL
        response = requests.get(url)
        if response.status_code == 200:
            # Generate the filename using 'm' + the product number
            image_name = f"m{product_number}.jpg"

            # Save the image to the output directory
            save_path = os.path.join(output_directory, image_name)
            with open(save_path, 'wb') as f:
                f.write(response.content)
            print(f"Downloaded: {save_path}")
        else:
            print(f"Failed to download image: {url}. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading image: {url}. Error: {e}")


def download_images_from_csv(csv_file, output_directory):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            image_url = row['코디 사진 링크']
            product_number = row['상품번호']
            download_image(image_url, product_number, output_directory)


directory = "../data/musinsa/"

files = os.listdir(directory)

for file in files:
    if file.endswith(".csv"):
        filename_without_extension = os.path.splitext(file)[0]
        
        # Construct the full path to the CSV file
        csv_file_path = os.path.join(directory, file)
        # Specify the directory where you want to save the downloaded images
        output_directory = os.path.join(directory, filename_without_extension)
        # Create the directory if it doesn't exist
        if not os.path.exists(output_directory):
            os.makedirs(output_directory)
        # Download images from the CSV file
        download_images_from_csv(csv_file_path, output_directory)

import csv

def store_outfits(outfits):
    # Define the field names for the CSV file
    fieldnames = ['상품번호', '코디 페이지 링크', '코디 사진 링크', '업로드 날짜', '코디 이름', '조회수', '댓글수', '성별']

    # Open the CSV file in write mode
    with open('outfits.csv', 'w', newline='', encoding='utf-8') as csvfile:
        # Create a CSV writer object
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write the header row
        writer.writeheader()

        # Write the outfits to the CSV file
        for outfit in outfits:
            writer.writerow(outfit)

# Example usage:
# outfits = [{'상품번호': '123', '코디 페이지 링크': 'https://example.com', ...}, {...}, ...]
# store_outfits(outfits)

import csv
import datetime
def calculate_midprice(data1, data2):
 price1 = float(data1[0])
price2 = float(data2[0])
midprice = (price1 + price2) / 2
 return midprice
def convert_time(seconds):
 time = datetime.datetime(2023, 1, 1) + datetime.timedelta(seconds=seconds)
 return time.strftime("%H:%M:%S")
# Calculate total number of midprice calculation points
calculation_points = (1048576 - 1) // 30 //book데이터 총 행의 개수=1048576-1
# Prepare data for feature.csv
feature_data = []
for n in range(calculation_points):
 row_index1 = 2 + 30 * n
 row_index2 = 17 + 30 * n
 with open('book.csv', 'r') as book_file:
 book_reader = csv.reader(book_file)
next(book_reader) # Skip header row
 for _ in range(row_index1):
 next(book_reader) # Skip rows until row_index1
 row1 = next(book_reader)
for _ in range(row_index2 - row_index1 - 1):
 next(book_reader) # Skip rows until row_index2
 row2 = next(book_reader)
midprice = calculate_midprice(row1, row2)
time = convert_time(n + 1)
 feature_data.append([midprice, time])
# Write data to feature.csv
with open('feature.csv', 'w', newline='') as feature_file:
 feature_writer = csv.writer(feature_file)
feature_writer.writerow(['midprice', 'feature_time'])
feature_writer.writerows(feature_data)

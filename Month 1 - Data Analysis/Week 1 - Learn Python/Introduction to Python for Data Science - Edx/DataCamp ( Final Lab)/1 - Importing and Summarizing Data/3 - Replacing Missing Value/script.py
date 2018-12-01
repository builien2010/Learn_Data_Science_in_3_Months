
'''
Exercise:
    There are some missing values in the dataset that are coded as a string. 
    You'll update these to a value that Python understands as "missing."

    The list columns contains the names of the columns you'll be working with in this exercise.

----------------------------------------------------------------------------------------------
Introduction:
    - Look at the dtypes of the columns in "columns" to make sure that the data is numeric.
    - It looks like a string is being used to encode missing values. 
    Use the .unique() method to figure out what the string is.
    - Search for missing values in the median, p25th, and p75th columns.
    - Replace the found missing values with a NaN value, using numpy's np.nan.

----------------------------------------------------------------------------------------------
Hint:
    Try selecting the three columns in columns and then looking at the .dtypes attribute of the resulting DataFrame.
    Call the .unique() method on the median column.
    Use a boolean expression to filter the columns so that you only have rows with a value of UN.
    numpy has an np.nan object that you can use to replace the values.

'''

'''
Bài tập :
    Có một vài giá trị bị thiếu trong tập dữ liệu được mã hóa như là một chuỗi
    Bạn sẽ cập nhật lại giá trị này để Python hiểu là đó là giá trị bị thiếu
    Danh sách "columns" chứa các tên cột mà bạn sẽ làm việc với bài tập này.

Hướng dẫn :
    - Nhìn vào dtypes của các cột trong "columns" : để chắc chắn dữ liệu là số
    - Có vẻ như một chuỗi đang được sử dụng như một giá trị bị thiếu bị mã hóa
    Sử dụng phương thức .unique() để tìm ra chuỗi đó
    - Tìm kiếm giá trị bị thiếu trong các cột : "median", "p25th", "p75th"
    - Thay thế giá trị tìm thấy bằng giá trị "NaN", sử dụng np.nan

Gợi ý :
    Thử chọn một trong 3 cột và sau đó xem thuộc tính ".dtypes" của kết quả DataFrame
    Gọi phương thức .unique() cho cột "median"
    Sử dụng biểu thức boolean để lọc các cột sao cho bạn chỉ có các hàng có giá trị 'UN'.
    numpy có một đối tượng np.nan mà bạn có thể sử dụng để thay thế các giá trị.

'''

# Names of the columns we're searching for missing values 
columns = ['median', 'p25th', 'p75th']

# Take a look at the dtypes
print(recent_grads[columns].dtypes)

# Find how missing values are represented
print(recent_grads["median"].unique())

# Replace missing values with NaN
for column in columns:
    recent_grads.loc[recent_grads[column] == 'UN', column] = np.nan
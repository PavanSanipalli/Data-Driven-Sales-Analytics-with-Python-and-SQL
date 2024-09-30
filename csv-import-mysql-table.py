import pandas as pd


df = pd.read_csv("C:\\ProgramData\\MySQL\\MySQL Server 8.0\\Uploads\\Sales_DataSet.csv")

#2. Drop Unnecessary Columns.

#       print(df[columns])
#       print(df.columns.value_counts())

col = ['Row ID', 'Order ID', 'Ship Date', 'Ship Mode', 'Customer Name', 'Segment', 'Country', 'City', 'State',
       'Postal Code', 'Product ID', 'Category', 'Sub-Category', 'Quantity', 'Discount', 'Profit']

df.drop(col, inplace=True, axis=1)

#print(df.head())


#3. Check For missing Values.

#print(df.isnull().sum())


#4   Drop rpws with missing values.
df = df.dropna()
df = df.fillna(0)


#5. Remove duplicate rows.

print(df.duplicated().sum())


#Rename columns to lowercase and remove spaces.
print(df.columns)


#4. Handle or data types...

df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
df['Order Date'] = df['Order Date'].dt.strftime('%Y-%m-%d')




#print(df.dtypes)



#5. DataFrame Export.
y = []
for i in range(len(df)):
    x = tuple(df.iloc[i])
    y.append(x)

#print(y)


# 6. Write the list of tuples to a text file.
with open('float-file.txt', 'w') as file:
    for tuples in y:
        file.write(str(tuples) + '\n')




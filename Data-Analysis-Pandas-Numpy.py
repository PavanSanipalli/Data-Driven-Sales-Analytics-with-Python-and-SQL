import pandas as pd
import numpy as np
import plotly.express as px

df = pd.read_csv("C:\\Users\\pavan\\PycharmProjects\\SuperStore-Connection-MySQL\\Sales.csv")
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Month'] = df['Order Date'].dt.to_period('M')


class DataAnalysis:
    def __init__(self, df):
        self.df = df

# Basic Statistics
    def basic_statistics(self):
        mean_sales = self.df['Sales'].mean()
        median_sales = self.df['Sales'].median()
        std_sales = self.df['Sales'].std()

        print(f"Mean Sales : {mean_sales}")
        print(f"Median Sales : {median_sales}")
        print(f"Standard Deviation of Sales : {std_sales}")

# Group and aggregating data
    def sales_by_month(self):
        sales_by_month = self.df.groupby('Month')['Sales'].sum()
        print("\nTotal Sales by Month : ")
        print(sales_by_month)
        return sales_by_month


#Total Sales by Product..
    def sales_by_product(self):
        sales_by_product = self.df.groupby('Product Name')['Sales'].sum()
        print("\nTotal Sales by Product : ")
        print(sales_by_product)
        return sales_by_product


#Identifying the trends.........
    def sales_trend_by_month(self):
        #Check Sales trend by month.
        monthly_sales_trend = self.df.groupby(df['Month'].dt.month)['Sales'].sum()
        print("\n Monthly Sales Trend")
        print(monthly_sales_trend)
        return monthly_sales_trend


#Best Selling Products..
    def best_selling_products(self):
        """Prints and returns the best-selling products based on total sales."""
        sales_by_product = self.sales_by_product()
        best_selling_products = sales_by_product.sort_values(ascending=False)
        print("\nBest Selling Products:")
        print(best_selling_products)
        return best_selling_products


#Regional Sales trends.
    def sales_by_region(self):
        sales_by_region = self.df.groupby('Region')['Sales'].sum()
        print("\nSales by Region : ")
        print(sales_by_region)
        return sales_by_region

    def plot_sales_by_month(self):
        sales_by_month = self.sales_by_month()
        fig = px.line(sales_by_month, x=sales_by_month.index.astype(str), y=sales_by_month.values,
                      title='Total Sales by Month', labels={'x': 'Month', 'y': 'Sales'})
        fig.show()
    def plot_sales_by_product(self):
        sales_by_product = self.sales_by_product()
        fig = px.bar(sales_by_product, x=sales_by_product.index, y=sales_by_product.values,
                     title='Total Sales by Product', labels={'x': 'Product Name', 'y': 'Sales'})
        fig.show()
    def plot_monthly_sales_trend(self):
        monthly_sales_trend = self.sales_trend_by_month()
        fig = px.line(monthly_sales_trend, x=monthly_sales_trend.index, y=monthly_sales_trend.values,
                      title='Monthly Sales Trend', labels={'x': 'Month', 'y': 'Sales'})
        fig.show()
    def plot_best_selling_products(self):
        best_selling_products = self.best_selling_products()
        fig = px.bar(best_selling_products, x=best_selling_products.values, y=best_selling_products.index,
                     orientation='h', title='Best Selling Products', labels={'x': 'Sales', 'y': 'Product Name'})
        fig.show()
    def plot_sales_by_region(self):
        sales_by_region = self.sales_by_region()
        fig = px.pie(sales_by_region, names=sales_by_region.index, values=sales_by_region.values,
                     title='Sales by Region')
        fig.show()



analysis = DataAnalysis(df)

analysis.basic_statistics()


analysis.sales_by_month()
analysis.sales_by_product()
analysis.sales_by_region()
analysis.best_selling_products()
analysis.sales_trend_by_month()


analysis = DataAnalysis(df)


analysis.plot_sales_by_month()
analysis.plot_sales_by_product()
analysis.plot_monthly_sales_trend()
analysis.plot_best_selling_products()
analysis.plot_sales_by_region()
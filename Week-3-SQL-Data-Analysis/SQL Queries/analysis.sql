SELECT * FROM sales;   -- View data
SELECT COUNT(*) AS Total_Orders FROM sales;   -- Total Orders
SELECT ROUND(SUM(TotalPrice), 2) AS Total_Revenue FROM sales;   -- Total Revenue
SELECT ROUND(AVG(TotalPrice), 2) AS Average_Order_Value FROM sales;   -- Average Order Value
SELECT Product, ROUND(SUM(TotalPrice), 2) AS Revenue FROM sales GROUP BY Product ORDER BY Revenue DESC;   -- Highest Revenue Products
SELECT Product, SUM(Quantity) AS Quantity_Sold FROM sales GROUP BY Product ORDER BY Quantity_Sold DESC;   -- Quantity Sold
SELECT PaymentMethod, COUNT(*) AS Orders FROM sales GROUP BY PaymentMethod ORDER BY Orders DESC;   -- Orders by Payment Method
SELECT OrderID, Product, TotalPrice FROM sales ORDER BY TotalPrice DESC LIMIT 10;   -- Top 10 Expensive Orders
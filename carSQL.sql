use car_db;
select*from cars;

-- Total Cars
SELECT COUNT(ID) AS Total_Cars
FROM cars;

-- Average Price
SELECT AVG(Price) AS Avg_Price
FROM cars;

-- Maximum Price
SELECT MAX(Price) AS Max_Price
FROM cars;

-- Average Car Age
SELECT AVG(car_age) AS Avg_Car_Age
FROM cars;

-- Price by Manufacturer
SELECT Manufacturer, AVG(Price) AS Avg_Price
FROM cars
GROUP BY Manufacturer
ORDER BY Avg_Price DESC;

-- Price by Fuel Type
SELECT Fuel_type, AVG(Price) AS Avg_Price
FROM cars
GROUP BY Fuel_type;

-- Price by Gear Box Type
SELECT Gear_box_type, AVG(Price) AS Avg_Price
FROM cars
GROUP BY Gear_box_type;

-- Price by Category
SELECT Category, AVG(Price) AS Avg_Price
FROM cars
GROUP BY Category;

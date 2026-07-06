use sales_project;

select * from product_sales_dataset;

select * from product_sales_dataset limit 10;

alter table product_sales_dataset
rename to sales_data;

-- rename table product_sales_dataset to sales_data;

desc sales_data;

select * from sales_data;

select * from sales_data limit 10;

select count(*) from sales_data;

-- remove null values
delete from sales_data
where order_id is null
	or order_date is null
    or product_name is null;
    
set sql_safe_updates=0;

UPDATE sales_data
SET order_date = 
    CASE
        -- Format: MM/DD/YYYY (e.g., 12/11/2024)
        WHEN order_date LIKE '%/%/%' AND LENGTH(order_date) = 10 
            THEN STR_TO_DATE(order_date, '%m/%d/%Y')

        -- Format: MM/DD/YY (e.g., 08/23/23)
        WHEN order_date LIKE '%/%/%' AND LENGTH(order_date) = 8 
            THEN STR_TO_DATE(order_date, '%m/%d/%y')

        -- Format: MM-DD-YY (e.g., 08-23-23)
        WHEN order_date LIKE '%-%-%' AND LENGTH(order_date) = 8 
            THEN STR_TO_DATE(order_date, '%m-%d-%y')

        -- Format: MM-DD-YYYY (if exists)
        WHEN order_date LIKE '%-%-%' AND LENGTH(order_date) = 10 
            THEN STR_TO_DATE(order_date, '%m-%d-%Y')

        ELSE NULL
    END;

-- convert datatype
ALTER TABLE sales_data
MODIFY order_date DATE;

-- chech failed rows 
SELECT * 
FROM sales_data
WHERE order_date IS NULL;

-- feature engineering 
alter table sales_data add year int, add month int;

update sales_data
set year=year(order_date),
	month=month(order_date);

select * from sales_data;

-- 1. data cleaning 
-- check total records 
select count(*) from sales_data;

-- find duplicates
select  order_id, count(*) as duplicate_count
from sales_data
group by order_id
having count(*) >1;

-- which region generates highest revenue 
select region, sum(revenue) as total_revenue
from sales_data
group by region 
order by total_revenue desc;

-- top 10 most profitable products 
select product_name, sum(revenue) as total_revenue
from sales_data
group by product_name
order by total_revenue desc 
limit 10;

-- category porpularity by region
select region, category, sum(revenue) as total_revenue 
from sales_data
group by region, category
order by region, total_revenue desc;

select customer_name, sum(revenue) as total_revenue
from sales_data
group by customer_name
order by total_revenue desc
limit 10;

-- monthly trend 
SELECT 
    YEAR,
    MONTH,
    SUM(revenue) AS monthly_revenue
FROM sales_data
GROUP BY year, month
ORDER BY year, month;

-- best month
SELECT year, month, SUM(revenue) AS revenue
FROM sales_data
GROUP BY year, month
ORDER BY revenue DESC
LIMIT 1;

-- worst month
SELECT year, month, SUM(revenue) AS revenue
FROM sales_data
GROUP BY year, month
ORDER BY revenue ASC
LIMIT 1;

-- avg order values
select avg(revenue) as avg_order_value from sales_data;

-- total order per regoin 
select region, count(order_id) as total_orders 
from sales_data
group by region;

-- Month-over-Month Growth
SELECT year, month, revenue,
       LAG(revenue) OVER (ORDER BY year, month) AS prev_month,
       revenue - LAG(revenue) OVER (ORDER BY year, month) AS growth
FROM (
    SELECT year, month, SUM(revenue) AS revenue
    FROM sales_data
    GROUP BY year, month
) t;


-- Top Product per Region
SELECT region, product_name, total_revenue
FROM (
    SELECT region, product_name,
           SUM(revenue) AS total_revenue,
           RANK() OVER (PARTITION BY region ORDER BY SUM(revenue) DESC) AS rnk
    FROM sales_data
    GROUP BY region, product_name
) t
WHERE rnk = 1;

-- Category Contribution %
SELECT category,
       SUM(revenue) AS total_revenue,
       ROUND(SUM(revenue) * 100 / (SELECT SUM(revenue) FROM sales_data), 2) AS percentage
FROM sales_data
GROUP BY category;

-- Underperforming Products
SELECT product_name,
       SUM(revenue) AS total_revenue
FROM sales_data
GROUP BY product_name
ORDER BY total_revenue ASC
LIMIT 10;

-- average revenue per customer 
select customer_name, avg(revenue) as avg_revenue
from sales_data
group by customer_name
order by avg_revenue desc
limit 10;

-- revenue by catrgory per month 
select year, month, category, sum(revenue) as revenue
from sales_data
group by year, month, category;

-- check nulls
select * from sales_data where order_date is null;

-- check data format 
select order_date from sales_data limit 10;

-- check year/ month
select year, month from sales_data limit 10; 

select * from sales_data;

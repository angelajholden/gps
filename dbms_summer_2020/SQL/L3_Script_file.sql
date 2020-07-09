-- capture the results into a text file to print later
--
spool U:\XYZ\myresults.txt

-- setup the width and height of the page to print
--
set linesize 80;
set pagesize 64;

-- Set echo on so that you can see the input as well in the spool file
set echo on;

--
-- Team Number: 100
-- Team Members: Saeed Rahimi, John Doe
-- My SQL Statements
--

--
-- reduce the widths of column being printed
-- column cname format A10;
-- column bname format A15;
--
-- Q1: Print the name of all customers in the bank.
Select cname from customer;
--
-- Q2: Print the name of all branches in the bank
Select bname from branch;
--
--
-- Close the spool file
spool off;

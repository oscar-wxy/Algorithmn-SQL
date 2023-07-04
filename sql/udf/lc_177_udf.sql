
# if limit has to parameters
# the first is the offset, the second is the count
# https://leetcode.com/problems/nth-highest-salary/description/
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
Declare M Int;
Set M=N-1;
  RETURN (
      # Write your MySQL query statement below.
      select distinct salary from employee order by salary desc limit m,1
  );
END
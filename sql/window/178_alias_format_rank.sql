# Write your MySQL query statement below

# below works
Select
s.score,
(select count(distinct score) from Scores where Score >= s.Score)  as 'rank'
from Scores s order by s.score desc

# below doesn't, the order can only recognize the column selected
# rank doesn't belong to Scores, that's why
Select
s.score,
(select count(distinct score) from Scores where Score >= s.Score)  as 'rank'
from Scores s order by rank  desc

# if really wants to order by rank
# Write your MySQL query statement below
select p.* from (Select
s.score,
(select count(distinct score) from Scores where Score >= s.Score)  as 'rank'
from Scores s) p order by p.rank

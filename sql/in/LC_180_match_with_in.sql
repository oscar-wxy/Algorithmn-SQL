# this is an example about how to match with in
select
distinct Num as ConsecutiveNums from Logs
where (id+1, num) in (select * from Logs) and (id+2,num) in (select * from Logs)
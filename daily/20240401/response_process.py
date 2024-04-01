# 输入
region = "jp"
execute_pending_records = {
"jp-20240302":1, 
"jp-20240303": 3
}
msg_arr = ["The number of records for date: 20240301 in status Pending is 18",
"The number of records for date: 20240301 in status Processed is 20",
"The number of records for date: 20240301 in status ProcessFailed is 23",
"The number of records for date: 20240301 in status Unprocessed is 25",
"The number of records for date: 20240302 in status Pending is 0",
"The number of records for date: 20240302 in status Processed is 20",
"The number of records for date: 20240302 in status ProcessFailed is 23",
"The number of records for date: 20240302 in status Unprocessed is 25",
"The number of records for date: 20240303 in status Pending is 1",
"The number of records for date: 20240303 in status Processed is 20",
"The number of records for date: 20240303 in status ProcessFailed is 23",
"The number of records for date: 20240303 in status Unprocessed is 25"]

def func(region, execute_pending_records):
	# print 更新后的execute_pending_records
	# 返回重跑Pending的command
    command_list = []
    command = "./batch-job.sh parser_orchestrastor "
    for msg in msg_arr:
        if "Pending" in msg:
            date = msg.split(" ")[6]
            num = int(msg.split(" ")[-1])
            key = region + "-" + date
            if num != 0:
                command += date+' '+region+'- Pending'
                command_list.append(command)
                command = "./batch-job.sh parser_orchestrastor "
                execute_pending_records[key] = execute_pending_records.get(key, 0) + 1
            else:
                if key in execute_pending_records:
                    execute_pending_records.pop(key)

    print(execute_pending_records)
    return command_list


c_l=func(region, execute_pending_records)
print(c_l)
def deletion_order(data_list,priority):
    if priority == "frequency":
        print(sorted(data_list, key = lambda item: item["frequency"]))
    elif priority == "last_updated":
        print(sorted(data_list, key = lambda item: item["last_updated"]))   


data_list = [{"id":"data1","last_updated":"18-03-2021","frequency":77},
{"id":"data5","last_updated":"18-03-2021","frequency":65},
{"id":"data3","last_updated":"19-03-2021","frequency":44},
{"id":"data4","last_updated":"01-03-2021","frequency":34},
{"id":"data2","last_updated":"20-03-2021","frequency":28},
]
deletion_order(data_list,priority="frequency")
  
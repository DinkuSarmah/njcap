import json
import numpy as np
arr = []
data_dict = []
with open("scheme_no.txt", "r") as f:
    for line in f:
        arr.append(int(line[:-1]))

for num in arr:
    with open ("funds_nav/"+str(num)+'.json','r') as f:
        json_string = ''
        data = []
        for line in f:
            json_string+=line

        json_data = json.loads(json_string)
        
        for nav_data in json_data["data"]:
            data.append(float(nav_data["nav"]))

        
        variance = np.var(data)
        cag = np.mean(data)
        data_object  = {"cag":cag, "risk":variance}
        meta_object = json_data["meta"]
        data_dict.append({"meta":meta_object,"data":data_object})
    print(num)
    
with open("funds_stats/" + "stats" + ".json", "w") as f:
        f.write(json.dumps(data_dict))


import json
data=[{"ini":"adas","zcfas":"retyre"}]
json_str=json.dumps(data,ensure_ascii=False)#ascii转中文
#转换数据类型
print(json_str)
d='[{"asdas":"sdas"},{"wrtwe":"hdfvsd"}]'
a=json.loads(d)
print(a)
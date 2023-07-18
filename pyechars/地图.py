from  pyecharts.charts import  Map
from  pyecharts.options import *
map=Map()
data=[
    ("北京市",99),
    ("安徽省",199),
    ("江苏省",299),
    ("上海市",399),
    ("江西省",499)
]
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min":1,"max":99,"label":"1-9","color":"#ccffff"},
            {"min": 100, "max": 199, "label": "100-199", "color": "#ccffff"},
            {"min": 200, "max": 299, "label": "200-299", "color": "#ff6666"},
            {"min": 300, "max": 399, "label": "300-399", "color": "#990033"},
            {"min": 400, "max": 499, "label": "400-499", "color": "#442255"}
        ]
    )
)
map.add("中国地图",data,"china")
map.render("地图.html")
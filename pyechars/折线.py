from pyecharts.charts import Line
from pyecharts.options import TitleOpts,ToolboxOpts,VisualMapOpts
line=Line()
#创建一个折线图对像
line.add_xaxis(["adsas","dadas","adtq"])#x轴
line.add_yaxis("das",[2311,231,554])#y轴
line.set_global_opts(
    title_opts=TitleOpts(title="GDP展示",pos_left="center",pos_top="1"),#标题
    toolbox_opts=ToolboxOpts(is_show=True),#工具箱
    visualmap_opts=VisualMapOpts(is_show=True)#视觉展示
)
line.render()#生成图像
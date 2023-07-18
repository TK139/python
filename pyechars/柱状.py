from pyecharts.charts import Bar
from pyecharts.options import *
bar=Bar()
bar.add_xaxis(["张三","李四","王五"])
bar.add_yaxis("分数",[70,80,90],label_opts=LabelOpts(position="right"))#数值放在右边
bar.reversal_axis()#x轴和y轴的翻转
bar.render("柱状图.html")

import package.k1
import package.k2
package.k1.a(1,2)
package.k2.b(1,2)
# 包类似于文件夹，把模块包括在包里，类似于路径，需要写具体
from package import k1
k1.a(1,2)
from package.k2 import b
b(1,2)
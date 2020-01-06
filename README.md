Python调用C#的.so文件来实现Python和C#的交互。
# 方法一：使用[PythonNet](https://pypi.org/project/pythonnet/2.2.1/) 包
> Python for .NET is a package that gives Python programmers nearly seamless integration with the .NET Common Language Runtime (CLR) and provides a powerful application scripting tool for .NET developers. It allows Python code to interact with the CLR, and may also be used to embed Python into a .NET application.

相较于另一个Python调用C#的包[IronPython](https://github.com/IronLanguages/ironpython3)，PythonNet是以Python为主体去调用的C#接口，而IronPython是.Net为主体，部分功能使用Python。

# 使用流程
### 安装PythonNet
- `pip install pythonnet` _这里直接使用来pip来进行安装，在使用conda安装的时候提示没有找到安装包_
### 生成类库
- 参考[C#生成dll类库]()，这里注意在使用VS生成类库的时候，生成的目标平台选择`X86`或者`x64`，应用程序的输出类型改为类库。
### 实际应用
- C#代码 `Class1.cs`
```C#
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Multi
{
    public class Class1
    {
        public void Show(int a,int b)
        {
            Console.WriteLine((Math.Pow(a, b).ToString()));
            Console.Read();
        }
    }
}
```
- Python代码 `test.py`
```Python
import clr
clr.AddReference('Multi') #加载的dll文件名称

from Multi import * #导入命名空间

cla=Class1() # 调用dll接口
cla.Show(2,3) # 接口使用
```
上面的Python代码在运行的时候要求C#的类库生成文件 `xxx.dll` 和Python文件处于同一个目录，如果需要在其他目录进行调用需要使用Python的 `sys` 包中 `append` 函数来添加工作目录。
```Python
import system
system.path.append("x://xxxxx//xxx")
```


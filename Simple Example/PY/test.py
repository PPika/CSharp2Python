import clr
import sys
sys.path.append(r'F:\DEMO\CSharp2Python\Simple Example\Multi\bin\Debug')

clr.AddReference('Multi')

from Multi import *

tt=Class1()
tt.Show(2,3)

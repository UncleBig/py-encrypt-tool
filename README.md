# py2so

编译py为so文件，更好的隐藏源码

# 准备工作

```
系统安装python-devel 和 gcc
Python安装cython
```

# 调用方式

```
编译某个文件夹：
  python py2so.py mydir_path
```

# 生成的文件

```
mydir_path/build文件夹下即为结果目录
```

# 验证

```
在 mydir_path/build/xxx 下使用ipython或python进入命令行，引用包即可
```

# 数据加密

```
调用encrypt.py中的加密、解密函数对字符加密，输入输出都是字符串格式，方便写入文件
```


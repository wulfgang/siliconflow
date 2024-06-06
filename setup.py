from setuptools import setup, find_packages

setup(
    # 包的名称
    name='siliconflow',

    # 包的版本
    version='0.1.0',

    # 包的描述
    description='A simple package to interact with SiliconFlow chat completion APIs',

    # 长描述，可以是 README 文件的内容
    long_description=open('README.md').read(),

    # 包的URL
    url='https://github.com/wulfgang/siliconflow',

    # 作者
    author='wulfgang',

    # 作者的电子邮箱
    author_email='wulfgang@163.com',

    # 许可证
    license='MIT',

    # 包包含的Python代码文件或目录
    packages=find_packages(),

    # 包依赖的其他库
    install_requires=[
        'requests>=2.25.1',
        # 如果有其他依赖，也在这里列出
    ],

    # 包需要的Python版本
    python_requires='>=3.6',

    # 其他元数据
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],

    # 包含的数据文件（如果有）
    include_package_data=True,
)

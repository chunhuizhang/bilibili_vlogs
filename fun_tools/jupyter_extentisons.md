

- 创建虚拟环境用于测试
    ```
    conda create -n jpt python=3.8 -y
    conda activate jpt
    ```
    
- 安装 jupyter
    ```
    pip install jupyter
    ```
    - 注意 notebook（会在安装 jupyter 时自动安装 notebook） 的版本
        ```bash
        pip install notebook==6.1.5
        ```

- 安装拓展
    ```
    pip install jupyter_contrib_nbextensions 
    pip install jupyter_nbextensions_configurator 
    jupyter contrib nbextension install --user
    ```
    

- 几个常用的拓展 
    - ExcecuteTime
    - Table of Contents 
    - Variable Inspector
    - Autopep8
    
# CloudPCAutoTest

基本功能：

使用selenium+Pytest+allure（后期可结合Jenkins落地）对Electron桌面程序，进行UI自动化测试。


环境准备：

	下载程序相应版本的chromedriver，配置driver到环境变量中
	安装selenium-client：终端pip install selenium 即可
	安装Pytest：终端pip install -U pytest 即可
	安装allure报告工具：pip install allure-pytest

执行用例：

Pycharm可以直接修改执行方式为pytest，邮件pytest执行整个项目，或者执行单个文件或单条case

命令行执行：

终端：pytest --alluredir=/tmp/my_allure_results test_demo.py


详细参数可见allure和pytest官方文档：

Pytest官方文档：https://docs.pytest.org/en/stable/
Allure官方文档：https://docs.qameta.io/allure/ 
Allure也可终端执行allure –help 命令查看用法


生成浏览器报告：

终端：allure serve /tmp/my_allure_results ，此方式会自动生成一个服务，访问浏览器即可查看报告。
也可执行：allure generate /tmp/my_allure_results ，生成html格式报告，双击即可本地打开。 


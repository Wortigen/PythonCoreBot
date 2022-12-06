
import os

main_path_base = os.getcwd()
main_folder_name = "New_bot_core"
main_path_project = main_path_base + "/" + main_folder_name
main_autoload = "autoload.py"

param = dict()
param["base_path"] = main_path_base
param["app_path"] = main_path_project
param["name"] = main_folder_name
param["schema"] = list()

exec(open(main_path_project+"/"+main_autoload).read())

app = Core(param)
app.Run()

#exec(open("./New_bot_core/init.py").read())

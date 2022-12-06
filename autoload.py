from pathlib import Path

main_libs = "libs"
main_action = "actions"
main_struct = "struct"
main_schema = "schema"

param["action_path"] = main_path_project + "/" + main_action
param["schema_path"] = main_path_project + "/" + main_schema
param["struct_path"] = main_path_project + "/" + main_struct
param["config_path"] = main_path_project + "/config"
param["temp_path"] = main_path_project + "/temp"


path_for_load = main_path_project + "/"

temp_path_script = path_for_load + main_libs
temp_scripts = os.listdir(temp_path_script)
for x in temp_scripts:
 script_name = x.split('.')[0]
 script_exp = x.split('.')[1]
 if script_exp == "py":
     file = Path(temp_path_script + "/" + script_name + ".py")
     if file.is_file():
         exec(open(file).read())

temp_path_script = path_for_load + main_schema
temp_scripts = os.listdir(temp_path_script)
for x in temp_scripts:
  script_name = x.split('.')[0]
  script_exp = x.split('.')[1]
  if script_exp == "py":
      file = Path(temp_path_script + "/" + script_name + ".py")
      if file.is_file():
          exec(open(file).read())

temp_path_script = path_for_load + main_struct
temp_scripts = os.listdir(temp_path_script)
for x in temp_scripts:
  script_name = x.split('.')[0]
  script_exp = x.split('.')[1]
  if script_exp == "py":
      file = Path(temp_path_script + "/" + script_name + ".py")
      if file.is_file():
          exec(open(file).read())

temp_path_script = path_for_load + main_action
temp_scripts = os.listdir(temp_path_script)
for x in temp_scripts:
 script_name = x.split('.')[0]
 script_exp = x.split('.')[1]
 if script_exp == "py":
     file = Path(temp_path_script + "/" + script_name + ".py")
     if file.is_file():
         exec(open(file).read())

del temp_scripts, temp_path_script

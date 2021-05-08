#DatabricksConnectEnv
## Description
a very simple and small script yet effective in it's usage and therefore worth to share. If you had the same problem like me working in several projects with different databricks workspaces at the same time and using databricks connect to keep your workflow smooth with your beloved IDE, than this script might be for you. Since I had to switch not only between clusters but between databricks instances I needed to update the the `.databricks-connect` file on the user folder. This can be annyoing since you need to enter all parameters by hand. With this script you create simple json file where you can store all your configurations, so you can update the databricks-connect configuration with one single line of code.

## Options
Lets make it short. You will have three super basic functions:
- `-ls` to list all available configurations in your `db_environment.json` file
- `-get` to choose one of your configs to be active
- `-set` to create a new configuration 

## How to use it
First of all you can clone the repository to get the script an the demo db_environment.json file. I would recommend to copy those files to your user base folder */Users/YOURUSER/*. This way you would just need to open the console and the script works without any adjustments.

If you want to show all available environments you can call:
`python dbenv.py -ls`
This will print all available configurations in the console

If you want to create a new environment use: `python dbenv.py -set NEW ENV NAME`
After that you will put all parameters in a console dialog as you would do normally when you call the normal `databicks-connect configure` command.

If you want to select a specific instance or configuration to be active run the command `python dbenv.py -get ENV NAME`. This will update the `.databricks-connect` file for you and you can directly start using it without going to the process of doing the manual configuration dialog again.

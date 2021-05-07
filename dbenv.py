#!/usr/bin/env python3

def get_config():
    
    # get environment form json storage
    with open("db_environments.json", "r") as config_file:
        configs = json.load(config_file)
    
    try:
        db_env = configs[env]
        
        # replace existing databricks configuration
        with open(".databricks-connect", "w") as db_connect_env:
            json.dump(db_env, db_connect_env, indent=4)
        
        
    except KeyError:
        print(f"no databricks environment {env} is available. try to set it")


def set_config(env_name: str):
    
    # add a new configuration to the json storage 
    # get environment form json storage

    with open("db_environments.json", 'r') as config_file:
        try:
            configs = json.load(config_file)
        except (JSONDecodeError, TypeError):
            configs = dict()
        
    new_env = dict()
    for param in ["host", "token", "cluster_id", "org_id", "port"]:
        value = str(input(f"{param}: "))
        new_env[param] = value
    
    configs[env_name] = new_env
    with open("db_environments.json", "w") as config_file:
        configs = json.dump(configs, config_file)


def ls_config():

    with open("db_environments.json", 'r') as config_file:
        try:
            configs = json.load(config_file)
        except (JSONDecodeError, TypeError) as e:
            configs = dict()
            print(e) 
    
    print("\nfollowing environments are available:")
    for key, values in configs.items():
        print(f"\nEnvironment: {key}")
        for param, setting in values.items():
            print(f"{param}: {setting}")
    
        

if __name__ == "__main__":
    import sys
    import json
    from json.decoder import JSONDecodeError
    
    # get arguments from command line
    script = sys.argv[0]
    action = sys.argv[1]

    try:
        env = sys.argv[2]
    except IndexError:
        env = ""
    
    # check if action is available
    assert action in ["-get", "-set", "-ls"], f"action is missing please check available options (-ls, -get or -set)"
    
    
    if action == "-get":
        get_config()
    elif action == "-set":
        set_config(env_name=env)
    else:
        ls_config()
        
        
        

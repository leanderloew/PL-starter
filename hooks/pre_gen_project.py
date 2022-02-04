import os
env_path = "../{{cookiecutter.project_name}}/.envs/"
os.makedirs(env_path, exist_ok=True)
with open(env_path+"gen.env", "w") as file:
    file.write("PYTHONPATH = /app\n")
with open(env_path+"dev.env", "w") as file:
    pass
with open(env_path+"prod.env", "w") as file:
    pass
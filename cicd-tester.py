from os import system, makedirs
from glob import glob
from pathlib import Path
from shutil import copy, rmtree

def pull_templates() -> Path:
    """Clones or pulls the cicd-templates repo. Returns the resulting Path"""
    templates_dir = Path("./cicd-templates").resolve()

    if not templates_dir.exists():
        print("cicd-templates not found")

        repo = input("Enter cicd-templates repo url: ")

        print("Cloning...")
        system(f"git clone {repo}")
        print("Cloned")
    else:
        print("Pulling latest templates...")

        system(f'pushd "{templates_dir}" && git pull && popd')
    
    print("cicd-templates up to date")
    
    return templates_dir

def collect_woodpecker(source_dir: Path):
    """Clear local .woodpecker configs, then find all woodpecker files in source_dir and copy them to .woodpecker"""
    source_dir = source_dir.relative_to(Path.cwd())
    destination_dir = Path(".woodpecker")

    if destination_dir.exists():
        rmtree(destination_dir)
    
    makedirs(destination_dir, exist_ok=True)

    files = glob(str(source_dir.joinpath("**/*woodpecker*.yml")), recursive=True)

    for file in files:
        new_filename = file.split("woodpecker/", 1)[1].replace("/", "-")
    
        copy(file, destination_dir.joinpath(new_filename))

if __name__ == "__main__":

    templates_dir = pull_templates()
    
    collect_woodpecker(source_dir=templates_dir)

        





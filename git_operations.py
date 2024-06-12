import subprocess
import importlib.util

def ensure_gitpython_and_push(repo_path, commit_message):
    package_name = 'gitpython'

    # Fonction pour vérifier si un package est installé
    def is_installed(package_name):
        spec = importlib.util.find_spec(package_name)
        return spec is not None

    # Vérifier si GitPython est installé, sinon l'installer
    if not is_installed(package_name):
        subprocess.run(['py', '-m', 'pip', 'install', package_name], check=True)

    # Importer GitPython après l'installation
    import git

    # Utiliser GitPython pour effectuer un git push
    repo = git.Repo(repo_path)

    # Ajouter tous les fichiers modifiés
    repo.git.add('--all')

    # Faire un commit
    repo.index.commit(commit_message)

    # Effectuer un push
    origin = repo.remote(name='origin')
    origin.push()



# Utiliser la fonction
repo_path = './'
commit_message = 'Votre message de commit'
ensure_gitpython_and_push(repo_path, commit_message)

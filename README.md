# Fase de testes ainda:

O script está em fase de testes mas já está funcionando normal. Se tiver alguma ideia de adição, você pode adicionar<br>
ou me chame e me fale para que eu possa adicionar!

# Sobre o script:

git.py  é uma ferramenta feita para baixar arquivos e informações de repositórios Git expostos em servidores web.<br>
Ela utiliza o conceito de fuzzing para acessar e explorar arquivos de um repositório Git, como .git/config, .git/HEAD, .git/index, entre outros, que podem revelar informações sensíveis, como configurações de repositório, logs de commit e até credenciais.<br>

O objetivo desta ferramenta é auxiliar na avaliação de segurança, permitindo avaliar se repositórios Git estão sendo expostos sem devida proteção.

# Funcionalidade

Exploração de arquivos Git: O script acessa arquivos comuns de repositórios Git expostos em servidores web, como .git/config, .git/HEAD, .git/index, e outros.
Recuperação de dados: A ferramenta tenta explorar diferentes caminhos de arquivos Git em busca de dados sensíveis.
Exposição de arquivos Git: Quando um servidor expõe arquivos Git sem proteção, esses arquivos podem conter informações como chaves de acesso, configurações de repositórios e históricos de commits.

# Como usar:

    git clone https://github.com/Nanxsec/GitFile
    cd GitFile
    python3 git.py ALVO-AQUI

# Observações:

O script é básico, apenas faz o download dos repositórios se caso estejam disponíveis!<br>
Você pode ficar a vontade para alterar esse script e deixá-lo do jeito que quiser.<br>
Você pode personalizar a lista de arquivos Git e diretórios no script, dependendo da necessidade do seu pentest. Basta editar a lista de arquivos na função principal.

# Estrutura de arquivos:

    .git/
    ├── HEAD
    ├── config
    ├── COMMIT_EDITMSG
    ├── description
    ├── hooks/
    │   ├── applypatch-msg.sample
    │   ├── commit-msg.sample
    │   ├── post-commit.sample
    │   └── pre-commit.sample
    ├── index
    ├── info/
    │   └── exclude
    └── objects/
        └── info/
            └── packs

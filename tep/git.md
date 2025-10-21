# 🧰 Guia de Comandos Git — Curso Sistemas para Internet | UNIESP

Este guia reúne os comandos mais usados no Git Bash para gerenciar repositórios, incluindo comandos de reversão para corrigir erros. Ideal para quem trabalha com múltiplos computadores e deseja manter o repositório organizado.

---

## 🔍 Verificar o estado do repositório

```bash
git status

O que faz: Mostra arquivos modificados, não rastreados e prontos para commit.

Quando usar: Antes de qualquer commit ou push.

➕ Adicionar arquivos ao staging

git add nome-do-arquivo
git add .  # adiciona todos os arquivos

O que faz: Prepara arquivos para serem salvos no próximo commit.

Quando usar: Após editar ou criar arquivos.

💾 Salvar alterações com commit

git commit -m "Mensagem explicando o que foi feito"

O que faz: Salva as alterações localmente com uma descrição.

Quando usar: Após adicionar arquivos com git add.

🚀 Enviar alterações para o GitHub

git push origin nome-da-branch

O que faz: Envia commits locais para o repositório remoto.

Quando usar: Após fazer commits que deseja sincronizar.

🔄 Atualizar seu repositório local

git pull origin nome-da-branch

O que faz: Baixa e aplica alterações do repositório remoto.

Quando usar: Antes de começar a trabalhar, para garantir que está com a versão mais atual.

🌿 Gerenciar branches

git branch              # lista branches
git branch nova-branch  # cria nova branch
git branch -d nome      # deleta branch

O que faz: Organiza diferentes linhas de desenvolvimento.

Quando usar: Para separar tarefas ou funcionalidades.

🔀 Fazer merge de branches

git checkout main
git merge nome-da-branch

O que faz: Junta o conteúdo de uma branch em outra.

Quando usar: Quando finaliza uma tarefa e quer integrar à principal.

🕵️ Ver histórico de commits

git log

O que faz: Exibe os commits realizados.

Quando usar: Para revisar alterações anteriores.

🏷️ Criar e gerenciar tags

git tag v1.0 -m "Versão inicial"
git push origin v1.0

O que faz: Marca versões específicas do projeto.

Quando usar: Para sinalizar entregas ou checkpoints importantes.

⏪ Comandos de reversão e correção

Desfazer alterações no arquivo (antes do commit)

git restore nome-do-arquivo

O que faz: Restaura o arquivo para o último commit.

Quando usar: Se editou algo errado e quer voltar ao estado anterior.

Remover arquivo do staging

git restore --staged nome-do-arquivo

O que faz: Remove o arquivo do staging sem apagar alterações.

Quando usar: Se adicionou por engano ao commit.

Desfazer último commit (mantendo alterações)

git reset --soft HEAD~1

O que faz: Remove o último commit, mas mantém os arquivos no staging.

Quando usar: Se cometeu com mensagem errada ou quer refazer.

Desfazer último commit (mantendo alterações no diretório)

git reset --mixed HEAD~1

O que faz: Remove o commit e staging, mas mantém os arquivos modificados.

Quando usar: Para revisar ou reorganizar os arquivos antes de novo commit.

Desfazer último commit (apagando alterações)

git reset --hard HEAD~1

O que faz: Remove o commit e apaga as alterações.

Quando usar: Se quer descartar completamente o que foi feito.

⚠️ Cuidado: --hard apaga tudo sem chance de recuperar.

Reverter um commit específico

git revert código-do-commit

O que faz: Cria um novo commit que desfaz o anterior.

Quando usar: Para desfazer algo já enviado ao GitHub sem apagar o histórico.

✅ Dicas finais

Sempre use git status antes de qualquer ação.

Faça git pull antes de começar a trabalhar em outro computador.

Use mensagens claras nos commits.

Evite reset --hard sem certeza absoluta.

Feito por Lucca — Curso Sistemas para Internet | UNIESP


---

👉 Agora é só colar esse conteúdo no arquivo `comandos_git.md` ou, se preferir, salvar como `.txt` (`comandos_git.txt`).  

Quer que eu também monte um **exemplo prático de fluxo de trabalho** (do clone até o merge) para você incluir nesse guia como um "passo a passo real"?
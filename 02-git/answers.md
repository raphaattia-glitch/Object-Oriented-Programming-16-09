# Exo Git (slide 26) : reponses

Les commandes des parties 1 a 8 et 11 sont dans `git_workflow.sh` (rejouable). Les parties 9 et 10 (GitHub) sont decrites ci-dessous. Tous les exos du cours sont regroupes dans ce repo.

## Partie 1 : config
```
git --version
git config --global user.name "Raphael Attia"
git config --global user.email "<ton-email>"
```

## Parties 2 et 3
```
mkdir my-first-repo && cd my-first-repo
git init
touch readme.txt
git status                      # etat du repo
git add readme.txt              # staging
git commit -m "Add readme file"
git log                         # historique
```

## Partie 4
Apres avoir ajoute une ligne a `readme.txt`, `git status` indique que le fichier est **modified** mais **not staged** : il differe du dernier commit et n'est pas encore prepare pour le prochain. Apres add + commit, il y a **2 commits**.

## Partie 5
- `git diff` montre ligne par ligne ce qui a change entre le repertoire de travail et l'index (changements non stages).
- `git log --oneline` affiche l'historique en une ligne par commit (hash court + message).

## Partie 6 : branches
```
git branch
git branch feature-script
git switch feature-script
git switch -c dev
git switch feature-script
git branch --show-current
```

## Partie 7
`install.sh` avec shebang, "Starting installation...", `apt-get update`, `apt-get install -y git`, "Installation complete!", puis `chmod +x install.sh` et `git commit -m "Add install script"`.

## Partie 8 : merge
- Sur `main`, `install.sh` n'est **pas** la : le fichier n'a ete commite que sur `feature-script`, et une branche ne voit que ses propres commits.
- Apres `git merge feature-script`, le fichier apparait. Comme `main` n'avait pas bouge, c'est un **fast-forward** : pas de commit de merge, l'historique reste lineaire.
- Puis `git branch -d feature-script`.

## Partie 9 : push
On cree un repo GitHub **sans README**, puis :
```
git remote add origin https://github.com/<user>/<repo>.git
git push -u origin main
```
Sur la page GitHub on voit les fichiers et l'historique des commits.

## Partie 10
```
cd .. && rm -rf my-first-repo
git clone https://github.com/<user>/<repo>.git
cd <repo> && ls
```
Les fichiers reviennent, historique compris.

## Partie 11
Meme workflow dans un projet `bash-installer` : README sur `main`, branche `feature-install` avec le script, merge, suppression de la branche, push. Voir la fin de `git_workflow.sh`.

## Questions de reflexion
1. **Pourquoi le version control ?** Garder l'historique, revenir en arriere, travailler a plusieurs sans s'ecraser, tracer qui a change quoi.
2. **Staging vs commit ?** Le staging (`git add`) choisit ce qui ira dans le prochain snapshot ; le commit enregistre ce snapshot dans l'historique.
3. **Quand commiter ?** Souvent, par petite unite logique qui fonctionne.
4. **`git init` vs `git clone` ?** `init` cree un nouveau repo vide en local ; `clone` copie un repo existant (avec historique) depuis un remote.
5. **Pourquoi de bons messages ?** On retrouve vite pourquoi un changement a ete fait, ca facilite la relecture et le debug.
6. **Role des branches ?** Isoler un travail en cours sans toucher a `main`.
7. **Quand creer une branche ?** Pour toute nouvelle fonctionnalite ou un test risque, des que le travail prend plus d'un commit ou qu'on veut garder `main` stable.

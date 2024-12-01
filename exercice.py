# Liste des todos
todos = []

# Fonction pour lister les todos
def lister_todos():
    """Lister les todos existants."""
    if not todos:
        print('Aucun todo disponible.')
    else:
        print('\n==== Liste des todos ====')
        for i, todo in enumerate(todos, start=1):
            print(f'{i}. {todo["titre"]}')
        print('=========================')

# Fonction pour créer un todo
def creer_todo():
    """Créer un todo."""
    titre = input('Entrez le titre du todo : ')
    todos.append({'titre': titre})
    print(f'Todo "{titre}" ajouté avec succès !')

# Menu principal
choix = ''
while choix != 'q':
    print('\n==== Menu principal ====')
    print('1: Lister les todos')
    print('2: Créer un todo')
    print('q: Quitter')
    print('=========================')

    choix = input('=> Choix : ')

    if choix == '1':
        lister_todos()
    elif choix == '2':
        creer_todo()
    elif choix == 'q':
        print('Au revoir !')
    else:
        print('Choix incorrect.')

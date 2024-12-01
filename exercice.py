# Liste des todos
todos = []

# Fonction pour lister les todos
def lister_todos():
    """Lister les todos existants avec leur statut."""
    if not todos:
        print('Aucun todo disponible.')
    else:
        print('\n==== Liste des todos ====')
        for i, todo in enumerate(todos, start=1):
            print(f'{i}. {todo["titre"]} - Statut : {todo["statut"]}')
        print('=========================')

# Fonction pour créer un todo
def creer_todo():
    """Créer un todo."""
    titre = input('Entrez le titre du todo : ')
    todos.append({'titre': titre, 'statut': 'À faire'})  # Ajoute le statut "À faire" par défaut
    print(f'Todo "{titre}" ajouté avec succès avec le statut "À faire" !')

# Fonction pour modifier le statut d'un todo
def modifier_statut_todo():
    """Modifier le statut d'un todo."""
    if not todos:
        print('Aucun todo disponible pour modification.')
        return

    lister_todos()
    try:
        choix = int(input('Entrez le numéro du todo à modifier : '))
        if 1 <= choix <= len(todos):
            todo = todos[choix - 1]
            if todo['statut'] == 'À faire':
                todo['statut'] = 'Fait'
                print(f'Le statut du todo "{todo["titre"]}" est maintenant "Fait".')
            elif todo['statut'] == 'Fait':
                todo['statut'] = 'À faire' #Correction de l'erreur volontaire
                print(f'Le statut du todo "{todo["titre"]}" est maintenant "À fair".')
        else:
            print('Numéro de todo invalide.')
    except ValueError:
        print('Veuillez entrer un numéro valide.')

# Menu principal
choix = ''
while choix != 'q':
    print('\n==== Menu principal ====')
    print('1: Lister les todos')
    print('2: Créer un todo')
    print('3: Modifier le statut d\'un todo')
    print('q: Quitter')
    print('=========================')

    choix = input('=> Choix : ')

    if choix == '1':
        lister_todos()
    elif choix == '2':
        creer_todo()
    elif choix == '3':
        modifier_statut_todo()
    elif choix == 'q':
        print('Au revoir !')
    else:
        print('Choix invalide.')



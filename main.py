MENU = {
    "expresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}


def report(list_of_resources):
    for key in list_of_resources:
        if key == "coffee":
            unity = "g"
        elif key == "money":
            unity = "$"
        else:
            unity = "ml"
        print(f"{key}: {list_of_resources[key]}{unity}")


def ressources_checked(resources, user_wish):
    """Permet de vérifier les ressources et de les mettres à jour"""
    produits = MENU[user_wish]["ingredients"]
    cost = MENU[user_wish]["cost"]

    for ingredient in produits:
        # TODO 4.Vérifiez les ressources
        if produits[ingredient] > resources[ingredient]:
            print(f"Désolé il n'y a pas assez de {ingredient}")
            return
    print("Veuillez insérer des pièces.")
    quarters = int(input("Combien de quarters?: "))
    dimes = int(input("Combien de dimes?: "))
    nickles = int(input("Combien de nickles?: "))
    pennies = int(input("Combien de pennies?: "))
    # TODO 5.Traiter les pièces
    money_client = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    if money_client < cost:
        print("Désolé vous n'avez pas mis assez de pièce")
        return
    else:
        resources["money"] += cost
        rest_money_client = money_client - cost
        if rest_money_client > 0:
            print(f"Voici votre money de {rest_money_client} $")
        for ingredient in produits:
            resources[ingredient] -= produits[ingredient]
        print(f"Voici votre {user_wish} 🍵. Profitez-en !")


def coffe_machine():

    machine_on = True
    while machine_on:
        user_wish = input("Ques souhaitez-vous (expresso/latte/cappuccino): ").lower()
        # TODO 2.Lorsque l'on rentre off en était la machine a café
        if user_wish == "off":
            machine_on = False
        # TODO 3.Imprimez le rapport
        # TODO 6.Vérifiez que la transaction a réussi
        if user_wish == "report":
            report(resources)

        # TODO 1.Demandez à l'utilisateur ce qu'il souhaite
        if user_wish == "expresso" or user_wish == "latte" or user_wish == "cappuccino":
            ressources_checked(resources, user_wish)


coffe_machine()


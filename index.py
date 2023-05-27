import io

print("Bienvenue sur AMS !")
print("Quelle option souhaitez-vous ?")
print("1. Générer un fichier Ajout.js (adapté pour React)")
print("2. Générer un fichier Suppr.js (adapté pour React)")
print("3. Générer un fichier Modif.js (adapté pour React)")
print("4. Tous les fichiers")
print("5. Quitter")
print("6. Personnaliser")
print("7. Aide")

choix = input("Votre choix : ")

if choix == "1":
    print("Générer un fichier Ajout.js (adapté pour React)")
    continuer = "O"
    objets = []
    while continuer == "O":
        nom_champ = input("Entrez le nom du champ : ")
        type_champ = input("Entrez le type du champ : ")
        objets.append((nom_champ, type_champ))
        continuer = input("Voulez-vous ajouter un autre champ ? (O/N) : ")

    nom_fichier = input("Entrez le nom du fichier : ")

    with io.open(nom_fichier + ".js", "w", encoding="utf-8") as file:
        file.write(f"import React, {{usestate}} from 'react';\n")
        file.write("import React from 'react';\n")
        file.write("const " + nom_fichier + " = () => {\n")
        for champ, valeur in objets:
            if valeur == "radio":
                file.write(f"    const [{champ}, set{champ}] = useState('');\n")
        file.write(f"    const nouveau{nom_fichier} = " + "{\n")
        for champ, valeur in objets:
            file.write(f"        {champ},\n")
        file.write("    };\n\n")
        file.write(f"    fetch('http://localhost:5000/ajouter-{nom_fichier}', {{\n")
        file.write("        method: 'POST',\n")
        file.write("        headers: {\n")
        file.write("            'Content-Type': 'application/json'\n")
        file.write("        },\n")
        file.write(f"        body: JSON.stringify(nouveau{nom_fichier})\n")
        file.write("    })\n")
        file.write("        .then(response => response.json())\n")
        file.write("        .then(data => {\n")
        file.write("            console.log('Success:', data);\n")
        file.write("        })\n")
        file.write("        .catch((error) => {\n")
        file.write("            console.error('Error:', error);\n")
        file.write("        });\n\n")
        file.write("    return (\n")
        file.write("        <div>\n")
        for champ, valeur in objets:
            if valeur == "radio":
                file.write(f"           <label>\n")
                file.write(f"               {champ}\n")
                file.write(f"               <input type='radio' name='{champ}' value='{champ}' onChange={{e => set{champ}(e.target.value)}} />\n")
                file.write(f"           </label>\n")
        file.write("        </div>\n")
        file.write("    );\n")
        file.write("};\n\n")
        file.write("export default " + nom_fichier + ";")

    print("Fichier", nom_fichier + ".js créé !")

elif choix == "2":
    print("Générer un fichier Suppr.js (adapté pour React)")
elif choix == "3":
    print("Générer un fichier Modif.js (adapté pour React)")
elif choix == "4":
    print("Tous les fichiers")
elif choix == "5":
    print("Quitter")
elif choix == "6":
    print("Personnaliser")
elif choix == "7":
    print("Aide")
else:
    print("Choix invalide. Veuillez sélectionner une option valide.")

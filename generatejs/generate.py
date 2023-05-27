import io
from format.text import format_const_name


def generate_ajout_js_file():
    objets = []
    continuer = "O"
    while continuer == "O":
        nom_champ = input("Entrez le nom du champ : ")
        type_champ = input("Entrez le type du champ (texte / oui-non) : ")
        objets.append((nom_champ, type_champ))
        continuer = input("Voulez-vous ajouter un autre champ ? (O/N) : ")

    nom_fichier = input("Entrez le nom du fichier : ")

    with io.open(nom_fichier + ".js", "w", encoding="utf-8") as file:
        file.write("import React, { useState } from 'react';\n")
        file.write(f"const {nom_fichier} = () => {{\n")
        for champ, valeur in objets:
            const_name = format_const_name(champ)
            file.write(f"    const [{const_name}, set{const_name}] = useState('')\n")
        file.write("\n")
        file.write("    const handleAjouter = () => {\n")
        file.write("        // Créer un objet représentant les nouveaux champs\n")
        file.write("        const nouveauxChamps = {\n")
        for champ, valeur in objets:
            const_name = format_const_name(champ)
            file.write(f"            {const_name},\n")
        file.write("        };\n\n")
        file.write("        // Envoyer les données des nouveaux champs à une API ou une base de données\n")
        file.write("        fetch('http://localhost:5000/ajouter-champs', {\n")
        file.write("            method: 'POST',\n")
        file.write("            headers: {\n")
        file.write("                'Content-Type': 'application/json'\n")
        file.write("            },\n")
        file.write("            body: JSON.stringify(nouveauxChamps)\n")
        file.write("        })\n")
        file.write("            .then(response => {\n")
        file.write("                if (response.ok) {\n")
        file.write("                    console.log('Champs ajoutés avec succès');\n")
        file.write("                } else {\n")
        file.write("                    console.log('Une erreur est survenue');\n")
        file.write("                }\n")
        file.write("            })\n")
        file.write("            .catch(error => {\n")
        file.write("                console.error('Une erreur est survenue  ', error);\n")
        file.write("            });\n")
        file.write("    };\n\n")
        file.write("    return (\n")
        file.write("        <div>\n")
        for champ, valeur in objets:
            const_name = format_const_name(champ)
            file.write("            <label>\n")
            file.write(f"                {champ}\n")
            if valeur.lower() == "texte":
                file.write(f"                <input type='text' value={{{const_name}}} onChange={{e => set{const_name}(e.target.value)}} />\n")
            elif valeur.lower() == "oui-non":
                file.write(f"                <select value={{{const_name}}} onChange={{e => set{const_name}(e.target.value)}}>\n")
                file.write("                    <option value=''>-- Sélectionner --</option>\n")
                file.write("                    <option value='oui'>Oui</option>\n")
                file.write("                    <option value='non'>Non</option>\n")
                file.write("                </select>\n")
            file.write("            </label>\n")
        file.write("            <button onClick={handleAjouter}>Ajouter</button>\n")
        file.write("        </div>\n")
        file.write("    );\n")
        file.write("};\n\n")
        file.write(f"export default {nom_fichier};\n")

    print("Fichier", nom_fichier + ".js créé !")
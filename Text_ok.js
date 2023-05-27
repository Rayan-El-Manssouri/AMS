import React, { useState } from 'react';
const Text_ok = () => {
    const [text1, settext1] =  useState('')
    const [text2, settext2] =  useState('')

    const handleAjouter = () => {
        // Créer un objet représentant les nouveaux champs
        const nouveauxChamps = {
            Text1,
            Text2,
        };

        // Envoyer les données des nouveaux champs à une API ou une base de données
        fetch('http://localhost:5000/ajouter-champs', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(nouveauxChamps)
        })
            .then(response => {
                if (response.ok) {
                    console.log('Champs ajoutés avec succès');
                } else {
                    console.log('Une erreur est survenue');
                }
            })
            .catch(error => {
                console.error('Une erreur est survenue  ', error);
            });
    };

    return (
        <div>
            <label>
                Text1
                <select value={text1} onChange={e => settext1(e.target.value)}>
                    <option value=''>-- Sélectionner --</option>
                    <option value='oui'>Oui</option>
                    <option value='non'>Non</option>
                </select>
            </label>
            <label>
                Text2
                <input type='text' value={text2} onChange={e => settext2(e.target.value)} />
            </label>
            <button onClick={handleAjouter}>Ajouter</button>
        </div>
    );
};

export default Text_ok;

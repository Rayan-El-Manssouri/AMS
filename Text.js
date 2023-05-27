import React, { useState } from 'react';
const Text = () => {
    const [text2, settext2] =  useState('')
    const [text3, settext3] =  useState('')

    const handleAjouter = () => {
        // Créer un objet représentant les nouveaux champs
        const nouveauxChamps = {
            text2,
            text3,
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
                Text2
                <select value={text2} onChange={e => settext2(e.target.value)}>
                    <option value=''>-- Sélectionner --</option>
                    <option value='oui'>Oui</option>
                    <option value='non'>Non</option>
                </select>
            </label>
            <label>
                Text3
                <input type='text' value={text3} onChange={e => settext3(e.target.value)} />
            </label>
            <button onClick={handleAjouter}>Ajouter</button>
        </div>
    );
};

export default Text;

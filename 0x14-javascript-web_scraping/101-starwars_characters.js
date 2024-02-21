#!/usr/bin/node
const request = require('request');

// Function to fetch characters of a specific movie
function fetchCharacters(movieId) {
    const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
    
    request(url, (error, response, body) => {
        if (error) {
            console.error('Error:', error);
        } else {
            const film = JSON.parse(body);
            const charactersUrls = film.characters;
            
            // Fetching characters
            charactersUrls.forEach(characterUrl => {
                request(characterUrl, (error, response, body) => {
                    if (error) {
                        console.error('Error:', error);
                    } else {
                        const character = JSON.parse(body);
                        console.log(character.name);
                    }
                });
            });
        }
    });
}

// Retrieve movie ID from command line argument
const movieId = process.argv[2];
if (!movieId) {
    console.error('Please provide a movie ID.');
} else {
    fetchCharacters(movieId);
}

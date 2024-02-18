#!/usr/bin/node

const request = require('request');
// Parse the ID from the firstitional argument
const movieId = process.argv[2];
// Construct the URL the movie endpoint

const movieUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the movie endpoint
request(movieUrl, async (err, res, body) => {
  if (err) {
    console.log(err);
  } else if (res.statusCode !== 200) {
    console.log('Unexpected status code: ', res.statusCode);
  } else {
    const characterUrlsArray = JSON.parse(body).characters;

    // Define an async function to fetch character names
    const fetchCharacterNames = async () => {
      const characterPromises = characterUrlsArray.map(url => {
        return new Promise((resolve) => {
          request(url, (err, res, body) => {
            if (err) {
              console.error(err);
            } else if (res.statusCode !== 200) {
              console.log('Unexpected status code: ', res.statusCode);
            } else {
              const data = JSON.parse(body).name;
              // Print the character name
              console.log(data);
              resolve(data);
            }
          });
        });
      });

      // Wait for all character promises to resolve
      await Promise.all(characterPromises);
    };

    // Call the async function to fetch character names
    fetchCharacterNames();
  }
});

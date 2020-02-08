const express = require("express");
const fs = require('fs');
const path = require('path');
const pug = require("pug");

const jokes = require("./jokes.json")

const app = express();
app.set('view engine', 'pug');
app.set('views', path.join(__dirname, '/views'));

const port = 3000;

app.get("/", (req, res) => {
    res.render('index', {joke: jokes["jokes"][Math.floor(Math.random() * jokes["jokes"].length)]});
});

app.listen(port, () => {
    console.log(`Listening to port ${port}`);
});
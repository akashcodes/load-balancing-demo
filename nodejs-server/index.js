const express = require("express");
const path = require('path');
const fetch = require('node-fetch');
const jokes = require("./jokes.json")

const app = express();


// Make express app to use view engine as pug
app.set('view engine', 'pug');


// Set views directory
app.set('views', path.join(__dirname, '/views'));

// Server PORT
const port = 3000;

//Detault message to send at GET /
const WELCOME_RESPONSE = `
    <html>
        <head>
            <title>Welcome!</title>
        </head>
        <body>
            <u><h3>Hello, stranger! Welcome to my Cloud Computing assignment.</h3></u>
            <li>GET /dad-joke ; to get a random Dad Joke.</li>
            <li>GET /dad-joke/:number ; with param(number=[1-99]) to get a particular Dad Joke Indexed[1 to 99].</li>
            <li>GET /palindrome/:string ; to check whether the "string" is a palindrome string</li>
            <li>GET /fetch; fetch json dummy data</li>
            <br/><br/>
            Adios!
    </html>
`;


// Default router
app.get("/", (req, res) => {
    res.send(WELCOME_RESPONSE);
});


// GET dad joke
app.get("/dad-joke", (req, res) => {
    res.render('index', {joke: jokes["jokes"][Math.floor(Math.random() * jokes["jokes"].length)]});
});


// GET dad-joke at index 'number'
app.get("/dad-joke/:number", (req, res) => {
    if(req.params["number"] <= 0 || req.params["number"] >= 100)
        res.send("Invalid index. Please enter an index i from 1 to 99")
    var i = req.params["number"];
    res.render('index', {joke: jokes["jokes"][i]});
});


// GET check is string is palidrome
app.get("/palindrome/:string", (req, res) => {
    var str = req.params["string"];
    var flag = true;
    var l = 0;
    var r = str.length - 1;
    while(l < r) {
        if(str[l] != str[r]) {
            flag = false;
            break;
        }
        l++;
        r--;
    }

    if(flag)
        res.send("True");
    else
        res.send("False");
});


app.get("/fetch", (req, res) => {
    fetch('https://jsonplaceholder.typicode.com/todos/1').then(data => data.json()).then(json => res.send(json)).catch(err => res.send(err));
});


// Start listening
app.listen(port, () => {
    console.log(`Listening to port ${port}`);
});
const express = require("express");
const fs = require('fs');
var path = require('path');


const app = express();

const port = 3000;

app.get("/", (req, res) => {
    res.sendFile(path.resolve(__dirname, 'html/index.html'));
});

app.listen(port, () => {
    console.log(`Listening to port ${port}`);
});
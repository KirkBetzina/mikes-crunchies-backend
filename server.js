////////////////////////////////
// Boilerplate
////////////////////////////////
require("dotenv").config();
const express = require("express");
const mongoose = require("./db/connection");
const morgan = require("morgan");
const cors = require("cors");
const app = express();
const { PORT= 5000 } = process.env;
const NODE_ENV = "development";



////////////////////////////////
// Middleware
////////////////////////////////

app.use(express.json());
app.use(morgan("tiny")); //logging

////////////////////////////////
// Welcome route
////////////////////////////////

app.get("/", (req, res) => res.send({
    status: 200,
    msg: "Thank you for connecting to Mikes Crunchies API!"
}));

const menusController = require('./controllers/menus.js')
app.use('/menus', menusController)


app.listen(PORT, () => console.log(`port running on ${PORT}`));
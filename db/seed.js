const manyGifs = require('./seed.json');
const mongoose = require('./connection');
const Gif = require('../models/gifs');
const db = mongoose.connection;

Gif.deleteMany({}).then(() => {
	Gif.insertMany(manyGifs).then((gifs) => {
		console.log('menu', gifs);
		db.close();
	});
});
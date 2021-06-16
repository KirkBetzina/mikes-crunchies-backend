const manyMenus = require('./seed.json');
const mongoose = require('./connection');
const Menu = require('../models/menus');
const db = mongoose.connection;

Menu.deleteMany({}).then(() => {
	Menu.insertMany(manyMenus).then((menus) => {
		console.log('menu', menus);
		db.close();
	});
});
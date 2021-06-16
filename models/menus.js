const mongoose = require('../db/connection');
const Schema = mongoose.Schema;

const menuSchema = new Schema(
	{
	"row_id": String,
    "Entry":String,
    "Food":String,
    "Description": String,
    "Price":String
	},
	{ timestamps: true }
);

const Menu = mongoose.model('Menu', menuSchema);

module.exports = Menu;
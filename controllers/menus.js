// import express
const express = require('express');
// instantiate a new instance of express.Router
const router = express.Router();
const mongoose = require('../db/connection')
const db = mongoose.connection;

// import the menu model
const Menu = require('../models/menus');



// POST ROUTE.../menus
router.post('/', async (req, res) => {
    const menu = await Menu.create(req.body)
    res.json({
        status: 200,
        data: menu
    })
});

//UPDATE ROUTE
router.put('/:menuId', async (req,res) => {
    
    const menu = await Menu.findByIdAndUpdate(req.params.menuId, req.body, {new: true})
    res.json({
        status: 200, 
        data: menu
    })
})
 
// INDEX - returns all menus
router.get('/', async (req, res) => {
	const allMenus = await Menu.find({})
	res.json({
		status: 200,
		data: allMenus,
	});
});
module.exports = router
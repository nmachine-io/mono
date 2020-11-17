'use strict';

const express = require('express');

const PORT = 8080;
const HOST = '0.0.0.0';

const app = express();
app.get('*', (req, res) => {
	console.log(req.path);
	console.log(req.query);
	const flavor = process.env.FLAVOR;
	const version = process.env.VERSION;
	res.send(`Nectar ice cream version ${version} with ${flavor}`);
});

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);
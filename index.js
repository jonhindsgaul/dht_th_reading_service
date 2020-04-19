var express = require('express');
var app = express();
var path = require('path');

const PORT = process.env.PORT || 5000;


app.get('/static')


app.use(express.static(path.join(__dirname,'public')));

app.listen(PORT, () => console.log(`Server started on port ${PORT}`));


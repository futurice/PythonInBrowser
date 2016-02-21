var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Chilicorn Code Club'});
});

router.get('/codeclub', function(req, res, next) {
  var exercises = require('../examples/examples.json');
  var modules = require('../examples/modules.json');
  console.log(JSON.stringify(modules, 2));
  res.render('codeclub', { title: 'Chilicorn Code Club', exercises: exercises, modules: modules });
});

router.get('/material', function(req, res, next) {
  var materialData = require('../examples/material.json');
  res.render('material', { title: 'Chilicorn Code Club', material: materialData.material});
});

module.exports = router;

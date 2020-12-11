// Cargamos el modulo express
const express = require('express');
const router = express.Router();
// Cargamos el controlador 
const interruptorContoller = require('../api/controllers/interruptores');
// Especificamos nuestras rutas teniendo en cuenta los metodos creados en nuestro controlador, y especificando que seran rutas que usaran el metodo POST
router.get('/', interruptorContoller.getAll);
router.post('/', interruptorContoller.create);
router.get('/:interruptorId', interruptorContoller.getById);
router.post('/:interruptorId', interruptorContoller.updateById);
module.exports = router;
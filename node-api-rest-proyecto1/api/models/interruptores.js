// Cargamos el módulo de mongoose
const mongoose = require('mongoose');
//Definimos los esquemas
const Schema = mongoose.Schema;
// Creamos el objeto del esquema con sus correspondientes campos
const interruptorSchema = new Schema({
 interruptora: {
  type: String,
  trim: true,  
  required: true,
 },
 gra: {
  type: Number,
  trim: true,  
  required: true,
 },
 interruptorb: {
  type: String,
  trim: true,  
  required: true,
 },
 grad: {
  type: Number,
  trim: true,  
  required: true,
 },
 fecha: {
  type: Date,
  trim: true,  
  required: true,
 }
});
// Exportamos el modelo para usarlo en otros ficheros
module.exports = mongoose.model('Interruptor', interruptorSchema);

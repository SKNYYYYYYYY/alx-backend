const express = require('express');
const redis = require('redis');
const { promisify } = require('util');

const client = redis.createClient();
client.on('connect', () => console.log('Redis client connected to the server'));
client.on('error', (err) => console.error('Redis error:', err));

// Promisify Redis commands
const hgetAsync = promisify(client.hget).bind(client);
const hsetAsync = promisify(client.hset).bind(client);

const listProducts = [
  { Id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
  { Id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
  { Id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
  { Id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

function getItemById(id) {
  return listProducts.find(item => item.Id === id);
}

async function reserveStockById(itemId, stock) {
  await hsetAsync(`item.${itemId}`, 'stock', stock);
}

async function getCurrentReservedStockById(itemId) {
  const stock = await hgetAsync(`item.${itemId}`, 'stock');
  return stock;
}

function rename(item) {
  return {
    itemId: item.Id,
    itemName: item.name,
    price: item.price,
    initialAvailableQuantity: item.stock
  };
}

const app = express();

app.get('/list_products', (req, res) => {
  const products = listProducts.map(rename);
  res.json(products);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  let reservedStock = await getCurrentReservedStockById(itemId);
  reservedStock = reservedStock !== null ? parseInt(reservedStock) : item.stock;

  const product = rename(item);
  product.currentQuantity = reservedStock;

  res.json(product);
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const item = getItemById(itemId);

  if (!item) {
    return res.json({ status: 'Product not found' });
  }

  let currentStock = await getCurrentReservedStockById(itemId);
  currentStock = currentStock !== null ? parseInt(currentStock) : item.stock;

  if (currentStock < 1) {
    return res.json({ status: 'Not enough stock available', itemId });
  }

  await reserveStockById(itemId, currentStock - 1);
  res.json({ status: 'Reservation confirmed', itemId });
});

app.listen(1245, () => {
  console.log('app running on localhost:1245');
});

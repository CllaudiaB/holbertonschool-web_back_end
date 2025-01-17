const express = require('express');
const redis = require('redis');
const util = require('util');


const listProducts = [
    {Id: 1, name: "Suitcase 250", price: 50, stock: 4},
    {Id: 2, name: "Suitcase 450", price: 100, stock: 10},
    {Id: 3, name: "Suitcase 650", price: 350, stock: 2},
    {Id: 4, name: "Suitcase 1050", price: 550, stock: 5},
]

function getItemById(id) {
    return listProducts.find(({ Id }) => Id === id);
};


const app = express();
const port = 1245;

app.listen(port, () => {
    console.log(`App listening on port ${port}`)
});

app.get("/list_products", (req, res) => {
    const products = listProducts.map((product) => ({
        itemId: product.Id,
        itemName: product.name,
        price: product.price,
        initialAvailableQuantity: product.stock,
    }));
  
    res.json(products);
});


const client = redis.createClient();
const get = util.promisify(client.get).bind(client);

function reserveStockById(itemId, stock) {
    client.set(`item.${itemId}`, stock);
}

async function getCurrentReservedStockById(itemId) {
    const value = await get(itemId);
    return value;
};

app.get("/list_products/:itemId", (req, res) => {
    try {
        const id = parseInt(req.params.itemId);
        const item = getItemById(id);
        const currentStock = getCurrentReservedStockById(id);
  
        res.json({
            itemId: item.Id,
            itemName: item.name,
            price: item.price,
            initialAvailableQuantity: item.stock,
            currentQuantity: currentStock,
      });
    } catch (err) {
        res.json({ status: "Product not found" });
    }
});

const express = require('express');
const app = express();
const bodyParser = require('body-parser');
app.use(bodyParser.json());

const PORT = 7865;

app.get('/', (req, res) => {
    res.send('Welcome to the payment system');
});
  
app.get('/cart/:id(\\d+)', (req, res) => {
    const cartId = req.params.id;
    res.send(`Payment methods for cart ${cartId}`);
});

app.get('/available_payments', (req, res) => {
    res.json(
        {
            payment_methods: {
                credit_cards: true,
                paypal: false
            }
        }
    );
});

app.post('/login', (req, res) => {
    const userName = req.body.userName;
    res.send(`Welcome ${userName}`);
});

app.listen(PORT, () => {
    console.log('API available on localhost port 7865');
});

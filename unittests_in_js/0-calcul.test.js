const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe("calculateNumber Tests", function () {
    it("Retourn sum", function () {
      assert.strictEqual(calculateNumber(1, 3), 4);
      assert.strictEqual(calculateNumber(1, 3.7), 5);
      assert.strictEqual(calculateNumber(1.2, 3.7), 5);
      assert.strictEqual(calculateNumber(1.5, 3.7), 6);
      assert.strictEqual(calculateNumber(-1.3, -4.5), -5);
      assert.strictEqual(calculateNumber(0.4, 0.6), 1);
    });
});
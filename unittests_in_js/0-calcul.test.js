const assert = require('assert');
const calculateNumber = require('./0-calcul.js');

describe("calculateNumber Tests", function () {
    it("Retourn 4 for calculateNumber(1, 3)", function () {
      assert.strictEqual(calculateNumber(1, 3), 4);
    });
    it("Retourn 5 for calculateNumber(1, 3.7)", function () {
      assert.strictEqual(calculateNumber(1, 3.7), 5);
      });
    it("Retourn 5 for calculateNumber(1.2, 3.7)", function () {
      assert.strictEqual(calculateNumber(1.2, 3.7), 5);
    });
    it("Retourn 6 for calculateNumber(1.5, 3.7)", function () {
      assert.strictEqual(calculateNumber(1.5, 3.7), 6);
    });
});
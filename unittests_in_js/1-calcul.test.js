const assert = require("assert");
const { calculateNumber } = require("./1-calcul.js");

describe("calculateNumber Tests", function () {
    it("Retourn 6 for calculateNumber('SUM', 1.4, 4.5)", function () {
      assert.strictEqual(calculateNumber("SUM", 1.4, 4.5), 6);
    });
    it("Retourn -4 for calculateNumber('SUBTRACT', 1.4, 4.5)", function () {
        assert.strictEqual(calculateNumber("SUBTRACT", 1.4, 4.5), -4);
      });
    it("Retourn 0.2 for calculateNumber('DIVIDE', 1.4, 4.5)", function () {
    assert.strictEqual(calculateNumber("DIVIDE", 1.4, 4.5), 0.2);
    });
    it("Retourn 'Error' for calculateNumber('DIVIDE', 1.4, 0)", function () {
        assert.strictEqual(calculateNumber("DIVIDE", 1.4, 0), "Error");
      });
});
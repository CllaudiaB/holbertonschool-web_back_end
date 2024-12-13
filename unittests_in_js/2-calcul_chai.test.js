const expect = require("chai").expect;
const calculateNumber = require("./2-calcul_chai.js");

describe("calculateNumber Tests", function () {
    it("Retourn 6 for calculateNumber('SUM', 1.4, 4.5)", function () {
        expect(calculateNumber("SUM", 1.4, 4.5)).be.equal(6);
    });
    it("Retourn -4 for calculateNumber('SUBTRACT', 1.4, 4.5)", function () {
        expect(calculateNumber("SUBTRACT", 1.4, 4.5)).be.equal(-4);
      });
    it("Retourn 0.2 for calculateNumber('DIVIDE', 1.4, 4.5)", function () {
        expect(calculateNumber("DIVIDE", 1.4, 4.5)).be.equal(0.2);
    });
    it("Retourn 'Error' for calculateNumber('DIVIDE', 1.4, 0)", function () {
        expect(calculateNumber("DIVIDE", 1.4, 0)).be.equal("Error");
    });
});

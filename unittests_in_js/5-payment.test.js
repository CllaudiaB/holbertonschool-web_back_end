const sinon = require("sinon");
const sendPaymentRequestToApi = require("./5-payment");
const Utils = require("./utils");

describe("sendPaymentRequestToApi", function () {
    let consoleSpy;

    beforeEach(function () {
        consoleSpy = sinon.spy(console, "log");
    });

    afterEach(function () {
        consoleSpy.restore();
    });

    it("should log the correct total for 100 and 20", function () {
        sendPaymentRequestToApi(100, 20);
        sinon.assert.calledOnce(consoleSpy);
        sinon.assert.calledWithExactly(consoleSpy, "The total is: 120");
    });

    it("should log the correct total for 10 and 10", function () {
        sendPaymentRequestToApi(10, 10);
        sinon.assert.calledOnce(consoleSpy);
        sinon.assert.calledWithExactly(consoleSpy, "The total is: 20");
    });
});

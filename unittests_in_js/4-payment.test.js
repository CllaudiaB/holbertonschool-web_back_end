const sinon = require("sinon");
const expect = require("chai").expect;
const Utils = require("./utils");
const sendPaymentRequestToApi = require("./4-payment");

describe("sendPaymentRequestToApi Tests", function () {
  let stub, spy;

  it("should call calculateNumber with correct arguments and log correct message", function () {
    stub = sinon.stub(Utils, "calculateNumber").returns(10);

    spy = sinon.spy(console, "log");

    sendPaymentRequestToApi(100, 20);

    expect(stub.calledWith("SUM", 100, 20)).to.be.true;
    expect(spy.calledWithExactly("The total is: 10")).to.be.true;

    stub.restore();
    spy.restore();
  });
});

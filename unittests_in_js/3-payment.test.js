const sinon = require("sinon");
const expect = require("chai");
const Utils = require("./utils");
const sendPaymentRequestToApi = require("./3-payment");

describe("sendPaymentRequestToApi Tests", function () {
  it("should call calculateNumber with correct arguments when sendPaymentRequestToApi is called", function () {
    sinon.spy(Utils, "calculateNumber");
    sendPaymentRequestToApi(100, 20);
    expect(Utils.calculateNumber("SUM", 100, 20).calledOnce).to.be
    .true;
    Utils.calculateNumber.restore();
  });
});

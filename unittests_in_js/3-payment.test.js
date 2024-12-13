const sinon = require("sinon");
const expect = require("chai");
const Utils = require("./utils");
const sendPaymentRequestToApi = require("./3-payment");

describe("sendPaymentRequestToApi Tests", function () {
  it("should call calculateNumber with correct arguments when sendPaymentRequestToApi is called", function () {
    sinon.spy(Utils, "calculateNumber");
    sendPaymentRequestToApi(100, 200);
    expect(Utils.calculateNumber.withArgs("SUM", 100, 200).calledOnce).to.be
      .true;
    Utils.calculateNumber.restore();
  });
});

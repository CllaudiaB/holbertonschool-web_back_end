const getPaymentTokenFromAPI = require('./6-payment_token');
const expect = require("chai").expect;

describe('getPaymentTokenFromAPI', function () {
    it('should return a resolved promise when success is true', function (done) {
      getPaymentTokenFromAPI(true)
        .then((data) => {
          expect(data).to.deep.equal({
            data: 'Successful response from the API',
          });
          done();
        })
        .catch((error) => done(error));
    });
  });

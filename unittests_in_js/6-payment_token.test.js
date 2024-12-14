const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', function () {
    it('should return a resolved promise when success is true', function (done) {
        getPaymentTokenFromAPI(true)
            .then((response) => {
                expect(response).toEqual({ data: 'Successful response from the API' });
                done();
            })
            .catch((error) => {
                done(error);
            });
    });

    it('should do nothing when success is false', function () {
        const result = getPaymentTokenFromAPI(false);
        expect(result).toBeUndefined();
    });
});

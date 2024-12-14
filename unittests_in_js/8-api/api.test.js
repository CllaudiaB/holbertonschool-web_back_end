const request = require('request');
const expect = require('chai').expect;

describe('Index page', function() {
  let serverUrl = 'http://localhost:7865';

  it('should return status code 200', function(done) {
    request.get(serverUrl, function(error, response, body) {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });

  it('should return the correct message', function(done) {
    request.get(serverUrl, function(error, response, body) {
      expect(body).to.equal('Welcome to the payment system');
      done();
    });
  });

  it('should return content-type text/plain', function(done) {
    request.get(serverUrl, function(error, response, body) {
      expect(response.headers['content-type']).to.include('text/plain');
      done();
    });
  });

  it('should be running on port 7865', function(done) {
    request.get(serverUrl, function(error, response, body) {
      expect(response.statusCode).to.equal(200);
      done();
    });
  });
});

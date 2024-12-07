function calculateNumber(type, a, b) {
    if (
      type === "SUM"
    ) {
      return Math.round(a) + Math.round(b);
    }
    else if (
      type === "SUBTRACT"
    ) {
      return Math.round(a) - Math.round(b);
    }
    else if (
      type === "DIVIDE"
    ) {
      if (Math.round(b) != 0)
      {
        return Math.round(a) / Math.round(b);
      }
      else {
        return "Error";
      }
    }
  
  }
  
  module.exports = { calculateNumber };
  
function calculator() {
  var sqft = Number(document.getElementById("sqft").value);
  var sqftlot = Number(document.getElementById("lotsqft").value);
  var bedrooms = Number(document.getElementById("bedrooms").value);
  var bathrooms = Number(document.getElementById("bathrooms").value);
  var p = Number(30);
  var result;
  var calc = document.getElementById("choice").value

// source https://www.census.gov/construction/chars/interactive/
  var AVG_BATHROOMS = 2.56
  var AVG_BEDROOMS = 3.5
  var AVG_SQFT = 2300
  var AVG_PRICE = 255000

// source https://www.census.gov/construction/chars/pdf/soldmedavgprice.pdf
// source https://www.trulia.com/home_prices/
  var AVG_METRO = 450000
  var AVG_CITY = 347000
  var AVG_TOWN = 268000

  switch (calc) {
    case "1":
      valua = AVG_METRO * (AVG_SQFT/sqft) * (bedrooms/AVG_BEDROOMS) * (bathrooms/AVG_BATHROOMS);
      break;
    case "2":
      valua = AVG_CITY * (AVG_SQFT/sqft) * (bedrooms/AVG_BEDROOMS) * (bathrooms/AVG_BATHROOMS);
      break;
    case "3":
      valua = AVG_TOWN * (AVG_SQFT/sqft) * (bedrooms/AVG_BEDROOMS) * (bathrooms/AVG_BATHROOMS);
      break;

  }

  document.getElementById("result").innerHTML = " = " + valua.toFixed(2);

}

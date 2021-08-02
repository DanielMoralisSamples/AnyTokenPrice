

//dApp frontend logic
async function getPrice(){
  const request_body = {"erc20_address":document.getElementById("tokenAddress").value};
  const request_moralis = fetch(`${window.origin}/request-price`, {
    method: "POST",
    body: JSON.stringify(request_body),
    headers: new Headers({"content-type": "application/json"})
    }).then(function (response) {
        if (response.status !== 200) {
          console.log(`Looks like there was a problem. Status code: ${response.status}`);
          return;
        }
        response.json().then(function (data) {
          convert_populate(data);
        });
      });   
}

function convert_populate(_response){
  result = _response.usdPrice
  document.getElementById("amountUSD").setAttribute("value", result);
}

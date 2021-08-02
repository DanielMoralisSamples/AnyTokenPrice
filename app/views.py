from app import app
from flask import render_template, request, make_response
import os, requests
from dotenv import load_dotenv

load_dotenv()

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/request-price", methods=["POST"])
def request_price():
    req = request.get_json()
    response = moralis_query(req["erc20_address"],'CHAIN','CHAIN NAME') #CHAINS - eth, bsc, polygon; CHAINNAME - for this project use mainnet
    res = make_response(response, 200)
    return res



def moralis_query(_address,_chain,_chain_name):
    moralis_url=f"https://deep-index.moralis.io/api/token/ERC20/{_address}/price?chain={_chain}&chain_name={_chain_name}"
    h_values = {'X-API-KEY':os.environ['API_KEY']}
    r = requests.get(moralis_url, headers=h_values) 
    return  r.json()


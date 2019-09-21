import requests

__author__ = 'sorabh86'


request = requests
request.get("https://www.amazon.in/IndoPrimo-Cotton-Casual-Fancy-Sleeves/dp/B07TXQS89Q?ref_=Oct_BSellerC_1968093031_0&pf_rd_p=e8b769a9-db0b-5574-8f58-9757b22513a9&pf_rd_s=merchandised-search-8&pf_rd_t=101&pf_rd_i=1968093031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_r=WFTBM48MSAVN1MYAV0FN&pf_rd_r=WFTBM48MSAVN1MYAV0FN&pf_rd_p=e8b769a9-db0b-5574-8f58-9757b22513a9")

#<span id="priceblock_saleprice" class="a-size-medium a-color-price priceBlockSalePriceString">₹&nbsp;699.00</span>

print(request.content)
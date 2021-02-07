# -*- coding: utf-8 -*- 

import keepa


accesskey = '5eqv8gldhmc3qgrna3p2g2o50mqf8cssaa0hvam0f6vn581lvpsunu053c0sn7vj' # enter real access key here

api = keepa.Keepa(accesskey)

asins = '059035342X'

products = api.query(asins)


print('ASIN is ' + products[0]['asin'])

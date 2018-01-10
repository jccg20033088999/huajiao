#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import urllib2, urllib

COOKIE = "your cookie"
def foo(code): 
    f = urllib2.Request(
        url     = 'https://activity.huajiao.com/Answer/activeByCode?code='+code+'&callback=_jsonppkwfg4z525',
        )

    f.add_header('Cookie', COOKIE);
    
    response = urllib2.urlopen(f)
    g = response.read()
    print g


codeList = ['BWJYXV','BRDF84','BTTP1B','BR6K53','BNQ119','BTWPUA','BBHCSL','BXH2K6','BK2MPC','BKE8CH','BKNGYS','BFHJBG','BM2VHY','BXFJ8Y','BRRMVG','BXWN0T','BGQXWH','BWXR5Z','bhhr2j','bp5U8V','Bneamc','br7gne','b34htq','blm5v7','BCW5WL','B7S109','BGCGSN','BVN410','BFDF9X','BXAKUG','BNHQUB','BF8JRW','BCPEM4','BMWUMM','B7JFAV','BB1BA8','BK5TBS','BV17KV','BKV1SX','BH1F7U','BL78VT','B7LJ95','BPLF7F','BP8036','BFAZBV','BXAYCJ','B785MP','BMU2P6','BHFXM6','BPXLDB','BMLQ3C','BKVA3B','B3WL3R','BR7HXC','BM1X2W','BMXADS','BF3CNV','BL8SDL','BBMKAK','BGRN4V','B3SY73','BKUY0Q','BLDYZL','BLX7K9','BXZP9X','BL99Z2','BXSKKJ','BWQBQE','BTV7VD','BLWJTG','BV7BUV','BX7BSJ','BTCHBP','BL5W12','BGVDMA','BB0N83','BLX4WE','BBON83','B34KDM','BF8BXK','BMG3JV','BC0HR2','BC0MDE','BGSA9B','B7NMCM','BHXTCR','BB2CUH','BP0QZ0','BWKYQF','BXGREA','BC5DUU','BXJXUN','BR53V5','BMR9SJ','BHV9JA','BBS5WB','BB0M6J','BHW80E','BTRFSH','BH6VZC','B7L2CT','BBU14B','BP3EED','B74MH5','BR20KJ','BMTNEJ','B3HEYB','BH9Y0Y','C','BR35MA','BC38KX','BCCFQH','BVW0CJ','B3QBM2','BGM3AV','BCJZCZ','BFD13R','BX2HH0','BG42UZ','BXXQUY','BK3KEP','BNDP65','bvbn5y','Blc8kp','Bkgqy6','Bfzk34','b38vp3','bgk2wk','bwql2c','BF75SQ','BHHQUG','BPRLNN','bxpq69','bgypr6','BGHTA6','BK5FS3','BWL14J','BPX6ZZ','B3KYD1','brfyqc','bhql6k','Bx84b4','BFT8W2','BW1AYC','BHLYLS','BHPBWX','bbq63c','BMKUL8','BM9BVD','BVDQ3K','BLT861','BVTQHR','BK6Q7S','B7RFLX','BPAJWM','BPHKA7','BV7QEM','BX6FZB','brblan','BN6TMR','BH1FN6','BRZSJ6','BKM8KB','BVQBFM','BBR03M','BF9ZZY','BRBKMU','B7SY2R','BHF3ZY','BBH6BW','B3akv6','BNVER2','B7MFGC','BNPPNE','B7EN47','Bxxy55','BF45UC','bpnkky','BVGX9Y','BBN24N']

for code in codeList:
    foo(code)

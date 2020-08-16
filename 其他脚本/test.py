#!/usr/bin/python

# 制作url遍历列表
for i in range(1,999):
   n=str(i)
   s = n.zfill(3)
   for coding in ("600"+s,"000"+s,"300"+s):
       url = 'http://vip.stock.finance.sina.com.cn/corp/view/vFD_FinanceSummaryHistory.php?stockid='+coding+'&type=NETPROFIT&cate=liru0'
       print(url)




#营业利润率
# http://vip.stock.finance.sina.com.cn/corp/view/vFD_FinancialGuideLineHistory.php?stockid=600256&typecode=financialratios30


#净利润
# http://vip.stock.finance.sina.com.cn/corp/view/vFD_FinanceSummaryHistory.php?stockid=000651&type=NETPROFIT&cate=liru0


# 股本结构
# http://vip.stock.finance.sina.com.cn/corp/go.php/vCI_StockStructureHistory/stockid/600256/stocktype/TotalStock.phtml

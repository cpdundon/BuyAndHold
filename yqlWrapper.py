#!/usr/bin/python
import os
import yql
import pandas as pd 
from datetime import datetime
import numpy as np #Will be needed for irr calcs

class YahooWrapper:
	def __init__(self):
		self.qDf = []

	def rtn_hist_data(self):
		return self.qDf

	def rtn_hist(self, begin, end):
		qry = hist_query_str(begin, end)
		print qry 

		y = yql.Public()
		result = y.execute(qry)

		rv = result.results

		quo = rv['quote'] 
		self.qDf = pd.DataFrame.from_records(quo)

		qDt = []
		for idx, dta in self.qDf.iterrows():
			str_ = dta['Date']
			d = datetime.strptime(str_, '%Y-%m-%d')
			qDt.append(d)

		arr = [qDt, self.qDf['Symbol']]
		tup = list(zip(*arr))
		idx = pd.MultiIndex.from_tuples(tup, names=['iDate','iSymbol'])

		self.qDf.index = idx

		return self.qDf

def hist_query_str(begin, end):
	b = begin.strftime('%Y-%m-%d')
	e = end.strftime('%Y-%m-%d')

	qry = ('use ' +
		'"http://www.datatables.org/yahoo/finance/yahoo.finance.historicaldata.xml" ' +
		'as hist; ' + 
		'select * from hist where symbol ' + 
		'in ("SPY","RSP") and startDate = "' + b + '" ' +
		'and endDate = "' + e +'"')

	return qry 
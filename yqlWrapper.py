#!/usr/bin/python
import os
import yql
import pandas as pd 
from datetime import datetime
import numpy as np #Will be needed for irr calcs

class YahooWrapper:
	def __init__(self):
		self.qDf = []
		self.sly = []

	def rtn_hist_data(self):
		return self.qDf

	def rtn_hist(self, begin, end):
		qry = hist_query_str(begin, end)
		print qry 

		y = yql.Public()
		result = y.execute(qry)
		
		rv = result.results
		
		if rv is None:
			self.qDf = []
			return self.qDf

		quo = rv['quote'] 
		self.qDf = pd.DataFrame.from_records(quo)

		idx = gen_multi_idx(self.qDf['Date'], self.qDf['Symbol'], ['iDate', 'iSymbol'])
 
		self.qDf.index = idx

		return self.qDf

	def hist_slicer(self, sym, begin, end):
		
		sly = self.qDf

		if (len(self.qDf) < 1):
			self.sly = []
			return self.sly

		sly = sly.ix[sly.Symbol == sym]
		
		sly = sly.ix[sly.Date >= begin.strftime("%Y-%m-%d")]
		sly = sly.ix[sly.Date <= end.strftime("%Y-%m-%d")]
		
		self.sly = sly
		
		return sly



def gen_multi_idx(iOne, iTwo, names_):

	arr = [iOne, iTwo]
	tup = list(zip(*arr))
	idx = pd.MultiIndex.from_tuples(tup, names=[names_[0], names_[1]])

	return idx

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
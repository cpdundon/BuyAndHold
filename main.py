#!/usr/bin/python
import os
import yqlWrapper as yahoo 
import pandas as pd 
from datetime import date
import calcs as calcs
import math as math

def main():
	'''Need to Add Next:
		-- Unit Testing
		-- Error trapping (return too large from Yahoo)
	'''

	end = date.today()
	endOrd = end.toordinal()

	begin = endOrd - 50
	#begin = endOrd - 1000
	begin = date.fromordinal(begin)
	print begin

	yoo = yahoo.YahooWrapper()

	yDta = yoo.rtn_hist(begin, end)
	#print yoo.rtn_hist_data()
	# Yahoo Data Connectivity Working as of 2015-03-24

	begin = endOrd - 25
	begin = date.fromordinal(begin)

	s = yoo.hist_slicer('RSP', begin, end)

	nCount = s.shape
	nCount = nCount[0]

	lDrp = list(range(1, nCount-1, 1))
	s = s.drop(s.index[lDrp])

	nCount = s.shape[0]
	
	s.ix[s.index[nCount-1], 'Adj_Close'] =  str(float(s.ix[s.index[nCount-1], 'Adj_Close']) * -1) 

	print s

	cal = calcs.Calcs()

	cal.fullDtaSet = s 
	cal.dataTrim()

	ir = cal.eIrr()	
	print 'System:'
	print ir 
	
	return


if __name__ == '__main__':
    main()
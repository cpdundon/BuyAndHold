#!/usr/bin/python
import os
import yqlWrapper as yahoo 
import pandas as pd 
from datetime import date
import numpy as np 

def main():
	'''Need to Add Next:
		-- Unit Testing
		-- Error trapping (return too large from Yahoo)
	'''

	end = date.today()
	endOrd = end.toordinal()

	begin = endOrd - 370
	begin = date.fromordinal(begin)

	yoo = yahoo.YahooWrapper()

	yDta = yoo.rtn_hist(begin, end)
	print yoo.rtn_hist_data()
	# Yahoo Data Connectivity Working as of 2015-03-24
	
	begin = endOrd - 1
	begin = date.fromordinal(begin)

	s = yoo.hist_slicer('RSP', begin, begin)
	print s 

	return


if __name__ == '__main__':
    main()
#!/usr/bin/python
import os
import yql
import pandas as pd 
# from datetime import date
import datetime
import numpy as np #Will be needed for irr calcs
import math as math
from scipy import optimize as optm

class Calcs:

	def __init__(self):
		self.fullDtaSet = []

	def dataTrim(self):
		cFlowDf_ = self.fullDtaSet.copy()
		cFlowDf_.drop(['Close', 'Volume', 'Open', 'High', 'Low'], inplace=True, axis=1)
		cFlowDf_.sort(columns=['Date']) 

		vec = []
		for idx, row in cFlowDf_.iterrows():
			cf = float(row.ix['Adj_Close'])
			vec.append(cf)

		cFlowDf_['Cash_Flow'] = vec

		self.cFlowDf = cFlowDf_ 
		return cFlowDf_

	def eIrr(self):
		cFlowDf_ = self.cFlowDf.copy()

		rI = optm.minimize_scalar(self.pVal)
		
		rI = rI.x

		return rI

	def discFac(self, r, t0, t1):
		nt0 = t0.toordinal()
		nt1 = t1.toordinal()
		dt = (nt1 - nt0)
		dt = float(dt)/365.
		r_ = float(r)

		discF = 1. / math.exp(r_*dt)

		return discF

	def pVal(self, r):

		cFlowDf = self.cFlowDf 

		maxI = cFlowDf.shape[0] - 1
		begin = cFlowDf.ix[cFlowDf.index[maxI], 'Date']
		begin = datetime.datetime.strptime(begin, '%Y-%m-%d')

		pv = 0
		for idx, row_ in cFlowDf.iterrows():
			ct = row_.ix['Date']
			cf = row_.ix['Cash_Flow']

			ct = datetime.datetime.strptime(ct, '%Y-%m-%d')

			df = self.discFac(r, begin, ct)
			pv = pv + (cf * df)

		pv = abs(pv)
		return pv

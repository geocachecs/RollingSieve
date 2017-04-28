	
class RollingSieve(object): 
	def __init__(self,evensOrOdds=None):
		if(evensOrOdds=="evens"):
			self.pattern = [2]
			self.start = 2
			self.lcm = 2
		elif(evensOrOdds=="odds"):
			self.pattern = [2]
			self.start= 1
			self.lcm = 1
		else:
			self.start=1
			self.pattern = [1]
			self.lcm = 1
			
		self.lengthOfPattern=1
		self.nextNum = 0 + self.pattern[0] # so it must start at either 2 or 1
		self.nextIndexCount = 0 #% self.lengthOfPattern
		
		self.lastNum = 0
	
	def gen(self):
		self.lastNum = self.nextNum
		self.nextNum += self._getPatternMember(self.nextIndexCount)
		self.nextIndexCount +=1
		return self.lastNum
	
	def _getPatternMember(self,index):
		return self.pattern[index%self.lengthOfPattern]
	
	def _setPattern(self,newPattern):
		self.pattern = newPattern
		self.lengthOfPattern = len(self.pattern)
	
	def banLast(self):
		if self.lastNum == 0:
			print "Cannot ban a number before one is generated"
		else:
			# get new LCM #
			if(self.lcm>=self.lastNum):
				largerFactor=self.lcm
				smallerFactor=self.lastNum
			else:
				largerFactor=self.lastNum
				smallerFactor=self.lcm
			factorMultiple = 1
			while(largerFactor*factorMultiple%smallerFactor!=0):
				factorMultiple+=1 
			oldLCM = self.lcm 
			self.lcm = largerFactor*factorMultiple	## setting lcm
			
			
			# initialize new pattern #
			newPattern = self.pattern[:(self.nextIndexCount-1)]
			
			# create new pattern #
			if(self.lastNum<oldLCM+self.start):
				tempNum = self.lastNum 
				iteration = self.nextIndexCount-1
			else:
				tempNum = oldLCM + self.start
				iteration = 0
			while(tempNum<=self.lcm):
				if(tempNum%self.lastNum==0):
					newPattern[len(newPattern)-1] += self._getPatternMember(iteration)
				else:
					newPattern.append(self._getPatternMember(iteration))

				tempNum += self._getPatternMember(iteration)
				iteration += 1
			
			# set the next index # 
			self.nextIndexCount -= 1
			
			# finish up #	
 			self._setPattern(newPattern)

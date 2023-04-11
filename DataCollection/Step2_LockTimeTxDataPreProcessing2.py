import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
import numpy as np




lstmtimestamps=3
blockFeatures=5
neuralTimestamps=1
txFeatures=7



blockindexposintx=11
confirmedtimeintx=12
receivetimeintx=7
feerateintx = 14








start_selection=621500

print(start_selection)


#
# blockstar_heightInx=10
# def searchtxretrivalIndex(txcollection,blockstar_height):
#   txpos=0
#   for i in range(txcollection.__len__()):
#     if int(txcollection[i][blockstar_heightInx])==blockstar_height:
#       txpos=i
#       break
#   return txpos
#
#
#
#
#
# time=1522372849
#
# def getHeight(tx_time, blockHeight, blockTime):
#     blockNum=blockHeight.size
#     start=0
#     end=blockNum-1
#
#     if tx_time > blockTime[start] or tx_time < blockTime[end]:
#         pos = -2000
#         return pos
#     else:
#         while start <= end:
#             mid = (start + end) // 2
#             if tx_time > blockTime[mid]:
#                 end = mid - 1
#             elif tx_time < blockTime[mid]:
#                 start = mid + 1
#             elif tx_time == blockTime[mid]:
#                 pos = mid
#                 break
#         if (start > end):
#             pos = end
#         return blockHeight[pos]
#
#
#
#
#
#
#
# # def getHeight2(tx_time, blockTime):
#     # blockNum=blockTime.shape[0]
#     # start=0
#     # end=blockNum-1
#
#     # pos=-2
#     # label=0
#
#
#     # #     mid = (start + end) // 2
#     # #     if tx_time>blockTime[mid]:
#     # #         end = mid - 1
#     # #     elif tx_time<blockTime[mid]:
#     # #         start = mid + 1
#     # #     elif tx_time==blockTime[mid]:
#     # #         pos=mid
#     # #         break
#     # # startValue=blockTime[start]
#     # # endValue=blockTime[end]
#     # # if tx_time>=startValue and tx_time<endValue and pos==-2:
#     # #     pos=startValue
#     # if tx_time>blockTime[start] or tx_time<blockTime[end]:
#         # pos=-2000
#         # return pos
#     # else:
#         # while start <= end:
#             # mid = (start + end) // 2
#             # if tx_time > blockTime[mid]:
#                 # end = mid - 1
#             # elif tx_time < blockTime[mid]:
#                 # start = mid + 1
#             # elif tx_time == blockTime[mid]:
#                 # pos = mid
#                 # break
#         # if(start>end):
#             # pos = end
#         # return pos
#
#
#
#
#
#
#  # keys=['block_index','height' ,'n_tx', 'size', 'bits', 'weight', 'fee', 'ver','time']
#
#
#
#
# #tx_features = ['tx_index', 'vin_sz', 'vout_sz', 'fee', 'ver', 'size', 'weight', 'time', 'relayed_by', 'lock_time',
# #               'block_height', 'block_index',confimredtime, waiting time,'feerate']
#
#
#
#
# ##Finaal  Final_tx_features=['tx_index','vin_sz','vout_sz','ver','size', 'weight', 'time','relayed_by', 'lock_time','fee',
#     ###############block_height', 'block_index','confirmedtime','watingtime','feerate','enterBlock','watiingblock']
#
# #Block keys=['block_index','height' ,'n_tx', 'size', 'bits', 'fee', 'ver','time']
#
#
#
# relayIndex=7
# timeIndex=6
# confirmedHeightIndex=10
#
#
# totalblockData=pd.read_csv('Block'+str(start_selection)+'Total.txt',header=None,sep=" ")
# totalblockData=totalblockData[::-1]
# blockHeight=totalblockData[1]
# blockTime=totalblockData[7]
# totalblockData.to_csv('Block'+str(start_selection)+'Total.csv',index=False,header=False)
#
#
#
#
#
#
# # construct dataset
#
#
#
#
# blockData=pd.read_csv('Block'+str(start_selection)+'.txt',header=None,sep=" ")
# txdata = pd.read_csv('txinBlock'+str(start_selection)+'.txt',header=None,sep=" ")
#
#
#
#
# #Turn to increasing order
# txdata = txdata[::-1]
# blockData=blockData[::-1]
#
#
# recordsNo=txdata.shape[0]
#
# # feature relayinfo
# encoder=LabelEncoder()
# txdata[relayIndex]=encoder.fit_transform(txdata[relayIndex])
# #firstSeen
# txTime = txdata[timeIndex]
#
# txNum=recordsNo
#
# txReceiveHeight=[]
# for i in range(txNum):
#     tx_time=txTime[i]
#     tx_height=getHeight(tx_time,blockHeight,blockTime)
#     txReceiveHeight.append(tx_height)
#     print(i)
#
# txdata[15]=pd.Series(txReceiveHeight)
# #index9 LocktimeHeight
# #index15 receiveTImeHeight
#
# validBlockTime = txdata[15]
#
# txdata[16]=txdata[confirmedHeightIndex]-validBlockTime+1
#
#
# blockData.to_csv('../block'+str(start_selection)+'new.csv',index=False,header=False)
# txdata.to_csv('txinblock'+str(start_selection)+'.csv',index=False,header=False)
#
#
# data=pd.read_csv('txinblock'+str(start_selection)+'.csv',sep=",",names=['tx_index','vin_sz','vout_sz','ver','size', 'weight', 'time','relayed_by', 'lock_time','fee',
#                                                  'block_height', 'block_index','confirmedtime','watingtime','feerate','enterBlock','watiingblock'])
#

data2=pd.read_csv('txinblock'+str(start_selection)+'.csv',sep=",",names=['tx_index','vin_sz','vout_sz','ver','size', 'weight', 'time','relayed_by', 'lock_time','fee',
                                                 'block_height', 'block_index','confirmedtime','watingtime','feerate','enterBlock','watiingblock'])

print('overall records')
print(data2.shape)



data3=data2[data2.lock_time<500000000]
print('locktime under 500000000')
print(data3.shape)
data4=data3[data3.enterBlock<data3.lock_time]
print('enter before locktime')
print(data4.shape)
data8=data4[data4.confirmedtime<data4.lock_time]
print('confirmed before  locktime')
print(data8.shape)

data9=data3[data3.confirmedtime<data3.enterBlock]
print('confirmedtime before enter')
print(data9.shape)



data5=data2[data2.lock_time>500000000]
print('locktime over 500000000')
print(data5.shape)
data6=data5[data5.time<data5.lock_time]
print('enter before locktime')
print(data6.shape)
data7=data6[data6.confirmedtime<data6.lock_time]
print('confirmed before  locktime')
print(data7.shape)

data1=data5[data5.confirmedtime<data5.time]
print('confirmedtime before enter')
print(data1.shape)



# data=data[data.feerate>0]
# data1=data[data.enterBlock<0]
# data1.to_csv('../Invalid_txinblock'+str(start_selection)+'.csv',index=False,header=False)
# data=data[data.enterBlock>0]
# data['feerate']=4*data['fee']//data['weight']

# data['watiingblock']=data['block_height']-data['enterBlock']+1
# data=data[data.watiingblock>=1]
# data.to_csv('../txinblock'+str(start_selection)+'.csv',index=False,header=False)

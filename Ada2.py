
from numpy import *
import matplotlib.pyplot as plt


# 加载数据集
def loadDataSet():
    dataMat = matrix([[0, 1], [1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]])
    labelMat = [1.0, 1.0, 1.0, -1.0, -1.0, -1.0, 1.0, 1.0, 1.0, -1.0]
    return dataMat, labelMat


def stumpClassify(dataMatrix, dimen, threshVal, threshIneq):
    retArray = ones((shape(dataMatrix)[0], 1))
    if threshIneq == 'lt':
        retArray[dataMatrix[:, dimen] <= threshVal] = -1.0
    else:
        retArray[dataMatrix[:, dimen] > threshVal] = -1.0
    return retArray



def buildStump(dataArr, classLabels, D):
    dataMatrix = mat(dataArr)
    labelMat = mat(classLabels).T
    m, n = shape(dataMatrix)
    numSteps = 10.0
    bestStump = {}
    bestClasEst = mat(zeros((m, 1)))
    minError = inf
    for i in range(n):  # 特征循环
        rangeMin = dataMatrix[:, i].min()
        rangeMax = dataMatrix[:, i].max()
        stepSize = (rangeMax - rangeMin) / numSteps
        for j in range(-1, int(numSteps) + 1):
            for inequal in ['lt', 'gt']:
                threshVal = (rangeMin + float(j) * stepSize)
                predictedVals = stumpClassify(dataMatrix, i, threshVal,
                                              inequal)
                errArr = mat(ones((m, 1)))
                errArr[predictedVals == labelMat] = 0
                weightedError = D.T * errArr
                if weightedError < minError:
                    minError = weightedError  # 最小误差
                    bestClasEst = predictedVals.copy()

                    bestStump['dim'] = i  # 特征（得到最优预测值的那个距离）
                    bestStump['ineq'] = inequal  # 大于还是小于
    return bestStump, minError, bestClasEst


# 循环构建numIt个弱分类器
def adaBoostTrainDS(dataArr, classLabels, numIt=40):
    weakClassArr = []  # 保存弱分类器数组
    m = shape(dataArr)[0]
    D = mat(ones((m, 1)) / m)
    aggClassEst = mat(zeros((m, 1)))  # 统计类别估计累积值
    for i in range(numIt):
        bestStump, error, classEst = buildStump(dataArr, classLabels, D)
        alpha = float(0.5 * log((1.0 - error) / max(error, 1e-16)))
        bestStump['alpha'] = alpha
        weakClassArr.append(bestStump)  # 加入单层决策树
        expon = multiply(-1 * alpha * mat(classLabels).T, classEst)
        D = multiply(D, exp(expon))  # 更新概率分布D向量
        D = D / D.sum()
        print(D)
        aggClassEst += alpha * classEst
        aggErrors = multiply(sign(aggClassEst) != mat(classLabels).T, ones((m, 1)))
        errorRate = aggErrors.sum() / m
        if errorRate == 0.0:
            break
    return weakClassArr, aggClassEst


# 预测 累加 多个弱分类器获得预测值*该alpha 得到 结果
def adaClassify(datToClass, classifierArr):
    dataMatrix = mat(datToClass)
    m = shape(dataMatrix)[0]
    aggClassEst = mat(zeros((m, 1)))
    # 循环所有弱分类器
    for i in range(len(classifierArr[0])):
        # 获得预测结果
        classEst = stumpClassify(dataMatrix, classifierArr[0][i]['dim'], classifierArr[0][i]['thresh'],
                                 classifierArr[0][i]['ineq'])
        aggClassEst += classifierArr[0][i]['alpha'] * classEst
    return sign(aggClassEst)


datArr, labelArr = loadDataSet()
classifierArr = adaBoostTrainDS(datArr, labelArr, 15)

testArr, testLabelArr = loadDataSet()
prediction10 = adaClassify(testArr, classifierArr)
errArr = mat(ones((10, 1)))
cnt = errArr[prediction10 != mat(testLabelArr).T].sum()
print(cnt / 10)

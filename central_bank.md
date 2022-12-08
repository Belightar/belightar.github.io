layout: page
title: "PAGE TITLE"
permalink: /new_page/

# 中国外汇交易中心、全国银行间同业拆借中心 (1)

[](https://www.chinamoney.com.cn/chinese/bkfrr/)

LIVE

[](https://www.chinamoney.com.cn/chinese/mkdatapm/)

HIST

[](https://www.chinamoney.com.cn/chinese/bkcrr/)

# 外汇市场

## 人民币汇率中间价

人民币汇率中间价指交易中心根据中国人民银行授权，每日计算和发布人民币对美元等主要外汇币种汇率中间价。

人民币对美元汇率中间价的形成方式为：交易中心于每日银行间外汇市场开盘前向外汇市场做市商询价。外汇市场做市商参考上日银行间外汇市场收盘汇率，综合考虑外汇供求情况以及国际主要货币汇率变化进行报价。交易中心将全部做市商报价作为人民币对美元汇率中间价的计算样本，去掉最高和最低报价后，将剩余做市商报价加权平均，得到当日人民币对美元汇率中间价，权重由交易中心根据报价方在银行间外汇市场的交易量及报价情况等指标综合确定。

人民币对港元汇率中间价由交易中心分别根据当日人民币对美元汇率中间价与上午9时国际外汇市场港元对美元汇率套算确定。

人民币对欧元、日元、英镑、澳大利亚元、新西兰元、新加坡元、瑞士法郎、加拿大元、林吉特、俄罗斯卢布、兰特、韩元、阿联酋迪拉姆、沙特里亚尔、匈牙利福林、波兰兹罗提、丹麦克朗、瑞典克朗、挪威克朗、土耳其里拉、墨西哥比索和泰铢汇率中间价形成方式为：交易中心于每日银行间外汇市场开盘前向银行间外汇市场相应币种的做市商询价，去掉最高和最低报价后，将剩余做市商报价平均，得到当日人民币对欧元、日元、英镑、澳大利亚元、新西兰元、新加坡元、瑞士法郎、加拿大元、林吉特、俄罗斯卢布、兰特、韩元、阿联酋迪拉姆、沙特里亚尔、匈牙利福林、波兰兹罗提、丹麦克朗、瑞典克朗、挪威克朗、土耳其里拉、墨西哥比索和泰铢汇率中间价。

  

```python
# LIVE 

url = "https://www.chinamoney.com.cn/r/cms/www/chinamoney/data/fx/ccpr-mth-avg.json?t=1666776044395"

# HIST

# 中间价
url = "https://www.chinamoney.com.cn/ags/ms/cm-u-bk-ccpr/CcprHisNew?startDate=2022-09-27&endDate=2022-10-26&currency=USD/CNY,EUR/CNY,100JPY/CNY,HKD/CNY,GBP/CNY,AUD/CNY,NZD/CNY,SGD/CNY,CHF/CNY,CAD/CNY,CNY/MYR,CNY/RUB,CNY/ZAR,CNY/KRW,CNY/AED,CNY/SAR,CNY/HUF,CNY/PLN,CNY/DKK,CNY/SEK,CNY/NOK,CNY/TRY,CNY/MXN,CNY/THB&pageNum=1&pageSize=10"

# 月平均
url = "https://www.chinamoney.com.cn/ags/ms/cm-u-bk-ccpr/CcprYearAvgHisNew?startYear=2012&endYear=2021&currency=USD/CNY,EUR/CNY,100JPY/CNY,HKD/CNY,GBP/CNY,AUD/CNY,NZD/CNY,SGD/CNY,CHF/CNY,CAD/CNY,CNY/MYR,CNY/RUB,CNY/ZAR,CNY/KRW,CNY/AED,CNY/SAR,CNY/HUF,CNY/PLN,CNY/DKK,CNY/SEK,CNY/NOK,CNY/TRY,CNY/MXN,CNY/THB&pageNum=1&pageSize=10"

# 年平均
url = "https://www.chinamoney.com.cn/ags/ms/cm-u-bk-ccpr/CcprYearAvgHisNew?startYear=2012&endYear=2021&currency=USD/CNY,EUR/CNY,100JPY/CNY,HKD/CNY,GBP/CNY,AUD/CNY,NZD/CNY,SGD/CNY,CHF/CNY,CAD/CNY,CNY/MYR,CNY/RUB,CNY/ZAR,CNY/KRW,CNY/AED,CNY/SAR,CNY/HUF,CNY/PLN,CNY/DKK,CNY/SEK,CNY/NOK,CNY/TRY,CNY/MXN,CNY/THB&pageNum=1&pageSize=10"
```

## 人民币参考汇率

根据中国人民银行授权，为便于有关主体了解未在中国外汇交易中心（简称“交易中心”）挂牌交易货币对人民币的折算汇率情况，交易中心计算并公布人民币参考汇率。具体计算方法是交易中心分别根据每月最后一个交易日人民币对美元汇率中间价与上午9时国际外汇市场相应货币对美元汇率套算形成。该汇率每月最后一个交易日更新，仅供参考使用。

```python
# LIVE 

"https://www.chinamoney.com.cn/r/cms/www/chinamoney/data/fx/crr-chrt-CNYALL.xml?t=1666776168853"

# HIST

"https://www.chinamoney.com.cn/r/cms/www/chinamoney/data/fx/crr-chrt-CNYALL.xml?t=1666776168853"

```

## 人民币汇率指数

为进一步增强CFETS人民币汇率指数货币篮子代表性，中国外汇交易中心（以下简称交易中心）拟根据《CFETS人民币汇率指数货币篮子调整规则》（中汇交公告〔2016〕81号）调整CFETS人民币汇率指数货币篮子的权重，新版指数自2022年1月1日起生效。

一、调整CFETS人民币汇率指数的货币篮子权重

CFETS人民币汇率指数的篮子货币权重是采用考虑转口贸易因素的贸易权重法计算而得，现版指数采用的是2019年度贸易数据。为进一步增强指数代表性，新版指数采用2020年度贸易数据作为权重进行调整。经历史回溯试算，新版和现版CFETS人民币汇率指数运行趋势基本吻合。

**表1 新版CFETS货币篮子和权重**

| 币种 | 权重 |
| --- | --- |
| USD | 0.1988 |
| EUR | 0.1845 |
| JPY | 0.1076 |
| HKD | 0.0346 |
| GBP | 0.0313 |
| AUD | 0.0571 |
| NZD | 0.0061 |
| SGD | 0.0302 |
| CHF | 0.0076 |
| CAD | 0.0217 |
| MYR | 0.0444 |
| RUB | 0.0366 |
| ZAR | 0.0121 |
| KRW | 0.0967 |
| AED | 0.0167 |
| SAR | 0.0228 |
| HUF | 0.004 |
| PLN | 0.0105 |
| DKK | 0.0046 |
| SEK | 0.0061 |
| NOK | 0.0037 |
| TRY | 0.0082 |
| MXN | 0.0206 |
| THB | 0.0335 |

二、保持BIS货币篮子和权重不变

国际清算银行（BIS）自2019年4月以来未调整汇率指数的货币篮子及权重，故交易中心继续保持BIS货币篮子人民币汇率指数的货币篮子和权重不变。

**表2 BIS货币篮子和权重**

| 币种 | 权重 |
| --- | --- |
| USD | 0.196807605546305 |
| EUR | 0.180341487906990 |
| JPY | 0.119337085872547 |
| HKD | 0.009545347000566 |
| GBP | 0.030100023232646 |
| AUD | 0.013762591023056 |
| NZD | 0.002288156660129 |
| SGD | 0.029627571487147 |
| CHF | 0.014074414390102 |
| CAD | 0.020534052391550 |
| MYR | 0.021461977052835 |
| RUB | 0.014234779188439 |
| THB | 0.021525322330631 |
| AED | 0.007726583944420 |
| ARS | 0.003832921664745 |
| BGN | 0.000906653219964 |
| BRL | 0.012050618379314 |
| CLP | 0.007589438341455 |
| COP | 0.002905041182442 |
| CZK | 0.006722982818794 |
| DKK | 0.004097265334114 |
| DZD | 0.001884431374940 |
| HRK | 0.000401733441415 |
| HUF | 0.004312711927208 |
| IDR | 0.013609912681645 |
| ILS | 0.004464240559451 |
| INR | 0.025170316543314 |
| KRW | 0.087769079809287 |
| MXN | 0.025457186558152 |
| NOK | 0.003527240428385 |
| PEN | 0.002907146893037 |
| PHP | 0.008420955588068 |
| PLN | 0.009643059812242 |
| RON | 0.002595755432589 |
| SAR | 0.009053862821189 |
| SEK | 0.007192810679931 |
| TRY | 0.009107158356225 |
| TWD | 0.059407216805689 |
| ZAR | 0.005433822973667 |
| ISK | 0.000169438345375 |

三、保持SDR货币篮子和权重不变

自2016年10月1日人民币正式加入SDR货币篮子以来，SDR货币篮子及权重未发生改变，故交易中心继续保持SDR货币篮子人民币汇率指数的货币篮子和权重不变。

**表3 SDR货币篮子和权重**

| 币种 | 权重 |
| --- | --- |
| USD | 0.4685 |
| EUR | 0.3472 |
| JPY | 0.0935 |
| GBP | 0.0908 |

```python
# LIVE 

"https://www.chinamoney.com.cn/ags/ms/cm-u-bk-fx/RmbIdxChrt?indexType=3&t=1666776284518"

# HIST

"https://www.chinamoney.com.cn/ags/ms/cm-u-bk-fx/RmbIdxHis?lang=cn&startDate=2021-11-24&endDate=2022-10-26&t=1666776349682"

```

## USD CIROR

境内外币同业拆放参考利率（CFETS Interbank Reference Offered Rate，简称CIROR）是由交易中心根据境内信用等级较高、外币定价能力较强、外币拆借交易相对活跃的银行报价计算并发布的以单利计息、无担保、批发性的拆出利率。目前公布的CIROR币种为美元，品种包括隔夜、1周、2周、1个月、3个月、6个月、9个月及1年。

交易中心每个交易日根据各报价行的报价，剔除最高、最低各2家报价，对其余报价进行算术平均计算后，得出每一期限品种的USD CIROR，并于10:00对外发布。

CIROR报价行与交易中心签署外币拆借报价行协议，承诺遵守报价规则，履行报价行义务，并接受交易中心的检查和评估。

| 序号 | 报价行名称 | 银行网址 |
| --- | --- | --- |
| 1 | 国开行 | http://www.cdb.com.cn/ |
| 2 | 进出口行 | http://www.eximbank.gov.cn/ |
| 3 | 工商银行 | http://www.icbc.com.cn |
| 4 | 农业银行 | http://www.abchina.com |
| 5 | 中国银行 | http://www.boc.cn |
| 6 | 建设银行 | http://www.ccb.com |
| 7 | 交通银行 | http://www.bankcomm.com |
| 8 | 中信银行 | http://www.ecitic.com |
| 9 | 光大银行 | http://www.cebbank.com |
| 10 | 华夏银行 | http://www.hxb.com.cn/chinese |
| 11 | 民生银行 | http://www.cmbc.com.cn |
| 12 | 邮储银行 | http://www.psbc.com |
| 13 | 浦发银行 | http://www.spdb.com.cn |
| 14 | 招商银行 | http://www.cmbchina.com/ |
| 15 | 兴业银行 | http://www.cib.com.cn |
| 16 | 广发银行 | http://www.cgbchina.com.cn |
| 17 | 浙商银行 | http://www.czbank.com |
| 18 | 上海银行 | http://www.bankofshanghai.com |
| 19 | 南京银行 | http://www.njcb.com.cn |
| 20 | 宁波银行 | http://www.nbcb.com.cn |
| 21 | 平安银行 | https://bank.pingan.com/ |
| 22 | 江苏银行 | http://www.jsbchina.cn/ |
| 23 | 杭州银行 | http://www.hzbank.com.cn/ |

USD CIROR均值

| USD CIROR | 2022-10-26 | 5日均值 | 10日均值 | 20日均值 |
| --- | --- | --- | --- | --- |
| O/N | 3.05 | 3.05 | 3.05 | 3.05 |
| 1W | 3.17 | 3.14 | 3.14 | 3.13 |
| 2W | 3.31 | 3.27 | 3.25 | 3.23 |
| 1M | 3.53 | 3.47 | 3.42 | 3.37 |
| 3M | 4.07 | 4.02 | 3.98 | 3.93 |
| 6M | 4.41 | 4.36 | 4.32 | 4.24 |
| 9M | 4.53 | 4.48 | 4.44 | 4.38 |
| 1Y | 4.68 | 4.63 | 4.59 | 4.53 |

```python
# LIVE
# 境内美元同业拆放参考利率(USD CIROR)
"https://www.chinamoney.com.cn/r/cms/www/chinamoney/data/shibor/usdshibor.json?t=1666778254678"

# USD CIROR均值
"https://www.chinamoney.com.cn/r/cms/www/chinamoney/data/shibor/USDMean.json?t=1666778112304"

# HIST
# USD CIROR数据
"https://www.chinamoney.com.cn/ags/ms/cm-u-bk-ciror/USDHis?lang=CN&startDate=2022-09-27&endDate=2022-10-26&t=1666778323820"

# USD CIROR均值数据
"https://www.chinamoney.com.cn/ags/ms/cm-u-bk-ciror/USDMnHis?lang=CN&startDate=2022-09-29&endDate=2022-10-26&tendencyvalue=&t=1666778448213"
```

## 外汇掉期曲线

**一、外汇掉期曲线**

外汇掉期曲线是由外汇掉期各期限代表性价格（掉期点）构成的行情曲线，曲线数据包括掉期点和掉期全价汇率。交易中心外汇掉期曲线选用了外汇交易系统行情（成交价、询价报价、C-Swap订单报价）和货币经纪报价（可成交报价、意向报价）为数据样本，利用报价数据过滤了异常交易价格，数据质量较高，可作为机构中后台外汇掉期等产品定价参考基准。

**（一）货币对和关键期限点**

| 货币对 | 关键期限 |
| --- | --- |
| USD.CNY | ON、TN、SN、1W、2W、3W、1M、2M、3M、4M、5M、6M、9M、1Y、18M、2Y、3Y、4Y、5Y |
| EUR.CNY | ON、TN、SN、1W、2W、3W、1M、2M、3M、4M、5M、6M、9M、1Y、18M、2Y、3Y |
| JPY.CNY | ON、TN、SN、1W、2W、3W、1M、2M、3M、4M、5M、6M、9M、1Y、18M、2Y、3Y |
| HKD.CNY | ON、TN、SN、1W、2W、3W、1M、2M、3M、4M、5M、6M、9M、1Y、18M、2Y、3Y |
| GBP.CNY | ON、TN、SN、1W、2W、3W、1M、2M、3M、4M、5M、6M、9M、1Y、18M、2Y、3Y |
| EUR.USD | ON、TN、SN、1W、2W、3W、1M、2M、3M、4M、5M、6M、9M、1Y |
| EUR.USD | ON、TN、SN、1W、2W、3W、1M、2M、3M、4M、5M、6M、9M、1Y |
| USD.HKD | ON、TN、SN、1W、2W、3W、1M、2M、3M、4M、5M、6M、9M、1Y |
| USD.HKD | ON、TN、SN、1W、2W、3W、1M、2M、3M、4M、5M、6M、9M、1Y |
| AUD.USD | ON、TN、SN、1W、2W、3W、1M、2M、3M、4M、5M、6M、9M、1Y |

**（二）曲线样本选择**

USD.CNY外汇掉期曲线数据样本包括外汇交易系统成交价、C-Swap订单报价、货币经纪可成交报价和货币经纪意向报价，EUR.CNY等其他货币对外汇掉期曲线数据样本为外汇交易系统成交价和询价双边报价。

选价流程：

1、发布时刻点，对于USD.CNY外汇掉期曲线，取出截止发布时刻点的各期限有效的成交价、最新C-Swap订单报价、货币经纪可成交报价和货币经纪意向报价；对于EUR.CNY等其他货币对外汇掉期曲线，取出截止发布时刻点的各期限有效的成交价、最新交易系统询价双边报价。

2、根据当日之前外汇掉期曲线历史波动方差，按照一定置信水平，确定当日的报价正常波动范围，该范围以外的报价（包括交易系统询价双边报价、C-Swap订单报价、货币经纪可成交报价和货币经纪意向报价）被判为异常价格。

3、选出每个期限最新的报买掉期点（bid）和报卖掉期点（ask）。对于USD.CNY外汇掉期曲线，根据C-Swap订单报价、货币经纪可成交报价计算出可成交代表性价格，bid和ask掉期点优先选用可成交代表性价格，可成交代表性价格缺失或价差过大时，选用货币经纪意向报价；对于EUR.CNY等其他货币对外汇掉期曲线，bid和ask掉期点取自交易系统询价双边报价。交易中心定期调整报价的选价优先级。

4、在发布时刻点，取出当日所有掉期点位于报价区间[bid, ask]内的成交，取成交时间最晚的成交作为该期限掉期点代表，标记数据源为交易数据；如果取不到交易数据，则利用报价均值作为该期限掉期点代表，标记数据源为报价数据。

**（三）曲线发布频率**

每个工作日17:00通过中国货币网发布当日16:30的外汇掉期曲线。

**二、USD.CNY外汇掉期C-Swap定盘曲线**

USD.CNY外汇掉期C-Swap定盘曲线是由外汇掉期各期限代表性价格（掉期点）构成的行情曲线，曲线选用了外汇交易系统C-Swap订单报价和成交价为数据样本，是C-Swap市场的估值定价基准曲线。

**（一）关键期限点**

ON、TN、SN、1W、2W、3W、1M、2M、3M、6M、9M、1Y等期限品种。

**（二）曲线样本选择**

外汇掉期C-Swap定盘曲线数据样本包括外汇交易系统C-Swap报价和成交价。

选价流程：

1、发布时刻点，取出截止发布时刻点的各期限有效的最新交易系统C-Swap最优订单报价、C-Swap成交价，分别取值为“报价”和“成交价”。

2、选出每个期限最新的最优订单报买掉期点（bid）和报卖掉期点（ask），如果最优订单同时存在报买和报卖，则“报价”取值为最优报价均值，最优订单同时存在报买和报卖但报价倒挂或只有单边报价，则“报价”取值为最新单边报价。

3、选出每个期限最新的成交价为“成交价”。

4、取“报价”和“成交价”最新的价格作为曲线数值，掉期点数据源分别标识为“报价数据”和“交易数据”。

**（三）曲线发布频率**

每个工作日17:00发布当日外汇掉期C-Swap定盘曲线。

```python

Foreign Exchange SWAP Curve

curveType_list = ['USD.CNY', 'EUR.CNY', 'JPY.CNY', 'HKD.CNY', 'GBP.CNY',
'EUR.USD', 'USD.JPY', 'USD.HKD', 'GBP.USD', 'AUD.USD']

# LIVE
"https://www.chinamoney.com.cn/r/cms/www/chinamoney/data/fx/fx-sw-curv-USD.CNY.json?t=1666839126219"

# HIST
"https://www.chinamoney.com.cn/ags/ms/cm-u-bk-fx/FxSwapHisory?startDate=2022-09-29&endDate=2022-10-27&curveType=&time=&page=1&pagesize=15"

https://www.chinamoney.com.cn/dqs/rest/cm-u-bk-fx/FxSwapHisoryExcel?startDate=2022-09-27&endDate=2022-10-27&curveType=&time=&t=1666850918929

Foreign Exchange C-SWAP Fixed Curve

curveType=USD.CNY fixed

# LIVE
"https://www.chinamoney.com.cn/r/cms/www/chinamoney/data/fx/fx-c-sw-curv-USD.CNY.json?t=1666839449516"

# HIST
"https://www.chinamoney.com.cn/ags/ms/cm-u-bk-fx/FxCSwapHisory?startDate=2022-09-27&endDate=2022-10-11&curveType=USD.CNY&time=&page=1&pagesize=15"
https://www.chinamoney.com.cn/dqs/rest/cm-u-bk-fx/FxCSwapHisoryExcel?startDate=2022-09-27&endDate=2022-10-21&curveType=USD.CNY&time=&t=1666851174849

```

## 外币隐含利率曲线

**外币隐含利率曲线编制说明**

外币隐含利率曲线是根据利率平价理论，由人民币利率和外汇掉期价格得到的各期限隐含外币利率的曲线。

**一、外币隐含利率曲线参数组合**

1、参数组合

外币隐含利率曲线的基础参数包括人民币利率、掉期价格和即期价格，交易中心共提供如下表所示的6类曲线。

| 人民币利率 | 外汇远/掉期点 | 外汇即期价格 |
| --- | --- | --- |
| Shibor | 掉期点 | 即期询价均值 |
| Shibor | 掉期点 | 中间价 |
| Shibor3M利率互换收盘曲线 | 掉期点 | 即期询价均值 |
| Shibor3M利率互换收盘曲线 | 掉期点 | 中间价 |
| FR007利率互换收盘曲线 | 掉期点 | 即期询价均值 |
| FR007利率互换收盘曲线 | 掉期点 | 中间价 |

2、人民币利率

Shibor是指1Y以下（含1Y）是Shibor（连续复利利率），1Y以上是交易中心Shibor3M利率互换收盘曲线的即期利率曲线（连续复利利率）

Shibor3M利率互换收盘曲线是指3M以下（含3M）是Shibor（连续复利利率），3M以上是交易中心Shibor3M利率互换收盘曲线的即期利率曲线（连续复利利率）。

FR007利率互换收盘曲线是指1D、1W、2W是FR001、FR007、FR014（连续复利利率），2W以上是交易中心FR007利率互换收盘曲线的即期利率曲线（连续复利利率）。

3、外汇远/掉期点

外汇远/掉期点是指交易中心外汇掉期曲线各关键期限点的曲线数据。

4、外汇即期价格

即期询价均值是指外汇交易系统的最新的询价最优买卖报价均值。

中间价是中国人民银行每日公布的人民币汇率中间价。

**二、  外币隐含利率曲线计算公式**

3M以下（含3M）Shibor3M利率互换收盘曲线（Shibor3M利率互换收盘曲线-掉期点-即期询价均值的参数组合）外币隐含利率曲线（连续复利利率）计算公式：

![https://www.chinamoney.com.cn/ewebeditor/uploadfile/20180406005538341001.png](https://www.chinamoney.com.cn/ewebeditor/uploadfile/20180406005538341001.png)

![https://www.chinamoney.com.cn/ewebeditor/uploadfile/20180406005538356002.png](https://www.chinamoney.com.cn/ewebeditor/uploadfile/20180406005538356002.png)

其他3M以下（含3M）和3M以上的计算公式则根据人民币利率曲线、人民币利率单复利、美元利率单复利、计息方式、外汇掉期点、外汇即期价格等要素做相应调整。

**三、曲线发布频率**

每个工作日16:50发布当日外币隐含利率曲线。

```python
# 数字非常近似
ccyPair_list = ['USD.CNY', 'EUR.CNY', 'JPY.CNY', 'HKD.CNY', 'GBP.CNY']
# 查询历史数据跨度一个月

# SHIBOR 3M

# Live
"https://www.chinamoney.com.cn/ags/ms/cm-u-bk-fx/IuirCurv?rmbRateSrc=24&bpSrc=26&spotrateSrc=29&ccyPair=USD.CNY&t=1666840175602"
# HIST 
"https://www.chinamoney.com.cn/ags/ms/cm-u-bk-fx/IuirCurvHis?rmbRateSrc=24&spotrateSrc=&bpSrc=&startDate=2022-09-27&endDate=2022-10-26&ccyPair=&page=1&pageSize=15"

# FROO7
# LIVE
"https://www.chinamoney.com.cn/ags/ms/cm-u-bk-fx/IuirCurv?rmbRateSrc=25&bpSrc=26&spotrateSrc=29&ccyPair=USD.CNY&t=1666840175602"
# HIST 
"https://www.chinamoney.com.cn/ags/ms/cm-u-bk-fx/IuirCurvHis?rmbRateSrc=25&spotrateSrc=&bpSrc=&startDate=2022-09-27&endDate=2022-10-12&ccyPair=&page=1&pageSize=15"

# SHIBOR
# LIVE
"https://www.chinamoney.com.cn/ags/ms/cm-u-bk-fx/IuirCurv?rmbRateSrc=23&bpSrc=26&spotrateSrc=29&ccyPair=USD.CNY&t=1666840130881"
# HIST
"https://www.chinamoney.com.cn/ags/ms/cm-u-bk-fx/IuirCurvHis?rmbRateSrc=23&spotrateSrc=&bpSrc=&startDate=2022-09-27&endDate=2022-10-12&ccyPair=&page=1&pageSize=15"

https://www.chinamoney.com.cn/dqs/rest/cm-u-bk-fx/IuirCurvHisExcel?lang=CN&rmbRateSrc=&spotrateSrc=&bpSrc=&startDate=2022-09-27&endDate=2022-10-27&ccyPair=&t=1666859784914
```

## 外汇期权隐含波动率曲线

**外币隐含利率曲线编制说明**

外币隐含利率曲线是根据利率平价理论，由人民币利率和外汇掉期价格得到的各期限隐含外币利率的曲线。

**一、外币隐含利率曲线参数组合**

1、参数组合

外币隐含利率曲线的基础参数包括人民币利率、掉期价格和即期价格，交易中心共提供如下表所示的6类曲线。

| 人民币利率 | 外汇远/掉期点 | 外汇即期价格 |
| --- | --- | --- |
| Shibor | 掉期点 | 即期询价均值 |
| Shibor | 掉期点 | 中间价 |
| Shibor3M利率互换收盘曲线 | 掉期点 | 即期询价均值 |
| Shibor3M利率互换收盘曲线 | 掉期点 | 中间价 |
| FR007利率互换收盘曲线 | 掉期点 | 即期询价均值 |
| FR007利率互换收盘曲线 | 掉期点 | 中间价 |

2、人民币利率

Shibor是指1Y以下（含1Y）是Shibor（连续复利利率），1Y以上是交易中心Shibor3M利率互换收盘曲线的即期利率曲线（连续复利利率）

Shibor3M利率互换收盘曲线是指3M以下（含3M）是Shibor（连续复利利率），3M以上是交易中心Shibor3M利率互换收盘曲线的即期利率曲线（连续复利利率）。

FR007利率互换收盘曲线是指1D、1W、2W是FR001、FR007、FR014（连续复利利率），2W以上是交易中心FR007利率互换收盘曲线的即期利率曲线（连续复利利率）。

3、外汇远/掉期点

外汇远/掉期点是指交易中心外汇掉期曲线各关键期限点的曲线数据。

4、外汇即期价格

即期询价均值是指外汇交易系统的最新的询价最优买卖报价均值。

中间价是中国人民银行每日公布的人民币汇率中间价。

**二、  外币隐含利率曲线计算公式**

3M以下（含3M）Shibor3M利率互换收盘曲线（Shibor3M利率互换收盘曲线-掉期点-即期询价均值的参数组合）外币隐含利率曲线（连续复利利率）计算公式：

![https://www.chinamoney.com.cn/ewebeditor/uploadfile/20180406005538341001.png](https://www.chinamoney.com.cn/ewebeditor/uploadfile/20180406005538341001.png)

![https://www.chinamoney.com.cn/ewebeditor/uploadfile/20180406005538356002.png](https://www.chinamoney.com.cn/ewebeditor/uploadfile/20180406005538356002.png)

其他3M以下（含3M）和3M以上的计算公式则根据人民币利率曲线、人民币利率单复利、美元利率单复利、计息方式、外汇掉期点、外汇即期价格等要素做相应调整。

**三、曲线发布频率**

每个工作日16:50发布当日外币隐含利率曲线。

```python
# 数字非常近似

volatilitySurface_dict = {
ATM     : 0,
10D PUT : 1,
10D CALL: 2,
25D PUT : 3,
25D CALL: 4,
25D RR  : 7,
25D BF  : 8,
10D RR  : 9,
10D BF  : a
}

tradeTime_list = ['10:00', '11:00', '14:00', '15:00', '16:00']

ccyPair_list = ['USD.CNY', 'EUR.CNY', 'JPY.CNY', 'HKD.CNY', 'GBP.CNY']

rmbRateSrc_dict = {
SHIBOR =  23,
SHIBOR 3M = 24,
FROO7 = 25
}
# 不指定就显示全部

spotrateSrc_dict = {
spot = 28,
# 即期均价报价均值
interval = 29
# 中间价
}
# 不指定就显示全部

# Live
https://www.chinamoney.com.cn/ags/ms/cm-u-bk-fx/FoivltltyCurv?ccyPair=USD.CNY&volatilitySurface=0&ccyTime=10:00&ccyDate=2022-10-27

https://www.chinamoney.com.cn/ags/ms/cm-u-bk-fx/FoivltltyCurv?ccyPair=USD.CNY&volatilitySurface=5&ccyTime=11:00&ccyDate=2022-10-27

https://www.chinamoney.com.cn/ags/ms/cm-u-bk-fx/FoivltltyCurv?ccyPair=USD.CNY&volatilitySurface=7&ccyTime=10:00&ccyDate=2022-10-27

# HIST 

https://www.chinamoney.com.cn/ags/ms/cm-u-bk-fx/IuirCurvHis?rmbRateSrc=23&spotrateSrc=28&bpSrc=26&startDate=2022-09-27&endDate=2022-10-27&ccyPair=USD.CNY&page=1&pageSize=15

# EXCEL
https://www.chinamoney.com.cn/ags/ms/cm-u-bk-fx/IuirCurvHis?rmbRateSrc=&spotrateSrc=29&bpSrc=26&startDate=2022-09-27&endDate=2022-10-27&ccyPair=USD.CNY
```

## 外汇期权Delta计量参数

为方便会员计量外汇期权产品Delta头寸，交易中心按日计算和发布USD.CNY外汇期权Delta头寸计量参数。

**一、USD.CNY外汇期权Delta头寸计量参数算法**

按照如下公式计量期权产品Delta头寸：

看涨期权

$Delta = e^{(-r_ft_2N(d_1))}$

看跌期权

$Delta = e^{(-r_ft_2[N(d_1)-1])}$

其中，

$d_1=\frac{ln(F/K)}{σ\sqrt{t_1}}+\frac{σ\sqrt{t_1}}{2}$

**二、USD.CNY外汇期权Delta头寸计量参数**

$S$（外汇即期汇率）：取自中间价、即期询价均值。

$σ$（波动率）：取外汇期权隐含波动率曲线（ATM）。

$r_d$（人民币利率）：人民币利率“Shibor”、人民币利率“回购定盘利率/FR007利率互换收盘曲线”、人民币利率“Shibor/Shibor3M利率互换收盘曲线”。

$r_f$（美元利率）：美元隐含利率曲线。

$t_1$（期限）：成交日至到期日。

$t_2$（期限）：即期起息日至交割日。

$K$（执行价格）：自行逐笔选取。

**三、发布的频率**

每个工作日17:00发布当日外汇期权Delta头寸计量参数。

```python

https://www.chinamoney.com.cn/dqs/rest/cm-u-bk-fx/FodpParamHisExcel?init=flase&startDate=2022-09-27&endDate=2022-10-27&spotPriceType=&rmbRateType=&volatilitySurface=&t=1666861218809
https://www.chinamoney.com.cn/dqs/rest/cm-u-bk-fx/FodpParamHisExcel?init=flase&startDate=2022-09-27&endDate=2022-10-27&spotPriceType=&rmbRateType=&volatilitySurface=&t=1666861336723
```

## 货币掉期曲线

货币掉期曲线由中国外汇交易中心编制和发布。

**一、货币掉期曲线种类及交易要素**

| 曲线种类 | 标准期限 | 付息周期 | 计息基准 |
| --- | --- | --- | --- |
| 人民币固定利率对美元Libor 3M | 1Y、2Y、3Y、4Y、
5Y | 人民币固定利率及3个月美元Libor付息周期均为三个月 | 人民币固定利率(Act/365)
美元Libor(Act/360) |
| 人民币Shibor 3M对美元Libor 3M | 1Y、2Y、3Y、4Y、
5Y | 3个月人民币Shibor及3个月美元Libor付息周期均为三个月 | 人民币Shibor(Act/360)
美元Libor(Act/360) |

**二、报价机构**

人民币外汇远掉期做市商。

**三、报价平台**

报价机构在外汇交易系统货币掉期双边报价界面同时报Bid/Ask两个方向报价。

**四、曲线算法**

交易中心取各机构的最新报价，根据以下规则计算：

（1）计算报买(Bid)曲线和报卖(Ask)曲线

在当天计算时点16:30，获取所有报价机构的最新有效报价。首先，剔除Bid >Ask报价数据；其次，对于有效Bid（Ask）报价，如果报价数量大于等于8个，剔除最高和最低的2个报价，如果报价数量小于8个，不做剔除。对剩余的Bid（Ask）报价做算数平均，得到报买曲线（报卖）曲线。

（2）计算均值曲线

均值曲线为报买和报卖曲线的平均。

**五、发布时间**

每个工作日17:15发布当日货币掉期曲线。

```python

# 时间：	16:30
curve_type_dict={
currency swap curve (RMB fixed rate 2 USD Libor 3M): 1,
#货币掉期曲线（人民币固定利率对美元LIBOR3M）
currency swap curve (RMB Shibor 3M 2 USD Libor 3M): 2
#货币掉期曲线（人民币SHIBOR3M对美元LIBOR3M）
}

All
https://www.chinamoney.com.cn/dqs/rest/cm-u-bk-fx/CswCurvHisExcel?startDate=2022-09-27&endDate=2022-10-27&curveType=0&bidAskType=0&t=1666861519902

currency swap curve (RMB fixed rate 2 USD Libor 3M)
https://www.chinamoney.com.cn/dqs/rest/cm-u-bk-fx/CswCurvHisExcel?startDate=2022-09-27&endDate=2022-10-27&curveType=1&bidAskType=0&t=1666861620870

currency swap curve (RMB Shibor 3M 2 USD Libor 3M)
https://www.chinamoney.com.cn/dqs/rest/cm-u-bk-fx/CswCurvHisExcel?startDate=2022-09-27&endDate=2022-10-27&curveType=2&bidAskType=0&t=1666861564064
```

# 本币市场

## Shibor

Shibor简介

上海银行间同业拆放利率（Shanghai Interbank Offered Rate，简称Shibor），以位于上海的全国银行间同业拆借中心为技术平台计算、发布并命名，是由信用等级较高的银行组成报价团自主报出的人民币同业拆出利率计算确定的算术平均利率，是单利、无担保、批发性利率。目前，对社会公布的Shibor品种包括隔夜、1周、2周、1个月、3个月、6个月、9个月及1年。

Shibor报价银行团现由18家商业银行组成。报价银行是公开市场一级交易商或外汇市场做市商，在中国货币市场上人民币交易相对活跃、信息披露比较充分的银行。中国人民银行成立Shibor工作小组，依据《上海银行间同业拆放利率（Shibor）实施准则》确定和调整报价银行团成员、监督和管理Shibor运行、规范报价行与指定发布人行为。

全国银行间同业拆借中心受权Shibor的报价计算和信息发布。每个交易日根据各报价行的报价，剔除最高、最低各4家报价，对其余报价进行算术平均计算后，得出每一期限品种的Shibor，并于11:00对外发布。

Shibor实施准则

**第一章 总 则**

第一条 为规范中国货币市场基准利率的形成机制、信息发布机制和监督管理机制，特制定本准则。

第二条 上海银行间同业拆放利率（Shanghai Interbank Offered Rate，简称Shibor）是由信用等级较高的银行自主报出的人民币同业拆出利率计算确定的算术平均利率，是单利、无担保、批发性利率。

第三条 市场利率定价自律机制成立Shibor工作组（以下简称工作组），依据本准则确定和调整报价银行团成员、监督和管理Shibor运行、规范报价行与指定发布人行为。

**第二章 报价银行团构成**

第四条 报价银行团由符合条件的商业银行组成。

第五条 报价行原则上应具备以下条件：

（一）是市场利率定价自律机制成员；

（二）具有公开市场一级交易商资格或外汇市场做市商资格；

（三）货币市场交易活跃，即交易量较大、交易连续性较好、价差较小。交易量指报价行在中国货币市场所有交易的总量，包括公开市场交易、同业拆借交易、债券回购交易、现券交易、货币市场衍生品交易等；

（四）信用等级较高；

（五）已建立内部收益率曲线和内部转移定价机制，具有较强的利率定价能力；

（六）通过上海银行间同业拆放利率网（www.shibor.org）等工作组指定的媒体每年披露经注册会计师审计的上年年度报告；

（七）有利于开展报价工作的其它条件。

第六条 符合上述条件、并愿意成为报价行的商业银行应于每年12月1日前向工作组提交申请及相关材料。经审核合格后可成为场外报价行，在场外进行Shibor报价。工作组结合报价等情况，在报价一年以上的场外报价行中，择优选取下一年的Shibor报价行。工作组根据本准则于每年年初公布当年的报价银行团成员名单。

**第三章 报价行职责**

第七条 提供拆出报价。该报价是基于市场情况的报价，是单利、无担保、批发性利率。报价行当日货币市场交易利率都以其报价利率为基准。报价行应独立报价，当日不得相互参照报价。

第八条 每个交易日（以下简称每日）上午10:55前通过上海银行间同业拆放利率网提供的报价界面完成报价。报价行每日应按时报价，保证质量。

第九条 每日对隔夜、1周、2周、1个月、3个月、6个月、9个月及1年八个品种进行报价。利率品种代码按期限长短排列为O/N、1W、2W、1M、3M、6M、9M、1Y（O/N代表隔夜，W代表周，M代表月，Y代表年）。

第十条 以年利率（％，Act/360，T+0）对各期限品种报价，保留4位小数。

第十一条 报价行应加强内控，建立流程清晰、权责明确的定价机制和报价程序，建立报价记录留存制度。报价行报价要做到专人专岗，并及时向市场利率定价自律机制备案。

第十二条 建立应急机制，确保每日按时报出各期限品种的利率。

**第四章 指定发布人及其职责**

第十三条 全国银行间同业拆借中心受权为Shibor的指定发布人。

第十四条 负责提供报价界面，对接收到的每一期限品种的拆出利率数据，剔除最高、最低各4家报价，对其余报价进行算术平均计算后，得出每一期限品种的Shibor，于每日上午11:00对外公布，同时公布各报价行的拆出报价。

第十五条 在上午10:55前鉴别报价行报价的可能差错，及时进行提示。如有报价行未报价，指定发布人根据已报的数据确定Shibor，同时将此情况以书面形式报告工作组。

第十六条 负责维护上海银行间同业拆放利率系统。

第十七条 建立Shibor的备份、应急机制，确保每日Shibor的正常运行和历史资料储存。

第十八条 组织Shibor场外报价行报价。

**第五章 工作组的运行机制**

第十九条 根据商业银行的申请，按照本准则确定和调整报价银行团成员和场外报价银行团成员。

第二十条 组织报价行和场外报价行按本准则要求开展报价，对指定发布人发布Shibor信息等行为进行日常管理。

第二十一条 按月、季、年评估报价行有关报价行为，通报Shibor运行情况，对报价行报价质量进行考评。

**第六章 监督管理**

第二十二条 对报价行实行淘汰制。工作组建立报价考评指标体系，并定期对报价行的报价质量、定价机制和报价程序等进行现场检查和非现场检查。工作组每年对所有报价银行团成员的报价记录进行考评，确定淘汰更新方案并公布。

第二十三条 工作组负责监督管理指定发布人，每年对指定发布人履行职责的各项情况进行考核。

第二十四条 指定发布人根据工作组授权，对报价行报价质量进行现场监督和考核。如果报价行出现违反本准则行为，应及时发出警告，要求其改正，并报告工作组。指定发布人应及时记录、披露报价行违反本准则的行为和改正情况，按月向工作组报告Shibor的运行情况。

### 报价行成员

[](https://www.chinamoney.com.cn/r/cms/www/chinamoney/data//shibor/shibor-pnl-bk.json)

```python
[https://www.chinamoney.com.cn/r/cms/www/chinamoney/data//shibor/shibor-pnl-bk.json](https://www.chinamoney.com.cn/r/cms/www/chinamoney/data//shibor/shibor-pnl-bk.json)
{"memCode":"100000911000000102001","code":"100009","cname":"光大银行","ename":"CEB","linkUrl":"http://www.cebbank.com","index":8}
```

| 序号 | 报价行名称 | 银行网址 |
| --- | --- | --- |
| 1 | 工商银行 | http://www.icbc.com.cn |
| 2 | 农业银行 | http://www.abchina.com |
| 3 | 中国银行 | http://www.boc.cn |
| 4 | 建设银行 | http://www.ccb.com |
| 5 | 交通银行 | http://www.bankcomm.com |
| 6 | 招商银行 | http://www.cmbchina.com/ |
| 7 | 中信银行 | http://www.citicbank.com |
| 8 | 光大银行 | http://www.cebbank.com |
| 9 | 兴业银行 | http://www.cib.com.cn |
| 10 | 浦发银行 | http://www.spdb.com.cn |
| 11 | 北京银行 | http://www.bankofbeijing.com.cn |
| 12 | 上海银行 | http://www.bankofshanghai.com |
| 13 | 汇丰银行 | http://www.hsbc.com.cn |
| 14 | 华夏银行 | http://www.hxb.com.cn/chinese |
| 15 | 广发银行 | http://www.cgbchina.com.cn |
| 16 | 邮储银行 | http://www.psbc.com |
| 17 | 国开行 | http://www.cdb.com.cn/ |
| 18 | 民生银行 | http://www.cmbc.com.cn |

```python
# LIVE 

https://www.chinamoney.com.cn/r/cms/www/chinamoney/data/shibor/shibor.json?t=1666926189889

# 均值
https://www.chinamoney.com.cn/r/cms/www/chinamoney/data/shibor/shibor-mn.json?t=1666926189888

# 成员报价
memCode = 
{"head":{"version":"2.0","provider":"CWAP","req_code":"","rep_code":"200","rep_message":"","ts":1616461500020,"producer":""},"records":[{"memCode":"100000111000000101001","code":"100001","cname":"工商银行","ename":"ICBC","linkUrl":"http://www.icbc.com.cn","index":1},{"memCode":"100000211000000101001","code":"100003","cname":"农业银行","ename":"ABC","linkUrl":"http://www.abchina.com","index":2},{"memCode":"100000311000000101001","code":"100002","cname":"中国银行","ename":"BOC","linkUrl":"http://www.boc.cn","index":3},{"memCode":"100000411000000101001","code":"100004","cname":"建设银行","ename":"CBC","linkUrl":"http://www.ccb.com","index":4},{"memCode":"100000531000000102001","code":"100005","cname":"交通银行","ename":"BOCOM","linkUrl":"http://www.bankcomm.com","index":5},{"memCode":"100000844030000102001","code":"100008","cname":"招商银行","ename":"CMB","linkUrl":"http://www.cmbchina.com/","index":6},{"memCode":"100000711000000102001","code":"100007","cname":"中信银行","ename":"CNCB","linkUrl":"http://www.citicbank.com","index":7},{"memCode":"100000911000000102001","code":"100009","cname":"光大银行","ename":"CEB","linkUrl":"http://www.cebbank.com","index":8},{"memCode":"100001435010000102001","code":"100014","cname":"兴业银行","ename":"CIB","linkUrl":"http://www.cib.com.cn","index":9},{"memCode":"200001131000000102001","code":"100011","cname":"浦发银行","ename":"SPDB","linkUrl":"http://www.spdb.com.cn","index":10},{"memCode":"101000111000000104001","code":"100073","cname":"北京银行","ename":"BOB","linkUrl":"http://www.bankofbeijing.com.cn","index":11},{"memCode":"102000031000000104001","code":"100051","cname":"上海银行","ename":"BOS","linkUrl":"http://www.bankofshanghai.com","index":12},{"memCode":"290000531000000106001","code":"102294","cname":"汇丰银行","ename":"HSBC","linkUrl":"http://www.hsbc.com.cn","index":13},{"memCode":"100001011000000102001","code":"100010","cname":"华夏银行","ename":"HXB","linkUrl":"http://www.hxb.com.cn/chinese","index":14},{"memCode":"100001244010000102001","code":"100012","cname":"广发银行","ename":"GDB","linkUrl":"http://www.cgbchina.com.cn","index":15},{"memCode":"101050011000000208011","code":"101747","cname":"邮储银行","ename":"PSBC","linkUrl":"http://www.psbc.com","index":16},{"memCode":"100005311000000103001","code":"100034","cname":"国开行","ename":"CDB","linkUrl":"http://www.cdb.com.cn/","index":17},{"memCode":"100001511000000102001","code":"100015","cname":"民生银行","ename":"CMSB","linkUrl":"http://www.cmbc.com.cn","index":18}]}

https://www.chinamoney.com.cn/ags/ms/cm-u-bk-shibor/ShiborPri?memCode=100001244010000102001
https://www.chinamoney.com.cn/ags/ms/cm-u-bk-shibor/ShiborPri?memCode=100000111000000101001

# HIST

# EXCEL 

https://www.chinamoney.com.cn/dqs/rest/cm-u-bk-shibor/ShiborHisExcel?lang=cn&startDate=2022-09-29&endDate=2022-10-26

# 成员报价数据 EXCEL

https://www.chinamoney.com.cn/dqs/rest/cm-u-bk-shibor/ShiborPriHisExcel?lang=cn&startDate=2022-09-29&endDate=2022-10-17&memCode=|100000111000000101001|100000211000000101001|100000311000000101001|100000411000000101001|100000531000000102001|100000844030000102001|100000711000000102001|100000911000000102001|100001435010000102001|200001131000000102001|101000111000000104001|102000031000000104001|290000531000000106001|100001011000000102001|100001244010000102001|101050011000000208011|100005311000000103001|100001511000000102001&instnCnNm=|工商银行|农业银行|中国银行|建设银行|交通银行|招商银行|中信银行|光大银行|兴业银行|浦发银行|北京银行|上海银行|汇丰银行|华夏银行|广发银行|邮储银行|国开行|民生银行&instnEnNm=|ICBC|ABC|BOC|CBC|BOCOM|CMB|CNCB|CEB|CIB|SPDB|BOB|BOS|HSBC|HXB|GDB|PSBC|CDB|CMSB

# 均值
https://www.chinamoney.com.cn/dqs/rest/cm-u-bk-shibor/ShiborMnHisExcel?lang=cn&startDate=2022-09-29&endDate=2022-10-28&tendencyvalue=
```

## 贷款市场报价利率

贷款市场报价利率（LPR）由各报价行按公开市场操作利率（主要指中期借贷便利利率）加点形成的方式报价，由全国银行间同业拆借中心计算得出，为银行贷款提供定价参考。目前，LPR包括1年期和5年期以上两个品种。

LPR报价行目前包括18家银行，每月20日（遇节假日顺延）9时前，各报价行以0.05个百分点为步长，向全国银行间同业拆借中心提交报价，全国银行间同业拆借中心按去掉最高和最低报价后算术平均，并向0.05%的整数倍就近取整计算得出LPR，于当日9时15分公布，公众可在全国银行间同业拆借中心和中国人民银行网站查询。

```python
# 报价成员

https://www.chinamoney.com.cn/r/cms/www/chinamoney/data/currency/lpr-pnl-bk.json?t=1666929167307

# HIST

https://www.chinamoney.com.cn/dqs/rest/cm-u-bk-currency/LprHisExcel?lang=CN&strStartDate=2021-10-29&strEndDate=2022-10-20

```

## 回购定盘利率

银行间回购定盘利率是以银行间市场每天上午9:00-11:30间的回购交易利率为基础同时借鉴国际经验编制而成的利率基准参考指标，每天上午11:30起对外发布。回购定盘利率包括FR001、FR007、FR014、FDR001、FDR007、FDR014等品种，其中FDR001、FDR007和FDR014为银银间回购定盘利率品种。

FR001、FR007和FR014编制方法如下：

1.以隔夜回购（R001）、七天回购（R007）、14天回购（R014）交易在每个交易日上午9:00-11:30之间（包括9:00和11:30）的全部成交利率为计算基础。特别地，交易对手相同(交易方向相同或相反)且交易利率相同的交易只作为一笔交易纳入样本。

2.分别对隔夜回购、七天回购、14天回购利率进行排序，记从小到大排序之后的最大序号为N，则[N/2]（向下取整）+1位置上的那个利率即为当日的定盘利率。

3.隔夜回购定盘利率、七天回购定盘利率、14天回购定盘利率分别以FR001、FR007、FR014进行标识。

4.异常情况处理。

如果当日某个回购品种在9:00-11:30没有成交数据，则选用当日Shibor对应期限利率*365/360作为当日定盘利率。

银银间回购定盘利率FDR001、FDR007和FDR014以银行间市场每天上午9:00-11:30存款类机构以利率债为质押的回购交易为样本，编制方法如下：

1、存款类机构包括政策性银行、大型商业银行、股份制银行、城市商业银行、农村商业银行及合作银行、农村信用联社、外资银行、民营银行、村镇银行等存款类机构；利率债包括国债、央行票据和政策性金融债。

2、以银银间隔夜回购（DR001）、7天回购（DR007）、14天回购（DR014）交易在每个交易日上午9:00-11:30的全部成交利率为计算基础。特别地，交易对手相同（交易方向相同或相反）且交易利率相同的交易只作为一笔交易纳入样本。

3、分别对银银间隔夜回购、7天回购、14天回购利率进行排序，记从小到大排序之后的最大序号为N，则[N/2]（向下取整）+1位置上的那个利率即为当日的银银间定盘利率。

4、银银间隔夜回购定盘利率、7天回购定盘利率、14天回购定盘利率分别以FDR001、FDR007、FDR014进行标识。

5、异常情况处理：如果当日某个银银间回购品种在9:00-11:30没有成交数据，则选用当日Shibor对应期限利率*365/360作为当日银银间回购定盘利率。

```python

# HIST
https://www.chinamoney.com.cn/dqs/rest/cm-u-bk-currency/FrrHisExcel?lang=CN&startDate=2022-09-29&endDate=2022-10-28

```

## 债券指数

## 基准债券

**一、基准债券分类**

基准债券是指根据银行间现券市场做市机构上报的做市券种列表进行综合分析，按照债券种类、期限分布、市场流动性等因素最终确定的一揽子基准债券。基准债券分为中长期债券和短期债券2类：中长期债券按月确定样本，包括国债、政策性金融债（国开行）、政策性金融债（进出口行）、政策性金融债（农发行）、中期票据（AAA）；短期债券按周确定样本，包括短期融资券（AAA）。根据基准债券选样结果，生成对应的实时收益率曲线系列。

**二、选券标准**

在银行间现券市场的做市券种中，根据债券类型、信用评级、关键期限点、平均竞争性做市机构数、报价覆盖度和做市券种活跃度指标等6个指标选取各类债券各关键期限点的基准债券，除基准债券以外的债券为样本债券。

（一）债券类型：固定利率债券、贴现债券、零息债券，非含权债。

（二）信用评级和关键期限点

信用评级都取自银行间市场本币交易系统，信用评级和关键期限点对应关系如下表所示。

| 基准债券种类 | 信用评级 | 关键期限点（年） |
| --- | --- | --- |
| 国债 | - | 0.25、0.5、1、2、3、5、7、10、15、20、30 |
| 政策性金融债（国开行） | - | 0.25、0.5、1、2、3、5、7、10、15、20、30 |
| 政策性金融债（进出口行） | - | 0.25、0.5、1、2、3、5、7、10、15、20、30 |
| 政策性金融债（农发行） | - | 0.25、0.5、1、2、3、5、7、10、15、20、30 |
| 中期票据（AAA） | 债项评级AAA | 0.25、0.5、1、2、3、5、7 |
| 短期融资券（AAA） | 发债主体评级AAA | 0.083、0.25、0.5、0.75、1 |

（三）平均竞争性做市机构数是指基准债券选样期内，对同一债券进行做市报价的平均做市机构数量。

（四）报价覆盖度是指在“平均竞争性做市机构数”选样基础上，在该债券上一选取周期中存在竞争性做市报价的天

数占实际可交易的天数的比例。

（五）做市券种活跃度指标分为中长期债券和短期债券。

中长期债券做市券种活跃度指标：

| 选样指标 | 满分 |
| --- | --- |
| 做市报价成交量 | 20 |
| 做市报价平均双边报价价差 | 20 |
| 做市报价量 | 20 |
| 整个现券市场成交量 | 10 |
| 债券待偿期与关键期限点的期限长度差 | 5 |
| 是否新发行债券 | 25 |
| 总分 | 100 |

短期债券做市券种活跃度指标：

| 选样指标 | 满分 |
| --- | --- |
| 做市报价成交量 | 30 |
| 做市报价量 | 30 |
| 债券待偿期与关键期限点的期限长度差 | 5 |
| 是否新发行债券 | 35 |
| 总分 | 100 |

其中，对于每类债券，选券优先级依次是平均竞争性做市机构数、报价覆盖度和做市券种活跃度指标，依次降序排序得到每类债券每个关键期限点的基准债券和样本债券。

以基准国债为例，如下表所示：

| 债券代码 | 关键期限点 | 基准/样本债券 | 竞争性做市机构数 | 报价覆盖度 | 做市券种活跃度指标 |
| --- | --- | --- | --- | --- | --- |
| 090021 | 0.5 | 基准债券 | 3 | 100% | 20 |
| 070011 | 0.5 | 样本债券 | 1 | 100% | 85 |
| 090008 | 0.5 | 样本债券 | 1 | 100% | 90 |
| 080004 | 1 | 基准债券 | 2 | 100% | 100 |
| 040004 | 1 | 样本债券 | 2 | 80% | 100 |

**三、基准债券应用周期和选样周期**

基准债券应用周期是指基准债券生效的交易日范围，选样周期是指基准债券选样所在交易日范围；应用周期和选样周期原则上按周、按月进行，具体视节假日调整而定。其中，选样周期通常是指上一应用周期，在选样周期最后一个交易日确定和公布下一应用周期的基准债券。

选样周期分为样本初选和确定样本两个阶段。其中，中长期债券在上一应用周期倒数第二个交易日完成样本初选，由业务人员征询市场成员意见后，于上一应用周期最后一个交易日完成基准债券的样本确认；短期债券在上一应用周期最后一个交易日中午完成样本初选，由业务人员征询市场成员意见后，于上一应用周期最后一个交易日收盘后完成基准债券的样本确认。

例如，国债应用周期201001对应的基准债券有效期是2010年1月1日至1月31日，选样周期是2009年12月1日至12月30日；短期融资券(AAA)应用周期201002对应的基准债券有效期是2010年1月11日至1月15日，选样周期是2010年1月4日至1月8日。

**四、基准债券自动换券机制**

由于一揽子基准债券是通过历史做市报价数据统计所得，因此可能会出现在后续交易日没有报价更新的情况，此时基准债券方案将启动自动换券机制，并及时告知市场成员。自动换券机制如下：

优先选择新发行债券：

如果某个关键期限点基准债券连续N天（通常是5天）没有价格，如果在该应用周期有新券发行，优先考虑最近连续N天（通常是5天）有双边报价的新券；如果有两只及两只以上的新券满足条件，按照平均做市机构数优于发行日优于发行量优于债券代码的规则换券。

其次选择样本债券：

如果选不出新券进行自动换券，选取该标准期限样本债券中连续N天（通常是5天）有双边报价，且分值最高的债券作为该应用周期的基准债券。如果挑选出的债券在应用期限出现连续N天（通常是5天）没有价格，更换基准债券规则同上。

继续选券：

如果以上两步仍然没有挑选出债券，基准债券当日不更换，该期限利率依然使用该债券历史报价利率；第二日重新根据以上两步挑选基准债券。

## 实时收益率曲线

实时收益率曲线（以下简称实时曲线）以基准债券为基础，选取银行间本币交易系统点击成交报价和上海国际货币经纪公司的最优买卖报价，通过线性插值计算得到实时曲线。点击成交报价和货币经纪报价均只选取清算速度为T+1的报价。

实时曲线于每个交易日9时30分发布首条曲线，每1小时更新一次，直至系统闭市。

**一、曲线类型**

实时曲线为到期收益率曲线，包括报买入、报卖出和均值曲线等3条曲线。

**二、基准债券券种**

实时曲线系列包括国债、政策性金融债（国开行）、政策性金融债（进出口行）、政策性金融债（农发行）、短期融资券（AAA）和中期票据（AAA）。债券样本均选取固定利率、贴现或零息的非含权债券。

**三、实时曲线构建方法**
 按照基准债券方案，每个选样周期末筛选出各个券种的各关键期限点的基准债券。其中，国债、政策性金融债（国开行）、政策性金融债（进出口行）、政策性金融债（农发行）和中期票据（AAA）按月选样，短期融资券（AAA）按周选样。
 在每类债券应用周期内，每个工作日实时选出各个标准期限基准债券最优报买、报卖收益率，如下表所示。**标准期限（年）基准债券剩余期限（年）最优报买入收益率（%）最优报卖出收益率（%）**0.2509贴现国债200.22471.24001.17010.509附息国债210.67671.43981.4298108国债041.28771.61001.6050208国债111.53701.60301.5950309附息国债152.54252.39002.3800509附息国债184.60002.98002.9600709附息国债196.63843.30003.26501008国债188.72883.54003.52501507特别国债0612.88773.85203.85003008国债0628.35344.22964.1295    以报买入利率为例，将表中（剩余期限，最优报买入收益率）为一组数据，以散点形式画在坐标轴上，将散点以直线相连形成实时报买入曲线；其中，国债实时曲线30年期报买入利率设计成与30年期基准债券的报买入利率相等，如果30年期基准债券没有利率，则实时曲线30年期利率为空。同理可得到国债实时报卖出曲线数据；均值曲线为报买入曲线和报卖出曲线的平均，如下图所示。

同时提供基准债券实时最优报价表，如下：**标准期限（年）基准债券剩余期限（年）最优报买入收益率（%）最优报卖出收益率（%）**0.2509贴现国债200.22471.24001.17010.509附息国债210.67671.43981.4298108国债041.28771.61001.6050208国债111.53701.60301.5950309附息国债152.54252.39002.3800509附息国债184.60002.98002.9600709附息国债196.63843.30003.26501008国债188.72883.54003.52501507特别国债0612.88773.85203.85003008国债0628.35344.22964.1295
 
如果某只基准债券最优报价产生变化，基准债券实时曲线和实时最优报价表会同步更新。
**四、 选价规则**
实时曲线数据源为银行间本币交易系统点击成交报价和国际货币经纪公司的债券报价，点击成交报价和货币经纪报价均只选取清算速度为T+1的报价；按照报价时间和有效性分为实时报价、当日报价、货币经纪报价和历史报价。
按照选价优先顺序，依次是实时有效点击报价、当日已失效点击报价、货币经纪报价、历史报价。以买报价为例，取价规则如下：
实时报价：选取发布时刻点基准债券有效的报买点击成交报价中最低的价格作为该基准债券最优报买价。
当日报价：选取发布时刻点之前最后一笔有效的报买点击成交报价作为价格代表。
货币经纪报价：选取发布时刻点取到的货币经纪报价中基准债券的报买价。
历史报价：如果截止到发布时刻基准债券当日没有报买点击成交和货币经纪报买价，则选定该债券最近有点击成交报买价或是货币经纪报买价的日期，选取该日期收盘时基准债券最优买报价利率作为当日发布时刻点利率代表。

**五、基准债券自动换券机制**
由于一揽子基准债券是通过历史做市报价数据统计所得，因此可能会出现在后续交易日没有报价更新的情况，此时基准债券方案将启动自动换券机制，并及时告知市场成员。自动换券机制如下：
优先选择新发行债券：
如果某个关键期限点基准债券连续N天（通常是5天）没有价格，如果在该应用周期有新券发行，优先考虑最近连续N天（通常是5天）有双边报价的新券；如果有两只及两只以上的新券满足条件，按照平均做市机构数优于发行日优于发行量优于债券代码的规则换券。
其次选择样本债券：
如果选不出新券进行自动换券，选取该标准期限样本债券中连续N天（通常是5天）有双边报价，且分值最高的债券作为该应用周期剩余期限的基准债券。如果挑选出的债券在应用期限出现连续N天（通常是5天）没有价格，更换基准债券规则同上。
继续选券：
如果以上两步仍然没有挑选出债券，基准债券当日不更换，该期限利率依然使用该债券历史报价利率。第二日重新根据以上两步挑选基准债券。

![https://www.chinamoney.com.cn/ewebeditor/uploadfile/20180406005221618.jpg](https://www.chinamoney.com.cn/ewebeditor/uploadfile/20180406005221618.jpg)

	

```python

# 国债
https://www.chinamoney.com.cn/ags/ms/cm-u-bk-currency/RtimeYldCurv?lang=CN&qttndate=&qttntime=&bondType=100101
# 政策性金融债（国开行）
https://www.chinamoney.com.cn/ags/ms/cm-u-bk-currency/RtimeYldCurv?lang=CN&qttndate=&qttntime=&bondType=230101
# 政策性金融债（进出口银行）
https://www.chinamoney.com.cn/ags/ms/cm-u-bk-currency/RtimeYldCurv?lang=CN&qttndate=&qttntime=&bondType=230102
# （农发行）
https://www.chinamoney.com.cn/ags/ms/cm-u-bk-currency/RtimeYldCurv?lang=CN&qttndate=&qttntime=&bondType=230103
# 短期融资券（AAA）
https://www.chinamoney.com.cn/ags/ms/cm-u-bk-currency/RtimeYldCurv?lang=CN&qttndate=&qttntime=&bondType=260101
# 中期票据（AAA）
https://www.chinamoney.com.cn/ags/ms/cm-u-bk-currency/RtimeYldCurv?lang=CN&qttndate=&qttntime=&bondType=270101
```

## 收盘收益率曲线

收盘收益率曲线（以下简称收盘曲线）包括国债、央行票据、政策性金融债、短期融资券各信用评级、中期票据各信用评级、超短期融资券各信用评级、企业债各信用评级、同业存单各信用评级、商业银行普通金融债各信用评级、商业银行二级资本债各信用评级、资产支持证券各信用评级、国际开发机构SDR债、证券公司短期融资券各信用评级等各类债券收盘曲线，每条收盘曲线发布到期收益率、即期利率和远期利率3类曲线。每个工作日17时15分，在中国货币网公布当日收盘曲线。

国债、央行票据、政策性金融债、短期融资券各信用评级、中期票据各信用评级、超短期融资券各信用评级、企业债各信用评级、同业存单各信用评级、商业银行普通金融债各信用评级、商业银行二级资本债各信用评级、资产支持证券各信用评级、国际开发机构SDR债、证券公司短期融资券各信用评级等曲线债券样本是银行间市场上市流通的、不含权、非浮动利率债券(固定利率债券、贴现债券、零息债券)。其中，企业债（AAA、AA+、AA、AA-）对应有担保的企业债，企业债（AAA2、AA+2、AA2、AA-2）对应无担保的企业债。政策性金融债、中期票据和企业债1Y_Depo或Shibor3M点差曲线债券样本是银行间市场上市流通的、不含权的浮动利率债券。

收盘曲线以当日对应债券样本的双边报价和成交数据为样本，利用线性回归模型计算得到收盘到期收益率曲线，利用收盘到期收益率曲线推导出对应的即期和远期利率曲线。

以国债收盘收益率曲线为例，介绍曲线构建方法：

一、设定国债关键期限点为0.083、0.25、0.5、0.75、1、2、3、5、7、10、15、20、30、40、50年。

二、取当日收盘前所有非浮动、非含权国债双边报价数据和交易数据。

三、对每一只国债，取出该债券每个做市机构的收盘前最新报价，剔除不合理的做市报价数据。

| 债券名称 | 报价机构 | 最新报买入收益率(%) | 最新报卖出收益率(%) | 剩余期限（年） |
| --- | --- | --- | --- | --- |
| 11贴现国债09 | 机构A | 3.0500 | 2.9503 | 0.3880 |
| 11附息国债11 | 机构B | 2.9900 | 2.9600 | 0.5027 |
| … | … | … | … | … |
| 11国债10 | 机构C | 4.1000 | 4.0300 | 19.4836 |

四、将报价数据按照“剩余期限”大小进行排序，取出每只债券最优报买和最优报卖收益率，得到剩余期限和报买、报卖收益率列表。

| 剩余期限（年） | 报买入收益率(%) | 报卖出收益率(%) |
| --- | --- | --- |
| 1.3716 | 3.1700 | 3.0000 |
| 2.3497 | 3.3950 | 3.3700 |
| 2.5792 | 3.3850 | 3.3700 |

五、利用线性回归算法计算得到关键期限点0.083、0.25、0.5、0.75、1、2、3、5、7、10、15、20、30、40、50年报买入和报卖出利率，均值利率为报买入利率和报卖出利率的平均值。连接关键期限点对应报买入、报卖出利率得到收盘报买入、报卖出曲线。

| 关键期限（年） | 报买入收益率(%) | 报卖出收益率(%) | 均值利率(%) |
| --- | --- | --- | --- |
| 0.083 | 2.6600 | 2.6500 | 2.6550 |
| 0.25 | 2.8880 | 2.8660 | 2.8770 |
| 0.5 | 3.0440 | 3.0300 | 3.0370 |
| 0.75 | 3.0456 | 3.0100 | 3.0278 |
| 1 | 3.0805 | 3.0456 | 3.0631 |
| 2 | 3.3321 | 3.2346 | 3.2834 |
| 3 | 3.4724 | 3.4056 | 3.4390 |
| 5 | 3.5978 | 3.5670 | 3.5824 |
| 7 | 3.6989 | 3.6038 | 3.6514 |
| 10 | 3.7800 | 3.7068 | 3.7434 |
| 15 | 4.0234 | 3.9678 | 3.9956 |
| 20 | 4.1050 | 4.0654 | 4.0852 |
| 30 | 4.2034 | 4.1621 | 4.1828 |
| 40 | 4.2620 | 4.2522 | 4.2571 |
| 50 | 4.3500 | 4.3400 | 4.3450 |

六、交易数据中剔除与报买入和报卖出收益率曲线相差较大的数据。

七、汇总上述报价和成交样本，利用线性回归方法计算关键期限点0.083、0.25、0.5、0.75、1、2、3、5、7、10、15、20、30、40、50年到期收益率。

| 关键期限（年） | 到期收益率 (%) |
| --- | --- |
| 0.083 | 2.6551 |
| 0.25 | 2.8750 |
| 0.5 | 3.0336 |
| 0.75 | 3.0284 |
| 1 | 3.0605 |
| 2 | 3.2821 |
| 3 | 3.4424 |
| 5 | 3.5756 |
| 7 | 3.6649 |
| 10 | 3.7445 |
| 15 | 3.9945 |
| 20 | 4.0850 |
| 30 | 4.1812 |
| 40 | 4.2562 |
| 50 | 4.3407 |

连接关键期限点对应收益率，得到国债收盘到期收益率曲线：

![https://www.chinamoney.com.cn/ewebeditor/uploadfile/20180406005312532.jpg](https://www.chinamoney.com.cn/ewebeditor/uploadfile/20180406005312532.jpg)

```python

reference_dict = {
'到期':1,
'即期':2,
'远期':3
}

termId_list = [0.1, 0.5, 1.0]

# HIST

# 国债
https://www.chinamoney.com.cn/ags/ms/cm-u-bk-currency/ClsYldCurvXml?
lang=CN&bondType=CYCC000&interestRateDate=2022-10-27&maturityYield=1&currentYield=&futureYield=

# EXCEL
https://www.chinamoney.com.cn/dqs/rest/cm-u-bk-currency/ClsYldCurvHisExcel?
lang=CN&bondType=CYCC000&reference=1,2,3&startDate=2022-10-27&endDate=2022-10-27&termId=0.5

# 央行票据
https://www.chinamoney.com.cn/dqs/rest/cm-u-bk-currency/ClsYldCurvHisExcel?
lang=CN&bondType=CYCC010&reference=1,2,3&startDate=2022-10-27&endDate=2022-10-27&termId=0.5

# ... 等等三十多项债券

```

## 利率互换曲线

**利率互换曲线编制方案**

利率互换曲线由全国银行间同业拆借中心编制和发布。

利率互换曲线分为利率互换定盘/收盘曲线和利率互换行情曲线。Shibor3M和FR007利率互换曲线包括利率互换定盘/收盘曲线和利率互换行情曲线，FDR001、FDR007、ShiborO/N、LPR1Y（季付）、LPR5Y（季付）利率互换曲线包括利率互换定盘/收盘曲线。

**一、利率互换定盘/收盘曲线**

利率互换定盘/收盘曲线种类与期限：

| 曲线种类 | 标准期限 |
| --- | --- |
| Shibor3M | 6M、9M、1Y、2Y、3Y、4Y、5Y、7Y、10Y |
| FR007 | 1M、3M、6M、9M、1Y、2Y、3Y、4Y、5Y、7Y、10Y |
| FDR001 | 1M、3M、6M、9M、1Y、2Y、3Y |
| FDR007 | 1M、3M、6M、9M、1Y、2Y、3Y、4Y、5Y、7Y、10Y |
| ShiborO/N | 1M、3M、6M、9M、1Y、2Y、3Y |
| LPR1Y（季付） | 6M、9M、1Y、2Y、3Y、4Y、5Y、7Y、10Y |
| LPR5Y（季付） | 6M、9M、1Y、2Y、3Y、4Y、5Y、7Y、10Y |

利率互换定盘/收盘曲线数据样本是X-Swap报价。定盘曲线取样时间为11:45-12:00，收盘取样时间为16:15-16:30。

计算规则：

在取样时间段每隔30秒选取一个取样点（例如收盘曲线取样点为16:15:30、16:16:00、…、16:30:00），每个取样点选取X-Swap报价，计算出每个取样点的报买、报卖和均值价格。对30个取样点按均值排序并过滤上下各25%价格后，将剩余报价按照报买和报卖价差倒数为权重加权，计算出可成交报价的报买、报卖和均值利率。

发布时间：每个工作日12:10发布当日利率互换定盘曲线，16:40发布当日利率互换收盘曲线。每类曲线发布报买、报卖和均值三条曲线。

**二、利率互换行情曲线**

利率互换行情曲线种类与期限：

| 品种 | 期限 |
| --- | --- |
| Shibor3M | 6M、9M、1Y、2Y、3Y、4Y、5Y、7Y、10Y |
| FR007 | 1M、3M、6M、9M、1Y、2Y、3Y、4Y、5Y、7Y、10Y |

利率互换行情曲线数据样本包括X-Swap报价、货币经纪可成交报价和货币经纪意向报价。发布时间为9:30-11:30,12:30-16:00，每30分一次。每条曲线取样时间为该曲线发布时间点之前的半小时。

计算规则：

1. 计算出可成交代表性价格

根据X-Swap报价和货币经纪可成交报价计算出可成交代表性价格。每个发布时间点，在取样时间段每隔一分钟选取一个取样点（10:00曲线取样点为9:31、9:32、…、10:00），每个取样点优先选取X-Swap报价，以货币经纪可成交报价为补充，计算出每个取样点的报买、报卖和均值价格。对30个取样点按均值排序并过滤上下各25%价格后，将剩余报价按照报买和报卖价差倒数为权重加权，计算出可成交报价的报买、报卖和均值利率。

2.选出货币经纪意向报价

获取截止发布时间点货币经纪各品种最新意向报价数据。

3.选出利率互换行情曲线利率值

选价顺序上，优先选用可成交代表性价格。如果可成交代表性价格存在，选用可成交报价的报买、报卖和均值利率作为利率互换行情曲线该品种报买、报卖和均值利率，否则选用货币经纪意向报价。如果某个品种既无可成交代表性价格，又无货币经纪意向报价，则利率互换行情曲线该品种价格显示为空。

```python
cfgItemType_dict = {
'Shibor3M':71,
'FROO7':72,
'FDROO1':84,
'FDROO7':77,
'ShiborON'73:,
'LPR1Y(Season)':83,
'LPR5Y(Season)':82
}

# FR007
https://www.chinamoney.com.cn/ags/ms/cm-u-bk-shibor/Ifcc?lang=CN&cfgItemType=72

# FR001
https://www.chinamoney.com.cn/ags/ms/cm-u-bk-shibor/Ifcc?lang=CN&cfgItemType=84
```

## 债券估值

[](https://www.chinamoney.com.cn/dqs/rest/cm-u-bk-bond/CDSIndxHisExcel?indxName=CFETS-SHCH%E6%B0%91%E4%BC%81CDS%E6%8C%87%E6%95%B0&startDate=2022-09-28&endDate=2022-10-28)

[中国外汇交易中心债券估值手册V1.1.pdf](%E4%B8%AD%E5%9B%BD%E5%A4%96%E6%B1%87%E4%BA%A4%E6%98%93%E4%B8%AD%E5%BF%83%E3%80%81%E5%85%A8%E5%9B%BD%E9%93%B6%E8%A1%8C%E9%97%B4%E5%90%8C%E4%B8%9A%E6%8B%86%E5%80%9F%E4%B8%AD%E5%BF%83%20(1)%20447321a73fd64855b247baf84e90d5c0/%25E4%25B8%25AD%25E5%259B%25BD%25E5%25A4%2596%25E6%25B1%2587%25E4%25BA%25A4%25E6%2598%2593%25E4%25B8%25AD%25E5%25BF%2583%25E5%2580%25BA%25E5%2588%25B8%25E4%25BC%25B0%25E5%2580%25BC%25E6%2589%258B%25E5%2586%258CV1.1.pdf)

[](https://www.chinamoney.com.cn/chinese/bkval/)

### 债券动态估值

### 债券收盘估值

## CDS指数

```python

{"head":{"version":"2.0","provider":"CWAP","req_code":"","rep_code":"200","rep_message":"","ts":1666862940409,"producer":""},
"records":[
{"dataList":[{"date":"2022-10-27","dateEN":"27 Oct 2022","prd":"3M","cdIndxVl":"28.50"},{"date":"2022-10-27","dateEN":"27 Oct 2022","prd":"6M","cdIndxVl":"33.80"},{"date":"2022-10-27","dateEN":"27 Oct 2022","prd":"1Y","cdIndxVl":"35.58"},{"date":"2022-10-27","dateEN":"27 Oct 2022","prd":"2Y","cdIndxVl":"39.50"},{"date":"2022-10-27","dateEN":"27 Oct 2022","prd":"3Y","cdIndxVl":"42.30"},{"date":"2022-10-27","dateEN":"27 Oct 2022","prd":"4Y","cdIndxVl":"45.51"},{"date":"2022-10-27","dateEN":"27 Oct 2022","prd":"5Y","cdIndxVl":"49.04"}],
"enName":"CDS-SHCH-GTJA High Grade CDS Index","maxDate":"2022-10-27","cnName":"CFETS-SHCH-GTJA高等级CDS指数","maxDateEn":"27 Oct 2022"},
{"dataList":[{"date":"2022-10-27","dateEN":"27 Oct 2022","prd":"3M","cdIndxVl":"76.25"},{"date":"2022-10-27","dateEN":"27 Oct 2022","prd":"6M","cdIndxVl":"84.01"},{"date":"2022-10-27","dateEN":"27 Oct 2022","prd":"9M","cdIndxVl":"91.30"},{"date":"2022-10-27","dateEN":"27 Oct 2022","prd":"1Y","cdIndxVl":"97.27"},{"date":"2022-10-27","dateEN":"27 Oct 2022","prd":"2Y","cdIndxVl":"110.54"},{"date":"2022-10-27","dateEN":"27 Oct 2022","prd":"3Y","cdIndxVl":"118.01"}],
"enName":"CFETS-SHCH Private Enterprise CDS Index","maxDate":"2022-10-27","cnName":"CFETS-SHCH民企CDS指数","maxDateEn":"27 Oct 2022"},
{"dataList":[{"date":"2022-10-27","dateEN":"27 Oct 2022","prd":"3M","cdIndxVl":"35.17"},{"date":"2022-10-27","dateEN":"27 Oct 2022","prd":"6M","cdIndxVl":"39.89"},{"date":"2022-10-27","dateEN":"27 Oct 2022","prd":"9M","cdIndxVl":"43.44"},{"date":"2022-10-27","dateEN":"27 Oct 2022","prd":"1Y","cdIndxVl":"47.13"},{"date":"2022-10-27","dateEN":"27 Oct 2022","prd":"2Y","cdIndxVl":"54.60"},{"date":"2022-10-27","dateEN":"27 Oct 2022","prd":"3Y","cdIndxVl":"59.11"}],
"enName":"CFETS-SHCH-CBR Yangtze River Delta CDS Index","maxDate":"2022-10-27","cnName":"CFETS-SHCH-CBR长三角区域CDS指数","maxDateEn":"27 Oct 2022"}]}

https://www.chinamoney.com.cn/r/cms/www/chinamoney/data/bond/CDSIndex.json
```

### CFETS-SHCH-GTJA高等级CDS指数

```python
# HIST

https://www.chinamoney.com.cn/dqs/rest/cm-u-bk-bond/CDSIndxHisExcel?indxName=CFETS-SHCH-GTJA高等级CDS指数&startDate=2022-09-28&endDate=2022-10-28

```

### CFETS-SHCH民企CDS指数

```python
# HIST

https://www.chinamoney.com.cn/dqs/rest/cm-u-bk-bond/CDSIndxHisExcel?indxName=CFETS-SHCH民企CDS指数&startDate=2022-09-28&endDate=2022-10-28
```

### CFETS-SHCH-CBR长三角区域CDS指数

## RMBS条件早偿率指数

[RMBS条件早偿率指数编制说明V1.0.pdf](%E4%B8%AD%E5%9B%BD%E5%A4%96%E6%B1%87%E4%BA%A4%E6%98%93%E4%B8%AD%E5%BF%83%E3%80%81%E5%85%A8%E5%9B%BD%E9%93%B6%E8%A1%8C%E9%97%B4%E5%90%8C%E4%B8%9A%E6%8B%86%E5%80%9F%E4%B8%AD%E5%BF%83%20(1)%20447321a73fd64855b247baf84e90d5c0/RMBS%25E6%259D%25A1%25E4%25BB%25B6%25E6%2597%25A9%25E5%2581%25BF%25E7%258E%2587%25E6%258C%2587%25E6%2595%25B0%25E7%25BC%2596%25E5%2588%25B6%25E8%25AF%25B4%25E6%2598%258EV1.0.pdf)

```python
# HIST
https://www.chinamoney.com.cn/ags/ms/cm-u-bk-bond/RMBSIndexHis
```

      

# 利率与汇率（SDDS）

## 利率数据

```python

https://www.chinamoney.com.cn/r/cms/www/chinamoney/data/currency/sdds-intr-rate.json?t=1666941147069
```

## 汇率数据

```python
https://www.chinamoney.com.cn/r/cms/www/chinamoney/data/fx/sdds-exch-rate.json?t=1666941345203
```
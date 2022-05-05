# 强烈建议修改
LAST_NAME = '尹'  # 姓氏
SEX = '女'  # 孩子性别，男 或者 女
year = 2022  # 出生的时间：年
month = "05"  # 出生的时间：月
date = 10  # 出生的时间：日
hour = 10  # 出生的时间：小时
minute = 30  # 出生的时间： 分钟

# 选择性修改
MIN_SINGLE_NUM = 2  # 单个字最少笔画过滤
MAX_SINGLE_NUM = 20  # 单个字最多笔画过滤
THRESHOLD_SCORE = 85  # 三才五格测试最低能接受的得分，结果记录在RESULT_FILE
SELECTED_XITONGSHEN = None  # 已知的喜用神，或者次喜用神。None表示没关系。这个喜用神自己在网站查查，选填，填了可能没有最佳匹配结果

# 尽量别改，除非你知道是什么意思
debug = False
my_write_num_list = [(7, 10)]  # 经过第一轮测试后笔画的结果， 自己记录下来
true_request = True  # 真实请求测试
# 名字固定要的字
fix_write_word = '姝'
SELECTED_SANCAI = ['大吉', '中吉']  # 三才中，如果为None就不特意选最好的

# 首先在http://www.qimingzi.net/ 网站提交基本信息，点击开始起名，F12查看请求信息把Cookie复制下来
headers = {
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'host': 'm.qimingzi.net',
  'Cookie': 'ASP.NET_SessionId=ryn2pxjopsjiuawfuccnstu2; 53gid2=11278657036001; 53gid0=11278657036001; 53gid1=11278657036001; 53revisit=1651742701522; 53kf_72241622_from_host=m.qimingzi.net; 53kf_72241622_keyword=http%3A%2F%2Fm.qimingzi.net%2Fxmcs%2F; 53kf_72241622_land_page=http%253A%252F%252Fm.qimingzi.net%252FnameReport.aspx%253Fsurname%253D%2525E5%2525B0%2525B9%2526name%253D%2525E5%252590%252589%2525E5%252587%2525AF%2526sex%253D%2525E7%252594%2525B7%2526year%253D2022%2526month%253D05%2526date%253D05%2526hour%253D17%2526minute%253D24; kf_72241622_land_page_ok=1; 53uvid=1; onliner_zdfq72241622=0; visitor_type=old'
}

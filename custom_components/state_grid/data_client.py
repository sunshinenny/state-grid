BZ='params4'
BY='params3'
BX='params1'
BW='queryYear'
BV='provinceCode'
BU='sceneType'
BT='consNoSrc'
BS='access_token'
BR='codeKey'
BQ='businessType'
BP='Channels'
BO='qrCodeSerial'
BN='redirect_url'
BM='_access_token'
BL='is_debug'
BK='refresh_interval'
BJ='doorAccountDict'
BI='refreshToken'
BH='accessToken'
BG='/osg-web0004/member/c24/f01'
BF='BCP_00026'
BE='serviceCode_smt'
BD='WEBA10070900'
BC='serviceType'
BB='jM_custType'
BA='jM_busiTypeCode'
B9='01008183'
B8='0101003'
B7='submit'
B2='consType'
B1='constType'
B0='powerUserList'
A_='publicKey'
Az='WEBA10070800'
Ay='timeDay'
Ax='105'
Aw='111'
Av='0901'
Au='WEBA10070700'
At='102'
As='0101143'
Ar='channelNo'
Ae='latestBillMonth'
Ad='yearTotalCost'
Ac='accountBalance'
Ab='userAccountId'
Aa='0000'
AZ='refresh_token'
AY='web'
AX='skey'
AW='userInfo'
AV=True
AU='215'
AT='0101046'
AJ='proCode'
AI='loginAccount'
AH='keyCode'
AG='querytypeCode'
AF='01010049'
AE='doorNumberManeger'
AD='monthBillList'
AC='list'
AB='userName'
AA='acctId'
A9='resultCode'
A8='quInfo'
A7='BCP_000026'
A6='app'
A5='WEBALIPAY_01'
A4='order'
A3='state_grid'
z=False
y='authFlag'
x='09'
w='0101183'
v='stepelect'
u='account'
t=len
s='consNo_dst'
r='token'
q='0101154'
p='getday'
n='consNo'
m='bizrt'
l='clearCache'
j='timestamp'
i='errmsg'
h='promotCode'
g='01'
f='SGAPP'
e='devciceId'
d='devciceIp'
c='orgNo'
b='tenant'
a='member'
Z=str
Y='daily_bill_list'
X='proNo'
W='promotType'
V='target'
U='userId'
T='srvrt'
S='subBusiTypeCode'
Q='serCat'
P='serialNo'
O='0902'
N='srvCode'
M='uscInfo'
L=None
K='busiTypeCode'
J='code'
I='channelCode'
H='1'
G='source'
E='funcCode'
D='serviceCode'
C='errcode'
B='data'
A=''
import json as AK,time as Af,aiohttp as Ag,urllib.parse,datetime as k
from.utils.logger import LOGGER as A0
from.utils.store import async_save_to_store as Ba
from.utils.crypt import a as AL,b as B3,c as A1,d as AM,e as Ah
o='3def6c365d284881bf1a9b2b502ee68c'
Ai='ab7357dae64944a197ace37398897f64'
F={M:{a:O,d:A,e:A,b:A3},G:f,V:'32101',I:O,Ar:O,'toPublish':g,'siteId':'2012000000033700',N:A,P:A,E:A,D:{A4:q,'uploadPic':'0101296','pauseSCode':'0101250','pauseTCode':'0101251','listconsumers':'0101093','messageList':'0101343',B7:B8,'sbcMsg':'0101210','powercut':'0104514','BkAuth01':'f15','BkAuth02':'f18','BkAuth03':'f02','BkAuth04':'f17','BkAuth05':'f05','BkAuth06':'f16','BkAuth07':'f01','BkAuth08':'f03'},'electricityArchives':{'servicecode':'0104505',G:O},'subscriptionList':{N:'APP_SGPMS_05_030',P:'22',I:O,E:'22',V:'-1'},'userInformation':{D:B9,G:f},'userInform':{D:w,G:f},'elesum':{I:O,E:A5,h:H,W:H,D:As,G:A6},u:{I:O,E:'WEBA1007200'},AE:{G:O,V:'-1',I:x,Ar:x,D:AF,E:'WEBA40050000',M:{a:O,d:A,e:A,b:A3}},'doorAuth':{G:f,D:'f04'},'xinZ':{Q:'101',BA:'101','fJ_busiTypeCode':At,BB:'03','fJ_custType':'02',BC:g,S:A,E:Au,A4:q,G:f,AG:H},'onedo':{D:AT,G:f,E:Au,'queryType':'03'},'xinHuTongDian':{Q:'110',K:'211',S:'21102',E:'WEBA10071200',I:O,G:x,D:w},'company':{Q:'104',E:Au,BC:'02',AG:H,y:H,G:f,A4:q},'charge':{I:x,E:'WEBA10071300',Ar:Av,Q:At,BB:g,BA:At},'other':{I:x,E:'WEBA10079700',Q:'129',K:'999',S:'21501',D:A7,N:A,P:A},'vatchange':{B7:B8,K:'320',S:A,Q:'115',E:'WEBA10074000',y:H},'bill':{l:H,E:A5,W:H,D:A7},v:{I:O,E:A5,W:H,l:x,D:A7,G:A6},p:{I:O,l:'11',E:A5,h:H,W:H,D:A7,G:A6},'mouthOut':{I:O,l:'11',E:A5,h:H,W:H,D:A7,G:A6},'meter':{Q:'114',K:'304',E:'WEBA10071000',S:A,D:AT,P:A},'complaint':{K:'005','srvMode':O,'anonymousFlag':'0','replyMode':g,'retvisitFlag':g},'report':{K:'006'},'tradewinds':{K:'019'},'somesay':{K:'091'},'faultrepair':{E:BD,D:w,Q:Aw,K:'001',S:'21505'},'electronicInvoice':{Q:Ax,K:'0'},'rename':{D:AT,E:'WEBA10076100',K:'210',Q:'109',y:H,'gh_busiTypeCode':'211','gh_subusi':'21101',P:A,N:A},'pause':{S:A,D:AF,E:'WEBA10073600',Q:'107',K:'203','jr_busi':'201',P:A,N:A},'capacityRecovery':{D:AF,G:f,N:A,P:A,E:'WEBA10073700','busiTypeCode_stop':'204','busiTypeCode_less':'202',K:'202',S:A,Q:'108',Ay:'5',y:H},'electricityPriceChange':{D:w,K:AU,S:'21502',Q:'113',y:H,Ay:'15',E:'WEBA10073900WEB',N:A,P:A},'electricityPriceStrategyChange':{D:B9,K:AU,S:'21506',Q:'160',E:'WEBV00000517WEB',N:A,P:A},'eemandValueAdjustment':{D:w,N:A,P:A,Q:'112',E:'WEBA10073800',K:AU,S:'21504',y:H,Ay:'5','getMonthServiceCode':AT},'businessProgress':{D:w,N:g,E:'WEB01'},'increase':{G:f,P:A,N:A,BE:AF,D:q,A4:q,E:Az,AG:H,Q:'106',K:Aw,S:A},'fjincrea':{Q:Ax,K:'110',S:A,G:f,E:Az,P:A,N:A,BE:AF,D:q,A4:q,AG:H},'persIncrea':{Q:Ax,K:'109',A4:q,S:A,G:f,E:Az,AG:H},'fgdChange':{D:w,N:g,I:x,E:BD,K:AU,S:'21505',Q:Aw,y:H},'createOrder':{I:O,E:A5,N:'BCP_000001','chargeMode':'02','conType':g,'bizTypeId':'BT_ELEC'},'largePopulation':{K:'383',E:'WEBA10076800',S:A,N:A,W:A,h:A,I:Av,Q:'383',D:A,P:A},'biaoJiCode':{D:'0104507',G:'1704',I:'1704'},'twoGuar':{K:'402',S:'40201',E:'web_twoGuar'},'electTrend':{D:BF,I:O},'emergency':{D:BF,E:'A10000000',I:O},'infoPublic':{D:'2545454',G:A6}}
B4='https://www.95598.cn/api'
B5='/oauth2/outer/c02/f02'
Aj='/osg-open-uc0001/member/c8/f24'
Ak='/osg-web0004/open/c50/f02'
Al='/osg-uc0013/member/c4/f04'
Am='/osg-open-uc0001/member/c8/f04'
An='/osg-uc0013/member/c4/f02'
B6='/osg-open-uc0001/member/c8/f11'
Ao='/oauth2/oauth/authorize'
AN='/oauth2/outer/getWebToken'
Ap='/oauth2/outer/refresh_web_token'
Aq='/osg-open-uc0001/member/c9/f02'
AO='/osg-open-bc0001/member/c05/f01'
AP='/osg-open-bc0001/member/c01/f02'
AQ='/osg-open-bc0001/member/c04/f03'
AR=BG
AS=BG
Bb=[Aj,Ak,Al,Am,An]
Bc=[Ak,Al,Am,An,B6,Ao,AN,Ap,Aq,AO,AP,AQ,AR,AS]
Bd=[Aq,AO,AP,AQ,AR,AS]
Be=[B6,AO,AP,AQ,AR,AS]
def A2(data):return AK.dumps(data,separators=(',',':'),ensure_ascii=z)
def R(data,key):
	if key in data:
		try:return float(data[key])
		except:return 0
	else:return 0
class StateGridDataClient:
	hass=L;session=L;keyCode=L;publicKey=L;need_login=z;phone=L;codeKey=L;serialNo=L;qrCodeSerial=L;userInfo=L;accountInfo=L;powerUserList=L;doorAccountDict={};cookie=[];timestamp=int(Af.time()*1000);accessToken=L;refreshToken=L;token=L;expirationDate=L;refresh_interval=12;is_debug=z
	def __init__(A,hass,config=L):
		B=config;A.hass=hass;C=Ag.TCPConnector(ssl=z);D=Ag.CookieJar(quote_cookie=AV);A.session=Ag.ClientSession(cookie_jar=D,connector=C)
		if B is not L:
			try:A.keyCode=B[AH];A.publicKey=B[A_];A.accessToken=B[BH];A.refreshToken=B[BI];A.token=B[r];A.userInfo=B[AW];A.powerUserList=B[B0];A.doorAccountDict=B[BJ];A.refresh_interval=B[BK];A.is_debug=B[BL]
			except Exception as E:A0.error(E)
	async def save_data(A):B={};B[AH]=A.keyCode;B[A_]=A.publicKey;B[BH]=A.accessToken;B[BI]=A.refreshToken;B[r]=A.token;B[AW]=A.userInfo;B[B0]=A.powerUserList;B[BJ]=A.doorAccountDict;B[BK]=A.refresh_interval;B[BL]=A.is_debug;await Ba(A.hass,'state_grid.config',B)
	def encrypt_post_data(B,data):C={BM:B.accessToken[t(B.accessToken)//2:]if B.accessToken else A,'_t':B.token[t(B.token)//2:]if B.token else A,'_data':data,j:B.timestamp};return B.encrypt_wapper_data(C)
	def encrypt_wapper_data(A,data):C=AL(A2(data),A.keyCode);return{B:C+A1(C+Z(A.timestamp)),AX:AM(A.keyCode,A.publicKey),j:Z(A.timestamp)}
	def handle_request_result_message(F,api,result):
		E='message';D='resultMessage';A=result;C=L
		if B in A and T in A[B]and D in A[B][T]:C=A[B][T][D]
		elif T in A and D in A[T]:C=A[T][D]
		elif E in A:C=A[E]
		else:C=A2(A)
		if F.is_debug:A0.error(api+': '+C);A0.error(A2(A))
		return C
	async def fetch(D,api,data,header=L):
		Y='encryptData';X='464606a4-184c-4beb-b442-2ab7761d0796';W='key_code';V='state';U='sign';T='grant_type';S='application/json;charset=UTF-8';R='Content-Type';Q=header;P='client_secret';N='client_id';H=api;D.timestamp=int(Af.time()*1000);F=D.timestamp
		if D.keyCode is L:D.keyCode=Ah(32,16,2)
		I=D.keyCode;K={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36','Accept':S,R:S,'version':'1.0',G:Av,j:Z(F),'wsgwType':AY,'appKey':o};C=data
		if H==B5:C={N:o,P:Ai};M=AL(A2(C),I);C={B:M+A1(M+Z(F)),AX:AM(I,'042BC7AD510BF9793B7744C8854C56A8C95DD1027EE619247A332EC6ED5B279F435A23D62441FE861F4B0C963347ECD5792F380B64CA084BE8BE41151F8B8D19C8'),N:o,j:Z(F)}
		elif H==Aj:C={BM:A,'_t':A,'_data':C,j:F}
		elif H==Ao:
			C={N:o,'response_type':J,BN:'/test',j:F,'rsi':D.token};C=urllib.parse.urlencode(C);K[R]='application/x-www-form-urlencoded; charset=UTF-8';K[AH]=I
			async with D.session.post(B4+H,data=C,headers=K)as O:D.session.cookie_jar.update_cookies(O.cookies);E=await O.json();E=B3(E[B],D.token);E=AK.loads(E);return E
		elif H==AN:C={T:'authorization_code',U:A1(o+Z(F)),P:Ai,V:X,W:I,N:o,j:F,J:C[J]};M=AL(A2(C),I);C={B:M+A1(M+Z(F)),AX:AM(I,D.publicKey),j:Z(F)}
		elif H==Ap:C={T:AZ,U:A1(o+Z(F)),P:Ai,V:X,W:I,N:o,j:F,AZ:D.refreshToken};M=AL(A2(C),I);C={B:M+A1(M+Z(F)),AX:AM(I,D.publicKey),j:Z(F)};H=AN
		else:C=D.encrypt_post_data(C)
		if Q is not L:K.update(Q)
		if H in Bb:K['sessionId']=AY+Z(F)
		if H in Bc:K[AH]=I
		if H in Bd:K['Authorization']='Bearer '+D.accessToken[:t(D.accessToken)//2]
		if H in Be:K['t']=D.token[:t(D.token)//2]
		async with D.session.post(B4+H,json=C,headers=K)as O:
			E=await O.text()
			if E.startswith('{'):
				E=AK.loads(E)
				if Y in E:E=B3(E[Y],I);E=AK.loads(E)
			return E
	async def __get_request_key(A):
		A.keyCode=L;D=await A.fetch(B5,{});E=A.handle_request_result_message('get_request_key_api',D)
		if D[J]==H:A.keyCode=D[B][AH];A.publicKey=D[B][A_];return{C:0}
		return{C:1,i:E}
	async def __get_qr_code(E):
		F={M:{d:A,b:A3,a:O,e:A},A8:{'optType':g,P:Ah(28,10,1)}};D=await E.fetch(Aj,F);G=E.handle_request_result_message('get_qr_code_api',D)
		if D[J]==1:
			if D[B]and D[B][T]and D[B][T][A9]==Aa:E.qrCodeSerial=D[B][m][BO];H=D[B][m]['qrCode'];return{C:0,B:H}
		return{C:1,i:G}
	async def __get_qr_code_status(D):
		E={m:{BO:D.qrCodeSerial}};F={r:'98'+Ah(10,10,1)};A=await D.fetch(Ak,E,F);G=D.handle_request_result_message('get_qr_code_status_api',A)
		if J in A and A[J]==1:
			if B in A and A[B]!='null':D.token=A[B];return{C:0}
			else:return{C:1,i:'未使用网上国网 App 扫码或确认登录'}
		return{C:1,i:G}
	async def __get_qr_code_token(B):
		D={M:{b:A3,a:O,'isEncrypt':AV},r:B.token};A=await B.fetch(Al,D);E=B.handle_request_result_message('get_qr_code_token_api',A)
		if T in A and A9 in A[T]and A[T][A9]==Aa:B.userInfo=A[m][AW];return{C:0}
		return{C:1,i:E}
	async def __send_code(E,phone):
		F=phone;E.phone=F;G={M:{d:A,b:A3,a:O,e:A},A8:{'sendType':'0',u:F,BQ:'login','accountType':A},BP:AY};D=await E.fetch(Am,G);H=E.handle_request_result_message('send_code_api',D)
		if D[J]==1:
			if D[B]and D[B][T]and D[B][T][A9]==Aa:E.codeKey=D[B][m][BR];return{C:0}
		return{C:1,i:H}
	async def __verfiy_code(B,code):
		E={M:{d:A,b:A3,a:O,e:A},A8:{u:B.phone,BQ:'login',J:code,'optSys':'ios','pushId':'00000',BR:B.codeKey},BP:AY};D=await B.fetch(An,E);F=B.handle_request_result_message('code_login_api',D)
		if T in D and A9 in D[T]and D[T][A9]==Aa:B.token=D[m][r];B.userInfo=D[m][AW][0];return{C:0}
		return{C:1,i:F}
	async def __get_request_authorize(D):
		A=await D.fetch(Ao,{});G=D.handle_request_result_message('get_request_authorize_api',A)
		if J in A and A[J]==H:E=A[B][BN];F=E.rfind('code=');D.authorizeCode=E[F+5:F+5+32];return{C:0}
		return{C:1,i:G}
	async def __get_web_token(A):
		E={J:A.authorizeCode};D=await A.fetch(AN,E);F=A.handle_request_result_message('get_web_token_api',D)
		if J in D and D[J]==H:A.accessToken=D[B][BS];A.refreshToken=D[B][AZ];return{C:0}
		return{C:1,i:F}
	async def __refresh_web_token(D):
		A=await D.fetch(Ap,{});E=D.handle_request_result_message('refresh_web_token_api',A)
		if J in A and A[J]==H:D.accessToken=A[B][BS];D.refreshToken=A[B][AZ];return{C:0}
		return{C:1,i:E}
	async def __get_door_number(E):
		H={D:F[D],G:F[G],V:F[V],M:{a:F[AE][M][a],d:F[AE][M][d],e:F[AE][M][e],b:F[AE][M][b]},A8:{U:E.userInfo[U]},r:E.token};A=await E.fetch(Aq,H);I=E.handle_request_result_message('get_door_number_api',A)
		if J in A and A[J]==1 and B in A and m in A[B]:E.powerUserList=A[B][m][B0];return{C:0}
		return{C:1,i:I}
	async def __get_door_balance(L,door_account):
		C=door_account;O={B:{N:A,P:A,I:F[u][I],E:F[u][E],AA:L.userInfo[U],AB:L.userInfo[AI],W:H,h:H,Ab:L.userInfo[U],AC:[{BT:C[s],AJ:C[X],BU:C[B1],n:C[n],c:C[c]}]},D:As,G:F[G],V:C[X]};K=await L.fetch(AO,O);L.handle_request_result_message('get_door_balance_api',K)
		if J in K and K[J]==1 and B in K and AC in K[B]:
			M=K[B][AC]
			if t(M)!=0:C[Ac]=M[0]
	async def __get_door_bill(L,door_account,year):
		Q='dataInfo';M='mothEleList';C=door_account;O={B:{N:A,P:A,I:F[u][I],E:F[u][E],AA:L.userInfo[U],AB:L.userInfo[AI],W:H,h:H,Ab:L.userInfo[U],AC:[{BT:C[s],AJ:C[X],BU:C['consSortCode'],n:C[n],c:C[c]}]},D:As,G:F[G],V:C[X]};O={B:{AA:L.userInfo[U],I:F[I],l:'11',B2:C[B1],E:'ALIPAY_01',c:C[c],AJ:C[X],h:H,W:H,P:A,N:A,AB:A,BV:C[X],Ab:L.userInfo[U],n:C[n],BW:year},D:A7,G:A6,V:C[X]};K=await L.fetch(AP,O);L.handle_request_result_message('get_door_bill_api',K)
		if J in K and K[J]==1 and B in K:
			if Q in K[B]:C[Ad]=K[B][Q]
			if M in K[B]:C[AD]=K[B][M];C[Ae]=K[B][M][-1]['month']
	async def __get_door_ladder(H,door_account,month):
		O='ladder_flag';M=month;C=door_account;Q=C[s];R={B:{I:F[v][I],E:F[v][E],W:F[v][W],l:F[v][l],n:C[s],h:C[X],c:C[c],'queryDate':M,BV:C[X],B2:C[B1],Ab:H.userInfo[U],P:A,N:A,AB:H.userInfo[AI],AA:H.userInfo[U]},D:F[v][D],G:F[v][G],V:C[X]};K=await H.fetch(AQ,R);S=H.handle_request_result_message('get_door_ladder_api',K)
		if J in K and K[J]==1 and B in K and AC in K[B]:
			L=K[B][AC]
			if t(L)!=0:
				L=L[0];L['month']=M
				if L['electricParticulars']['levelFlag']=='2':C[O]=1
				else:C[O]=0
				H.doorAccountDict[Q]['ladder']=L
	async def __get_door_daily_bill(C,door_account,year,start_date,end_date):
		L='sevenEleList';K=door_account;O={BX:{D:F[D],G:F[G],V:F[V],M:{a:F[M][a],d:F[M][d],e:F[M][e],b:F[M][b]},A8:{U:C.userInfo[U]},r:C.token},BY:{B:{AA:C.userInfo[U],n:K[s],B2:g,'endTime':end_date,c:K[c],BW:year,AJ:K[X],P:A,N:A,'startTime':start_date,AB:C.userInfo[AI],E:F[p][E],I:F[p][I],l:F[p][l],h:F[p][h],W:F[p][W]},D:F[p][D],G:F[p][G],V:K[X]},BZ:'010103'};H=await C.fetch(AS,O);Q=C.handle_request_result_message('get_door_daily_bill_api',H)
		if J in H and H[J]==1 and B in H and L in H[B]:K[Y]=H[B][L]
	async def __get_door_pay_record(C,door_account):J=door_account;L=J[s];K={BX:{D:F[D],G:F[G],V:F[V],M:{a:F[M][a],d:F[M][d],e:F[M][e],b:F[M][b]},A8:{U:C.userInfo[U]},r:C.token},BY:{B:{AA:C.userInfo[U],'bgnPayDate':'2023-04-24',I:F[I],n:J[s],'endPayDate':'2024-04-24',E:'webALIPAY_01','number':100,c:J[c],'page':H,AJ:J[X],h:H,W:H,P:A,N:A,AB:C.userInfo[AI]},D:'0101051',G:g,V:J[X]},BZ:'010104'};O=await C.fetch(AR,K)
	async def get_qr_code(B):
		A=await B.__get_request_key()
		if C in A and A[C]!=0:return A
		return await B.__get_qr_code()
	async def check_qr_code(B):
		A=await B.__get_qr_code_status()
		if C in A and A[C]!=0:return A
		A=await B.__get_qr_code_token()
		if C in A and A[C]!=0:return A
		return await B.__get_token()
	async def send_phone_code(B,phone):
		A=await B.__get_request_key()
		if C in A and A[C]!=0:return A
		return await B.__send_code(phone)
	async def verfiy_phone_code(B,code):
		A=await B.__verfiy_code(code)
		if C in A and A[C]!=0:return A
		return await B.__get_token()
	async def __get_token(D):
		A=await D.__get_request_key()
		if C in A and A[C]!=0:return A
		A=await D.__get_request_authorize()
		if C in A and A[C]!=0:return A
		A=await D.__get_web_token()
		if C in A and A[C]!=0:return A
		A=await D.__get_door_number()
		if C in A and A[C]!=0:return A
		D.need_login=z;await D.save_data();return{C:0,B:D.powerUserList}
	async def refresh_data(B,setup=z):
		q='daily_t_ele_num';p='daily_n_ele_num';o='daily_v_ele_num';n='daily_p_ele_num';m='daily_ele_num';l='last_month_ele_cost';j='last_month_ele_num';i='year_ele_cost';h='year_ele_num';g='monthEleNum';f='thisTPq';e='thisNPq';d='thisVPq';c='thisPPq';S='balance';Q='ladder_level_num';P='ladder_level';L='%Y%m%d';K='day';I='dayElePq';r=setup or int(Af.time()*1000)-B.timestamp>B.refresh_interval*3600*1000
		if r is z:return
		E=await B.__get_door_number()
		if C in E and E[C]!=0:
			A0.warning('刷新 Token');E=await B.__get_request_key()
			if C in E and E[C]!=0:return
			E=await B.__refresh_web_token()
			if C in E and E[C]==0:await B.save_data()
			else:B.need_login=AV;A0.error('刷新 Token 失败');return
			E=await B.__get_door_number()
			if C in E and E[C]!=0:B.need_login=AV;A0.error('重新请求失败');return
		T=k.datetime.now();J=T-k.timedelta(days=1);u=f"{J.year}-{J.month:02d}-{J.day:02d}";M=J-k.timedelta(days=40);v=f"{M.year}-{M.month:02d}-{M.day:02d}"
		for A in B.powerUserList:
			w=A[s];B.doorAccountDict[w]=A;await B.__get_door_balance(A);await B.__get_door_daily_bill(A,T.year,v,u);N=A[Y][0]
			try:float(N[I])
			except:A[Y].pop(0)
			N=A[Y][0];F=k.datetime.strptime(N[K],L);U=0;V=0;W=0;X=0;Z=0
			for D in A[Y]:
				H=k.datetime.strptime(D[K],L)
				if H.month!=F.month:break
				U+=R(D,I);V+=R(D,c);W+=R(D,d);X+=R(D,e);Z+=R(D,f)
			O=F-k.timedelta(days=F.day);a=f"{O.year}-{O.month:02d}"
			if Ae not in A or A[Ae]!=a:await B.__get_door_bill(A,O.year);await B.__get_door_ladder(A,a)
			x=k.datetime.strptime(A[Ae],'%Y%m')
			if x.month==12:
				G=0
				for D in A[Y]:
					H=k.datetime.strptime(D[K],L)
					if H.month!=12:break
					G+=R(D,I)
			else:
				G=0
				for D in A[AD]:G+=R(D,g)
				y=t(A[AD])
				for D in A[Y]:
					H=k.datetime.strptime(D[K],L)
					if H.month<=y:break
					G+=R(D,I)
			if G<=2760:A[P]='第一阶梯';A[Q]=1
			elif G<=4800:A[P]='第二阶梯';A[Q]=2
			else:A[P]='第三阶梯';A[Q]=3
			if Ac in A:
				A[S]=R(A[Ac],'prepayBal');b=R(A[Ac],'historyOwe')
				if b>0:A[S]=-b
			else:A[S]=0
			if Ad in A:A[h]=R(A[Ad],'totalEleNum');A[i]=R(A[Ad],'totalEleCost')
			else:A[h]=0;A[i]=0
			if AD in A:A[j]=R(A[AD][-1],g);A[l]=R(A[AD][-1],'monthEleCost')
			else:A[j]=0;A[l]=0
			if Y in A:A[m]=R(A[Y][0],I);A[n]=R(A[Y][0],c);A[o]=R(A[Y][0],d);A[p]=R(A[Y][0],e);A[q]=R(A[Y][0],f)
			else:A[m]=0;A[n]=0;A[o]=0;A[p]=0;A[q]=0
			A['month_ele_num']=U;A['month_p_ele_num']=V;A['month_v_ele_num']=W;A['month_n_ele_num']=X;A['month_t_ele_num']=Z;A['daily_lasted_date']=f"{F.year}-{F.month:02d}-{F.day:02d}"
		await B.save_data()
	async def get_door_account_list(A):return list(A.doorAccountDict.values())
	def get_door_account(A):return A.doorAccountDict
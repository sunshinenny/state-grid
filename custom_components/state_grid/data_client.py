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
Ac='userAccountId'
Ab='0000'
Aa='refresh_token'
AZ='web'
AY='skey'
AX='userInfo'
AW=True
AV='215'
AU='0101046'
AK='accountBalance'
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
k='timestamp'
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
R='serCat'
Q='serialNo'
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
import json as AL,time as Af,aiohttp as Ag,urllib.parse,datetime as j
from.utils.logger import LOGGER as A0
from.utils.store import async_save_to_store as Ba
from.utils.crypt import a as AM,b as B3,c as A1,d as AN,e as Ah
o='3def6c365d284881bf1a9b2b502ee68c'
Ai='ab7357dae64944a197ace37398897f64'
F={M:{a:O,d:A,e:A,b:A3},G:f,V:'32101',I:O,Ar:O,'toPublish':g,'siteId':'2012000000033700',N:A,Q:A,E:A,D:{A4:q,'uploadPic':'0101296','pauseSCode':'0101250','pauseTCode':'0101251','listconsumers':'0101093','messageList':'0101343',B7:B8,'sbcMsg':'0101210','powercut':'0104514','BkAuth01':'f15','BkAuth02':'f18','BkAuth03':'f02','BkAuth04':'f17','BkAuth05':'f05','BkAuth06':'f16','BkAuth07':'f01','BkAuth08':'f03'},'electricityArchives':{'servicecode':'0104505',G:O},'subscriptionList':{N:'APP_SGPMS_05_030',Q:'22',I:O,E:'22',V:'-1'},'userInformation':{D:B9,G:f},'userInform':{D:w,G:f},'elesum':{I:O,E:A5,h:H,W:H,D:As,G:A6},u:{I:O,E:'WEBA1007200'},AE:{G:O,V:'-1',I:x,Ar:x,D:AF,E:'WEBA40050000',M:{a:O,d:A,e:A,b:A3}},'doorAuth':{G:f,D:'f04'},'xinZ':{R:'101',BA:'101','fJ_busiTypeCode':At,BB:'03','fJ_custType':'02',BC:g,S:A,E:Au,A4:q,G:f,AG:H},'onedo':{D:AU,G:f,E:Au,'queryType':'03'},'xinHuTongDian':{R:'110',K:'211',S:'21102',E:'WEBA10071200',I:O,G:x,D:w},'company':{R:'104',E:Au,BC:'02',AG:H,y:H,G:f,A4:q},'charge':{I:x,E:'WEBA10071300',Ar:Av,R:At,BB:g,BA:At},'other':{I:x,E:'WEBA10079700',R:'129',K:'999',S:'21501',D:A7,N:A,Q:A},'vatchange':{B7:B8,K:'320',S:A,R:'115',E:'WEBA10074000',y:H},'bill':{l:H,E:A5,W:H,D:A7},v:{I:O,E:A5,W:H,l:x,D:A7,G:A6},p:{I:O,l:'11',E:A5,h:H,W:H,D:A7,G:A6},'mouthOut':{I:O,l:'11',E:A5,h:H,W:H,D:A7,G:A6},'meter':{R:'114',K:'304',E:'WEBA10071000',S:A,D:AU,Q:A},'complaint':{K:'005','srvMode':O,'anonymousFlag':'0','replyMode':g,'retvisitFlag':g},'report':{K:'006'},'tradewinds':{K:'019'},'somesay':{K:'091'},'faultrepair':{E:BD,D:w,R:Aw,K:'001',S:'21505'},'electronicInvoice':{R:Ax,K:'0'},'rename':{D:AU,E:'WEBA10076100',K:'210',R:'109',y:H,'gh_busiTypeCode':'211','gh_subusi':'21101',Q:A,N:A},'pause':{S:A,D:AF,E:'WEBA10073600',R:'107',K:'203','jr_busi':'201',Q:A,N:A},'capacityRecovery':{D:AF,G:f,N:A,Q:A,E:'WEBA10073700','busiTypeCode_stop':'204','busiTypeCode_less':'202',K:'202',S:A,R:'108',Ay:'5',y:H},'electricityPriceChange':{D:w,K:AV,S:'21502',R:'113',y:H,Ay:'15',E:'WEBA10073900WEB',N:A,Q:A},'electricityPriceStrategyChange':{D:B9,K:AV,S:'21506',R:'160',E:'WEBV00000517WEB',N:A,Q:A},'eemandValueAdjustment':{D:w,N:A,Q:A,R:'112',E:'WEBA10073800',K:AV,S:'21504',y:H,Ay:'5','getMonthServiceCode':AU},'businessProgress':{D:w,N:g,E:'WEB01'},'increase':{G:f,Q:A,N:A,BE:AF,D:q,A4:q,E:Az,AG:H,R:'106',K:Aw,S:A},'fjincrea':{R:Ax,K:'110',S:A,G:f,E:Az,Q:A,N:A,BE:AF,D:q,A4:q,AG:H},'persIncrea':{R:Ax,K:'109',A4:q,S:A,G:f,E:Az,AG:H},'fgdChange':{D:w,N:g,I:x,E:BD,K:AV,S:'21505',R:Aw,y:H},'createOrder':{I:O,E:A5,N:'BCP_000001','chargeMode':'02','conType':g,'bizTypeId':'BT_ELEC'},'largePopulation':{K:'383',E:'WEBA10076800',S:A,N:A,W:A,h:A,I:Av,R:'383',D:A,Q:A},'biaoJiCode':{D:'0104507',G:'1704',I:'1704'},'twoGuar':{K:'402',S:'40201',E:'web_twoGuar'},'electTrend':{D:BF,I:O},'emergency':{D:BF,E:'A10000000',I:O},'infoPublic':{D:'2545454',G:A6}}
B4='https://www.95598.cn/api'
B5='/oauth2/outer/c02/f02'
Aj='/osg-open-uc0001/member/c8/f24'
Ak='/osg-web0004/open/c50/f02'
Al='/osg-uc0013/member/c4/f04'
Am='/osg-open-uc0001/member/c8/f04'
An='/osg-uc0013/member/c4/f02'
B6='/osg-open-uc0001/member/c8/f11'
Ao='/oauth2/oauth/authorize'
AO='/oauth2/outer/getWebToken'
Ap='/oauth2/outer/refresh_web_token'
Aq='/osg-open-uc0001/member/c9/f02'
AP='/osg-open-bc0001/member/c05/f01'
AQ='/osg-open-bc0001/member/c01/f02'
AR='/osg-open-bc0001/member/c04/f03'
AS=BG
AT=BG
Bb=[Aj,Ak,Al,Am,An]
Bc=[Ak,Al,Am,An,B6,Ao,AO,Ap,Aq,AP,AQ,AR,AS,AT]
Bd=[Aq,AP,AQ,AR,AS,AT]
Be=[B6,AP,AQ,AR,AS,AT]
def A2(data):return AL.dumps(data,separators=(',',':'),ensure_ascii=z)
def P(data,key):
	if key in data:
		try:return float(data[key])
		except:return 0
	else:return 0
class StateGridDataClient:
	hass=L;session=L;keyCode=L;publicKey=L;need_login=z;phone=L;codeKey=L;serialNo=L;qrCodeSerial=L;userInfo=L;accountInfo=L;powerUserList=L;doorAccountDict={};cookie=[];timestamp=int(Af.time()*1000);accessToken=L;refreshToken=L;token=L;expirationDate=L;refresh_interval=12;is_debug=z
	def __init__(A,hass,config=L):
		B=config;A.hass=hass;C=Ag.TCPConnector(ssl=z);D=Ag.CookieJar(quote_cookie=AW);A.session=Ag.ClientSession(cookie_jar=D,connector=C)
		if B is not L:
			try:A.keyCode=B[AH];A.publicKey=B[A_];A.accessToken=B[BH];A.refreshToken=B[BI];A.token=B[r];A.userInfo=B[AX];A.powerUserList=B[B0];A.doorAccountDict=B[BJ];A.refresh_interval=B[BK];A.is_debug=B[BL]
			except Exception as E:A0.error(E)
	async def save_data(A):B={};B[AH]=A.keyCode;B[A_]=A.publicKey;B[BH]=A.accessToken;B[BI]=A.refreshToken;B[r]=A.token;B[AX]=A.userInfo;B[B0]=A.powerUserList;B[BJ]=A.doorAccountDict;B[BK]=A.refresh_interval;B[BL]=A.is_debug;await Ba(A.hass,'state_grid.config',B)
	def encrypt_post_data(B,data):C={BM:B.accessToken[t(B.accessToken)//2:]if B.accessToken else A,'_t':B.token[t(B.token)//2:]if B.token else A,'_data':data,k:B.timestamp};return B.encrypt_wapper_data(C)
	def encrypt_wapper_data(A,data):C=AM(A2(data),A.keyCode);return{B:C+A1(C+Z(A.timestamp)),AY:AN(A.keyCode,A.publicKey),k:Z(A.timestamp)}
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
		I=D.keyCode;K={'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Mobile Safari/537.36','Accept':S,R:S,'version':'1.0',G:Av,k:Z(F),'wsgwType':AZ,'appKey':o};C=data
		if H==B5:C={N:o,P:Ai};M=AM(A2(C),I);C={B:M+A1(M+Z(F)),AY:AN(I,'042BC7AD510BF9793B7744C8854C56A8C95DD1027EE619247A332EC6ED5B279F435A23D62441FE861F4B0C963347ECD5792F380B64CA084BE8BE41151F8B8D19C8'),N:o,k:Z(F)}
		elif H==Aj:C={BM:A,'_t':A,'_data':C,k:F}
		elif H==Ao:
			C={N:o,'response_type':J,BN:'/test',k:F,'rsi':D.token};C=urllib.parse.urlencode(C);K[R]='application/x-www-form-urlencoded; charset=UTF-8';K[AH]=I
			async with D.session.post(B4+H,data=C,headers=K)as O:D.session.cookie_jar.update_cookies(O.cookies);E=await O.json();E=B3(E[B],D.token);E=AL.loads(E);return E
		elif H==AO:C={T:'authorization_code',U:A1(o+Z(F)),P:Ai,V:X,W:I,N:o,k:F,J:C[J]};M=AM(A2(C),I);C={B:M+A1(M+Z(F)),AY:AN(I,D.publicKey),k:Z(F)}
		elif H==Ap:C={T:Aa,U:A1(o+Z(F)),P:Ai,V:X,W:I,N:o,k:F,Aa:D.refreshToken};M=AM(A2(C),I);C={B:M+A1(M+Z(F)),AY:AN(I,D.publicKey),k:Z(F)};H=AO
		else:C=D.encrypt_post_data(C)
		if Q is not L:K.update(Q)
		if H in Bb:K['sessionId']=AZ+Z(F)
		if H in Bc:K[AH]=I
		if H in Bd:K['Authorization']='Bearer '+D.accessToken[:t(D.accessToken)//2]
		if H in Be:K['t']=D.token[:t(D.token)//2]
		async with D.session.post(B4+H,json=C,headers=K)as O:
			E=await O.text()
			if E.startswith('{'):
				E=AL.loads(E)
				if Y in E:E=B3(E[Y],I);E=AL.loads(E)
			return E
	async def __get_request_key(A):
		A.keyCode=L;D=await A.fetch(B5,{});E=A.handle_request_result_message('get_request_key_api',D)
		if D[J]==H:A.keyCode=D[B][AH];A.publicKey=D[B][A_];return{C:0}
		return{C:1,i:E}
	async def __get_qr_code(E):
		F={M:{d:A,b:A3,a:O,e:A},A8:{'optType':g,Q:Ah(28,10,1)}};D=await E.fetch(Aj,F);G=E.handle_request_result_message('get_qr_code_api',D)
		if D[J]==1:
			if D[B]and D[B][T]and D[B][T][A9]==Ab:E.qrCodeSerial=D[B][m][BO];H=D[B][m]['qrCode'];return{C:0,B:H}
		return{C:1,i:G}
	async def __get_qr_code_status(D):
		E={m:{BO:D.qrCodeSerial}};F={r:'98'+Ah(10,10,1)};A=await D.fetch(Ak,E,F);G=D.handle_request_result_message('get_qr_code_status_api',A)
		if J in A and A[J]==1:
			if B in A and A[B]!='null':D.token=A[B];return{C:0}
			else:return{C:1,i:'未使用网上国网 App 扫码或确认登录'}
		return{C:1,i:G}
	async def __get_qr_code_token(B):
		D={M:{b:A3,a:O,'isEncrypt':AW},r:B.token};A=await B.fetch(Al,D);E=B.handle_request_result_message('get_qr_code_token_api',A)
		if T in A and A9 in A[T]and A[T][A9]==Ab:B.userInfo=A[m][AX];return{C:0}
		return{C:1,i:E}
	async def __send_code(E,phone):
		F=phone;E.phone=F;G={M:{d:A,b:A3,a:O,e:A},A8:{'sendType':'0',u:F,BQ:'login','accountType':A},BP:AZ};D=await E.fetch(Am,G);H=E.handle_request_result_message('send_code_api',D)
		if D[J]==1:
			if D[B]and D[B][T]and D[B][T][A9]==Ab:E.codeKey=D[B][m][BR];return{C:0}
		return{C:1,i:H}
	async def __verfiy_code(B,code):
		E={M:{d:A,b:A3,a:O,e:A},A8:{u:B.phone,BQ:'login',J:code,'optSys':'ios','pushId':'00000',BR:B.codeKey},BP:AZ};D=await B.fetch(An,E);F=B.handle_request_result_message('code_login_api',D)
		if T in D and A9 in D[T]and D[T][A9]==Ab:B.token=D[m][r];B.userInfo=D[m][AX][0];return{C:0}
		return{C:1,i:F}
	async def __get_request_authorize(D):
		A=await D.fetch(Ao,{});G=D.handle_request_result_message('get_request_authorize_api',A)
		if J in A and A[J]==H:E=A[B][BN];F=E.rfind('code=');D.authorizeCode=E[F+5:F+5+32];return{C:0}
		return{C:1,i:G}
	async def __get_web_token(A):
		E={J:A.authorizeCode};D=await A.fetch(AO,E);F=A.handle_request_result_message('get_web_token_api',D)
		if J in D and D[J]==H:A.accessToken=D[B][BS];A.refreshToken=D[B][Aa];return{C:0}
		return{C:1,i:F}
	async def __refresh_web_token(D):
		A=await D.fetch(Ap,{});E=D.handle_request_result_message('refresh_web_token_api',A)
		if J in A and A[J]==H:D.accessToken=A[B][BS];D.refreshToken=A[B][Aa];return{C:0}
		return{C:1,i:E}
	async def __get_door_number(E):
		H={D:F[D],G:F[G],V:F[V],M:{a:F[AE][M][a],d:F[AE][M][d],e:F[AE][M][e],b:F[AE][M][b]},A8:{U:E.userInfo[U]},r:E.token};A=await E.fetch(Aq,H);I=E.handle_request_result_message('get_door_number_api',A)
		if J in A and A[J]==1 and B in A and m in A[B]:E.powerUserList=A[B][m][B0];return{C:0}
		return{C:1,i:I}
	async def __get_door_balance(L,door_account):
		C=door_account;O={B:{N:A,Q:A,I:F[u][I],E:F[u][E],AA:L.userInfo[U],AB:L.userInfo[AI],W:H,h:H,Ac:L.userInfo[U],AC:[{BT:C[s],AJ:C[X],BU:C[B1],n:C[n],c:C[c]}]},D:As,G:F[G],V:C[X]};K=await L.fetch(AP,O);L.handle_request_result_message('get_door_balance_api',K)
		if J in K and K[J]==1 and B in K and AC in K[B]:
			M=K[B][AC]
			if t(M)!=0:C[AK]=M[0]
	async def __get_door_bill(L,door_account,year):
		P='dataInfo';M='mothEleList';C=door_account;O={B:{N:A,Q:A,I:F[u][I],E:F[u][E],AA:L.userInfo[U],AB:L.userInfo[AI],W:H,h:H,Ac:L.userInfo[U],AC:[{BT:C[s],AJ:C[X],BU:C['consSortCode'],n:C[n],c:C[c]}]},D:As,G:F[G],V:C[X]};O={B:{AA:L.userInfo[U],I:F[I],l:'11',B2:C[B1],E:'ALIPAY_01',c:C[c],AJ:C[X],h:H,W:H,Q:A,N:A,AB:A,BV:C[X],Ac:L.userInfo[U],n:C[n],BW:year},D:A7,G:A6,V:C[X]};K=await L.fetch(AQ,O);L.handle_request_result_message('get_door_bill_api',K)
		if J in K and K[J]==1 and B in K:
			if P in K[B]:C[Ad]=K[B][P]
			if M in K[B]:C[AD]=K[B][M];C[Ae]=K[B][M][-1]['month']
	async def __get_door_ladder(H,door_account,month):
		O='ladder_flag';M=month;C=door_account;P=C[s];R={B:{I:F[v][I],E:F[v][E],W:F[v][W],l:F[v][l],n:C[s],h:C[X],c:C[c],'queryDate':M,BV:C[X],B2:C[B1],Ac:H.userInfo[U],Q:A,N:A,AB:H.userInfo[AI],AA:H.userInfo[U]},D:F[v][D],G:F[v][G],V:C[X]};K=await H.fetch(AR,R);S=H.handle_request_result_message('get_door_ladder_api',K)
		if J in K and K[J]==1 and B in K and AC in K[B]:
			L=K[B][AC]
			if t(L)!=0:
				L=L[0];L['month']=M
				if L['electricParticulars']['levelFlag']=='2':C[O]=1
				else:C[O]=0
				H.doorAccountDict[P]['ladder']=L
	async def __get_door_daily_bill(C,door_account,year,start_date,end_date):
		L='sevenEleList';K=door_account;O={BX:{D:F[D],G:F[G],V:F[V],M:{a:F[M][a],d:F[M][d],e:F[M][e],b:F[M][b]},A8:{U:C.userInfo[U]},r:C.token},BY:{B:{AA:C.userInfo[U],n:K[s],B2:g,'endTime':end_date,c:K[c],BW:year,AJ:K[X],Q:A,N:A,'startTime':start_date,AB:C.userInfo[AI],E:F[p][E],I:F[p][I],l:F[p][l],h:F[p][h],W:F[p][W]},D:F[p][D],G:F[p][G],V:K[X]},BZ:'010103'};H=await C.fetch(AT,O);P=C.handle_request_result_message('get_door_daily_bill_api',H)
		if J in H and H[J]==1 and B in H and L in H[B]:K[Y]=H[B][L]
	async def __get_door_pay_record(C,door_account):J=door_account;L=J[s];K={BX:{D:F[D],G:F[G],V:F[V],M:{a:F[M][a],d:F[M][d],e:F[M][e],b:F[M][b]},A8:{U:C.userInfo[U]},r:C.token},BY:{B:{AA:C.userInfo[U],'bgnPayDate':'2023-04-24',I:F[I],n:J[s],'endPayDate':'2024-04-24',E:'webALIPAY_01','number':100,c:J[c],'page':H,AJ:J[X],h:H,W:H,Q:A,N:A,AB:C.userInfo[AI]},D:'0101051',G:g,V:J[X]},BZ:'010104'};O=await C.fetch(AS,K)
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
		q='daily_t_ele_num';p='daily_n_ele_num';o='daily_v_ele_num';n='daily_p_ele_num';m='daily_ele_num';l='last_month_ele_cost';k='last_month_ele_num';i='year_ele_cost';h='year_ele_num';g='monthEleNum';f='thisTPq';e='thisNPq';d='thisVPq';c='thisPPq';T='balance';S='ladder_level_num';R='ladder_level';L='%Y%m%d';K='day';I='dayElePq';r=setup or int(Af.time()*1000)-B.timestamp>B.refresh_interval*3600*1000
		if r is z:return
		E=await B.__get_door_number()
		if C in E and E[C]!=0:
			A0.warning('刷新 Token');E=await B.__get_request_key()
			if C in E and E[C]!=0:return
			E=await B.__refresh_web_token()
			if C in E and E[C]==0:await B.save_data()
			else:B.need_login=AW;A0.error('刷新 Token 失败');return
			E=await B.__get_door_number()
			if C in E and E[C]!=0:B.need_login=AW;A0.error('重新请求失败');return
		M=j.datetime.now();J=M-j.timedelta(days=1);u=f"{J.year}-{J.month:02d}-{J.day:02d}";N=J-j.timedelta(days=40);v=f"{N.year}-{N.month:02d}-{N.day:02d}"
		for A in B.powerUserList:
			w=A[s];B.doorAccountDict[w]=A;await B.__get_door_balance(A);await B.__get_door_daily_bill(A,M.year,v,u);O=A[Y][0]
			try:float(O[I])
			except:A[Y].pop(0)
			O=A[Y][0];F=j.datetime.strptime(O[K],L);U=0;V=0;W=0;X=0;Z=0
			for D in A[Y]:
				H=j.datetime.strptime(D[K],L)
				if H.month!=F.month:break
				U+=P(D,I);V+=P(D,c);W+=P(D,d);X+=P(D,e);Z+=P(D,f)
			Q=F-j.timedelta(days=F.day);a=f"{Q.year}-{Q.month:02d}"
			if Ae not in A or A[Ae]!=a:await B.__get_door_bill(A,Q.year);await B.__get_door_ladder(A,a)
			x=j.datetime.strptime(A[Ae],'%Y%m')
			if x.month==12:
				G=0
				for D in A[Y]:
					H=j.datetime.strptime(D[K],L)
					if H.month!=12:break
					G+=P(D,I)
			else:
				G=0
				for D in A[AD]:G+=P(D,g)
				y=t(A[AD])
				for D in A[Y]:
					H=j.datetime.strptime(D[K],L)
					if H.month<=y:break
					G+=P(D,I)
			if G<=2760:A[R]='第一阶梯';A[S]=1
			elif G<=4800:A[R]='第二阶梯';A[S]=2
			else:A[R]='第三阶梯';A[S]=3
			if AK in A:
				A1=P(A[AK],'estiAmt');A2=P(A[AK],'prepayBal');A[T]=A2-A1;b=P(A[AK],'historyOwe')
				if b>0:A[T]=-b
			else:A[T]=0
			if Ad in A:A[h]=P(A[Ad],'totalEleNum');A[i]=P(A[Ad],'totalEleCost')
			else:A[h]=0;A[i]=0
			if AD in A:A[k]=P(A[AD][-1],g);A[l]=P(A[AD][-1],'monthEleCost')
			else:A[k]=0;A[l]=0
			if Y in A:A[m]=P(A[Y][0],I);A[n]=P(A[Y][0],c);A[o]=P(A[Y][0],d);A[p]=P(A[Y][0],e);A[q]=P(A[Y][0],f)
			else:A[m]=0;A[n]=0;A[o]=0;A[p]=0;A[q]=0
			A['month_ele_num']=U;A['month_p_ele_num']=V;A['month_v_ele_num']=W;A['month_n_ele_num']=X;A['month_t_ele_num']=Z;A['daily_lasted_date']=f"{F.year}-{F.month:02d}-{F.day:02d}";A['refresh_time']=j.datetime.strftime(M,'%Y-%m-%d %H:%M:%S')
		await B.save_data()
	async def get_door_account_list(A):return list(A.doorAccountDict.values())
	def get_door_account(A):return A.doorAccountDict
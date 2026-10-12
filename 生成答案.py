# -*- coding: utf-8 -*-
"""生成 答案.json：把 100 道题的 FOFA 查询语句填进答案模板。"""
import json

ANSWERS = {
    "M001-S009": 'ip="20.247.40.92"',
    "M002-S004": 'ip="124.255.254.0/24"',
    "M003-S002": 'domain="zendesk.com"',
    "M004-S003": 'host="www.amazon.com"',
    "M005-S004": 'host="vpn"',
    "M006-S002": 'country="GB"',
    "M007-S007": 'country="KR" && region="Gangwon"',
    "M008-S009": 'country="DE" && region="Bavaria" && city="Munich"',
    "M009-S008": 'asn="4134"',
    "M010-S009": 'country="NL" && cloud_name="AWS"',
    "M011-S005": 'country="CN" && region="Hebei" && org="Huawei"',
    "M012-S009": 'port="3000"',
    "M013-S003": '(title="Jenkins" || body="jenkins") && country!="CN" && after="2026-08-01"',
    "M014-S002": 'country="CN" && protocol="dns"',
    "M015-S001": 'protocol="socks5"',
    "M016-S006": 'protocol="ssh" && port="22022"',
    "M017-S001": 'base_protocol="tcp"',
    "M018-S006": 'protocol="snmp"',
    "M019-S010": 'protocol="memcached" && country="US"',
    "M020-S005": 'protocol="ftp" && base_protocol="tcp"',
    "M021-S010": 'protocol="ssh" && banner="OpenSSH_10.4"',
    "M022-S007": 'country="JP" && body="Hikvision"',
    "M023-S002": 'host*="?.?.163.com"',
    "M024-S005": 'product.version="10.0.0"',
    "M025-S010": 'category="中间件"',
    "M026-S002": 'body="NoSuchUpload"',
    "M027-S008": 'header="Content-Security-Policy-Report-Only"',
    "M028-S011": 'status_code="308"',
    "M029-S010": 'banner="SSH-2.0-OpenSSH_6.1"',
    "M030-S003": 'header="Set-Cookie: PHPSESSID"',
    "M031-S009": 'js_name="jquery.min.js"',
    "M032-S010": 'country="NL" && city="Amsterdam" && port="554" && banner="200 OK"',
    "M033-S003": 'cert.issuer.org="GlobalSign" && cert.is_expired=false',
    "M034-S007": 'cert.subject.cn="apple.com" && host!="apple.com"',
    "M035-S010": 'cert="TrustAsia"',
    "M036-S007": 'cert.subject.org="Alibaba"',
    "M037-S008": 'domain="sohu.com" && banner!="" && banner!="apache"',
    "M038-S009": 'cert="adobe.com"',
    "M039-S001": 'cert.subject.cn="qq.com"',
    "M040-S011": 'cert="godaddy" && domain!="godaddy.com"',
    "M041-S001": 'cert="google.com" && is_honeypot=false && is_fraud=false',
    "M042-S003": 'cert.subject="example.com" || cert="example.com"',
    "M043-S004": 'tls.version="TLS 1.0" && cert.is_expired=false',
    "M044-S007": 'jarm="21d21d00021d21d00021d21d21d21dce319294781f0e12867fd06896a000ea" && status_code="307" && header="Content-Length: 0"',
    "M045-S001": 'os="linux"',
    "M046-S013": 'country="CN" && region!="HK" && region!="TW" && region!="MO" && is_domain=false && (protocol="http" || protocol="https")',
    "M047-S011": 'cert.is_equal=false',
    "M048-S001": 'country="CA" && cert.is_match=false',
    "M049-S010": 'country="TR" && tls.ja3s="f4febc55ea12b31ae17cfb7e614afda8"',
    "M050-S004": 'org="Inc"',
    "M051-S001": 'country="US" && org="OVH SAS" && port="2087" && title=="WHM 登录"',
    "M052-S002": 'host=".io" && app="WordPress"',
    "M053-S009": 'city="Xiamen" && port="80" && status_code="200"',
    "M054-S009": 'country="GB" && org="DigitalOcean" && body="/api/show"',
    "M055-S003": 'country="CN" && region!="HK" && region!="TW" && region!="MO" && header="Set-Cookie" && body="/admin"',
    "M056-S008": 'domain="baidu.com" && (body="Login" || body="admin" || body="Dashboard" || body="管理" || header="Set-Cookie")',
    "M057-S012": 'ip="13.0.0.0/8" && status_code="200" && (body="Welcome" || body="Sign in" || body="Dashboard")',
    "M058-S012": 'country="DE" && (host="amazonaws.com" || domain="amazonaws.com" || cname_domain="amazonaws.com" || cert="amazonaws.com" || cert.domain="amazonaws.com")',
    "M059-S006": 'port="143" && cert.sn="1" && (cert="TAK" || cert="ATAK" || cert="WinTAK" || cert="Squad" || cert="CoT")',
    "M060-S010": 'ip="113.247.228.0/24" && (port="80" || port="443" || port="8080" || port="8443")',
    "M061-S005": 'port="80" && (title="Sign in" || title="Login") && is_ipv6=false',
    "M062-S010": 'country="NZ" && (port="80" || port="443") && is_cloud=true',
    "M063-S001": '(banner="IIS" && banner="1.") || header="IIS"',
    "M064-S004": 'country="JP" && is_domain=true && port="443" && status_code="200" && cert.is_valid=true && (title="大学" || title="学部" || title="研究" || body="入学案内" || body="学生")',
    "M065-S004": 'domain="baidu.com" && (title="系统" || title="平台" || title="登录" || title="管理" || title="API" || host="api" || host="admin" || host="dev" || host="test" || host="uat" || host="pre")',
    "M066-S006": 'category="邮件系统" && title="Mail" && country!="US"',
    "M067-S008": 'port="8888" && country="CN" && region!="HK" && region!="TW" && region!="MO"',
    "M068-S005": 'body="Jenkins" && title!="Jenkins"',
    "M069-S001": 'region="TW" && asn="20940" && port="443" && tls.version="TLS 1.3" && cert.issuer.org!="Let\'s Encrypt" && cert.issuer.org!="ZeroSSL"',
    "M070-S003": 'app="HFS" && status_code="200" && title=="HFS /" && country!="JP" && cloud_name!="AWS"',
    "M071-S006": 'app="Grafana" && country="CN" && region!="HK" && region!="TW" && region!="MO"',
    "M072-S008": 'host=".edu.ar" && (port="80" || port="443") && server!="Nginx" && category!="WAF"',
    "M073-S003": 'ip="1.1.1.1" && is_domain=true',
    "M074-S008": 'cert="aliyun.com" && cert.is_valid=true && is_domain=false',
    "M075-S006": 'country="CN" && is_domain=true && header="x-qiniu-zone" && domain!="qiniudn.com"',
    "M076-S004": 'status_code="200" && title=="" && fid!="" && icon_hash!="" && host="admin" && (domain*="????.com" || domain*="*.cn")',
    "M077-S009": 'body="class=\\"container\\""',
    "M078-S009": 'body="\\"exception\\": \\"Symfony\\\\Component\\\\ErrorHandler\\\\Error\\\\FatalError\\""',
    "M079-S006": 'ip="40.88.0.0/16"',
    "M080-S006": '(ip="47.96.0.1" || ip="47.96.0.2" || ip="47.96.0.3" || ip="47.96.0.4" || ip="47.96.0.5") && (port="80" || port="443")',
    "M081-S011": 'app="Grafana" && ((header_hash!="" && body_hash!="") || (header_hash!="" && icon_hash!="") || (header_hash!="" && fid!="") || (body_hash!="" && icon_hash!="") || (body_hash!="" && fid!="") || (icon_hash!="" && fid!=""))',
    "M082-S001": '(domain="kuaihuoyun.com" || domain="wlhyos.cn" || domain="wlhyos.com" || domain="56ctms.com" || domain="xiaokuaikeji.com" || domain="zhihuiwuliu.org.cn" || cert="kuaihuoyun.com" || cert="wlhyos.cn" || cert="wlhyos.com" || cert="56ctms.com" || cert="xiaokuaikeji.com" || cert="zhihuiwuliu.org.cn") && cert.is_match=true && cert.is_valid=true',
    "M083-S008": 'server="nginx" && title="Welcome"',
    "M084-S004": 'title="Grafana" && body="JavaScript"',
    "M085-S001": 'body="login" && (host="bet" || host="casino" || host="kasino")',
    "M086-S006": 'domain="google" && domain!="google.com" && title==""',
    "M087-S009": 'server="Tengine" || header="x-cache: MISS"',
    "M088-S004": 'region="HK" && server=="Apache" && asn!="4134"',
    "M089-S010": 'app="HFS" && (port="80" || (port="8080" && status_code="200"))',
    "M090-S008": 'header="Etag: \\"6aa522a3-493\\"" && header="Content-Length: 1171" && header="Accept-Ranges" && header="Cache-Control" && header="Content-Type" && header="Date" && header="Last-Modified" && header="Server" && header="Vary"',
    "M091-S009": "该需求不能直接转换为FOFA搜索语句",
    "M092-S007": "该需求不能直接转换为FOFA搜索语句",
    "M093-S004": "该需求不能直接转换为FOFA搜索语句",
    "M094-S004": "该需求不能直接转换为FOFA搜索语句",
    "M095-S010": "该需求不能直接转换为FOFA搜索语句",
    "M096-S001": '(body="Jenkins-Agent-Protocols" || body="Jenkins-Version" || body="Jenkins-Session" || body="Remoting-Minimum-Version" || banner="Jenkins-Agent-Protocols" || banner="Jenkins-Version" || banner="Jenkins-Session" || banner="Remoting-Minimum-Version")',
    "M097-S001": 'icon_hash="-1766690195"',
    "M098-S001": 'host="msp.gov.cn" && is_fraud=true',
    "M099-S001": 'server="Apache/2.4.49" || server="Apache/2.4.50"',
    "M100-S001": 'cert.issuer.cn="ZeroSSL ECC DV SSL CA 2" && cert.sn="63:BD:83:71:62:14:83:6E:F8:00:75:35:61:61:EB:06"',
}

# 读取原始题目与模板，按题目顺序校验完整性
def load_clean(path):
    with open(path, encoding='utf-8') as f:
        raw = f.read()
    # 清洗网页复制引入的不可见字符（零宽空格/BOM/不换行空格）
    for ch in ('\u200b', '\ufeff', '\u200c', '\u200d', '\xa0'):
        raw = raw.replace(ch, '')
    return json.loads(raw)

questions = load_clean('题目.md')
template = load_clean('答案模板.md')

qids = [q["题号"] for q in questions]
aids = list(ANSWERS.keys())

missing = [q for q in qids if q not in ANSWERS]
extra = [a for a in aids if a not in qids]
assert not missing, f"缺题: {missing}"
assert not extra, f"多余题号: {extra}"
assert len(qids) == 100, f"题目数异常: {len(qids)}"

# 填充模板（保持模板结构与顺序）
for item in template["答案"]:
    item["查询语句"] = ANSWERS[item["题号"]]
template["选手名称"] = "丁恺文"
template["参赛包编号"] = "pkg-08e82c8d"

with open('答案.json', 'w', encoding='utf-8') as f:
    json.dump(template, f, ensure_ascii=False, indent=2)

print(f"OK: 共 {len(template['答案'])} 题全部填充")
print("抽样检查:")
for tid in ["M001-S009", "M051-S001", "M077-S009", "M078-S009", "M090-S008", "M097-S001"]:
    q = next(a["查询语句"] for a in template["答案"] if a["题号"] == tid)
    print(f"  {tid}: {q}")

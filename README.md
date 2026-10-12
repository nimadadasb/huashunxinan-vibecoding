# huashunxinan-vibecoding — FOFA 查询语句作答

华顺信安 FOFA 查询语句转换赛 · 参赛包编号 **pkg-08e82c8d**

## 文件

- `答案.json`：题目集全部 100 题的 FOFA 查询语句答案（UTF-8，保留参赛包编号），可直接上传比赛网站。
- `生成答案.py`：作答脚本——读取题目/模板 JSON → 填充 100 条查询语句 → 校验题号完整性后输出答案文件。

## 作答方法

按 FOFA 官方查询语法逐题转换，重点覆盖证书类与标记类字段：

- 证书：`cert.subject.cn` / `cert.subject.org` / `cert.issuer.org` / `cert.issuer.cn` / `cert.sn` / `cert.is_valid` / `cert.is_expired` / `cert.is_match` / `cert.is_equal` / `cert.domain`
- TLS 与指纹：`tls.version` / `tls.ja3s` / `jarm` / `icon_hash` / `fid`
- 标记类：`is_fraud` / `is_honeypot` / `is_cloud` / `cloud_name` / `category` / `product.version`
- 地理解析：`country` / `region` / `city`（含港澳台排除写法）
- 通配：`*=` 模糊匹配（`?.?.163.com` 类子域名形态）

对无法直接转换为 FOFA 查询的需求（非法端口/IP、自相矛盾条件、无可查数据源等）按要求填写固定答案：`该需求不能直接转换为FOFA搜索语句`。

## 校验

- 100 题全覆盖，无缺题、无重复题号、无空答案。
- 提交前请核对 `答案.json` 中 `选手名称` 字段。

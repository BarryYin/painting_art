
#  APIPASSWORD gzplsktULBGbkbQLUdAV:wgRHXkQPvSHkWUyERaVI
'''
curl -i -k -X POST 'https://spark-api-open.xf-yun.com/v1/chat/completions' \
--header 'Authorization: Bearer gzplsktULBGbkbQLUdAV:wgRHXkQPvSHkWUyERaVI' \
--header 'Content-Type: application/json' \
--data '{
    "model":"generalv3.5",
    "messages": [
        {
            "role": "user",
            "content": "来一个只有程序员能听懂的笑话"
        }
    ],
    "stream": true
}'


ws(s)://spark-openapi.cn-huabei-1.xf-yun.com/v1/assistants/ub9erzzhewqn_v1
e6950ae6


curl -i -k -X POST 'ws://spark-openapi.cn-huabei-1.xf-yun.com/v1/assistants/ub9erzzhewqn_v1' \
--header 'Authorization: Bearer e6950ae6' \
--header 'Content-Type: application/json' \
--data '{
    "model":"generalv3.5",
    "messages": [
        {
            "role": "user",
            "content": "来一个只有程序员能听懂的笑话"
        }
    ],
    "stream": true
}'
'''

from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage
import re
#from teststr import changestr

#星火认知大模型Spark Max的URL值，其他版本大模型URL值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
#SPARKAI_URL = 'ws://spark-openapi.cn-huabei-1.xf-yun.com/v1/assistants/ub9erzzhewqn_v1'
#SPARKAI_URL = "wss://spark-openapi.cn-huabei-1.xf-yun.com/v1/assistants/mjdb4ugt88cw_v1" #高更
#SPARKAI_URL = "ws://spark-openapi.cn-huabei-1.xf-yun.com/v1/assistants/7eiewgq1xvhi_v1" #莫奈
#SPARKAI_URL = "wss://spark-openapi.cn-huabei-1.xf-yun.com/v1/assistants/xzfix52x2oz8_v1" #梵高
#SPARKAI_URL = "wss://spark-openapi.cn-huabei-1.xf-yun.com/v1/assistants/jcrtz4ufw8w2_v1" #马奈#
#SPARKAI_URL = "wss://spark-openapi.cn-huabei-1.xf-yun.com/v1/assistants/jng35xjelibp_v1" #毕加索#
#SPARKAI_URL = "wss://spark-openapi.cn-huabei-1.xf-yun.com/v1/assistants/ctzla42n56q1_v1" #安格尔#
#SPARKAI_URL = "wss://spark-openapi.cn-huabei-1.xf-yun.com/v1/assistants/nz84zzqt6lxz_v1" #弗朗索瓦·米勒#

#星火认知大模型调用秘钥信息，请前往讯飞开放平台控制台（https://console.xfyun.cn/services/bm35）查看
# SPARKAI_APP_ID = 'e6950ae6'
# SPARKAI_API_SECRET = 'NzRkOWNlZDUzZThjMDI5NzI0N2EyMGRh'
# SPARKAI_API_KEY = 'f2d4b9650c13355fc8286ac3fc34bf6e'
SPARKAI_APP_ID = '3a115b20'
SPARKAI_API_SECRET = 'ZGMyMzA3MGFlM2MzM2UxZWE1YTJhYjgw'
SPARKAI_API_KEY = '9d1b7a738c3e63a79656df4222d12cef'
#星火认知大模型Spark Max的domain值，其他版本大模型domain值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
SPARKAI_DOMAIN = 'generalv3.5'

def talkwithboss(who,text):
    if who == "莫奈":
         SPARKAI_URL = "ws://spark-openapi.cn-huabei-1.xf-yun.com/v1/assistants/7eiewgq1xvhi_v1"
    elif who == "高更":
         SPARKAI_URL = "wss://spark-openapi.cn-huabei-1.xf-yun.com/v1/assistants/mjdb4ugt88cw_v1" 
    elif who == "梵高":
         SPARKAI_URL = "wss://spark-openapi.cn-huabei-1.xf-yun.com/v1/assistants/xzfix52x2oz8_v1"
    elif who == "马奈":
         SPARKAI_URL = "wss://spark-openapi.cn-huabei-1.xf-yun.com/v1/assistants/jcrtz4ufw8w2_v1"
    elif who == "毕加索":
         SPARKAI_URL = "wss://spark-openapi.cn-huabei-1.xf-yun.com/v1/assistants/jng35xjelibp_v1"
    elif who == "安格尔":
         SPARKAI_URL = "wss://spark-openapi.cn-huabei-1.xf-yun.com/v1/assistants/ctzla42n56q1_v1"
    elif who == "弗朗索瓦·米勒":
         SPARKAI_URL = "wss://spark-openapi.cn-huabei-1.xf-yun.com/v1/assistants/nz84zzqt6lxz_v1"
    else:
         SPARKAI_URL = "ws://spark-openapi.cn-huabei-1.xf-yun.com/v1/assistants/7eiewgq1xvhi_v1" #兜底的，后面替换下
 
    spark = ChatSparkLLM(
        spark_api_url=SPARKAI_URL,
        spark_app_id=SPARKAI_APP_ID,
        spark_api_key=SPARKAI_API_KEY,
        spark_api_secret=SPARKAI_API_SECRET,
        spark_llm_domain=SPARKAI_DOMAIN,
        streaming=False,
    )
    messages = [ChatMessage(
        role="user",
        content= text
    )]
    handler = ChunkPrintHandler()
    a = spark.generate([messages], callbacks=[handler])
    # 使用正则表达式查找content字段的值
    match = re.search(r"content='(.*?)'", str(a))

    if match:
        content = match.group(1)
        print(content)
        # 将\n替换为<br>以便在HTML中正确显示换行
        print(type(content))
        content = re.sub(r'\n\n+', '<p></p>', content)
        content = re.sub(r'\n', '<br>', content)
        #B = changestr(content)
       # print(B)
        print(content)
        return content
    else:
        print("未找到content字段")
    #print(a)

if __name__ == '__main__':
      talkwithboss("弗朗索瓦·米勒","你是谁？")
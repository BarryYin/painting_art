from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage

'''
星火智能体
API Secret:
NzRkOWNlZDUzZThjMDI5NzI0N2EyMGRh
API Key：
f2d4b9650c13355fc8286ac3fc34bf6e
已绑定的APPID:
e6950ae6
'''
#星火认知大模型Spark Max的URL值，其他版本大模型URL值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
#SPARKAI_URL = 'wss://spark-api.xf-yun.com/v3.5/chat'  ub9erzzhewq   
SPARKAI_URL =   'wss://spark-openapi.cn-huabei-1.xf-yun.com/v1/assistants/ub9erzzhewqn_v1'
#星火认知大模型调用秘钥信息，请前往讯飞开放平台控制台（https://console.xfyun.cn/services/bm35）查看
from config import Config

SPARKAI_APP_ID = Config.XUNFEI_APP_ID
SPARKAI_API_SECRET = Config.XUNFEI_API_SECRET
SPARKAI_API_KEY = Config.XUNFEI_API_KEY
#星火认知大模型Spark Max的domain值，其他版本大模型domain值请前往文档（https://www.xfyun.cn/doc/spark/Web.html）查看
#SPARKAI_DOMAIN = 'generalv3.5'
SPARKAI_DOMAIN = 'generalv3.5'


def talkwithboss(who,text):
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
        content='你好呀,你是谁呀'
    )]
    handler = ChunkPrintHandler()
    a = spark.generate([messages], callbacks=[handler])
    print(a)

if __name__ == '__main__':
    talkwithboss()
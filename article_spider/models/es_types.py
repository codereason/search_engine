#coding=utf-8
from datetime import datetime
from elasticsearch_dsl import Document,Date,Nested,Boolean,\
    analyzer,Completion,Keyword,Text
from elasticsearch_dsl.connections import connections
connections.create_connection(hosts=['localhost'])

class ArticleType(Document):
    suggest = Completion(analyzer="ik_max_word")
    title = Text(analyzer="ik_max_word")
    create_date = Date()
    url = Keyword()
    url_object_id = Keyword()
    tags = Text(analyzer="ik_max_word")
    content = Text(analyzer="ik_max_word")


    class Index:
        ''':arg
        name of the doc_type in elasticsearch. By default it will be constructed from the class name (MyDocument -> my_document)

        '''
        name = "jianshu"
        _doc_type = "article"


if __name__ == '__main__':
    ArticleType.init()
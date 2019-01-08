from scrapy.conf import settings
from scrapy.exporters import CsvItemExporter


# 输出有空行，找到源码，修改scrapy.exporters.CsvItemExporter，在self.stream = io.TextIOWrapper(加入参数newline=''
# 源码位置python\Lib\site-packages\scrapy\exporters.py
class CSVkwItemExporter(CsvItemExporter):

    def __init__(self, *args, **kwargs):
        kwargs['fields_to_export'] = settings.getlist('EXPORT_FIELDS') or None
        kwargs['encoding'] = settings.get('EXPORT_ENCODING', 'utf-8')

        super(CSVkwItemExporter, self).__init__(*args, **kwargs)
